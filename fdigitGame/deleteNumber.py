class delNum:
    list=[0,1,2,3,4,5,6,7,8,9]

    def __init__(self,numbers):
        self.numbers=numbers


    def deletingNumbers(self):
        for j in range (len(self.numbers)):
            if self.numbers[j] in self.list:
                self.list.remove(self.numbers[j])
        return self.list
