# Generated by Django 4.2.6 on 2023-11-12 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_alter_osoba_miesiac_dodania'),
    ]

    operations = [
        migrations.AddField(
            model_name='osoba',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]