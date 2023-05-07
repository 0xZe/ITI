from django.shortcuts import render

# Create your views here.

from valeo.models import Employee


def employees(request): 
    return render(request , 'valeo/employees.html', {'emp':Employee.objects.all()})

