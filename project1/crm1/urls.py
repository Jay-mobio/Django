from re import template
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import views
from . import cbv
from .views import (home_views,register_views,userpage_views,
accountsettings_views,products_views,customer_views,
createorder_views,updateorder_views,deleteorder_views,
password_change_done_views,password_complete_views,password_confirm_views,
password_reset_views,login_views,logout_views,feedback_views
)


app_name = 'crm1'

# function base views
# urlpatterns = [
#     path('', views.home,name='home'),
#     path('register/', views.registerPage,name='register'),
#     path('login/', views.loginPage,name = "login"),
#     path('logout/', views.logoutuser,name = "logout"),
#     path('account/', views.accountSettings, name="account"),
#     path('user/', views.userPage,name='user'),
#     path('products/', views.products,name='products'),
#     path('customer/<str:pk>/', views.customer, name="customer"),
#     path('create_order/<str:pk>',views.createOrder,name='create_order'),
#     path('udate_order/<str:pk>',views.updateOrder,name='update_order'),
#     path('delete_order/<str:pk>',views.deleteOrder,name='delete_order'),

#     path('reset_password/',views.PasswordResetView.as_view(),name="reset_password"),

#     path('password_reset/sent/',views.PasswordChangeDoneView.as_view(),name='reset_password_done'),

#     path('reset/<uidb64>/<token>/',views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),

#     path('reset_password_complete/',views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
# ]

#class based views
urlpatterns = [
    path('',home_views.home.as_view(),name='home'),
    path('register/',register_views.RegisterView.as_view(),name='register'),
    path('login/',login_views.LoginView.as_view(),name='login'),
    path('logout/',logout_views.LogoutView.as_view(),name='logout'),
    path('user/',userpage_views.UserPageViews.as_view(),name='user'),
    path('account/',accountsettings_views.AccountSettingsViews.as_view(),name='account'),
    path('products/',products_views.ProductViews.as_view(),name='products'),
    path('customer/<str:pk>/',customer_views.CustomerViews.as_view(),name='customer'),
    path('create_order/<str:pk>',createorder_views.CreateOrderViews.as_view(),name='create_order'),
    path('udate_order/<str:pk>',updateorder_views.UpdateOrderViews.as_view(),name='update_order'),
    path('delete_order/<str:pk>',deleteorder_views.DeleteOrdeerViews.as_view(),name='delete_order'),

    path('reset_password/',password_reset_views.PasswordResetView.as_view(),name="reset_password"),

    path('password_reset/sent/',password_change_done_views.PasswordChangeDoneView.as_view(),name='reset_password_done'),

    path('reset/<uidb64>/<token>/',password_confirm_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),

    path('reset_password_complete/',password_complete_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    path('feed_back/',feedback_views.FeedBackViews.as_view(),name='feed_back')
]

