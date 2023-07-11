from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("newListing", views.new_listing, name="newListing"),
    path("newComment", views.new_comment, name="newComment"),
    path("newBid", views.new_bid, name="newBid"),
    path("<int:id>", views.listing_item, name="itemListing")
]
