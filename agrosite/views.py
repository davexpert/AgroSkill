from django.shortcuts import render
from django.http import HttpResponse, request
from agrosite.models import *


def main_page_view(request):
    category = Category.objects.all()
    return render(request,
                  'index.html',
                  context={'category': category})


def fruits_view(request):
    category = Category.objects.all()
    return render(request,
                  'fruits.html',
                  context={'fruits': category})

def fruit_detail_view(request):
    return render(request,
                  'fruit_detail.html',
                  context={'fruit_id': 'fruit_id'})

