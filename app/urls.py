from rest_framework.routers import DefaultRouter

from app.views import (
    CurrencyViewSet,
    ItemViewSet,
    WatchListViewSet,
    OfferViewSet,
    InventoryViewSet,
    TradeViewSet
)


router = DefaultRouter()
router.register('inventory', InventoryViewSet)
router.register('currency', CurrencyViewSet)
router.register('offer', OfferViewSet)
router.register('trade', TradeViewSet)
router.register('item', ItemViewSet)
router.register('watch_list', WatchListViewSet)
urlpatterns = router.urls
