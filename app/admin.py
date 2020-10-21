from django.contrib import admin

from .models import Currency, Item, WatchList, Price, Offer, Inventory, Trade, User

admin.site.register(Currency)
admin.site.register(Item)
admin.site.register(WatchList)
admin.site.register(Price)
admin.site.register(Offer)
admin.site.register(Inventory)
admin.site.register(Trade)
admin.site.register(User)
