from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('learndj/',views.learn_django),
    path('learnpy/',views.learn_python),
]