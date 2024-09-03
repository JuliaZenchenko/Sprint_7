import requests
import urls


class ScooterApi:
    @staticmethod
    def create_courier(body):
        return requests.post(urls.BASE_URL + urls.CREATE_COURIER, json=body)

    @staticmethod
    def login(body):
        return requests.post(urls.BASE_URL + urls.LOGIN_COURIER, json=body)

    @staticmethod
    def order(body):
        return requests.post(urls.BASE_URL + urls.ORDER, json=body)

    @staticmethod
    def get_list_of_orders():
        return requests.get(urls.BASE_URL + urls.LIST_OF_ORDERS)

    @staticmethod
    def delete_courier(body):
        response = ScooterApi.login(body)
        courier_id = response.json().get("id")
        if courier_id:
            requests.delete(f'{urls.BASE_URL}/{courier_id}')

    @staticmethod
    def get_courier_id(body):
        response = ScooterApi.login(body)
        return response.json().get("id")