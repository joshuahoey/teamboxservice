from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from PIL import Image
import datetime


# Create your models here.

def name_image(instance, filename):
    return '/'.join(['images', str(instance.name), filename])


class User(AbstractUser):
    phone_number = models.CharField(blank=True, null=True, unique=True, max_length=12)
    registration_date = models.DateField(default=datetime.date.today)
    start_date = models.DateField(blank=True)
    address = models.CharField(blank=True, null=True, max_length=250)
    tokens = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(2)])
    image = models.ImageField(upload_to=name_image, blank=True, null=True)
    ## add ForeignKey fields

