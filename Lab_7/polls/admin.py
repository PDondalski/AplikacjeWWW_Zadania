from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Team, Person, Question, Choice, Stanowisko, Osoba
# Register your models here.
admin.site.register(Team)
admin.site.register(Person)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Stanowisko)
admin.site.register(Osoba)

class OsobaAdmin(admin.ModelAdmin):
    list_display = ['imie', 'nazwisko', 'disp_stanowisko', 'data_dodania', 'slug']
    list_filter = ['stanowisko', 'data_dodania']
    readonly_fields = ['data_dodania']

    @admin.display(description='Stanowisko')
    def disp_stanowisko(self, obj):
        return f'{obj.stanowisko.nazwa} ({obj.stanowisko.id})'

class StanowiskoAdmin(admin.ModelAdmin):
    list_display = ('nazwa', 'opis')
    search_fields = ('nazwa',)


admin.site.unregister(Osoba)
admin.site.unregister(Stanowisko)
admin.site.register(Stanowisko, StanowiskoAdmin)
admin.site.register(Osoba, OsobaAdmin)


