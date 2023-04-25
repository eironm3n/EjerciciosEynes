import math

class Circulo:
    
    def __init__(self, radio):
        if radio <= 0:
            raise ValueError("El radio debe ser mayor a 0.")
        self._radio = radio
    
    def __str__(self):
        return f"Círculo de radio {self._radio}"
    
    @property
    def radio(self):
        return self._radio
    
    @radio.setter
    def radio(self, new_radio):
        if new_radio <= 0:
            raise ValueError("El radio debe ser mayor a 0.")
        self._radio = new_radio
    
    def area(self):
        return math.pi * self._radio ** 2
    
    def perimetro(self):
        return 2 * math.pi * self._radio
    
    def __mul__(self, n):
        if n <= 0:
            raise ValueError("El número multiplicador debe ser mayor a 0.")
        return Circulo(self._radio * n)
    

c1 = Circulo(5)
print(c1)
print("Radio: ", c1.radio)
print("Área: ", c1.area())
print("Perímetro: ", c1.perimetro())

c1.radio = 10
print("Radio modificado:", c1.radio)

c2 = c1 * 3
print(c2)