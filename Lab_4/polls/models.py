from django.db import models


# Create your models here.

# deklaracja statycznej listy wyboru do wykorzystania w klasie modelu
MONTHS = models.IntegerChoices('Miesiace', 'Styczeń Luty Marzec Kwiecień Maj Czerwiec Lipiec Sierpień Wrzesień Październik Listopad Grudzień')

SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    )


class Plec(models.IntegerChoices):
    MEZCZYZNA = 1, "Mezczyzna"
    KOBIETA = 2, "Kobieta"
    INNA = 3, "Inna"

class Team(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name}"


class Person(models.Model):

    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=2, choices=SHIRT_SIZES, default=SHIRT_SIZES[0][0])
    month_added = models.IntegerField(choices=MONTHS.choices, default=MONTHS.choices[0][0])
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Stanowisko(models.Model):
    nazwa = models.CharField(null=False, blank=False, max_length=30)
    opis = models.CharField(null=True, blank=True, max_length=200)

    def __str__(self):
        return self.nazwa


class Osoba(models.Model):
    imie = models.CharField(null=False, blank=False, max_length=20)
    nazwisko = models.CharField(null=False, blank=False, max_length=25)
    plec = models.IntegerField(choices=Plec.choices)
    stanowisko = models.ForeignKey(Stanowisko, on_delete=models.CASCADE)
    data_dodania = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["nazwisko"]

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'

