from django.db import models

# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=32)
    abbreviation = models.CharField(max_length=2)


class County(models.Model):
    name = models.CharField(max_length=32)

    state = models.ForeignKey(State, related_name='counties')


class Town(models.Model):

    name = models.CharField(max_length=32)
    population = models.IntegerField()

    county = models.ForeignKey(County, related_name='towns')
