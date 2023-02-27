from django.shortcuts import render
from django.http import JsonResponse
import asyncio
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

def login(request):
   
   # my_list = list(user.values())
    username = request.GET.get('username')
    password = request.GET.get('pwd')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        response_data = {'status': 200 , 'message': user.id}
    else:
        response_data = {'status': 404 , 'message': "wrong"}
        


    



    


    print('test')
    return JsonResponse(response_data,safe=False)