"""
+++++++++++++++++++++++++++++++++++++++++
+ Project: File server                  +
+ Developer: Viharev Ivan Alexandrovich +
+ Year: 2022                            +
+++++++++++++++++++++++++++++++++++++++++
"""

import argparse
import logging
import os

from server.FileService import change_dir
from utils.log_config import LogSetter


def main():
    """Start of the file server."""
    logging.info('Start of the file server...')

    change_dir(args.dir)

    logging.info('File server stopped.')


def parses_arguments():
    """Parses arguments.

    Returns:
        parser object.

        Args:
        * -d --dir: path to the working directory.
        * -l --level: logging level.
        * -f --logfilename: logging file name with extension.
    """
    parser = argparse.ArgumentParser(description='Path to the working directory')

    # Current working directory.
    parser.add_argument(
        '-d',
        '--dir',
        type=str,
        help='Input path to the working directory',
        default=os.getcwd()
    )
    # Log level.
    parser.add_argument(
        '-l',
        '--level',
        type=str,
        help='Input the logging level',
        choices=list(logging._nameToLevel.keys()),
        default='INFO'
    )
    # Log file name.
    parser.add_argument(
        '-f',
        '--logfilename',
        type=str,
        help='Input the logging file name with extension',
        default='server.log'
    )

    return parser.parse_args()


if __name__ == '__main__':
    # Parses arguments.
    args = parses_arguments()
    # Setting up logging.
    LogSetter(args.logfilename, args.level).set_mode2()
    # Start file server.
    main()
