from django.urls import path

from . import views

urlpatterns= [
    path('', views.index, name='index'),
    path('processa_formulario/', views.processa_formulario, name='processa_formulario'),
    path('lista_nao_classificados/', views.lista_nao_classificados, name='lista_nao_classificados'),
    path('lista_classificados/', views.lista_classificados, name='lista_classificados'),
    path('classificar_cliente/', views.classificar_cliente, name='classificar_cliente'),
]