import pytest
from rest_framework.test import APITestCase, APIClient
from django.shortcuts import reverse
from conftest import EVERYTHINF_EQUALS_NOT_NONE


pytestmark = [pytest.mark.django_db]


class GuestEndpointsTestCase(APITestCase):
    fixtures = [
        'catalog/tests/fixtures/categories_fixrure.json',
        'catalog/tests/fixtures/category_fixture.json',
        'catalog/tests/fixtures/discount_fixture.json',
        'catalog/tests/fixtures/products_fixture.json',
        'catalog/tests/fixtures/seller_fixture.json'
    ]

    def test_categories_list(self):
        url = reverse('categories')
        response = self.client.get(url)
        assert response.status_code == 200
        assert isinstance(response.data, list)
        assert response.data == [
            {
                "id": 1,
                "name": EVERYTHINF_EQUALS_NOT_NONE,
                "description": EVERYTHINF_EQUALS_NOT_NONE
            },
            {
                "id": 2,
                "name": EVERYTHINF_EQUALS_NOT_NONE,
                "description": EVERYTHINF_EQUALS_NOT_NONE
            },
            {
                "id": 3,
                "name": EVERYTHINF_EQUALS_NOT_NONE,
                "description": EVERYTHINF_EQUALS_NOT_NONE
            },
        ]

    def test_category_products(self):
        url = reverse('category-products', kwargs={"category_id": 3})
        response = self.client.get(url)

        assert response.status_code == 200
        assert response.data == [
            {
                'id': 5,
                'name': EVERYTHINF_EQUALS_NOT_NONE,
                'price': EVERYTHINF_EQUALS_NOT_NONE,
                'articul': EVERYTHINF_EQUALS_NOT_NONE,
                'count_on_stock': EVERYTHINF_EQUALS_NOT_NONE,
                'discount': EVERYTHINF_EQUALS_NOT_NONE,
                'category': EVERYTHINF_EQUALS_NOT_NONE,
                'seller': EVERYTHINF_EQUALS_NOT_NONE,
                'description': EVERYTHINF_EQUALS_NOT_NONE
            }
        ]
        assert response.data[0]["discount"] == {
            "id": 1,
            'name': EVERYTHINF_EQUALS_NOT_NONE,
            "percent": 5,
            "date_start": EVERYTHINF_EQUALS_NOT_NONE,
            "date_end": EVERYTHINF_EQUALS_NOT_NONE
        }
