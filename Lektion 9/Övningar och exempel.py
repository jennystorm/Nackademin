# En klass som beskriver/definierar en rektangel

class Rectangle():
    # Attribut
    length = 0
    width = 0

    # Metoder
    def area(self):
        return self.width * self.length

    def omkrets(self):
        return self.width * 2 + self.length *2


# Object av klassen Rectangle
r1 = Rectangle()
r1.width = 5
r1.length = 10
print("Area rektangel 1:", r1.area())
print("Omkrets rektangel 1:", r1.omkrets())

r2 = Rectangle()
r2.width = 10
r2.length = 10
print("Area rektangel 2:", r2.area())
print("Omkrets rektangel 2:", r2.omkrets())

class Parallellogram():
    def __init__(self, length, width):
        self.__length = length  #Skyddar attributen, privata
        self.__width = width    #Attributen kallas även instans

    #Getter
    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width


    #Setter
    def set_length(self, length):
        if length > 0:
            self.__length = length
        else:
            print("Längden måste vara längre än 0.")

    def set_width(self, width):
        if width > 0:
            self.__width = width
        else:
            print("Bredden måste vara bredare än 0.")


    def area(self):
        return self.get_width() * self.get_length()

p1 = Parallellogram(1, 2)

p1.set_width(6)
p1.set_length(2)

print(p1.get_length())
print(p1.get_width())
print(p1.area())

# Lista av object
p_lista = [
    Parallellogram(1,2),
    Parallellogram(3, 4),
    Parallellogram(5, 6)
]

print("Lista med areor:")
for p in p_lista:
    print(p.area())

def get_summa(lista):
    summa = 0
    for r in lista:
        summa += r.area()
    return summa

#Lista med 1000 slumpartade parallellogram
import random
slump_lista = []
for i in range (0, 1000):
    slump_lista.append(Parallellogram(random.randint(1,10), random.randint(1, 10)))

print("Slumpartad lista:")
for i in slump_lista:
    print (i.area())

print(get_summa(slump_lista))