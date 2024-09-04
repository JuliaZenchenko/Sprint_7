import pytest


from helper import CreateHelper
from scooterapi import ScooterApi


@pytest.fixture(scope='function')
def get_new_data():
    payload = CreateHelper.generate_create_body()

    yield payload

    ScooterApi.delete_courier(payload)



