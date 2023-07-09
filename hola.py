#code by @sov - sonv-1
#utf-8 

print("HOLA MUNDO")

name = input("Ingrese el nomnbre a almacenar: ")
print(" -----> " + name)
# simplificado y con "f-strings"
name1 = input("Name: ")
print(f"Hello, {name1}")

#           Secuencias de elementos
# STRINGS - ordenadas, inmutables
cadena_texto = "texto"

# LISTAS - ordenadas, mutables
lista = ['Harry', 'Ron', 'Hermione']
print(lista)
lista.append('Draco')
lista.sort()
print(lista)

# TUPLAS - ordenado, inmutable   _ generalmente para coordenadas o así
tupla = (12, 56)

# SETS - desordenado, NA  - lista sin repeticiones de elementos (como no es ordenado no se accede a elementos individuales con un índice)
s = set()
# Add some elements:
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)
s.add(1)
s.remove(2)

# Print the set:
print(s)


# DICCIONARIOS - desordenados, mutables, similar a un json, se obtinen elementos por un llave asociada  
casas = {'harry':'grif', 'draco':'slith'}
# llave la primera parte, dato almacenado la segunda -> casas['harry'] devuelve: 'grif'
casas['hermione'] = 'grif'


#            CLASES (Con ejemplo)

class vuelo():
  def __init__(self, capacidad):
    self.capacidad = capacidad
    self.pasajeros = []

  def agregar_pasajeros(self, nombre):
    if not self.puestos_disponibles():
      return False
    self.pasajeros.append(nombre)
    return True
    
  def puestos_disponibles(self):
    return self.capacidad - len(self.pasajeros)
  

avion = vuelo(3)
lista = ['Harry', 'Ron', 'Hermione']
lista.append('Draco')

for persona in lista:
  if avion.agregar_pasajeros(persona):
    print(f"Puesto asgurado para {persona}")
  else:
    print(f"No hay puesto para {persona}")



#       