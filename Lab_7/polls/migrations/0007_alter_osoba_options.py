# Generated by Django 4.2.6 on 2023-10-25 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_alter_osoba_plec'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='osoba',
            options={'ordering': ['nazwisko']},
        ),
    ]