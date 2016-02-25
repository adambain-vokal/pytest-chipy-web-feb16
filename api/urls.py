from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from rest_framework_extensions.routers import NestedRouterMixin

from .town_api import StateViewSet, StateByAbbrViewSet, CountyViewSet, TownViewSet


class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass


router = NestedDefaultRouter()

router.register(
    r'state', StateViewSet, 'state').register(
    r'county', CountyViewSet, 'state-county', parents_query_lookups=['state']).register(
    r'town', TownViewSet, 'state-county-town', parents_query_lookups=['county__state', 'county'])

router.register(
    r'state-abbr', StateByAbbrViewSet, 'state-abbr').register(
    r'county', CountyViewSet, 'state-abbr-county',
        parents_query_lookups=['state__abbreviation']).register(
    r'town', TownViewSet, 'state-abbr-county-town',
        parents_query_lookups=['county__state__abbreviation', 'county'])


router.register(r'county', CountyViewSet, 'county',).register(
    r'town', TownViewSet, 'county-town', parents_query_lookups=['county'])


router.register(r'town', TownViewSet, 'town')


urlpatterns = [
    url(r'^', include(router.urls)),
]
