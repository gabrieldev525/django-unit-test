
# django imports
from django.test import TestCase, Client
from django.contrib.auth.models import User

# third imports
from faker import Faker


class TestUtils(TestCase):

    def setUp(self):
        self.faker = Faker()

        # create user to login
        self.user = User.objects.create(username=self.faker.first_name())
        self.password = self.faker.password()
        self.user.set_password(self.password)
        self.user.is_staff = True
        self.user.save()

        self.client = Client()
        self.client.login(username=self.user.username, password=self.password)
