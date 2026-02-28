import json
import os
import pytest
from services.user_service import UserService

@pytest.fixture(scope="session")
def user_service():
    return UserService()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@pytest.fixture(scope="session")
def user_register_login_data():
    with open(os.path.join(BASE_DIR, "testdata", "user_login_register_data.json")) as file:
        return json.load(file)

@pytest.fixture(scope="session")
def user_update():
    with open(os.path.join(BASE_DIR, "testdata", "user_update.json")) as file:
        return json.load(file)