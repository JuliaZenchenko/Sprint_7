# Sprint_7
Цель проекта:
покрыть автоматизированными тестами api сайта: https://qa-scooter.praktikum-services.ru/


Структура проекта:

allure_results - директория с отчетами allure
test - директория, которая содержит тесты:
test_create_courier, ручка: post /api/v1/courier - тестирование создания курьера
test_create_order, ручка: post /api/v1/orders - тестирование создания заказа
test_authorization_courier, ручка: post /api/v1/courier/login - тестирование авторизации курьера в системе
test_list_of_order, ручка: get /api/v1/orders - тестирование получения списка заказов
conftest -фикстуры
data - содержит данные 
urls - содержит все необходимые урлы для запросов
helpers - содержит методы для генерации данных для курьера
scooterapi - содержит методы для тестирования api в тестах