from typing import NewType
from django.shortcuts import render
from .models import Newnumber
from django.contrib import messages
from .generateNumber import genNum
from .check import checkGuess

# Create your views here.
def add(request):

    numbers = Newnumber.objects.all()


    if request.method=='POST':
        number = request.POST['number']
        if len(set(number)) == 4:
            Newnumber.objects.create(number=number)
            messages.success(request,'Numero agregado')
        elif len(set(number)) != 4 :
            messages.warning(request,'Numero sin repeticiones y/o 4 cifras')
    
    return render(request,'fdigitGame/nuevoNumero.html',{'numbers':numbers})

def generate(request):
    if request.method == 'GET':
        lista = [1,2,3,4,5,6,7,8,9,0]
        all = genNum(lista)
        guess = all.generatingNumber()
        print(guess)
    return render(request,'fdigitGame/nuevoNumero.html',{'guess':guess})

def check(request,guess):
    if request.method == 'GET':
        request.POST.get('guess')
    
        print(number)
        print(guess)

