from django.shortcuts import redirect, render
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser
from .serializers import task_serialze
from .models import tasks,user_password_reset_time
from accounts.models import UserAccounts
from rest_framework_simplejwt.tokens import AccessToken, SlidingToken
from rest_framework.views import APIView
from .utils import getEmail
from .user_expiration import UserExperation
from . send_email import send_link 
from rest_framework_simplejwt.exceptions import TokenError
from django.contrib.auth.hashers import make_password
class ToDoList(APIView):
    '''
    This class is the heart of the project all major operations such as get ,post,delete
    are performed here
    '''
    permission_classes=[IsAuthenticated]
    def post(self,request,email):
        datas=JSONParser().parse(request)
        print("post func "+getEmail(request))
        print(email)
        if email==getEmail(request):
            
            serail=task_serialze(data=datas)
            if serail.is_valid():
                serail.save()
                return JsonResponse(datas,status=200)
            else :
                return JsonResponse({'error':'Error'})
        else :
            print('no')
            return JsonResponse({'error':'Error'})
    def get(self,request,email):
        print(email)
        if email==getEmail(request):
            data=tasks.objects.filter(email=email)
            serial=task_serialze(data,many=True)
            return JsonResponse(serial.data,status=200,safe=False)
        else:
            return JsonResponse({'status':200})
    def delete(self,request,pk):
        pks=int(pk)
        data=tasks.objects.get(task_id=pks)
        data.delete()
        return HttpResponse(204)
class update(APIView):
    '''
    This class is used to update the task 
    '''
    permission_classes=[IsAuthenticated]
    def patch(self,request,pk):
        data=JSONParser().parse(request)
        tas=tasks.objects.get(task_id=pk)
        serial=task_serialze(tas,data=data,partial=True)
        if serial.is_valid():
            serial.save()
            return HttpResponse(204)
class updateStatus(APIView):
    '''
    This class is used to mark the status of the task  true or false ie completed or incomplte
    '''
    permission_classes=[IsAuthenticated]
    def patch(self,request,pk):
        data =JSONParser().parse(request)
        tas=tasks.objects.get(task_id=pk)
        serial=task_serialze(tas,data=data,partial=True)
        if serial.is_valid():
            serial.save()
            return HttpResponse(204)
        else :
            return HttpResponse(400)
class ChangePassword(APIView):
    '''
    here the  user will  reset or update  his password to a new one form the front end form.
    the token he had used to prove his credentials will be blacklisted here so that
    he cannot reset the password from the same link twice
    '''
    permission_classes=[IsAuthenticated]
    def patch(self,request,email):
        data =JSONParser().parse(request)
        try:
            if email==getEmail(request) and getEmail(request)==data['email']:
                print('yes')
                password=make_password(data['password'])
                user=UserAccounts.objects.filter(email=data['email'])
                user.update(password=password)
                token=request.META.get('HTTP_AUTHORIZATION','').split()[1]
                a=SlidingToken(token)
                a.blacklist()
                return JsonResponse({'msg':'success'})
            else :
                return JsonResponse({'msg':'Fail'})
        except TokenError :
            return JsonResponse({'msg':'error'})
