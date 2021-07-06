from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
# def hithere(request):
#     return HttpResponse('Hello friend!')


def hithere(request):
    return render(request, 'generator/hithere.html')


def home(request):
    return render(request, 'generator/home.html', {'password': 'hkfg5'})


# def password(request):
#     return HttpResponse('Password page...')


def password(request):
    characters = list('abcdefghjklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()-+'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('selection'))
    showlength = ''

    thepass = ''

    # for key in range(len(characters)):
    for key in range(length):
        thepass += random.choice(characters)
        showlength = len(thepass)

    return render(request, 'generator/password.html', {'password': thepass, 'showlength': showlength})


def description(request):
    return render(request, 'generator/description.html')
