# vamos a desarrollar un algoritmo que muestre los numeros divisibles entre 5 
# de una lista de numeros

# creando nuestro Lista de numeros 
numeros = [15, 24, 35, 42, 50, 66, 73]
# Lista vacia para almacenar los numeros divisibles entre 5
Divisible = []
# Recorremos cada elemento en la lista de numeros
for x in numeros:
    #Aca va a verificar si el numero es divisible entre 5
    if x % 5 == 0:
      # si es divisible, se agregara a la lista de numeros divisible entre 5 
      Divisible.append(x) # Append se usa para agrega un ítem al final de la lista
