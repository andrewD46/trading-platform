from rest_framework.test import APIClient
from app.models import Currency
import pytest
from app.serializers import CurrencySerializer


@pytest.fixture
def api_client():
    """Function creates client object"""
    return APIClient()


@pytest.fixture
def create_currency():
    """Function creates currencies objects"""
    Currency.objects.create(code='USD', name='Dollar')
    Currency.objects.create(code='EUR', name='Euro')
    currencies = Currency.objects.all()
    return currencies


@pytest.fixture
def currency_serializes(create_currency):
    """Function serializes currency obj"""
    serializer = CurrencySerializer(create_currency, many=True)
    serializer_data = serializer.data
    return serializer_data
