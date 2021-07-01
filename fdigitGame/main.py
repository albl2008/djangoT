from askNewNumber import askNew
from check import checkGuess
from generateNumber import genNum
import time

list=[0,1,2,3,4,5,6,7,8,9]
intentos = 1
number=[]
while (True):   
    try:
        while (len(set(number))!=4):
            numbers = input("Ingrese un numero de 4 cifras donde no se repite ningun cifra: ")
            for i in range (4):
                number.append(int(numbers[i]))

        if len(set(number))!=4:
            number=[]
            print ("Ingrese numeros sin repeticiones.")
        if len(number) != 4:
            number=[]
            print("Ingrese solo 4 cifras")
        else:
            break

    except ValueError:
        print("Error")
        


all = genNum(list)                      #instancio la clase genNum con la lista completa de numeros
guess = all.generatingNumber()  # genero un nuevo numero
print(guess)
firstResult = checkGuess(number,guess)  # instancio la clase checkGuess con el numero correcto y el intento
answer1= firstResult.verifyNumber()   # guardo la respuesta en answer
newGuess=askNew(answer1,guess)  #instancio la case askNew con la respuesta y el intento
newNumber = newGuess.newNumber()
print("Bien:",answer1[0],"Regular:",answer1[1],"Mal:",answer1[7])

while(True):

    intentos += 1
    results = checkGuess(number,newNumber)
    answer = results.verifyNumber()
    print(newNumber)
    print("Bien:",answer[0],"Regular:",answer[1],"Mal:",answer[7])

    if answer[0]==4:
        print("Numero adivinado despues de: " ,intentos," intentos")
        break
    else:
        newGuess=askNew(answer,guess)
        newNumber = newGuess.newNumber()








