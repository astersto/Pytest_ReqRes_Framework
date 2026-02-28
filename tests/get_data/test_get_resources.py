import pytest

@pytest.mark.smoke
class Test_Get_Resources:

    def test_get_all_resources(self, user_service):
        response = user_service.get_all_resources()
        assert response.status_code == 200
        assert response.json()["total_pages"] == 2
        assert response.json()["data"][0]["name"] == "cerulean"

    def test_get_single_resource(self, user_service):
        response = user_service.get_single_resource(3)
        assert response.status_code == 200
        assert response.json()["data"]["name"] == "true red"