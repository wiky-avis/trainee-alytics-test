from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new_graph/', views.new_graph, name='new_graph'),
]
