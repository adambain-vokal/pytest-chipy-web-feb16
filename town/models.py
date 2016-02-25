from django.db import models


class State(models.Model):
    name = models.CharField(max_length=32)
    abbreviation = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class County(models.Model):
    name = models.CharField(max_length=32)

    state = models.ForeignKey(State, related_name='counties')

    def __str__(self):
        return "{}, {}".format(self.name, self.state.abbreviation)


class Town(models.Model):

    name = models.CharField(max_length=32)
    population = models.IntegerField()

    county = models.ForeignKey(County, related_name='towns')

    def __str__(self):
        return "{} (pop: {}), {} County, {}".format(
            self.name, self.population, self.county.name, self.county.state.abbreviation)
