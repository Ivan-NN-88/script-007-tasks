
#

https://aiohttp-session.readthedocs.io/en/stable/


# Ready to use

Official:

- [aiohttp-security](https://github.com/aio-libs/aiohttp-security) auth and permissions for aiohttp.web.
  https://aiohttp-security.readthedocs.io/en/latest/usage.html

Unofficial:

- [aioauth-client](https://github.com/klen/aioauth-client) OAuth client for aiohttp.
- [aiohttp-login](https://github.com/imbolc/aiohttp-login) Registration and authorization (including social) for aiohttp applications.

#

[identity](https://aiohttp-security.readthedocs.io/en/latest/glossary.html#term-identity)
Session-wide str for identifying user.

## Abstract policies

[Abstract policies](https://aiohttp-security.readthedocs.io/en/latest/reference.html#abstract-policies)
- `AbstractIdentityPolicy`
  It responds on remembering, retrieving and forgetting identity into some session storage, e.g. HTTP cookie or authorization token.
  - `identify(self, request)`
  - `remember(self, request, response, identity, **kwargs)`

- `AbstractAuthorizationPolicy`
  It is responsible to return persistent userid for session-wide identity and check user’s permissions.
  - `permits(self, identity, permission, context=None)`
  - `authorized_userid(self, identity)`
  - `forget(self, request, response)`

[Sources](https://github.com/aio-libs/aiohttp-security/blob/master/aiohttp_security/abc.py)

# TODO

https://aiohttp-security.readthedocs.io/en/latest/reference.html#abstract-policies
https://github.com/aio-libs/aiohttp-security/blob/master/demo/database_auth/handlers.py
https://github.com/aio-libs/aiohttp-security/blob/master/demo/simple_example_auth.py
https://asvetlov.blogspot.com/
https://habr.com/ru/post/544638/
https://www.programcreek.com/python/?code=lablup%2Fbackend.ai-manager%2Fbackend.ai-manager-master%2Fsrc%2Fai%2Fbackend%2Fgateway%2Fratelimit.py
https://github.com/aio-libs/aiohttp-remotes/blob/master/aiohttp_remotes/basic_auth.py
