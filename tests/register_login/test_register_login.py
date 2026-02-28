import pytest
from models.user_create_and_login import User_Create_And_Login

class Test_User_Creation_And_Login:

    @pytest.mark.smoke
    def test_create_user(self, user_service, user_register_login_data):
        for data in user_register_login_data:
            user = User_Create_And_Login(
                email=data["email"],
                password=data["password"]
            )
            response = user_service.register_user(user.to_dict())
            self.assert_checks(response)

    @pytest.mark.smoke
    def test_login_user(self, user_service, user_register_login_data):
        for data in user_register_login_data:
            user = User_Create_And_Login(
                email=data["email"],
                password=data["password"]
            )
            response = user_service.login_user(user.to_dict())
            self.assert_checks(response)

    def assert_checks(self, response):
        assert response.status_code == 200
        assert response.json()["_meta"]["powered_by"] == "ReqRes"