from django.db import models


# Create your models here.

class Employee(models.Model): 
    
    first_name =  models.CharField(max_length=30)
    last_name  =  models.CharField(max_length=30, null=True)
    id         =  models.IntegerField(primary_key=True)
    email      =  models.EmailField( null=True, blank=True)
    salery     =  models.DecimalField(max_digits=10 , decimal_places=2)
    created_at =  models.DateTimeField(auto_now_add=True,  null=True)
    updated_at =  models.DateTimeField(auto_now=True,  null=True)