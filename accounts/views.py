from django.shortcuts import render,redirect
from rest_framework.parsers import JSONParser
from .models import UserAccounts
from django.http import JsonResponse,HttpResponse

from todoList.models import tasks,user_password_reset_time

from rest_framework_simplejwt.tokens import AccessToken, SlidingToken
from rest_framework.views import APIView
from todoList.utils import getEmail
from todoList.user_expiration import UserExperation
from todoList.send_email import send_link 
from rest_framework_simplejwt.exceptions import TokenError

class user_create(APIView):
    '''
    This class will create users and store them using cutsom model UserAccounts
    '''
    def post(self,request):
        data=JSONParser().parse(request)
        print(data)
        if ('@' in data['email']) and ('.com' in data['email'] ) and (len(data['password'])>=8) :
            a=UserAccounts.objects.filter(email=data['email']).values('email')
            print(list(a))
            if len(list(a))==0:
                print('yes')
                UserAccounts.objects.create_users(data['email'],data['password'])
                return JsonResponse({'msg':'created user'})
            else:
                return  JsonResponse({'msg':'user already taken'})
        else:
            return JsonResponse({'msg':'invalid email or password'})
class ForgetPassword(APIView):
    '''
    This class is responsible for sending the user's password reset link.
    It will first check if the time of last reset link sent and based on it the new links will be sent
    '''
    def post(self ,request):
        data=JSONParser().parse(request)
        users=user_password_reset_time()
        msg=UserExperation(data)
        if msg=='insert':
            users.user=data['email']
            users.save()
            user=UserAccounts.objects.get(email=data['email'])
            a=SlidingToken.for_user(user)
            send_link().send_reset_link(a,data['email'])
            return JsonResponse({'msg':"success"})
        elif msg=='can resend link':
            users.user=data['email']
            users.save()
            user=UserAccounts.objects.get(email=data['email'])
            a=SlidingToken.for_user(user)
            send_link().send_reset_link(a,data['email'])
            return JsonResponse({'msg':"success"})
        elif msg=='cannot resend link':
            return JsonResponse({'msg':"error1"})
        else: 
            return JsonResponse({'msg':"error"})
