from django.shortcuts import render
from django.http import HttpResponse, request
from agrosite.models import *

# Create your views here.
def main_page_view(request):
    category = Category.objects.all()
    return render(request,
                  'index.html',
                  context={'category': category})


