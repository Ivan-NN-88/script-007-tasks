"""
+++++++++++++++++++++++++++++++++++++++++
+ Project: File server                  +
+ Developer: Viharev Ivan Alexandrovich +
+ Year: 2022                            +
+++++++++++++++++++++++++++++++++++++++++
"""

import logging
from traceback import format_exc

from config.config import config
from server.FileService import change_dir
from utils.log_config import Color, LogSetter


def main():
    """Start of the file server."""
    logging.info('Start of the file server...')

    change_dir(config.dir)

    logging.info('File server stopped.')


if __name__ == '__main__':
    # Setting up logging.
    LogSetter(config.logfilename, config.level).set_mode2()

    # Start file server.
    try:
        main()
    except Exception:
        Color.logging_color(f'The server is stopped:\n{format_exc()}', 'error')
