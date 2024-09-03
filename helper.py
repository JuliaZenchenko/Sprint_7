from data import TestCreate
class TestCreateHelper:
    @staticmethod
    def modify_create_body_request(key, value):
        body = TestCreate.CREATE_COURIER.copy()
        body[key] = value

        return body

    @staticmethod
    def generate_create_body():
        fake = Faker()

        return TestCreateHelper.modify_create_body_request('login', fake.login())