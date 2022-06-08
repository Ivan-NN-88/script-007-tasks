"""Working with user."""

import logging

import psycopg2
from psycopg2.extensions import AsIs

from config.config import config
from utils.log import Color


class UserDataBase:
    """Working with the user database"""

    def __init__(self):
        self.conn = psycopg2.connect(**config.db)
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()
        self.table = config.user_table_name
        self.tableAs = AsIs(self.table)
        # I check the availability of the necessary table in the database.
        # If not, I create it.
        self.__get_user_table()

    def __del__(self):
        # Close user database.
        self.cursor.close()
        self.conn.close()

    def __get_user_table(self) -> None:
        """
        Checking the availability of the required table in the database.
        If not, create a database.
        """
        logging.info(f'Getting a table [{self.table}] from the database...')

        self.cursor.execute(
            "select * from information_schema.tables where table_name=%s",
            (self.table, ))
        if not self.cursor.rowcount:
            Color.logging_color(f'Table [{self.table}] not found! Creating...',
                                'warn')

            query = '''create table if not exists %s (
                    id uuid primary key,
                    username varchar(20) not null,
                    userpass varchar(255) not null,
                    hiredate timestamp
                    )
                    '''
            self.cursor.execute(query, (self.tableAs, ))

        logging.info(f'Table [{self.table}] is obtained from the database.')

    def login(self, username: str, password: str) -> bool:
        """
        Checking the user for the presence
        of records in the database and login.
        """
        query = '''select username, userpass from %s
                where username=%s and userpass=%s
                '''
        self.cursor.execute(query, (self.tableAs, username))
        for record in self.cursor.fetchall():
            print(record)

        ...     # TODO need to finish

    def check_auth(self, token: str) -> bool:
        ...     # TODO need to finish

    def logout(self, token: str) -> None:
        ...     # TODO need to finish

    def register(self, username: str, password: str) -> None:
        ...     # TODO need to finish
