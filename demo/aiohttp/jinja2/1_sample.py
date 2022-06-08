from aiohttp import web
import aiohttp_jinja2
import jinja2


@aiohttp_jinja2.template('hello.html.j2')
async def handle_decorator(request):
    # http://127.0.0.1/?name=User
    params = request.rel_url.query
    name = params['name'] if 'name' in params else 'Anonymous!'
    return {'name': name, 'approach': 'decorator'}


async def handler_render(request):
    params = request.rel_url.query
    name = params['name'] if 'name' in params else 'Anonymous!'
    context = {'name': name, 'approach': 'render_template'}
    response = aiohttp_jinja2.render_template('hello.html.j2', request, context)
    return response


# https://docs.aiohttp.org/en/stable/web_quickstart.html#class-based-views
class ViewHandler(web.View):
    async def get(self):
        params = self.request.rel_url.query
        name = params['name'] if 'name' in params else 'Anonymous!'
        context = {'name': name, 'approach': 'web view class'}
        response = aiohttp_jinja2.render_template('hello.html.j2', self.request, context)
        return response


app = web.Application()
app.add_routes([
    web.get('/', handle_decorator),
    web.get('/r', handler_render),
    web.view('/v', ViewHandler)
])
aiohttp_jinja2.setup(
    app,
    loader=jinja2.FileSystemLoader('demo/aiohttp/jinja2/templates')
)

if __name__ == '__main__':
    web.run_app(app, host='127.0.0.1', port=8080)
