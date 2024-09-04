import allure
import pytest
from helper import CreateHelper
from scooterapi import ScooterApi
from data import TestAuthorization


class TestAuthorizationCourier:
    @allure.title('Проверка авторизации курьера с заполнением всех обязательных полей')
    def test_login_courier_positive(self, get_new_data):
        response = ScooterApi.create_and_login_courier(get_new_data)
        assert response.status_code == 200 and 'id' in response.json()

    @allure.title('Проверка авторизации курьера c пустыми полями')
    def test_login_courier_with_empty_body(self):
        response = ScooterApi.login(TestAuthorization.AUTH_COURIER_WITH_EMPTY_BODY)
        assert response.status_code == 400 and response.json()[
            'message'] == TestAuthorization.MESSAGE_AUTHORIZATION_COURIER_WITH_EMPTY_BODY

    @allure.title('Проверка авторизации несуществующего курьера')
    def test_login_non_existen_courier(self):
        response = ScooterApi.login(TestAuthorization.AUTH_NON_EXISTEN_COURIER)
        assert response.status_code == 404 and response.json()[
            'message'] == TestAuthorization.MESSAGE_AUTHORIZATION_NON_EXISTEN_COURIER

