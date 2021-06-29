from generateNumber import genNum
from deleteNumber import delNum



class askNew:
    delete=[]

    def __init__(self,answer,guess):
        self.answer=answer
        self.guess=guess

    def newNumber(self):

        if self.answer[0]==0 and self.answer[1]==0:
            list = delNum(self.answer[7])
            newNumber = genNum(list.deletingNumbers())
            number = newNumber.generatingNumber()
            return number
        elif self.answer[0] == 0 and self.answer[1] >= 1:
            list = delNum(self.answer[7])
            newNumber = genNum(list.deletingNumbers())
            number=newNumber.put(self.answer[4],self.answer[5])

            return number
        elif self.answer[0] >= 1 and self.answer[1] == 0:

            list = delNum(self.answer[7])
            newNumber = genNum(list.deletingNumbers())
            number=newNumber.assing(self.answer[2],self.answer[3])

            return number
        elif self.answer[0] >= 1 and self.answer[1] >= 1:
            list = delNum(self.answer[7])
            newNumber = genNum(list.deletingNumbers())
            number=newNumber.case(self.answer[2],self.answer[3],self.answer[4],self.answer[5])

            return number
            

