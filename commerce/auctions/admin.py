from django.contrib import admin

from .models import *

# Register your models here.
class ListingsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "image", "dateCreated", "active")

class CommentsAdmin(admin.ModelAdmin):
    list_display = ("id", "stars", "owner", "listing")
    
class BidsAdmin(admin.ModelAdmin):
    list_display = ("listing", "bid", "owner")
    
class WatchlistsAdmin(admin.ModelAdmin):
    list_display = ("id", "owner", "products")

admin.site.register(User)
admin.site.register(Listings, ListingsAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Bids, BidsAdmin)
admin.site.register(Watchlists, WatchlistsAdmin)