"""
+++++++++++++++++++++++++++++++++++++++++
+ Project: File server                  +
+ Developer: Viharev Ivan Alexandrovich +
+ Year: 2022                            +
+++++++++++++++++++++++++++++++++++++++++
"""

import logging
from traceback import format_exc

from aiohttp import web

from config.config import config
from server.WebHandler import WebHandler
from utils.log import Color, LogSetter


def main():
    """Start of the file server."""
    logging.info('Start of the file server...')

    handler = WebHandler()
    app = web.Application()
    app.add_routes([
        web.get('/', handler.handle),
        web.get('/files', handler.get_files),
        web.get('/files/{file_path:.+}', handler.get_file_data),
        web.post('/change_dir/{path:.+}', handler.change_dir),
        web.post('/files/{file_path}', handler.create_file),
        web.delete('/files/{path:.+}', handler.delete_obj),
    ])
    web.run_app(app, port=config.port)

    logging.info('File server stopped.')


if __name__ == '__main__':
    # Setting up logging.
    LogSetter(config.logfilename, config.level).set_mode2()

    # Start file server.
    try:
        main()
    except Exception:
        Color.logging_color(f'The server is stopped:\n{format_exc()}', 'error')
