from django.urls import path

from valeo import views

urlpatterns = [


    path('employees', views.employees, name='employees'),
    

]
