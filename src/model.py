import os

from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from langchain_openai import AzureChatOpenAI
from sqlalchemy import create_engine

load_dotenv()


class Singleton:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls)
        return cls._instances[cls]


class DBSingleton(Singleton):
    def __init__(self):
        conn_str = os.getenv("SQL_CONN_STR")
        engine_azure = create_engine(conn_str, echo=False)
        self.db = SQLDatabase(engine=engine_azure, schema="SalesLT")


class LLM_Singleton(Singleton):
    def __init__(self):
        AZURE_OPENAI_API_KEY = os.environ.get("AZURE_OPENAI_API_KEY")
        OPENAI_API_VERSION = os.environ.get("OPENAI_API_VERSION")
        AZURE_OPENAI_DEPLOYMENT_NAME = os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME")

        self.llm = AzureChatOpenAI(
            api_version=OPENAI_API_VERSION,
            api_key=AZURE_OPENAI_API_KEY,
            deployment_name=AZURE_OPENAI_DEPLOYMENT_NAME,
        )


db_singleton = DBSingleton()
db = db_singleton.db

llm_singleton = LLM_Singleton()
llm = llm_singleton.llm
