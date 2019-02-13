import uuid

from django.db import models


class Menu(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.description


class Order(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=50)
    custom_spec = models.CharField(max_length=250)


class Company(models.Model):
    name = models.CharField(max_length=250)
    slack_webhook = models.CharField(max_length=250, default=None)

    def __str__(self):
        return self.name

class Meal(models.Model):
    description = models.CharField(max_length=250)
    menu = models.ManyToManyField(Menu)
