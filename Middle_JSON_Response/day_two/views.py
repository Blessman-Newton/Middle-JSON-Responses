from django.shortcuts import render
from django.http import JsonResponse

def json_view(request):
    data = {'message': 'Hello, JSON!'}
    return JsonResponse(data)