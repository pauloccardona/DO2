from django.db import models

# Create your models here.
#food&dishes related models -all menu related, plate construction options with basic ingredients, avoids, extras and preparation


class Ingredient(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return(self.name)

class Plate(models.Model):
    name = models.CharField(max_length=64, unique=True)
    ingredients = models.ManyToManyField(Ingredient, through = 'IngredientQuantity')

    def __str__(self):
        return(self.name)

class IngredientQuantity(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    plate = models.ForeignKey(Plate, on_delete=models.CASCADE)
    extra_ingredient = models.BooleanField(default=False)
    avoid_ingredient = models.BooleanField(default=False)

    def __str__(self):
        return "{}_{}".format(self.plate.__str__(), self.ingredient.__str__())

