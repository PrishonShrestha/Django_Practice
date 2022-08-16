from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    #passing dynamic value in index.html
    '''context = {
        'name': 'Prishon',
        'age' : 20,
        'nationality': 'Nepali'
    }'''
    # return render(request, 'index.html', context)
    return render(request, 'index.html')
