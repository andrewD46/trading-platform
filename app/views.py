from rest_framework import viewsets

from .models import Currency, Item, WatchList, Price, Offer, Inventory, Trade
from .serializers import (
    OfferSerializer,
    PriceSerializer,
    WatchListSerializer,
    TradeSerializer,
    CurrencySerializer,
    InventorySerializer,
    ItemSerializer,
)


# Create your views here.
class CurrencyViewSet(viewsets.ModelViewSet):
    serializer_class = CurrencySerializer
    queryset = Currency


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item


class WatchListViewSet(viewsets.ModelViewSet):
    serializer_class = WatchListSerializer
    queryset = WatchList


class PriceViewSet(viewsets.ModelViewSet):
    serializer_class = PriceSerializer
    queryset = Price


class OfferViewSet(viewsets.ModelViewSet):
    serializer_class = OfferSerializer
    queryset = Offer


class InventoryViewSet(viewsets.ModelViewSet):
    serializer_class = InventorySerializer
    queryset = Inventory


class TradeViewSet(viewsets.ModelViewSet):
    serializer_class = TradeSerializer
    queryset = Trade
