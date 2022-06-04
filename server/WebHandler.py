"""Web handler for the file server."""

import base64
import json
import logging
from traceback import format_exc

from aiohttp import web

from config.config import config
import server.FileService as FileService
from utils.log_config import Color


class WebHandler:
    """aiohttp handler with coroutines."""

    def __init__(self) -> None:
        FileService.change_dir(config.dir)

    async def handle(self, request: web.Request, *args, **kwargs) -> web.Response:
        """Basic coroutine for connection testing.

        Args:
            request (Request): aiohttp request.

        Returns:
            Response: JSON response with status.
        """
        return web.json_response(data={
            'status': 'success'
        })

    async def change_dir(self, request: web.Request, *args, **kwargs) -> web.Response:
        """Coroutine for changing working directory with files.

        Args:
            request (Request): aiohttp request, contains JSON in body. JSON format:
            {
                "path": "string. Directory path. Required",
            }.

        Returns:
            Response: JSON response with success status and success message or error status and error message.

        Raises:
            HTTPBadRequest: 400 HTTP error, if error.
        """
        try:
            Color.logging_color(f'(!) Received a request to change the directory!', 'warn')
            path = request.match_info.get('path', '')
            logging.info(f'directory to change = [{path}]')
            autocreate = False if request.query.get('autocreate', '').lower() == 'false' else True
            logging.info(f'autocreate parameter = [{autocreate}].')

            FileService.change_dir(path, autocreate=autocreate)

            return web.json_response(data={
                'status': 'success',
                'message': f'The current directory has been successfully changed to [{path}].'
            })
        except Exception:
            data = {
                'status': 'error',
                'message': f'An error occurred when changing the directory: [{format_exc()}].'
            }
            raise web.HTTPBadRequest(body=str(data))

    async def get_files(self, request: web.Request, *args, **kwargs) -> web.Response:
        """Coroutine for getting info about all files in working directory.

        Args:
            request (Request): aiohttp request.

        Returns:
            Response: JSON response with success status and data or error status and error message.

        Raises:
            HTTPBadRequest: 400 HTTP error, if error.
        """
        try:
            Color.logging_color('(!) A request was received to get a list of files from directory :'
                                f'[{config.dir}].', 'warn')

            files = FileService.get_files()

            return web.json_response(data={
                'status': 'success',
                'data': files
            })
        except Exception:
            data = {
                'status': 'error',
                'message': f'An error occurred while receiving files: [{format_exc()}].'
            }
            raise web.HTTPBadRequest(body=str(data))

    async def get_file_data(self, request: web.Request, *args, **kwargs) -> web.Response:
        """Coroutine for getting full info about file in working directory.

        Args:
            request (Request): aiohttp request, contains filename and is_signed parameters.

        Returns:
            Response: JSON response with success status and data or error status and error message.

        Raises:
            HTTPBadRequest: 400 HTTP error, if error.
        """
        try:
            Color.logging_color('(!) A request for file data has been received!', 'warn')
            file_path = request.match_info.get('file_path', '')
            logging.info(f'file_path = [{file_path}].')

            file_data = FileService.get_file_data(file_path)

            return web.json_response(data={'status': 'success', 'data': file_data})
        except Exception:
            data = {
                'status': 'error',
                'message': (f'An error occurred while extracting data from file '
                            f'[{file_path}]: [{format_exc()}].')
            }
            raise web.HTTPBadRequest(body=str(data))    # todo вопрос (?)

    async def create_file(self, request: web.Request, *args, **kwargs) -> web.Response:
        """Coroutine for creating file.

        Args:
            request (Request): aiohttp request, contains bytes in body. Optional.

        Returns:
            Response: JSON response with success status and data or error status and error message.

        Raises:
            HTTPBadRequest: 400 HTTP error, if error.
        """
        try:
            Color.logging_color('(!) Received a request to create a file!', 'warn')
            file_path = request.match_info.get('file_path', '')
            logging.info(f'file_path = [{file_path}].')

            # Checking for the presence of content in the request.
            try:
                content = await request.read()
            except Exception:
                content = None

            file_data = FileService.create_file(file_path, content=content)

            return web.json_response(data={'status': 'success', 'data': file_data})
        except Exception:
            data = {
                'status': 'error',
                'message': (f'An error occurred while creating file [{file_path}]: [{format_exc()}].')
            }
            raise web.HTTPBadRequest(body=str(data))

    async def delete_file(self, request: web.Request, *args, **kwargs) -> web.Response:
        """Coroutine for deleting file.

        Args:
            request (Request): aiohttp request, contains filename.

        Returns:
            Response: JSON response with success status and success message or error status and error message.

        Raises:
            HTTPBadRequest: 400 HTTP error, if error.

        """
        try:
            Color.logging_color('(!) Received a request to delete file!', 'warn')
            file_path = request.match_info.get('file_path', '')
            logging.info(f'file_path = [{file_path}].')

            FileService.delete_file(file_path)

            return web.json_response(data={
                'status': 'success',
                'message': f'file {file_path} was successfully deleted.'
            })
        except Exception:
            data = {
                'status': 'error',
                'message': (f'An error occurred when deleting file [{file_path}]: [{format_exc()}].')
            }
            raise web.HTTPBadRequest(body=str(data))
