import pytest

class Test_Delete_Users:

    @pytest.mark.smoke
    def test_delete_users(self, user_service):
        response = user_service.delete_single_user(2)
        assert response.status_code == 204