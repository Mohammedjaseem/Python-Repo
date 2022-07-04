class human:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    
    def _bmi_calc(self):
        #(BMI) = (weight (kg) / height (m2)
        bmi = self.weight / (self.height ** 2)*100
        print("Yor BMI is: ", bmi,end=" ")
        return bmi

    def _bmi_status(bmi):
        print("\nIt's Status is: ", end="")
        if bmi < 18.5:
            print("Underweight")
        elif bmi >= 18.5 and bmi <= 24.9:
            print("Normal")
        elif bmi >= 25 and bmi <= 29.9:
            print("Overweight")
        elif bmi >= 30:
            print("Obese")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in cm: "))
height = height / 10 #convert to m
weight = float(input("Enter your weight: "))

Human = human(name, age, height, weight)
print("\nName is: ",Human.name)
bmi =  human._bmi_calc(Human)
human._bmi_status(bmi)



        