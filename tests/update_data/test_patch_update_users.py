import pytest
from models.user_update import Data, Support, Cta, _Meta, User_Update

class Test_Patch_Update_Users:

    @pytest.mark.smoke
    def test_patch_update_users(self, user_service, user_update):
        for data in user_update:
            user = User_Update(
                data = Data(
                    first_name= "Yash",
                    last_name= "Yukti"
                )
            )
            response = user_service.update_single_user_patch(user.to_dict(), 2)
            assert response.status_code == 200
            assert response.json()["data"]["first_name"] == "Yash"
            assert response.json()["data"]["last_name"] == "Yukti"

