import os
import traceback
from dotenv import load_dotenv

env_path = "./.env"
load_dotenv(dotenv_path=env_path)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
model_name = "text-ada-001"

