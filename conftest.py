import pytest

from helper import *


@pytest.fixture
def get_new_data():
    payload = TestCreateHelper.generate_create_body()

    yield payload