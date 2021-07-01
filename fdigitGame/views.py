from typing import NewType
from django.shortcuts import render
from .models import Newnumber, Guess
from django.contrib import messages
from .generateNumber import genNum
from .check import checkGuess
from .askNewNumber import askNew
# Create your views here.
def add(request):

    numbers = Newnumber.objects.all()


    if request.method=='POST':
        number = request.POST['number']
        if len(set(number)) == 4:
            Newnumber.objects.create(numberR=number)
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
        formatGuess=''
        for i in range (4):
                formatGuess = formatGuess + str(guess[i])
        Guess.objects.create(intento=int(formatGuess))
    return render(request,'fdigitGame/nuevoNumero.html',{'guess':int(formatGuess)})

def check(request):
    if request.method == 'POST':
        guess = Guess.objects.last()
        number = Newnumber.objects.last()
        print(guess.intento)
        print(number.numberR)
        strguess=str(guess.intento)
        strnumber=str(number.numberR)
        numberlist = []
        guesslist = []
        for i in range(4):
            numberlist.append(int(strnumber[i]))
            guesslist.append(int(strguess[i]))

        firstResult = checkGuess(numberlist,guesslist)
        answer1= firstResult.verifyNumber()
        newGuess=askNew(answer1,guesslist)
        nuevoNumber = newGuess.newNumber()
        print("Bien:",answer1[0],"Regular:",answer1[1],"Mal:",answer1[7])
        intentos = 1
        while(True):
            results = checkGuess(number,nuevoNumber)
            answer = results.verifyNumber()
            print(nuevoNumber)
            print("Bien:",answer[0],"Regular:",answer[1],"Mal:",answer[7])

            if answer[0]==4:
                print("Numero adivinado despues de: " ,intentos," intentos")
                break
            else:
                newGuess=askNew(answer,guess)
                newNumber = newGuess.newNumber()

    return render(request,'fdigitGame/nuevoNumero.html',{'guess':guess , 'number':number, 'intentos':intentos})
