# django imports
from django.urls import reverse

# python imports
from random import randint
from urllib.parse import urlencode
import hashlib

# third imports
from rest_framework import status
from .utils import TestUtils


class TestRegisterList(TestUtils):

    def get_url(self):
        return reverse('api-core:register-list')

    def test_list(self):
        response = self.client.get(self.get_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_anonymous_user(self):
        self.client.logout()

        response = self.client.get(self.get_url())
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TestRegisterListFilter(TestUtils):
    def get_url(self):
        return reverse('api-core:register-list')

    def setUp(self):
        super().setUp()

        self.data = []
        # generate the data to search
        for i in range(0, 10):
            current_data = {
                'name': self.faker.name(),
                'desc': self.faker.text(),
                'target': self.faker.name()
            }
            self.client.post(self.get_url(), current_data)
            self.data.append(current_data)

    def test_search_filter(self):
        # a random index to test
        rand_index = randint(0, len(self.data) - 1)
        name = self.data[rand_index]['name']
        query = urlencode({'search': name})
        response = self.client.get(f'{self.get_url()}?{query}')
        content_data = response.data

        result = list(filter(lambda x: x['name'] == name, content_data))
        self.assertTrue(len(result) > 0)

    def test_search_with_a_no_result_key(self):
        query = urlencode({'search': hashlib.sha256().hexdigest()})

        # test with a random hash to search and not find it
        response = self.client.get(f'{self.get_url()}?{query}')
        self.assertTrue(len(response.data) == 0)
