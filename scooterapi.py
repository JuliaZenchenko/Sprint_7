import allure
import requests
import urls


class ScooterApi:

    @staticmethod
    @allure.step('Логин курьера в системе')
    def login(body):
        return requests.post(urls.BASE_URL + urls.LOGIN_COURIER, data=body)

    @staticmethod
    @allure.step('Создание заказа')
    def order(body):
        return requests.post(urls.BASE_URL + urls.ORDER, json=body)

    @staticmethod
    @allure.step('Получение списка заказов')
    def get_list_of_orders():
        return requests.get(urls.BASE_URL + urls.LIST_OF_ORDERS)

    @staticmethod
    @allure.step('Удаление курьера в системе')
    def delete_courier(body):
        response = ScooterApi.login(body)
        courier_id = response.json().get("id")
        requests.delete(f'{urls.BASE_URL}/{courier_id}')

    @staticmethod
    @allure.step('Получение id курьера из системы')
    def courier_id(body):
        response = ScooterApi.login(body)
        return response.json().get("id")


    @allure.step('Создание курьера')
    def create_courier(body):
        return requests.post(urls.BASE_URL + urls.CREATE_COURIER, json=body)

    @allure.step('Создание нового курьера в системе и получение его логина и пароля')
    def register_new_courier_and_return_login_password(self, get_new_data):
        body = get_new_data
        response = requests.post(urls.BASE_URL + urls.CREATE_COURIER, json=body)
        if response.status_code == 201:
            return body

    @staticmethod
    @allure.step('Создание и логин курьера')
    def create_and_login_courier(payload):
        requests.post(urls.BASE_URL + urls.CREATE_COURIER, data=payload)
        response = requests.post(urls.BASE_URL + urls.LOGIN_COURIER, data=payload)
        return response

