from django.db import models
from django.db.models import Model


# Create your models here.


class Nursery(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    district = models.CharField(max_length=30)
    taluka = models.CharField(max_length=30)
    incharge = models.CharField(max_length=30)
    mobile = models.IntegerField()
    photo = models.ImageField(default='default.jpg',upload_to='images/')
