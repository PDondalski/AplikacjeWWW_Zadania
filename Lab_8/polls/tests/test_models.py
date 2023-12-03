from django.test import TestCase
from rest_framework.authtoken.admin import User

from ..models import Person, Osoba, Stanowisko

class OsobaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user('username', 'email@example.com', 'password')
        Stanowisko.objects.create(nazwa='Tester ', opis='przeprowadza testy')
        Osoba.objects.create(imie='Jan', nazwisko='Kowalski', plec=1, stanowisko=Stanowisko.objects.first(), wlasciciel_id=1)

    def test_first_name_label(self):
        osoba = Osoba.objects.get(id=1)
        field_label = osoba._meta.get_field('imie').verbose_name
        self.assertEqual(field_label, 'imie')

    def test_first_name_max_length(self):
        osoba = Osoba.objects.get(id=1)
        max_length = osoba._meta.get_field('imie').max_length
        self.assertEqual(max_length, 20)

    def test_ludzie_class(self):

        osoba1 = Osoba.objects.create(imie='Pior', nazwisko='kowalski', plec=1, stanowisko=Stanowisko.objects.first(), wlasciciel_id=1)
        osoba2 = Osoba.objects.create(imie='Tobiasz', nazwisko='kowalski', plec=1, stanowisko=Stanowisko.objects.first(), wlasciciel_id=1)

        self.assertEqual(osoba1.id + 1 , osoba2.id)

    def test_stanowisko_class(self):
        stanowisko1 = Stanowisko.objects.create(nazwa='Policjant')
        stanowisko2 = Stanowisko.objects.create(nazwa='Zolnierz')

        self.assertEqual(stanowisko1.id+1, stanowisko2.id)



'''
class PersonModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Person.objects.create(name='Jan', shirt_size='L')

    def test_first_name_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_first_name_max_length(self):
        person = Person.objects.get(id=1)
        max_length = person._meta.get_field('name').max_length
        self.assertEqual(max_length, 60)
'''