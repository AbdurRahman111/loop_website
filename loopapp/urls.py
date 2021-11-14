from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('loop_function_url/', views.loop_function_url, name="loop_function_url"),

]