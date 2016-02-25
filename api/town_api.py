from rest_framework import viewsets

from rest_framework_extensions.mixins import NestedViewSetMixin

from town.models import State, County, Town
from town.serializers import StateSerializer, CountySerializer, TownSerializer


class StateViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer


class StateByAbbrViewSet(StateViewSet):
    lookup_field = 'abbreviation'


class CountyViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = County.objects.all()
    serializer_class = CountySerializer


class TownViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Town.objects.all()
    serializer_class = TownSerializer
