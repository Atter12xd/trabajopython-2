# Vamos a desarrollar un algoritmo en la que muestra la suma del numero actual y su anterior
# Vamos a indicar cuantos numeros desea
a = int(input("Ingrese el valor: "))

# Ahora usaremos las funciones "for" "in" "range"
for i in range (1, a ):
    a = i
    suma = a + (a-1)
# Ahora tocaria sumar del numerol actual y su anterior 

    print("la suma de", a, "+", a - 1, "es", suma)
