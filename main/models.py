from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()

# Pocket class to contain items
class Pocket(models.Model):
    items = models.ManyToManyField(Item)
    name = models.CharField(max_length=255)