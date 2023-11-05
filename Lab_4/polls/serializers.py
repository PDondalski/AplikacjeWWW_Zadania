from rest_framework import serializers
from .models import Osoba, Team, Person, Stanowisko


class StanowiskoSerializer(serializers.Serializer):
    nazwa = serializers.CharField(required=True)
    opis = serializers.CharField(default='', allow_null=True, allow_blank=True)

    def create(self, validated_data):
        return Stanowisko.objects.create(**validated_data)

    def update(instance, validated_data):
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.opis = validated_data.get('opis', instance.opis)
        instance.save()
        return instance

class OsobaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Osoba
        fields = '__all__'
        read_only_fields = ['id']

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        read_only_fields = ['id']

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
        read_only_fields = ['id']

