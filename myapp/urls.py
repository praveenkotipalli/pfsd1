from django.urls import path
from . import views


urlpatterns = [
    path('', views.navbar , name='navbar'),
    path('register', views.register, name='register' ),
    path('custom',views.custom , name= 'custom'),
    path('home',views.home , name= 'home'),
    path('index',views.index ,name='index'),
    path('account',views.account ,name='account'),
    path('history',views.history ,name='history'),
    path('balance', views.balance, name='balance'),
    path('transaction', views.transaction, name='transaction')

]
