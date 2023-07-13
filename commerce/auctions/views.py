from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *
from .forms import *


def index(request):
    return render(request, "auctions/index.html",{
        "listings": Listings.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required(login_url='login')
def new_listing(request):
    if request.method == "POST":

        # fills a form with user supplied data
        listingForm = NewListing(request.POST)
        if listingForm.is_valid():
            
            # save data using models.py and goes back to index
            l = Listings()
            # take each field using "form.cleaned_data['attr_name']"
            l.title = listingForm.cleaned_data["title"]
            l.description = listingForm.cleaned_data["description"]
            l.bid = listingForm.cleaned_data["bid"]
            l.image = listingForm.cleaned_data["image"]
            l.category = listingForm.cleaned_data["category"]
            l.owner = User.objects.get( pk=int( request.POST["owner"] ) )
            l.save()

            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/newListing.html", {
                "listingForm": listingForm
            })
    
	# default view 
    return render(request, "auctions/newListing.html", {
        "listingForm": NewListing()
	})

def listing_item(request, id):
    l = Listings.objects.get(pk=id)
    c = Comments.objects.filter(listing=id)
    b = Bids.objects.filter(listing = id)
    u = 'none user bid yet'
	# find higher bid
    h = l.bid 
    for offers in b:
        if offers.bid > h:
            h = offers.bid
            u = offers.owner

    return render(request, "auctions/itemListing.html", {
        "item": l,
        "comments":c,
        "offers":b,
        "higherBid": h,
        "higherBidUser": u
    })

@login_required(login_url='login')
def new_comment(request):
    if request.method == 'POST':
        commentForm = NewComment(request.POST)
        if commentForm.is_valid():
            c = Comments()
            c.stars = commentForm.cleaned_data["stars"]
            c.comment = commentForm.cleaned_data["comment"]
            c.owner = User.objects.get(pk=int(commentForm.cleaned_data["owner"]) )
            c.listing = Listings.objects.get(pk=int(commentForm.cleaned_data["listing"]))
            c.save()
            return HttpResponseRedirect(reverse("itemListing", kwargs={'id':commentForm.cleaned_data["listing"] }))
        else:
            pass


@login_required(login_url='login')
def new_bid(request):
    if request.method == 'POST':
        b = Bids()
        b.bid = int(request.POST["offerBid"])
        b.owner = User.objects.get( pk=int(request.POST["owner"]) )
        b.listing = Listings.objects.get( pk=int(request.POST["listing"]) )
        b.save()
        return HttpResponseRedirect(reverse("itemListing", kwargs={'id':request.POST["listing"]}))
    else:
        pass
    
def changeStateAuction(request):
    if request.method == 'POST':
        item = request.POST["itemToChange"]
        l = Listings.objects.get(pk=int(item))
        if l.active == True:
            l.active = False
        else:
            l.active = True
        l.save()
        return HttpResponseRedirect(reverse('itemListing', kwargs={'id':item}))
    return HttpResponseRedirect(reverse('index'))

@login_required(login_url='login')
def watchlist(request, itemId, userId):
    l = Listings.objects.get(pk=itemId)
    u = User.objects.get(pk=userId)
    w = Watchlists.objects.filter(owner=userId, products=itemId)

    list = Watchlists()
    list.owner = u
    list.products = l
    list.save()
    
    return HttpResponseRedirect(reverse("index"))

def view_watchlist(request):
    w = Watchlists.objects.filter(owner = 3)
    return render(request, "auctions/watchlist.html",{
        "listings": w
    })