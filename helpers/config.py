from dotenv import load_dotenv
import os


load_dotenv()

USERNAME = os.environ.get("LOGIN")
PASSWORD = os.environ.get("PASSWORD")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
BASE_URL = os.environ.get('BASE_URL')
