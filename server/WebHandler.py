"""Web handler for the file server."""

import base64
import json
import logging
import os
from traceback import format_exc

from aiohttp import web

from config.config import config
from server import FileService
from server.UserService import UserDataBase
from utils.log import Color


class WebHandler:
    """aiohttp handler with coroutines."""

    def __init__(self) -> None:
        FileService.change_dir(config.main_dir)
        self.user_db = UserDataBase()

    def __authorize(self, request: web.Request) -> str:
        """Authorizes the user from whom the request was received.

        Args:
            request (web.Request): aiohttp request.

        Returns:
            str: user token, if the user is logged in.

        Raises:
            HTTPUnauthorized: 401 HTTP error, if error.
        """
        login, password = base64.b64decode(
            request.headers['Authorization'][6:]).decode('utf-8').split(':')

        # Checking the user for entries in the database.
        self.user_db.login(login, password)

        ...     # TODO need to finish

        data = {'status': 'error', 'message': 'Please log in!'}
        raise web.HTTPUnauthorized(body=json.dumps(data, indent=4),
                                   headers=request.headers)

    def __get_exception(self, error_text: str) -> web.HTTPBadRequest:
        """Gets an HTTPBadRequest exception (400 HTTP error).

        Args:
            error_text (str): the message passed to the exception.

        Returns:
            HTTPBadRequest exception: 400 HTTP error.
        """
        data = {'status': 'error', 'message': error_text}
        raise web.HTTPBadRequest(body=json.dumps(data, indent=4))

    async def handle(self, request: web.Request) -> web.Response:
        """Basic coroutine for connection testing.

        Args:
            request (Request): aiohttp request.

        Returns:
            Response: JSON response with status.
        """
        try:
            Color.logging_color(
                '(!) A request has been received '
                'to display the current directory!', 'warn')
            data = {
                'status': 'success',
                'directory': os.getcwd().split(config.root_dir_name)[-1]
            }
            return web.json_response(data=data)
        except Exception:
            self.__get_exception(
                'An error occurred while processing a request to display '
                f'the current directory: [{format_exc()}].')

    async def change_dir(self, request: web.Request) -> web.Response:
        """Coroutine for changing working directory with files.

        Args:
            request (Request): aiohttp request, contains JSON in body.
            JSON format:
            {
                "path": "string. Directory path. Required",
            }.

        Returns:
            Response: JSON response with success status and success
            message or error status and error message.

        Raises:
            HTTPBadRequest: 400 HTTP error, if error.
        """
        try:
            Color.logging_color(
                '(!) Received a request to change the directory!', 'warn')

            path = request.match_info.get('path', '')
            logging.info(f'input path = [{path}]')
            path = '..' if path == 'back' else path

            abs_path = os.path.abspath(path)
            logging.info(f'directory to change = [{abs_path}]')

            autocreate = False if request.query.get(
                'autocreate', '').lower() == 'false' else True
            logging.info(f'autocreate parameter = [{autocreate}].')

            FileService.change_dir(abs_path, autocreate=autocreate)

            data = {
                'status': 'success',
                'message': ('The current directory has been '
                            f'successfully changed to [{abs_path}].')
            }
            return web.json_response(data=data)
        except Exception:
            self.__get_exception('An error occurred when changing '
                                 f'the directory: [{format_exc()}].')

    async def get_files(self, request: web.Request) -> web.Response:
        """Coroutine for getting info about all files in working directory.

        Args:
            request (Request): aiohttp request.

        Returns:
            Response: JSON response with success status and data or
            error status and error message.

        Raises:
            HTTPBadRequest: 400 HTTP error, if error.
        """
        try:
            Color.logging_color('(!) A request was received to get a list '
                                'of files from directory : '
                                f'[{config.dir}].', 'warn')

            files = FileService.get_files()

            return web.json_response(data={'status': 'success', 'data': files})
        except Exception:
            self.__get_exception(
                f'An error occurred while receiving files: [{format_exc()}].')

    async def get_file_data(self, request: web.Request) -> web.Response:
        """Coroutine for getting full info about file in working directory.

        Args:
            request (Request): aiohttp request, contains filename and
            is_signed parameters.

        Returns:
            Response: JSON response with success status and data or
            error status and error message.

        Raises:
            HTTPBadRequest: 400 HTTP error, if error.
        """
        try:
            Color.logging_color(
                '(!) A request for file data has been received!', 'warn')
            file_path = request.match_info.get('file_path', '')
            logging.info(f'file_path = [{file_path}].')

            file_data = FileService.get_file_data(file_path)

            data = {
                'status': 'success',
                'data': file_data
            }
            return web.json_response(data=data)
        except Exception:
            self.__get_exception(
                'An error occurred while extracting data from file '
                f'[{file_path}]: [{format_exc()}].')

    async def create_file(self, request: web.Request) -> web.Response:
        """Coroutine for creating file.

        Args:
            request (Request): aiohttp request, contains bytes in body.
            Optional.

        Returns:
            Response: JSON response with success status and data or
            error status and error message.

        Raises:
            HTTPBadRequest: 400 HTTP error, if error.
        """
        try:
            Color.logging_color('(!) Received a request to create a file!',
                                'warn')
            file_path = request.match_info.get('file_path', '')
            logging.info(f'file_path = [{file_path}].')

            # Checking for the presence of content in the request.
            try:
                content = await request.read()
            except Exception:
                content = None

            file_data = FileService.create_file(file_path, content=content)

            return web.json_response(data={
                'status': 'success',
                'data': file_data
            })
        except Exception:
            self.__get_exception('An error occurred while creating file '
                                 f'[{file_path}]: [{format_exc()}].')

    async def delete_obj(self, request: web.Request) -> web.Response:
        """Coroutine for deleting file|directory.

        Args:
            request (Request): aiohttp request, contains path object.

        Returns:
            Response: JSON response with success status and success message or
            error status and error message.

        Raises:
            HTTPBadRequest: 400 HTTP error, if error.

        """
        try:
            Color.logging_color('(!) Received a request to delete object!',
                                'warn')
            path = request.match_info.get('path', '')
            abs_path = os.path.abspath(path)
            logging.info(f'path = [{abs_path}].')

            FileService.delete_obj(abs_path)

            return web.json_response(
                data={
                    'status': 'success',
                    'message': f'[{path}] was successfully deleted.'
                })
        except Exception:
            self.__get_exception('An error occurred when deleting file '
                                 f'[{path}]: [{format_exc()}].')
