import pytest

class Test_Get_Users:

    @pytest.mark.smoke
    def test_get_all_users(self, user_service):
        response = user_service.get_all_users()
        assert response.status_code == 200
        assert response.json()["data"][0]["email"] == "george.bluth@reqres.in"

    @pytest.mark.smoke
    def test_get_single_user(self, user_service):
        response = user_service.get_single_user(2)
        assert response.status_code == 200
        assert response.json()["data"]["email"] == "janet.weaver@reqres.in"