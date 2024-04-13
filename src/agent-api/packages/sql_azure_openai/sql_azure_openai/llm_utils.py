import os

from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI

load_dotenv()

AZURE_OPENAI_API_KEY = os.environ.get("AZURE_OPENAI_API_KEY")
OPENAI_API_VERSION = os.environ.get("OPENAI_API_VERSION")
AZURE_OPENAI_API_ENDPOINT = os.environ.get("AZURE_OPENAI_API_ENDPOINT")
AZURE_OPENAI_DEPLOYMENT_NAME = os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME")

llm = AzureChatOpenAI(
    api_version=OPENAI_API_VERSION,
    api_key=AZURE_OPENAI_API_KEY,
    deployment_name=AZURE_OPENAI_DEPLOYMENT_NAME,
)
