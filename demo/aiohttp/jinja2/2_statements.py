from aiohttp import web
import aiohttp_jinja2
import jinja2


async def handler_render(request):
    params = request.rel_url.query
    context = {
        'params': params,
        'users': [
            { 'name': 'Maxim', 'is_active': True, 'password': '123' },
            { 'name': 'Eugene', 'is_active': False, 'password': '456' },
        ],
    }
    response = aiohttp_jinja2.render_template('statements.html.j2', request, context)
    return response


app = web.Application()
app.add_routes([
    web.get('/', handler_render),
])
aiohttp_jinja2.setup(
    app,
    loader=jinja2.FileSystemLoader('demo/aiohttp/jinja2/templates')
)

if __name__ == '__main__':
    web.run_app(app, host='127.0.0.1', port=8080)
