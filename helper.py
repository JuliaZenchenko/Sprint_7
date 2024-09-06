import urls
import allure
import requests

from faker import Faker


class CreateHelper:
    @allure.step('Генерация логина пароля имени для курьера')
    def generate_create_body():
        fake = Faker()
        login = fake.user_name()
        password = fake.password()
        firstname = fake.first_name()
        body = {
            "login": login,
            "password": password,
            "firstname": firstname
        }
        return body


