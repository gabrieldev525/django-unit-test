# django imports
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

# third imports
from rest_framework import status


class TestApi(TestCase):
    def setUp(self):
        # for every test this is called

        # create user to login
        self.user = User.objects.create(username='test')
        self.password = '123'
        self.user.set_password(self.password)
        self.user.is_staff = True
        self.user.save()

        self.client = Client()
        self.client.login(username=self.user.username, password=self.password)

    def test_list_registers(self):
        response = self.client.get(reverse('api-core:register-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
