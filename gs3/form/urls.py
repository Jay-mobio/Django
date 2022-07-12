from django.urls import path
from . import views
urlpatterns = [
    path('regestration/', views.showformdata),
]
