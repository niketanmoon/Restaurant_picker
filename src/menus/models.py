from django.conf import settings
from django.db import models
from django.urls import reverse
from restaurants.models import RestaurantLocation


User = settings.AUTH_USER_MODEL
# Create your models here.
class Item(models.Model):
    #Associations
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(RestaurantLocation, on_delete=models.CASCADE)

    #Item Stuff
    #name , contents, excludes, public, timestamp, updated
    name = models.CharField(max_length = 120)
    contents  = models.TextField(help_text='Separate each item by comma')
    excludes  = models.TextField(
        blank=True,
        null=True,
        help_text='Separate each item by comma'
    )
    public = models.BooleanField(default=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated','-timestamp']

    def get_absolute_url(self):
        return reverse('menus:detail',kwargs={'pk':self.pk})

    def get_contents(self):
        return self.contents.split(",")

    def get_excludes(self):
        return self.excludes.split(",")
