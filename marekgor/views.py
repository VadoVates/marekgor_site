from django.shortcuts import render

from marekgor.models import Marek


def index(request):
    return render(request, 'index.html')

def about (request):
    return render (request, 'about.html')

def contact(request):
    return render (request, 'contact.html')

def marek(request):
    mareks = Marek.objects.all()
    return render(request, 'marek_list.html', {'mareks': mareks})