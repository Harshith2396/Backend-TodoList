from rest_framework.views import APIView
from django.shortcuts import redirect
from django.http import HttpResponse
from rest_framework_simplejwt.tokens import AccessToken,SlidingToken
from rest_framework_simplejwt.exceptions import TokenError
class blacklist(APIView):
    def post(self,request,token):
        try:
            a=SlidingToken(token)
            a.blacklist()
            return redirect ("https://www.w3schools.com")
        except TokenError:
            return HttpResponse("Token has been blacklisted")