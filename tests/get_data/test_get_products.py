import pytest

class Test_Get_Products:

    @pytest.mark.scope
    def test_get_all_products(self, user_service):
        response = user_service.get_all_products()
        assert response.json()["total_pages"] == 2
        assert response.json()["data"][0]["name"] == "cerulean"
