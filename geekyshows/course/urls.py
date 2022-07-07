from django.contrib import admin
from django.urls import path
from . import views

app_name = 'course'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('learndj/',views.learn_django),
    path('learnpy/',views.learn_python),
    path('home/',views.home),
    path('about/',views.about, name='aboutus'),
    path('core/',views.core),
    
    
]