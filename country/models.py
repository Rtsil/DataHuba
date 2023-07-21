from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)
    name_official = models.CharField(max_length=100)
    tld = models.CharField(max_length=4)  # .mg
    independent = models.BooleanField()  # is independent
    UN_member = models.BooleanField()  # UN member?
    currencies = models.CharField(max_length=100)
    idd = models.CharField(max_length=5)  # +261
    flag_emoji = models.CharField(max_length=1)
    pop_name = models.CharField(max_length=100)  # population name
    languages = models.JSONField()
    maps = models.JSONField()
    populations = models.BigIntegerField()  # Num
    car_side = models.CharField(max_length=10)  # driving side of car
    timezones = models.CharField(max_length=10)
    continents = models.CharField(max_length=50)
    flag_img_url = models.CharField(max_length=100)
    flag_img_alt = models.TextField()
    coatofarms_img_url = models.CharField(max_length=100)

    def __str__(self):
        return self.name
