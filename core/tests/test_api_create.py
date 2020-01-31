# django imports
from django.urls import reverse

# third imports
from rest_framework import status
from .utils import TestUtils


class TestRegisterCreate(TestUtils):

    def get_url(self):
        return reverse('api-core:register-list')

    def setUp(self):
        super().setUp()

        self.data = {
            'name': self.faker.name(),
            'desc': self.faker.text(),
            'target': '192.168.0.1, 192.168.0.2, 192.168.0.3'
        }

    def test_create_register(self):
        response = self.client.post(self.get_url(), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_register_return(self):
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
