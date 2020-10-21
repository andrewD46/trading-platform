import pytest
from faker import Faker
from rest_framework.test import APIClient

from app.models import User, Currency, Item, Inventory, Offer, WatchList
from app.serializers import UserSerializer, CurrencySerializer, InventorySerializer, OfferSerializer, \
    WatchListSerializer


@pytest.fixture
def api_client():
    """Function creates client object"""
    return APIClient()


@pytest.fixture
def user():
    faker = Faker()
    request_data = {
        "username": faker.user_name(),
        "password": faker.password(),
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "email": faker.email(),
        "balance": 5.0
    }
    return request_data


@pytest.fixture
def user_from_db(user):
    user_obj = User.objects.create(username=user['username'],
                                   password=user['password'],
                                   first_name=user['first_name'],
                                   last_name=user['last_name'],
                                   email=user['email'],
                                   balance=user['balance'],
                                   )
    return user_obj


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


@pytest.fixture
def create_inventory(user_from_db):
    first_item = Item.objects.create(code='AAPL',
                                     name='Apple',
                                     actual_price=118,
                                     is_active=True
                                     )
    second_item = Item.objects.create(code='TSLA',
                                      name='Tesla',
                                      actual_price=422,
                                      is_active=True)
    Inventory.objects.create(user=user_from_db, item=first_item, quantity=5)
    Inventory.objects.create(user=user_from_db, item=second_item, quantity=5)
    user_inventory = Inventory.objects.filter(user=user_from_db)
    return user_inventory


@pytest.fixture
def user_inventory_serializes(create_inventory):
    serializer = InventorySerializer(create_inventory, many=True)
    serializer_data = serializer.data
    return serializer_data


@pytest.fixture
def create_offers(user_from_db, create_inventory):
    """Func create offer in db"""
    inventory_obj = create_inventory[0]
    item = inventory_obj.item
    item_quantity = inventory_obj.quantity
    Offer.objects.create(user=user_from_db,
                         item=item,
                         order_type=1,
                         entry_quantity=item_quantity,
                         quantity=item_quantity,
                         price=7)
    Offer.objects.create(user=user_from_db,
                         item=item,
                         order_type=0,
                         entry_quantity=item_quantity,
                         quantity=item_quantity,
                         price=5)

    offers = Offer.objects.filter(user=user_from_db)
    return offers


@pytest.fixture
def offer_serializes(create_offers):
    serializer = OfferSerializer(create_offers, many=True)
    serializer_data = serializer.data
    return serializer_data


@pytest.fixture
def create_watch_list(user_from_db, create_inventory):
    """Func create offer in db"""
    inventory_obj = create_inventory[0]
    item = inventory_obj.item
    WatchList.objects.create(user=user_from_db, item=item)
    WatchList.objects.create(user=user_from_db, item=item)
    watch_list = WatchList.objects.filter(user=user_from_db)
    return watch_list


@pytest.fixture
def watch_list_serializes(create_watch_list):
    serializer = WatchListSerializer(create_watch_list, many=True)
    serializer_data = serializer.data
    return serializer_data


@pytest.mark.django_db
def test_get_currency(api_client, currency_serializes):
    url = "/currency/"
    response = api_client.get(url)
    response_data = response.data
    assert currency_serializes == response_data


@pytest.mark.django_db
def test_get_currency_with_pk(api_client, currency_serializes):
    currency_serializes_data = currency_serializes[0]
    currency_id = currency_serializes_data['id']
    url = f"/currency/{currency_id}/"
    response = api_client.get(url)
    response_data = response.data
    assert currency_serializes_data == response_data


@pytest.mark.django_db
def test_get_inventory(api_client, user_inventory_serializers):
    url = "/inventory/"
    response = api_client.get(url)
    response_data = response.data
    assert user_inventory_serializers == response_data


@pytest.mark.django_db
def test_get_inventory_with_pk(api_client, user_inventory_serializers):
    user_inventory_serializers_data = user_inventory_serializers[0]
    inventory_id = user_inventory_serializers_data['id']
    url = f"/inventory/{inventory_id}/"
    response = api_client.get(url)
    response_data = response.data
    assert user_inventory_serializers_data == response_data


@pytest.mark.django_db
def test_create_offers(api_client, offer_serializes):
    url = '/offer/'
    response = api_client.get(url)
    response_data = response.data
    assert offer_serializes == response_data


@pytest.mark.django_db
def test_create_watch_list(api_client, watch_list_serializes):
    url = '/watch_list/'
    response = api_client.get(url)
    response_data = response.data
    assert watch_list_serializes == response_data
