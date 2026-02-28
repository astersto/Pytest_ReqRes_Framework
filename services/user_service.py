from base.base_test import BaseTest
from constants.endpoints import (
    GET_ALL_USERS,GET_SINGLE_USER,GET_ALL_RESOURCES,GET_SINGLE_RESOURCE,GET_ALL_PRODUCTS,
    REGISTER_USER,LOGIN_USER,
    UPDATE_SINGLE_USER,
    DELETE_SINGLE_USER
)

class UserService(BaseTest):

    def get_all_users(self):
        return self.get(GET_ALL_USERS)

    def get_single_user(self, id):
        return self.get(GET_SINGLE_USER.format(id=id))

    def get_all_resources(self):
        return self.get(GET_ALL_RESOURCES)

    def get_single_resource(self, id):
        return self.get(GET_SINGLE_RESOURCE.format(id=id))

    def get_all_products(self):
        return self.get(GET_ALL_PRODUCTS)

    def register_user(self, body):
        return self.post(REGISTER_USER, body)

    def login_user(self, body):
        return self.post(LOGIN_USER,body)

    def update_single_user_put(self, body, id):
        return self.put(UPDATE_SINGLE_USER.format(id=id), body)

    def update_single_user_patch(self, body, id):
        return self.patch(UPDATE_SINGLE_USER.format(id=id), body)

    def delete_single_user(self, id):
        return self.delete(DELETE_SINGLE_USER.format(id=id))