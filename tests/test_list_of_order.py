import allure

from scooterapi import ScooterApi


class TestOrderList:
    @allure.title('Проверка получения списка заказов')
    def test_get_order_list(self):
        order_list = ScooterApi.get_list_of_orders()
        assert order_list.status_code == 200 and 'orders' in order_list.json()