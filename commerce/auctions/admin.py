from django.contrib import admin

from .models import *

# Register your models here.
class ListingsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "image", "dateCreated")


admin.site.register(User)
admin.site.register(Listings, ListingsAdmin)