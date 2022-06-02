"""Logging configuration for the file server."""

# Python standard libraries.
import logging, logging.handlers
import os
import sys
# Python external libraries.
import colorama


# Setting the color text.
colorama.init()
# Logging levels.
LOGGING_LEVELS = ['DEBUG', 'INFO', 'WARN', 'ERROR', 'FATAL']


def get_logging_level(level: str):
    """Gets the logging level by the specified value.

    Args:
        level (str): value logging level.

    Returns:
        logging level object.

    Raises:
        ValueError: if level is invalid.
    """
    # Checks if the level value is correct.
    if not level in LOGGING_LEVELS:
        raise ValueError(f'{level} - level is not correct. Please correct level!')

    # Get level object.
    if level == 'DEBUG':
        return logging.DEBUG
    elif level == 'INFO':
        return logging.INFO
    elif level == 'WARN':
        return logging.WARN
    elif level == 'ERROR':
        return logging.ERROR
    elif level == 'FATAL':
        return logging.FATAL


class LogSetter:
    """Sets the configuration for logging.

    Args:
        log_file_name (str): specify a name for the logging file. * Default value - 'server.log' *
        level (str): specify the logging level value. * Default value - 'INFO' *
    """

    def __init__(self, log_file_name: str = 'server.log', level: str = 'INFO') -> None:

        colorama.init()

        self.log_file_name = log_file_name
        self.level = level
        self.log_dir_path = os.path.join(os.getcwd(), 'logs')
        self.main_log_file_path = os.path.join(self.log_dir_path, log_file_name)
        self.last_log_file_path = os.path.join(self.log_dir_path, 'last_' + log_file_name)

        # Prepare logs directory.
        if not os.path.isdir(self.log_dir_path):
            os.makedirs(self.log_dir_path)

        # Deletes the last log file, if any.
        if os.path.exists(self.last_log_file_path):
            os.remove(self.last_log_file_path)

    def set_mode1(self):
        """Configuration with file rotation by day."""
        logging.basicConfig(
            level=get_logging_level(self.level),
            format='%(asctime)s %(lineno)4s %(funcName)-20s %(levelname)-7s %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            handlers=[
                logging.handlers.TimedRotatingFileHandler(self.main_log_file_path, when='midnight'),
                logging.StreamHandler(sys.stdout)
            ]
        )

        Color.logging_color('*' * 35)
        logging.info('"set 1" is selected for logging.')

    def set_mode2(self):
        """Configuration with last file log and file rotation by size."""
        logging.basicConfig(
            level=get_logging_level(self.level),
            format='%(asctime)s *** %(funcName)20s *** %(lineno)4d *** %(levelname)8s *** %(message)8s',
            datefmt='%d.%m.%Y %H:%M:%S',
            handlers=[
                logging.handlers.RotatingFileHandler(self.main_log_file_path, maxBytes=int(1e+7), backupCount=1),
                logging.handlers.RotatingFileHandler(self.last_log_file_path),
                logging.StreamHandler(sys.stdout)
            ]
        )

        Color.logging_color('*' * 35)
        logging.info('"set 2" is selected for logging.')


class Color:
    """Colors logs by levels"""

    @staticmethod
    def logging_color(message: str, level: str ="info", background: bool =False):
        """Colors the text of the logging library logs in the console.

        Args:
            message (str): log text.
            level (str): logging level value. * Default value - 'info' *
            background (bool): paint the background of the log, not the text. * Default value - False *

        Raises:
            ValueError: if level log is invalid.

        Usage example:
            Color.logging_color('My text log', 'warn')
        """
        if level == 'info':
            print(colorama.Fore.GREEN if not background else colorama.Back.GREEN,
                 colorama.Style.BRIGHT, sep='', end='')
            logging.info(message)
            print(colorama.Style.RESET_ALL, end='')
        elif level == 'warn':
            print(colorama.Fore.YELLOW if not background else colorama.Back.YELLOW,
                 colorama.Style.BRIGHT, sep='', end='')
            logging.warning(message)
            print(colorama.Style.RESET_ALL, end='')
        elif level == 'error':
            print(colorama.Fore.RED if not background else colorama.Back.RED,
                 colorama.Style.BRIGHT, sep='', end='')
            logging.error(message)
            print(colorama.Style.RESET_ALL, end='')
        else:
            raise ValueError("Failed to colorize the log text!"
                            "Specify the string as the first argument, "
                            "the second (optional) 'info'/'warn'/'error', "
                            "the third (optional) True/False")
