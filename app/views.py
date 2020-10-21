from rest_framework import viewsets
from rest_framework import mixins
from .models import Currency, Item, WatchList, Offer, Inventory, Trade
from .serializers import (
    OfferSerializer,
    WatchListSerializer,
    TradeSerializer,
    CurrencySerializer,
    InventorySerializer,
    ItemSerializer,
)


class CurrencyViewSet(viewsets.ModelViewSet):
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class WatchListViewSet(viewsets.ModelViewSet):
    serializer_class = WatchListSerializer
    queryset = WatchList.objects.all()


class OfferViewSet(viewsets.ModelViewSet):
    serializer_class = OfferSerializer
    queryset = Offer.objects.all()


class InventoryViewSet(viewsets.ModelViewSet):
    serializer_class = InventorySerializer
    queryset = Inventory.objects.all()


class TradeViewSet(viewsets.ModelViewSet):
    serializer_class = TradeSerializer
    queryset = Trade.objects.all()
