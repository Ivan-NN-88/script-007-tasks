"""Configuration of the file server."""

import argparse
import logging
import os

import yaml
from dotmap import DotMap


CONFIG_YAML_FILEPATH = os.path.join(os.path.dirname(__file__), 'config.yaml')


def parses_args_CLI():
    """Parses arguments from CLI.

    Returns:
        dictionary with the following keys {'dir': ..., 'level': ..., ...}:

    Args CLI:
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
        help='Path to the working directory',
        default=''
    )
    # Log level.
    parser.add_argument(
        '-l',
        '--level',
        type=str,
        help='Logging level',
        choices=list(logging._nameToLevel.keys()),
        default=''
    )
    # Log file name.
    parser.add_argument(
        '-f',
        '--logfilename',
        type=str,
        help='Logging file name with extension',
        default=''
    )

    # Clear all empty args and return result.
    return {k: v for k, v in parser.parse_args().__dict__.items() if v}


def parses_args_env():
    """Parses arguments from enviroment.

    Returns:
        dictionary with keys/values from environment variables.
    """
    return {k: v for k, v in sorted(os.environ.items())}


def parses_args_YAML():
    """Parses arguments from config YAML file.

    Returns:
        dictionary with keys/values from config YAML file.
    """
    with open(CONFIG_YAML_FILEPATH, 'r') as file:
        return yaml.safe_load(file)


config = {
    'dir': 'test_value'
}
config.update(parses_args_YAML())
config.update(parses_args_env())
config.update(parses_args_CLI())
config = DotMap(config)
