from polls.views import osoba_list, stanowisko_list
from django.test import RequestFactory, TestCase
from django.urls import reverse

class Stanowisko_viewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_home_view(self):
        request = self.factory.get(reverse("stanowiskos_list"))
        response = stanowisko_list(request)
        self.assertEqual(response.status_code, 200)

'''
class Osoba_listTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_home_view(self):
        request = self.factory.get(reverse("osobas"))
        response = osoba_list(request)
        self.assertEqual(response.status_code, 200)
'''