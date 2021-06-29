from typing import NewType
from django.shortcuts import render
from .models import Newnumber
from django.contrib import messages

# Create your views here.
def add(request):

    numbers = Newnumber.objects.all()


    if request.method=='POST':
        number = request.POST['number']
        Newnumber.objects.create(number=number)
        messages.success(request,'Numero agregado')
    return render(request,'fdigitGame/nuevoNumero.html',{'numbers':numbers})