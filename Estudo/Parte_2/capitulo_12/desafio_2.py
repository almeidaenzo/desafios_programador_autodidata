# Crie uma classe Circle com um método chamado area que calcule e retorne sua
# área. Em seguida, crie um objeto Circle,chame area nele e exiba o resultado. Use a função 
# pi do módulo interno math do Python.
import math

class Circle:
    def __init__(self, r):
        self.raio = r

    def area(self):
        return self.raio ** 2 * math.pi
    
area_circulo = Circle(8)
print(area_circulo.area())