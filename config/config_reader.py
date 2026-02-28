import os
from dotenv import load_dotenv

load_dotenv()

BASE_URI = os.getenv("BASE_URI")
X_API_KEY = os.getenv("X_API_KEY")
API_AUTH_HEADER = os.getenv("API_AUTH_HEADER")
TIMEOUT = int(os.getenv("TIMEOUT"))

HEADERS = {
    "Content-Type" : "application/json",
    API_AUTH_HEADER : X_API_KEY
}