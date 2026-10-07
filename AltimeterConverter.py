#Imports
from os import system

#Classes
class Altimeter:
    def __init__(self):
        self.hPa = 1013.25/29.9212
        self.inHg = 29.9212/1013.25  

    def unit(self,value:float):
        if value < 100:
            return "inHg"
        else:
            return "hPa"

    def convert(self,value:float):
        self.original = self.unit(value)
        if self.original == "inHg":
            return f"{value*self.hPa:.0f} hPa\n"
        elif self.original == "hPa":
            return f"{value*self.inHg:.2f} inHg\n"
        else:
            return "N/A\n"

#Functions
def toFloat(question:str):
    while True:
            try:
                variable = input(question).lower()
                if variable == "cls":
                    system("cls")
                elif variable == "exit":
                    exit()
                else:
                    variable = float(variable)
                    return variable
            except ValueError:
                print("Not a valid number or command")
                continue

#Backend
alt = Altimeter()
system("cls")

while True:
    #Input
    entered = toFloat("Enter value: ")

    #Convert
    converted = alt.convert(entered)

    #Output
    print(converted)