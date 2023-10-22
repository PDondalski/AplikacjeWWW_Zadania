from django.contrib import admin
from .models import Team, Person, Question, Choice
# Register your models here.
admin.site.register(Team)
admin.site.register(Person)
admin.site.register(Question)
admin.site.register(Choice)