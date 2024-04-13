import os
from sqlalchemy import create_engine
from langchain.sql_database import SQLDatabase


class DatabaseUtils:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        conn_str = os.getenv("SQL_CONN_STR")
        engine_azure = create_engine(conn_str, echo=False)
        self.db = SQLDatabase(engine=engine_azure, schema="SalesLT")

    def get_database(self):
        return self.db
