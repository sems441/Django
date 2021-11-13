from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    image = models.TextField()
    price = models.FloatField()
    release_date = models.DateField()
    lte_exists = models.TextField()
    slug = models.SlugField()
