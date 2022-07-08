#decalre class Car

class cars():
    def __init__(self, modelname, make, color):
        self.modelname = modelname
        self.make = make
        self.color = color
        

honda = cars('city', 'honda', 'red')
#addning new value to the class
honda.cc = 1200
toyota = cars('corolla', 'toyota', 'blue')
bmw = cars('x5', 'bmw', 'black')

'''
honda.price = "$100"
honda.color = "red"
honda.model = "Civic"

toyota.price = "$200"
toyota.color = "blue"
toyota.model = "Corolla"

bmw.price = "$300"
bmw.color = "black"
bmw.model = "X5"

'''

print(honda.modelname)
print(honda.__dict__)