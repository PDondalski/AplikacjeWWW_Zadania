# Generated by Django 4.2.6 on 2023-11-19 14:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0012_osoba_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='osoba',
            name='wlasciciel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='osobas', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
