from re import template
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .cbv import *

app_name = 'crm1'

#function base views
urlpatterns = [
    path('', views.home,name='home'),
    path('register/', views.registerPage,name='register'),
    path('login/', views.loginPage,name = "login"),
    path('logout/', views.logoutuser,name = "logout"),
    path('account/', views.accountSettings, name="account"),
    path('user/', views.userPage,name='user'),
    path('products/', views.products,name='products'),
    path('customer/<str:pk>/', views.customer, name="customer"),
    path('create_order/<str:pk>',views.createOrder,name='create_order'),
    path('udate_order/<str:pk>',views.updateOrder,name='update_order'),
    path('delete_order/<str:pk>',views.deleteOrder,name='delete_order'),

    path('reset_password/',views.PasswordResetView.as_view(),name="reset_password"),

    path('password_reset/sent/',views.PasswordChangeDoneView.as_view(),name='reset_password_done'),

    path('reset/<uidb64>/<token>/',views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),

    path('reset_password_complete/',views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
]

