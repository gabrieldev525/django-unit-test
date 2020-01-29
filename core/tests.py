# django imports
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

# third imports
from rest_framework.test import APITestCase
from model_bakery import baker

# local imports
from .models import Register


class RegisterTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='user')
        self.user.set_password('123')
        self.user.save()

        self.client = Client()
        self.client.login(username=self.user.username, password=self.user.password)

    def test_create(self):
        data = {
            'name': 'Gabriel',
            'desc': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
        }
        obj = self.client.post(reverse('api-core:register-list'), data)
        self.assertEqual(obj.status_code, 202)
