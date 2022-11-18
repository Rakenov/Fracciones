class Fraction:
    ##Inicio atributos##
    numerator=0
    denominator=1
    ##Fin Atributos##
    

    ## Inicio metodos##
    def __init__(self, numerator, denominator): # Constructor##
        self.numerator = numerator
        self.denominator = denominator

    def multiply(self, b):  # Multiplicación
        numerator = self.numerator*b.numerator
        denominator = self.denominator*b.denominator
        r = Fraction(numerator, denominator)
        r.show()

    def division(self, b):  # División
        numerator = self.numerator*b.denominator
        denominator = self.denominator*b.numerator
        r = Fraction(numerator, denominator)
        r.show()

    def addition(self, b):  # Suma
        numerator = self.numerator*b.denominator + self.denominator*b.numerator
        denominator = self.denominator*b.denominator
        r = Fraction(numerator, denominator)
        r.show()

    def substraction(self,b):  # Resta
        numerator = self.numerator*b.denominator - self.denominator*b.numerator
        denominator = self.denominator*b.denominator
        r = Fraction(numerator, denominator)
        r.show()

    def show(self):  # Mostrar en pantalla
        print(self.numerator,"/",self.denominator)
    ## Fin metodos##

A = int(input("Ingrese Numerador A:"))
B = int(input("Ingrese Denominador A:"))
    

D = int(input("Ingrese Numerador B:"))
C = int(input("Ingrese Denominador B:"))

a=Fraction(A,B)
b=Fraction(D,C)

a.show()
b.show()

if(B!=0):
    if(C!=0):
        
        Menu=int(input("Elija una de las siguientes operaciones. \n \n 1)Multiplicación \n 2)División \n 3)Suma \n 4)Resta \n 5)Salir\n" ))

        if(Menu==1):    
            a.multiply(b)
        elif(Menu==2):
            a.division(b)
        elif(Menu==3):
            a.addition(b)
        elif(Menu==4):
            a.substraction(b)
        elif(Menu==5):
            print("Saliendo")
        else:
            print("Ingrese un número valido")
    else:(print("Ingrese denominadores validos"))        
else:(print("Ingrese denominadores validos"))            

