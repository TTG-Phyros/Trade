
class Pattern:

    def __init__(self):
        self.buying = False
        self.selling = False
        self.testDict = {
            "abandonnedBaby" : self.isAbandonnedBaby,
            "beltHold" : self.isBeltHold,
        }

    def isAbandonnedBaby(self, param):
        if (param == 1):
            self.buying = True
            self.selling = False
            return True
        return False
    
    def isBeltHold(self, param):
        if (param == 2):
            self.buying = False
            self.selling = True
            return True
        return False
    
    def checkPattern(self, param):
        for name, function in self.testDict.items():
            if (function(param) == True):
                return name



pattern = Pattern()

print(pattern.checkPattern(3))
print(pattern.buying)
print(pattern.selling)