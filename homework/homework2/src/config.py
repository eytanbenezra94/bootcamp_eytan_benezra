from dotenv import load_dotenv
import os

def load_env():
    load_dotenv()

def get_key(name="API_KEY"):
    return os.getenv(name)