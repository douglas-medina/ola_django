from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog(request):
    print('Página do blog')
    return HttpResponse('Blog do app')