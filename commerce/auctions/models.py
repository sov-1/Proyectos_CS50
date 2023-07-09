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
        
	def __str__(self):
		  return f"Listing {self.id}, article {self.title}, categories: {self.category}"