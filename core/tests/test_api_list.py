# django imports
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

# python imports
import json
from random import randint
import hashlib

# third imports
from rest_framework import status
from faker import Faker


class TestRegisterList(TestCase):

    def get_url(self):
        return reverse('api-core:register-list')

    def setUp(self):
        self.faker = Faker()

        # create user to login
        self.user = User.objects.create(username=self.faker.first_name())
        self.password = self.faker.password()
        self.user.set_password(self.password)
        self.user.save()

        # instance the test client
        self.client = Client()
        self.client.login(username=self.user.username, password=self.password)

    def test_list(self):
        response = self.client.get(self.get_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_anonymous_user_access(self):
        self.client.logout()

        response = self.client.get(self.get_url())
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_search_filter(self):
        data = []

        # generate the data to search
        for i in range(0, 10):
            current_data = {'name': self.faker.name(), 'desc': self.faker.text(), 'target': self.faker.name()}
            response = self.client.post(self.get_url(), current_data)
            data.append(current_data)

            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # a random index to test
        rand_index = randint(0, len(data) - 1)
        name = data[rand_index]['name']
        response = self.client.get(f'{self.get_url()}?search={name}')
        content_data = response.data

        result = list(filter(lambda x : x['name'] == name, content_data))
        self.assertTrue(len(result) > 0)

        # test with a random hash to search and not find it
        response = self.client.get(f'{self.get_url()}?search={hashlib.sha256().hexdigest()}')
        self.assertTrue(len(response.data) == 0)