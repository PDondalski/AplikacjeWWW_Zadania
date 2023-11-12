from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .models import Osoba, Stanowisko
from .serializers import OsobaSerializer, StanowiskoSerializer
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.text import slugify
# Zad7 - zmiana implementacji API
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics


# Create your views here.

'''
# OSOBA
# określamy dostępne metody żądania dla tego endpointu
@api_view(['GET'])
def osoba_list(request):
    """
    Lista wszystkich obiektów modelu Osoba.
    """
    if request.method == 'GET':
        osobas = Osoba.objects.all()
        serializer = OsobaSerializer(osobas, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def osoba_list_filtered(request, slug):
    """
    Lista wszystkich obiektów modelu Osoba, które zawierają w polu nazwisko zadany łańcuch znaków.
    """
    if request.method == 'GET':
        osobas = Osoba.objects.filter(nazwisko__contains=slug)
        serializer = OsobaSerializer(osobas, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def osoba_detail(request, pk):

    """
    :param request: obiekt DRF Request
    :param pk: id obiektu Osoba
    :return: Response (with status and/or object/s data)
    """
    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    """
    Zwraca pojedynczy obiekt typu Osoba.
    """
    if request.method == 'GET':
        osoba = Osoba.objects.get(pk=pk)
        serializer = OsobaSerializer(osoba)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OsobaSerializer(osoba, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        osoba.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def osoba_add(request):
    """
    Dodaje nowy obiekt typu Osoba.
    """
    if request.method == 'POST':
        serializer = OsobaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
'''

#Zad.7 - Zamiana implementcji API dla modelu Osoba
class OsobaList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        osobas = Osoba.objects.all()
        serializer = OsobaSerializer(osobas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OsobaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OsobaDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Osoba.objects.get(pk=pk)
        except Osoba.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        osoba = self.get_object(pk)
        serializer = OsobaSerializer(osoba)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        osoba = self.get_object(pk)
        serializer = OsobaSerializer(osoba, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        osoba = self.get_object(pk)
        osoba.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OsobaList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Osoba.objects.all()
    serializer_class = OsobaSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class OsobaDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Osoba.objects.all()
    serializer_class = OsobaSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class OsobaList(generics.ListCreateAPIView):
    queryset = Osoba.objects.all()
    serializer_class = OsobaSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Osoba.objects.all()
    serializer_class = OsobaSerializer

# STANOWISKO
@api_view(['GET'])
def stanowisko_list(request):
    """
    Lista wszystkich obiektów modelu Stanowisko.
    """
    if request.method == 'GET':
        stanowiskos = Stanowisko.objects.all()
        serializer = StanowiskoSerializer(stanowiskos, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def stanowisko_detail(request, pk):

    """
    :param request: obiekt DRF Request
    :param pk: id obiektu Stanowisko
    :return: Response (with status and/or object/s data)
    """
    try:
        stanowisko = Stanowisko.objects.get(pk=pk)
    except Stanowisko.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    """
    Zwraca pojedynczy obiekt typu Person.
    """
    if request.method == 'GET':
        stanowisko = Stanowisko.objects.get(pk=pk)
        serializer = StanowiskoSerializer(stanowisko)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StanowiskoSerializer(stanowisko, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        stanowisko.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def stanowisko_add(request):
    """
    Dodaje nowy obiekt typu Stanowisko.
    """
    if request.method == 'POST':
        serializer = OsobaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
