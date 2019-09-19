from django.conf import settings
from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from .utils import unique_slug_generator

from restaurants.validators import validate_category

User = settings.AUTH_USER_MODEL
# Create your models here.
class RestaurantLocation(models.Model):
    owner       = models.ForeignKey(
                    User,
                    on_delete = models.CASCADE,
                    related_name="restaurant_records"
                )
    name        = models.CharField(max_length = 120)
    location    = models.CharField(max_length = 120, null=True, blank=True)
    category    = models.CharField(max_length = 120, null=True, blank=True,validators=[validate_category])
    timestamp   = models.DateTimeField(auto_now_add=True, null=True)
    updated     = models.DateTimeField(auto_now=True)
    slug        = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name

    def get_absolute_url(self):
        return reverse('restaurant-detail',kwargs={'slug':self.slug})

def rl_pre_save_receiver(sender,instance,*args,**kwargs):
    instance.category = instance.category.capitalize()
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver,sender=RestaurantLocation)
