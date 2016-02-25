from django.test import TestCase

import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

from .models import State, County, Town


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def state():
    return State.objects.create(name="Illinois", abbreviation="IL")


@pytest.fixture
def county(state):
    return County.objects.create(name="Cook", state=state)


# @pytest.fixture
# def town(county):
#     return Town.objects.create(name="Chicago", population=2500000, county=county)


@pytest.fixture(params=[
    ('state-county-town-list', "[state.id, county.id]"),
    ('state-abbr-county-town-list', "[state.abbreviation, county.id]"),
    ('county-town-list', "[county.id]"),
    ('town-list', "[]"),
])
def reverse_args(request, state, county):
    return (request.param[0], eval(request.param[1]))

@pytest.mark.django_db
def test_create(client, county, reverse_args):
    url = reverse(reverse_args[0], args=reverse_args[1])
    data = {'name': 'Schaumburg', 'population': 75000, 'county': county.id}
    # print(">>>     ", url)
    response = client.post(url, data)

    assert response.status_code == status.HTTP_201_CREATED
    assert 'id' in response.data
    assert Town.objects.count() == 1
