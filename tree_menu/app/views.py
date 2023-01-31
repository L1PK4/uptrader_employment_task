from django.shortcuts import render


def index(request, name):
    return render(request, 'app/index.html', context={'item_name': name})