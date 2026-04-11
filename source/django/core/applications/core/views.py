from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, World!"})

def home(request):
    context = {
        "title": "AvantKeel"
    }
    return render(request, 'core/home_ES.html', context)

def learnmore(request):
    return render(request, 'core/about_ES.html')