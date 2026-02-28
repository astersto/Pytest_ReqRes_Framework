import pytest
from models.user_update import Data, Support, _Meta, Cta, User_Update


class Test_Put_Update_Users:

    @pytest.mark.smoke
    def test_put_update_users(self, user_service, user_update):
        for data in user_update:
            user = User_Update(
                data=Data(
                    id=data["data"]["id"],
                    email=data["data"]["email"],
                    first_name= "LOL",
                    last_name=data["data"]["last_name"],
                    avatar=data["data"]["avatar"]
                ),
                support=Support(
                    url=data["support"]["url"],
                    text=data["support"]["text"]
                ),
                _meta=_Meta(
                    powered_by=data["_meta"]["powered_by"],
                    docs_url=data["_meta"]["docs_url"],
                    upgrade_url=data["_meta"]["upgrade_url"],
                    example_url=data["_meta"]["example_url"],
                    variant=data["_meta"]["variant"],
                    message=data["_meta"]["message"],
                    context=data["_meta"]["context"],
                    cta=Cta(
                        label=data["_meta"]["cta"]["label"],
                        url=data["_meta"]["cta"]["url"]
                    )
                )
            )
            response = user_service.update_single_user_put(user.to_dict(), 2)
            assert response.status_code == 200
            assert response.json()["data"]["first_name"] == "LOL"
