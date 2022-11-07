from django.shortcuts import render
from django.http import HttpResponse
from .form import formularioCadastro
from .models import client
from django.core import serializers
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    form = formularioCadastro()
    return render(request, 'index.html', {'form':form})

def processa_formulario(request):
    form = formularioCadastro(request.POST)
    form.save()
    return HttpResponse('Finish')

def lista_nao_classificados(request):
    list_client = client.objects.filter(marketin_validation=False)
    serialized_queryset = serializers.serialize('json', list_client)
    return JsonResponse(serialized_queryset, safe=False)

def lista_classificados(request):
    list_client = client.objects.filter(marketin_validation=True)
    serialized_queryset = serializers.serialize('json', list_client)
    return JsonResponse(serialized_queryset, safe=False)

@csrf_exempt
def classificar_cliente(request):
    request_pk = request.POST.get('pk')
    cliente = client.objects.get(pk=request_pk)
    cliente.marketin_validation = True
    cliente.save()
    return HttpResponse('Finish')