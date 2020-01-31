# django imports
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

# third imports
from rest_framework import status
from faker import Faker


class TestRegisterCreate(TestCase):

    def get_url(self):
        return reverse('api-core:register-list')

    def setUp(self):
        self.faker = Faker()

        # create user to login
        self.user = User.objects.create(username=self.faker.first_name())
        self.password = self.faker.password()
        self.user.set_password(self.password)
        self.user.is_staff = True
        self.user.save()

        # instance the test client
        self.client = Client()
        self.client.login(username=self.user.username, password=self.password)

        self.data = {
            'name': self.faker.name(),
            'desc': self.faker.text(),
            'target': '192.168.0.1, 192.168.0.2, 192.168.0.3'
        }

    def test_create_register(self):
        response = self.client.post(self.get_url(), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        content_data = response.data
        self.assertEqual(content_data['name'], self.data['name'])
        self.assertEqual(content_data['desc'], self.data['desc'])
        self.assertEqual(content_data['target'], self.data['target'])

    def test_create_without_required_data(self):
        self.data.pop('target')
        response = self.client.post(self.get_url(), self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_register_with_anonymous_user(self):
        self.client.logout()
        response = self.client.post(self.get_url(), self.data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_register_with_a_unauthorized_user(self):
        self.user.is_staff = False
        self.user.save()
        self.client.login(username=self.user.username, password=self.password)

        response = self.client.post(self.get_url(), self.data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
