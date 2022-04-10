from tkinter import N
from tkinter.messagebox import NO
from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import auth


class LoginView(APIView):

    def post(self,request):
        response={}
        response['status']=500
        response['message']='something went wrong'
        try:
            data = request.data
            if data.get('username') is None:
                response['message']='key user not found'
                raise Exception('key user not found')
            if data.get('password') is None:
                response['message']='key password not found'
                raise Exception('key password not found')

            check_user= User.objects.filter(username=data.get('username')).first()
        
            if check_user is None:
                response['message']='invalid username, user not found'
                raise Exception('invalid username, user not found')

            user_obj = authenticate(username= data.get('username'), password= data.get('password'))

            if user_obj:
                login(request,user_obj)
                response['status']=200
                response['message']='Welcome'
            else:
                response['message']='invalid password'
                raise Exception('invalid password')
        
        except Exception as e:
            print(e)

        return Response(response)



LoginView = LoginView.as_view()


class RegisterView(APIView):

    def post(self,request):
        response={}
        response['status']=500
        response['message']='something went wrong'
        try:
            data = request.data
            if data.get('username') is None:
                response['message']='key user not found'
                raise Exception('key user not found')
            if data.get('password') is None:
                response['message']='key password not found'
                raise Exception('key password not found')

            check_user= User.objects.filter(username=data.get('username')).first()
        
            if check_user:
                response['message']='username already exists'
                raise Exception('username already exists')
            user_obj= User.objects.create(username=data.get('username'))    
            user_obj.set_password(data.get('password'))
            user_obj.save()
            response['status']=200
            response['message']='user created'
        
        except Exception as e:
            print(e)

        return Response(response)

RegisterView=RegisterView.as_view()

