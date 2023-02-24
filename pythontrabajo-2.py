num_actual = int(input("Ingrese un número: "))
num_anterior = 0

while num_actual != 0:
    suma = num_actual + num_anterior
    print(f"La suma de {num_actual} y {num_anterior} es {suma}")
    num_anterior = num_actual
    num_actual = int(input("Ingrese otro número: "))
