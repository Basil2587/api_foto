from django.test import TestCase, Client
from .models import User
from django.urls import reverse


class SimpleTestCase(TestCase):
    def setUp(self):
        self.client = Client()
                # создаём пользователя
        self.user = User.objects.create_user(
                        username="testname", email="myname@test.com", password="1234567hjh"
                )
        self.client.force_login(self.user)

    def test_profile(self):
        profile = User.objects.get()
        self.assertEqual(
            profile.get_username(), "testname")
'''
    def test_list_album(self):
        response = self.client.get(reverse("album"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["results"]), 1)
        '''