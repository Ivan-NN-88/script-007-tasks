import datetime
from aiohttp import web
import aiohttp_session
from aiohttp_session.cookie_storage import EncryptedCookieStorage
import hashlib

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


# https://github.com/aio-libs/aiohttp-remotes/blob/master/aiohttp_remotes/basic_auth.py


def init():
    app = web.Application()
    aiohttp_session.setup(app, EncryptedCookieStorage(generate_256_key()))
    app.router.add_route('GET', '/', handler)
    return app

web.run_app(init(), host='127.0.0.1', port=8080)
