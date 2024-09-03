import urls
import allure
import requests

from faker import Faker


class TestCreateHelper:
    @staticmethod
    def generate_create_body():
        fake = Faker()
        login = fake.user_name()
        password = fake.password()
        firstName = fake.first_name()
        body = {
            "login": login,
            "password": password,
            "firstName": firstName
        }
        return body

    def register_new_courier_and_return_login_password(get_new_data):
        body = get_new_data
        response = requests.post(urls.BASE_URL + urls.CREATE_COURIER, data=body)
        if response.status_code == 201:
            return body

