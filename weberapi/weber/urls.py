from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListVillager.as_view()),
    path('<int:pk>/', views.DetailVillager.as_view()),

]