import mysql.connector


class MySQLManager:
    """A base class for mysql database connection."""

    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        print("Connecting to the database...")
        self.connection = mysql.connector.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database,

        )
        print("Connected successfully!")
        return self.connection

    def disconnect(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    def execute_saved_log_query(self, name_test, execution_time, status):
        if not self.connection:
            raise Exception("Not connected to the database.")
        cursor = self.connection.cursor()
        query = "INSERT INTO tests_status (name_test, execution_time, status) VALUES (%s, %s, %s)"
        cursor.execute(query, (name_test, execution_time, status))
        self.connection.commit()
        return cursor
