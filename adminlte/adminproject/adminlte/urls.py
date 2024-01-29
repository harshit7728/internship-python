from . import views
from .views import *
from django.urls import path

urlpatterns = [path('', views.index, name='index'),
               path('form/', views.form, ),
               path('update/', views.update, ),
               path('datatable/',  StudentView.as_view(), ),
               ]
