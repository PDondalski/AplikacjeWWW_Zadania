from rest_framework import status
from rest_framework.authtoken.admin import User
from rest_framework.test import APITestCase

from polls.models import Stanowisko


class OsobaTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='dondalski', password='pdondalskii')
        Stanowisko.objects.create(nazwa='Testernik ', opis='przeprowadza testy')

    def test_endpoint_with_password_auth(self):
        login = self.client.login(username='dondalski', password='pdondalskii')
        self.assertTrue(login)
        post_data = {
            "imie": "Jan",
            "nazwisko": "Kowalski",
            "plec": 2,
            "stanowisko": 1
        }
        response = self.client.post('http://127.0.0.1:8000/polls/osobas/add/',
                                    post_data,
                                    content_type='application/json')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.client.logout()