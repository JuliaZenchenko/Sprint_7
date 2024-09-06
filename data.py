class TestAuthorization:
    CREATE_COURIER = {
        "login": "ninja",
        "password": "1234",
        "firstName": "saske"
    }

    CREATE_COURIER_WITHOUT_LOGIN = {
        "password": "1234",
        "firstName": "saske"
    }

    CREATE_COURIER_WITHOUT_PASSWORD = {
        "login": "ninja",
        "firstName": "saske"
    }

    AUTH_COURIER_WITH_EMPTY_BODY: dict[str, str] = {
        "login": "",
        "password": "",
         }

    AUTH_NON_EXISTEN_COURIER: dict[str, str] = {
        "login": "tratata",
        "password": "133589",
    }

    MESSAGE_CREATE_COURIER = True
    MESSAGE_CREATE_DUPLICATE_COURIER = 'Этот логин уже используется. Попробуйте другой.'
    MESSAGE_CREATE_COURIER_WITHOUT_DATE = 'Недостаточно данных для создания учетной записи'
    MESSAGE_AUTHORIZATION_COURIER_WITH_EMPTY_BODY = 'Недостаточно данных для входа'
    MESSAGE_AUTHORIZATION_NON_EXISTEN_COURIER = 'Учетная запись не найдена'


class Order:
    ORDER_1 = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK"]
    }

    ORDER_2 = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK" or "GREY"]
    }

    ORDER_3 = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": []
    }




