#Cree un bucle For de Python.

def counting(max_num):
  for c in range(1, max_num+1):
    print(c)


counting(10)

#Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.

def suma(x, y, z):
  return x + y + z

print(suma(1, 2, 3))

#Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.

suma_lambda = lambda x, y, z: x + y + z

print(suma_lambda(4, 5, 6))

#Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista. 

nombre = 'Enrique'

lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']

for nombre_lista in lista_nombre:
  if nombre == nombre_lista:
      print(f"{nombre} esta en la lista.")
      break
else:
  print(f"{nombre} no esta en la lista.")
