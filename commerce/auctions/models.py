from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listings(models.Model):
	title = models.CharField(max_length=100)
    # According to documentation TextField correspond to a textarea in HTML
	description = models.TextField()
    # According to documentation PositiveIntegerField allow numbers between 0 and 32767
	bid = models.PositiveSmallIntegerField() 
	image = models.URLField(blank=True)
	category = models.CharField(max_length=100)
	dateCreated = models.DateTimeField(auto_now=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="creator")
        
	def __str__(self):
		  return f"Listing {self.id}, article {self.title}, categories: {self.category}"
	
class Comments(models.Model):
	stars = models.PositiveSmallIntegerField()
	comment = models.TextField()
	owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="commenter")
	listing = models.ForeignKey(Listings, on_delete=models.CASCADE, null=True, blank=True, related_name="product")
	date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"Comment {self.id}, made by {self.owner} to Listing {self.listing}, says: '{self.comment}' on {self.date}. Rated with {self.stars} stars."
	
class Bids(models.Model):
	listing = models.ForeignKey(Listings, on_delete=models.CASCADE, null=True, blank=True, related_name="offer")
	owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="bider")
	bid = models.PositiveSmallIntegerField()

	def __str__(self):
		return f"User {self.owner} offer ${self.bid} on Listing: {self.listing}"
	

class Watchlists(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	products = models.ForeignKey(Listings, on_delete=models.CASCADE, blank=True, related_name="listing")

	def __str__(self):
		return f"Watchlis from user {self.owner}, products: {self.products}"