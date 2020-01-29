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
        self.user = baker.make(User)
        self.client = Client()
        self.client.force_login(self.user)

    def test_create(self):
        data = {
            'name': 'Gabriel',
            'desc': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
        }
        self.client
        obj = self.client.post('/core/register', data)
        self.assertEqual(obj.status_code, 202)
