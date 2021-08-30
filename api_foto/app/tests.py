from .models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class SimpleTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testname", email="myname@test.com", password="1234567hjh"
            )
        self.client.force_authenticate(self.user)

    def test_profile(self):
        profile = User.objects.get()
        self.assertEqual(profile.get_username(), "testname")

    def test_can_read_user_list(self):
        response = self.client.get(reverse('users-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_user_detail(self):
        response = self.client.get(
            reverse('users-detail', args=[self.user.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/api/v1/users/1/')
        self.assertEqual(resp.status_code, 200)

    def test_authorization_post(self):
        test_username = "testname2"
        email = "myname2@test.com"
        password = "1234567hjh2"
        self.client.post('/api/v1/users/', {"username": test_username,
                                            "email": email,
                                            "password": password})
        response = self.client.get('/api/v1/users/2/')
        self.assertContains(response, test_username)

    def test_album_post(self):
        test_album = "one album"
        self.client.post('/api/v1/users/1/album/', {"title": test_album})
        response = self.client.get('/api/v1/users/1/album/1/')
        self.assertContains(response, test_album)


'''Tester for training :)))'''
