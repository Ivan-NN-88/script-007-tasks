import datetime
from aiohttp import web
import aiohttp_session
from aiohttp_session.cookie_storage import EncryptedCookieStorage
import hashlib
from aiohttp_security.abc import AbstractAuthorizationPolicy


NOT READY!!!!!!!!!!!!

class DBAuthorizationPolicy(AbstractAuthorizationPolicy):
    def __init__(self, dbengine):
        self.dbengine = dbengine

    async def authorized_userid(self, identity):
        async with self.dbengine.acquire() as conn:
            where = sa.and_(db.users.c.login == identity,
                            sa.not_(db.users.c.disabled))
            query = db.users.count().where(where)
            ret = await conn.scalar(query)
            if ret:
                return identity
            else:
                return None

    async def permits(self, identity, permission, context=None):
        if identity is None:
            return False

        async with self.dbengine.acquire() as conn:
            where = sa.and_(db.users.c.login == identity,
                            sa.not_(db.users.c.disabled))
            query = db.users.select().where(where)
            ret = await conn.execute(query)
            user = await ret.fetchone()
            if user is not None:
                user_id = user[0]
                is_superuser = user[3]
                if is_superuser:
                    return True

                where = db.permissions.c.user_id == user_id
                query = db.permissions.select().where(where)
                ret = await conn.execute(query)
                result = await ret.fetchall()
                if ret is not None:
                    for record in result:
                        if record.perm_name == permission:
                            return True

            return False



async def check_credentials(db_engine, username, password):
    async with db_engine.acquire() as conn:
        where = sa.and_(db.users.c.login == username,
                        sa.not_(db.users.c.disabled))
        query = db.users.select().where(where)
        ret = await conn.execute(query)
        user = await ret.fetchone()
        if user is not None:
            hashed = user[2]
            return sha256_crypt.verify(password, hashed)
    return False


def generate_256_key() -> bytes:
    """Generate 256-bit key

    Returns:
        bytes: key
    """

    # return b'Thirty  two  length  bytes  key.'

    passphrase = b'secret'
    m = hashlib.sha256()
    m.update(passphrase)
    return m.digest()

async def handler(request):
    session = await aiohttp_session.get_session(request)
    last_visit = session.get('last_visit', 'never')
    session['last_visit'] = str(datetime.datetime.now())
    return web.Response(text=f"""
Now is {session['last_visit']}.
Last time we saw you {last_visit}.
""")

def init():
    app = web.Application()
    aiohttp_session.setup(app, EncryptedCookieStorage(generate_256_key()))
    app.router.add_route('GET', '/', handler)
    return app

web.run_app(init(), host='127.0.0.1', port=8080)
