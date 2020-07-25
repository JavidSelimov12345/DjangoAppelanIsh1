from django.urls import path
from .views import HomeView,DEview

urlpatterns=[
    
    path('',HomeView.as_view(),name='index'),
    path('elan/<int:pk>/',DEview.as_view(),name='detail'),
]