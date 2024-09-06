import pytest
import allure

from scooterapi import ScooterApi
from data import Order


class TestCreateOrder:
    @allure.title('Проверка создания заказа с разными цветами скутеров')
    @pytest.mark.parametrize("color", [Order.ORDER_1, Order.ORDER_2, Order.ORDER_3])
    def test_create_order(self, color):
        order = ScooterApi.order(color)
        assert order.status_code == 201 and "track" in order.json()