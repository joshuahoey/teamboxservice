from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from PIL import Image
import datetime


# Create your models here.

class Subscription(models.Model):
    pass


class StandardBox(models.Model):
    pass


class ClothingItem(models.Model):
    pass


def name_image(instance, filename):
    return '/'.join(['images', str(instance.username), filename])


class User(AbstractUser):
    phone_number = models.CharField(blank=True, null=True, unique=True, max_length=12)
    start_date = models.DateField(blank=True, null=True)
    address = models.CharField(blank=True, null=True, max_length=250)
    tokens = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(2)])
    image = models.ImageField(upload_to=name_image, blank=True, null=True)
    is_employee = models.BooleanField(null=True)
    subscription_type = models.ForeignKey(Subscription, on_delete=models.PROTECT, null=True)
    standard_box = models.ForeignKey(StandardBox, on_delete=models.PROTECT, null=True)
    bonus_item = models.ForeignKey(ClothingItem, on_delete=models.PROTECT, null=True)
