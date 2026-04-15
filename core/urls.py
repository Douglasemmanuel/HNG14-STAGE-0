from django.urls import path
from .views import classify_name , home

urlpatterns = [
     path('', home),
    path('classify/', classify_name),
]