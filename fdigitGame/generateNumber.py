import random

class genNum:
    numbers=[]
    posicions=[]
    numbersb=[]
    posicionsb=[]
    
    def __init__(self,list):
         self.list = list
    
    def generatingNumber(self):
        random.shuffle(self.list)
        number = self.list[0:4]
        return number

    def assing(self,numbersb,posicionsb):
        self.numbersb = numbersb
        self.posicionsb = posicionsb
        testNumber = self.generatingNumber()
        while(True):
            for i in range (len(self.numbersb)):
                testNumber[self.posicionsb[i]]=self.numbersb[i]
            if len(set(testNumber))==4:
                return testNumber
                break
            else:
                testNumber = self.generatingNumber()


    def put(self,numbers,posicions):
        self.numbers = numbers
        self.posicions = posicions
        testNumber = self.generatingNumber()
        while(True):
            if len(self.numbers) == 1:
                if self.numbers[0] in testNumber and testNumber[posicions[0]] != self.numbers[0]:
                    return testNumber
                    break
                else:
                    testNumber = self.generatingNumber()
            elif len(self.numbers)==2:
                if self.numbers[0] in testNumber and testNumber[posicions[0]] != self.numbers[0] and testNumber[posicions[1]] != self.numbers[1] and self.numbers[1] in testNumber:

                    return testNumber
                    break
                else:
                    testNumber=self.generatingNumber()
            elif len(self.numbers)==3:
                testNumber[self.posicions[0]]=self.numbers[1]
                testNumber[self.posicions[1]]=self.numbers[2]
                testNumber[self.posicions[2]]=self.numbers[0]
                if len(set(testNumber))==4:

                    return testNumber
                    break
                else:
                    testNumber=self.generatingNumber()
            elif len(self.numbers)==4:
                testNumber[self.posicions[0]]=self.numbers[1]
                testNumber[self.posicions[1]]=self.numbers[3]
                testNumber[self.posicions[2]]=self.numbers[0]
                testNumber[self.posicions[3]]=self.numbers[2]
                return testNumber

    def case(self,numbersb,posicionsb,numbers,posicions):
        self.numbers = numbers
        self.posicions = posicions
        self.numbersb = numbersb
        self.posicionsb = posicionsb
        testNumber = self.generatingNumber()
        if len(self.numbers) == 1 and len(self.numbersb) == 1:
            while (True):
                testNumber[self.posicionsb[0]]=self.numbersb[0]
                for i in range (4):
                    if testNumber[i] == self.numbers[0] and i != self.posicions[0] and len(set(testNumber))==4:
                        return testNumber
                        break
                    else:
                         testNumber=self.generatingNumber()

        elif len(self.numbers) == 2 and len(self.numbersb) == 1:
            while (True):
                testNumber[self.posicionsb[0]]=self.numbersb[0]
                testNumber[self.posicions[0]]=self.numbers[1]
                testNumber[self.posicions[1]]=self.numbers[0]
                if len(set(testNumber))==4:
                    return testNumber
                    break
                else:
                     testNumber=self.generatingNumber()
        elif len(self.numbers) == 2 and len(self.numbersb) == 2:
            testNumber[self.posicionsb[0]]=self.numbersb[0]
            testNumber[self.posicionsb[1]]=self.numbersb[1]
            testNumber[self.posicions[0]]=self.numbers[1]
            testNumber[self.posicions[1]]=self.numbers[0]
            
            return testNumber
        elif len(self.numbers) == 1 and len(self.numbersb) == 2:
            while (True):
                testNumber[self.posicionsb[0]]=self.numbersb[0]
                testNumber[self.posicionsb[1]]=self.numbersb[1]
                if self.numbers[0] in testNumber:
                    if len(set(testNumber)) == 4:
                        return testNumber
                        break
                    else:
                        testNumber=self.generatingNumber()
                else:
                    testNumber=self.generatingNumber()
        elif len(self.numbers)== 3 and len(self.numbersb)==1:
            testNumber[self.posicionsb[0]]=self.numbersb[0]
            testNumber[self.posicions[0]]=self.numbers[1]
            testNumber[self.posicions[1]]=self.numbers[2]
            testNumber[self.posicions[2]]=self.numbers[0]

            return testNumber


        

            


