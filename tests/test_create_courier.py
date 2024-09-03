import allure

from helper import TestCreateHelper
from scooterapi import ScooterApi
from data import TestAuthorization


class TestCreateCourier:
    @allure.title('Проверка, что курьера можно создать c заполнением всех обяз полей и запрос возвращает правильный ответ')
    def test_create_courier(self):
        response = ScooterApi.create_courier(TestCreateHelper.generate_create_body())
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title('Проверка, что нельзя создать двух одинаковых курьеров')
    def test_create_same_courier(self):
        response = ScooterApi.create_courier(TestAuthorization.CREATE_COURIER)
        message = response.json()
        assert response.status_code == 409 and message['message'] == TestAuthorization.MESSAGE_CREATE_DUPLICATE_COURIER

    @allure.title('Проверка, что нельзя создать курьера без логина')
    def test_create_courier_without_login(self):
        response = ScooterApi.create_courier(TestAuthorization.CREATE_COURIER_WITHOUT_LOGIN)
        message = response.json()
        assert response.status_code == 400 and message['message'] == TestAuthorization.MESSAGE_CREATE_COURIER_WITHOUT_DATE


    @allure.title('Проверка, что нельзя создать курьера без пароля')
    def test_create_courier_without_password(self):
        response = ScooterApi.create_courier(TestAuthorization.CREATE_COURIER_WITHOUT_PASSWORD)
        message = response.json()
        assert response.status_code == 400 and message['message'] == TestAuthorization.MESSAGE_CREATE_COURIER_WITHOUT_DATE

