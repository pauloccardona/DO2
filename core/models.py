from django.db import models

# Create your models here.
#food&dishes related models -all menu related, plate construction options with basic ingredients, avoids, extras and preparation
class Preparation(models.Model):
    name = models.CharField(max_length=48)

    def __str__(self):
        return(self.name)


class Ingredient(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return(self.name)

class Plate(models.Model):
    name = models.CharField(max_length=64)
    ingredients = models.ManyToManyField(Ingredient, through = 'IngredientQuantity')
    preparations = models.ManyToManyField(Preparation, through = 'PreparationDirective')

    def __str__(self):
        return(self.name)

class IngredientQuantity(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    plate = models.ForeignKey(Plate, on_delete=models.CASCADE)
    extra_ingredient = models.BooleanField(default=False)
    avoid_ingredient = models.BooleanField(default=False)

    def __str__(self):
        return "{}_{}".format(self.plate.__str__(), self.ingredient.__str__())

class PreparationDirective(models.Model):
    preparation = models.ForeignKey(Preparation, on_delete=models.CASCADE)
    plate = models.ForeignKey(Plate, on_delete=models.CASCADE)

    def __str__(self):
        return "{}_{}".format(self.plate.__str__(), self.preparation.__str__())
