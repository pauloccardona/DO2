from django.db import models
import uuid

# Create your models here.
class Order(models.Model):
    id = models.UUIDField(
        primary_key= True,
        default = uuid.uuid4,
        editable = False
    )

    customer = models.CharField(max_length=64, blank=True, null= False)
    address = models.CharField(max_length=64, blank=True, null= False)

class Waitress(models.Model):
    id = models.UUIDField(
        primary_key= True,
        default= uuid.uuid4,
        editable= False
    )

    name = models.CharField(max_length=64, blank=True, null= False)

class Topping(models.Model):
    name = models.CharField(primary_key=True, max_length=64)

class Pizza(models.Model):
    id = models.UUIDField(
        primary_key= True,
        default= uuid.uuid4,
        editable= False
    )

    order = models.ForeignKey(
        "pizzaria.Order",
        on_delete = models.CASCADE,
        related_name= "pizzas",
        null= False
    )

    waitress = models.OneToOneField(
        "pizzaria.Waitress",
        on_delete = models.SET_NULL,
        related_name = "waitresses",
        null = True
    )

    toppings = models.ManyToManyField(
        "pizzaria.Topping",
        related_name = '+'
    )

