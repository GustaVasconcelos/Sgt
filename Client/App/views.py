from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return HttpResponse("Hello, world!")

@csrf_exempt
def cadastrar(request):
    if(request.method == 'POST'):
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        return JsonResponse({'nome':nome,'senha':senha})
