from aiohttp import web
import aiohttp_jinja2
import jinja2

async def handler_index(request):
    raise web.HTTPFound('/auth')

# https://docs.aiohttp.org/en/stable/web_quickstart.html#class-based-views
class ViewHandler(web.View):
    async def get(self):
        params = self.request.rel_url.query
        name = params['name'] if 'name' in params else 'Anonymous!'
        context = {'name': name, 'approach': 'web view class'}
        response = aiohttp_jinja2.render_template('form.html.j2', self.request, context)
        return response

    async def post(self):
        data = await self.request.post()
        context = {
            'login': data.get('login', ''),
            'password': data.get('password', ''),
        }

        if context['password'] == 'secret':
            raise web.HTTPFound('/secret')

        response = aiohttp_jinja2.render_template('form.html.j2', self.request, context)
        return response

async def handler_secret(request):
    params = request.rel_url.query
    name = params['name'] if 'name' in params else 'Anonymous!'
    context = {'name': name, 'approach': 'render_template'}
    response = aiohttp_jinja2.render_template('hello.html.j2', request, context)
    return response

app = web.Application()
app.add_routes([
    web.get('/', handler_index),
    web.view('/auth', ViewHandler),
    web.get('/secret', handler_secret),
])
aiohttp_jinja2.setup(
    app,
    loader=jinja2.FileSystemLoader('demo/aiohttp/jinja2/templates')
)

if __name__ == '__main__':
    web.run_app(app, host='127.0.0.1', port=8080)
