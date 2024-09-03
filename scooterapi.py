import requests
import urls


class ShopApi:
    @staticmethod
    def create(body):
        return requests.post(urls.BASE_URL + urls.CREATE_COURIER, json=body)

    @staticmethod
    def login(body):
        return requests.post(urls.BASE_URL + urls.LOGIN_COURIER, data=body)
