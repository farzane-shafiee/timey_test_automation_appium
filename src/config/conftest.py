import os
import datetime
import yaml
import json
from src.db_connection.mysql_db import MySQLManager


class ConfigTest:
    mysql_manager = None

    @classmethod
    def read_data_device(cls, file_path):
        with open(file_path) as file:
            data_device = yaml.safe_load(file)
            json_data = json.dumps(data_device)
            return json.loads(json_data)

    @classmethod
    def getting_os_date_time(cls):
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime('%Y-%m-%d %H')
        return formatted_datetime

    @classmethod
    def initialize_mysql_manager(cls):
        db_host = os.environ.get('DB_HOST')
        db_user = os.environ.get('DB_USER')
        db_password = os.environ.get('DB_PASSWORD')
        db_port = os.environ.get('DB_PORT')
        db_database = os.environ.get('DB_DATABASE')

        # Check if environment variables are not None
        assert db_host is not None, 'DB_HOST is not set'
        assert db_user is not None, 'DB_USER is not set'
        assert db_password is not None, 'DB_PASSWORD is not set'
        assert db_port is not None, 'DB_PORT is not set'
        assert db_database is not None, 'DB_DATABASE is not set'

        # Connect to Mysql
        cls.mysql_manager = MySQLManager(
            host=db_host,
            user=db_user,
            password=db_password,
            port=int(db_port),
            database=db_database,
        )
        cls.mysql_manager.connect()
