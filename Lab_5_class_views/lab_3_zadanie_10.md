from polls.models import Osoba, Stanowisko

Zadanie 1 - wyświetl wszystkie obiekty modelu Osoba
>>> Osoba.objects.all()
<QuerySet [<Osoba: Edyta Dolniak>, <Osoba: Samuel Umtiti>, <Osoba: Ebenezer Wokulski>, <Osoba: Andrzej Zatorski>]>


Zadanie 2 - wyświetl obiekt modelu Osoba z id = 3
>>> Osoba.objects.get(id=3)
<Osoba: Andrzej Zatorski>


Zadanie 3 - wyświetl obiekty modelu Osoba, których nazwa rozpoczyna się na wybraną przez Ciebie literę alfabetu (tak, żeby był co najmniej jeden wynik)
>>> Osoba.objects.filter(imie__startswith='E')
<QuerySet [<Osoba: Edyta Dolniak>, <Osoba: Ebenezer Wokulski>]>


Zadanie 4 - wyświetl unikalną listę stanowisk przypisanych dla modeli Osoba
>>> stanowiska = Osoba.objects.values_list('stanowisko__nazwa', flat=True)
>>> unikalne_stanowiska = list(set(stanowiska))
>>> print(unikalne_stanowiska)
['Pilkarz', 'Szarlatan', 'Magik', 'Podroznik']


Zadanie 5 - wyświetl nazwy stanowisk posortowane alfabetycznie malejąco
>>> Stanowisko.objects.order_by('-nazwa')
<QuerySet [<Stanowisko: Szarlatan>, <Stanowisko: Podroznik>, <Stanowisko: Pilkarz>, <Stanowisko: Magik>]>


Zadanie 6 - dodaj nową instancję obiektu klasy Osoba i zapisz w bazie
>>> o = Osoba(imie="Karol", nazwisko="Stoik", plec=1, stanowisko=Stanowisko.objects.first())
>>> o.save()
>>> Osoba.objects.all()
<QuerySet [<Osoba: Edyta Dolniak>, <Osoba: Karol Stoik>, <Osoba: Samuel Umtiti>, <Osoba: Ebenezer Wokulski>, <Osoba: Andrzej Zatorski>]>
