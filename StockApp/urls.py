from django.urls import path

from StockApp.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register_user',RegisterView.as_view(),name='register_user'),
    path('Login_user',LoginView.as_view(),name='Login_user'),
    path('logout_user', logout_view, name='logout_user'),
    path('user_login', User_login, name='user_login'),
    path('user_query/<str:id>',User_query,name='user_query'),
    path('user_query_save', User_query_save.as_view(), name='user_query_save'),
 ]
