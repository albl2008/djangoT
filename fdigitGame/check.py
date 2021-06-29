class checkGuess:
    numerosmal=[]

    def __init__(self,number,guess):
        self.number=number
        self.guess=guess
        

    def verifyNumber(self):
        posicion = []
        opcorrecta = []
        opregular = []
        bien = 0
        regular = 0
        posicionregular=[]
        mal = 0
        posicionmal=[]

        for i in range (4):
            if self.guess[i] == self.number[i]:
                posicion.append(int(i))
                opcorrecta.append(int(self.guess[i]))
                bien += 1
        for i in range (4):
            for j in range (4):
                if self.number[i] == self.guess[j] and i != j:
                    regular += 1
                    posicionregular.append(int(j))
                    opregular.append(int(self.guess[j]))
        for i in range (4):
            if self.guess[i] not in self.number:
                mal += 1
                self.numerosmal.append(self.guess[i])
                posicionmal.append(int(i))

          
        respuestas=[bien, regular,opcorrecta,posicion,opregular,posicionregular,mal,self.numerosmal, posicionmal]
        return respuestas
        
