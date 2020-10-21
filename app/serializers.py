from rest_framework.serializers import ModelSerializer

from .models import Currency, Item, WatchList, Price, Offer, Inventory, Trade, User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class InventorySerializer(ModelSerializer):
    class Meta:
        model = Inventory
        fields = "__all__"


class WatchListSerializer(ModelSerializer):
    class Meta:
        model = WatchList
        fields = "__all__"


class CurrencySerializer(ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class OfferSerializer(ModelSerializer):
    class Meta:
        model = Offer
        fields = "__all__"


class TradeSerializer(ModelSerializer):
    class Meta:
        model = Trade
        fields = '__all__'
