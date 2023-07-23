from django.db import models


# Create your models here.
class FoodRecipe(models.Model):
    meal_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    instructions = models.TextField()
    meal_image = models.CharField(max_length=100, blank=True)
    tags = models.CharField(max_length=100, blank=True)
    youtube_link = models.CharField(max_length=100, blank=True)
    ingredients_and_measures = models.JSONField()

    def __str__(self):
        return self.meal_name


class FoodCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name