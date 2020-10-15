from rest_framework.serializers import ModelSerializer

from .models import Currency, Item, WatchList, Price, Offer, Inventory, Trade


class CurrencySerializer(ModelSerializer):
    class Meta:
        model = Currency
        fields = ("id", "code", "name", "url")


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ("id", "code", "name", "price", "currency", "details", "url")


class WatchListSerializer(ModelSerializer):
    class Meta:
        model = WatchList
        fields = ("id", "user", "item", "url")


class PriceSerializer(ModelSerializer):
    class Meta:
        model = Price
        fields = ("id", "currency", "item", "price", "date", "url")


class OfferSerializer(ModelSerializer):
    class Meta:
        model = Offer
        fields = (
            "id",
            "user",
            "item",
            "entry_quantity",
            "quantity",
            "order_type",
            "price",
            "is_active",
            "url",
        )


class InventorySerializer(ModelSerializer):
    class Meta:
        model = Inventory
        fields = ("id", "user", "item", "quantity", "url")


class TradeSerializer(ModelSerializer):
    class Meta:
        model = Trade
        fields = (
            "id",
            "seller",
            "buyer",
            "quantity",
            "unit_price",
            "description",
            "buyer_offer",
            "seller_offer",
        )
