Przygotowanie do zadań
>>>> from polls.models import Osoba, Team, Person, Stanowisko
>>> from polls.serializers import StanowiskoSerializer, OsobaSerializer, TeamSerializer, PersonSerializer
>>> from rest_framework.renderers import JSONRenderer
>>> from rest_framework.parsers import JSONParser
>>> import io

Zad.1 Stworzenie nowej instancji klasy

Dla pierwszego serializera:

>>> o = Osoba(imie='Piotr', nazwisko='Dondalski', plec=1, stanowisko=Stanowisko.objects.first())
>>> o.save()
>>> Osoba.objects.all()
<QuerySet [<Osoba: Edyta Dolniak>, <Osoba: Piotr Dondalski>, <Osoba: Karol Stoik>, <Osoba: Samuel Umtiti>, <Osoba: Ebenezer Wokulski>, <Osoba: Andrzej Zatorski>]>

Dla drugiego serializera:
>>> s = Stanowisko(nazwa='Mysliciel',opis='Mysli')
>>> s.save()
>>> Stanowisko.objects.all()
<QuerySet [<Stanowisko: Magik>, <Stanowisko: Pilkarz>, <Stanowisko: Podroznik>, <Stanowisko: Szarlatan>, <Stanowisko: Filozof>, <Stanowisko: Kasjer>, <Stanowisko: Mysliciel>]>


Zad.2 Inicjowanie serializera

Dla pierwszego serializera:

>>> serializer = OsobaSerializer(o)
>>> serializer.data
{'id': 6, 'imie': 'Piotr', 'nazwisko': 'Dondalski', 'plec': 1, 'data_dodania': '2023-10-30', 'stanowisko': 1}

Dla drugiego serializatora:

>>> serializerdwa = StanowiskoSerializer(s)
>>> serializerdwa.data
{'nazwa': 'Mysliciel', 'opis': 'Mysli'}

Zad.3 serializacja danych do formatu JSON

Dla pierwszego serializera:

>>> from rest_framework.renderers import JSONRenderer
>>> content = JSONRenderer().render(serializer.data)
>>> content
b'{"id":6,"imie":"Piotr","nazwisko":"Dondalski","plec":1,"data_dodania":"2023-10-30","stanowisko":1}'


Dla drugiego serializera:

>>> contentdwa = JSONRenderer().render(serializerdwa.data)
>>> contentdwa
b'{"nazwa":"Mysliciel","opis":"Mysli"}'

Zad.4 

Dla pierwszego serializera:

>>> import io
>>> stream = io.BytesIO(content)
>>> data = JSONParser().parse(stream)

Dla drugiego serializera:

>>> streamdwa = io.BytesIO(contentdwa)
>>> datadwa = JSONParser().parse(streamdwa)

Utworzenie obiektu dedykowanego serializera i przekazanie sparsowanych danych

Dla pierwszego serializera:

>>> deserializer = OsobaSerializer(data=data)
>>> deserializer.is_valid()
True

Dla drugiego serializera:

>>> deserializerdwa = StanowiskoSerializer(data=datadwa)
>>> deserializerdwa.is_valid()
True

Błędy walidacji dla pierwszego serializera:

>>> deserializer.errors
{}

Błędy walidacji dla drugiego serializera:

>>> deserializerdwa.errors
{}

Pola wczytanego serializera/deserializera 

dla pierwszego serializera:

>>> deserializer.fields
{'id': IntegerField(label='ID', read_only=True), 'imie': CharField(max_length=20), 'nazwisko': CharField(max_length=25), 'plec': ChoiceField(choices=[(1, 'Mezczyzna'), (2, 'Kobieta'), (3, 'Inna')]), 'data_dodania': DateField(read_only=True), 'stanowisko': PrimaryKeyRelatedField(queryset=Stanowisko.objects.all())}

dla drugiego serializera:

>>> deserializerdwa.fields
{'nazwa': CharField(required=True), 'opis': CharField(allow_blank=True, allow_null=True, default='')}

Inny sposób

dla pierwszego serializera:

>>> repr(deserializer)
"OsobaSerializer(data={'id': 6, 'imie': 'Piotr', 'nazwisko': 'Dondalski', 'plec': 1, 'data_dodania': '2023-10-30', 'stanowisko': 1}):\n    id = IntegerField(label='ID', read_only=True)\n    imie = CharField(max_length=20)\n    nazwisko = CharField(max_length=25)\n    plec = ChoiceField(choices=[(1, 'Mezczyzna'), (2, 'Kobieta'), (3, 'Inna')])\n    data_dodania = DateField(read_only=True)\n    stanowisko = PrimaryKeyRelatedField(queryset=Stanowisko.objects.all())"

dla drugiego serializera:

>>> repr(deserializerdwa)
"StanowiskoSerializer(data={'nazwa': 'Mysliciel', 'opis': 'Mysli'}):\n    nazwa = CharField(required=True)\n    opis = CharField(allow_blank=True, allow_null=True, default='')"

Sprawdzenie jak wyglądają dane obiektów po deserializacji i walidacji

dla pierwszego serializera:

>>> deserializer.validated_data
OrderedDict([('imie', 'Piotr'), ('nazwisko', 'Dondalski'), ('plec', 1), ('stanowisko', <Stanowisko: Magik>)])

dla drugiego serializera:

>>> deserializerdwa.validated_data
OrderedDict([('nazwa', 'Mysliciel'), ('opis', 'Mysli')])

Utrwalenie danych

dla pierwszego serializera:

>>> deserializer.save()
<Osoba: Piotr Dondalski>

dla drugiego serializera:

>>> deserializerdwa.save()
<Stanowisko: Mysliciel>

Sprawdzenie

>>> deserializerdwa.data
{'nazwa': 'Mysliciel', 'opis': 'Mysli'}
