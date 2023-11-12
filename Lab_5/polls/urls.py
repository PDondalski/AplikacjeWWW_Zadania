from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('osobas/<int:pk>/', views.osoba_detail),
    path('osobas/', views.osoba_list),
    path('osobas/add/', views.osoba_add),
    path('osobas_filtered/<slug:slug>', views.osoba_list_filtered),
    path('stanowiskos/<int:pk>/', views.stanowisko_detail),
    path('stanowiskos/', views.stanowisko_list),
    path('stanowiskos/add/', views.stanowisko_add),
]