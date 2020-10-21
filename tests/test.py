import pytest
from tests.fixtures import api_client, currency_serializes


@pytest.mark.django_db
def test_get_currency(api_client, currency_serializes):
    url = '/currency/'
    response = api_client.get(url)
    response_data = response.data
    assert currency_serializes == response_data
