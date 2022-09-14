from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from requests import exceptions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from StockApp.models import *


class HomeView(View):
 def get(self, request, *args, **kwargs):
     product = Product.objects.all()
     return render(request, 'index.html',{"product":product})

def User_login(request):
    return render(request, 'login.html')



class RegisterView(View):

    def post(self, request, *args, **kwargs):
        full_name = request.POST['uname']
        email = request.POST['email']
        mob = request.POST['mob']
        paswrd = request.POST['psw']


        username = email

        user_obj = StockUser.objects.filter(username=username)
        if not user_obj.exists():
            StockUser.objects.create_user(username=username,full_name=full_name,password=paswrd,mobile=mob)
        else:
            return HttpResponse("data already exists")
        return HttpResponse('user created')


class LoginView(View):

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        paswrd = request.POST['psw']

        user_obj = authenticate(username=email, password=paswrd)

        if user_obj is not None:
            login(request, user_obj)

        else:
            return HttpResponse('check Your username and password')

        token_obj = TokenObtainPairSerializer()
        token = token_obj.validate({"username": email, "password": paswrd})
        access_token = token.get('access')
        refresh_token = token.get('refresh')

        user_auth_token_obj = UserAuthTokens.objects.filter(user_info=user_obj)
        if user_auth_token_obj.exists():
            user_auth_token_obj.update(access_token=access_token, refresh_token=refresh_token)
        else:
            UserAuthTokens.objects.create(user_info=user_obj, access_token=access_token, refresh_token=refresh_token)


        return redirect('home')




def logout_view(request):
    logout(request)
    return redirect('home')


def User_query(request,id):
    user=request.user
    usr_ob=StockUser.objects.filter(username=user)
    if usr_ob.exists():
        prod_obj=Product.objects.filter(id=id)
        return render(request, 'user_query.html', {"prod_obj": prod_obj})
    else:
        return redirect('user_login')


class User_query_save(View):
    def post(self, request, *args, **kwargs):
        name = request.POST['pro_nm']
        uname = request.POST['uname']
        mssg = request.POST['msg']
        product_obj=Product.objects.get(name=name)
        user_ob=StockUser.objects.get(username=uname)

        query_obj=UserQuerys.objects.create(name=product_obj, user_name=user_ob, query=mssg)
        return redirect('home')











