def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

print("calculadora sencilla")
print("1. sumar")
print("2. restar")
print("3. multiplicar")
print("4. dividir")

opcion = input("selecciona una opcion (1-4): ")

num1 = float(input("ingresa el primer numero: "))
num2 = float(input("ingresa el segundo numero: "))

if opcion == "1":
    resultado = sumar(num1, num2)
elif opcion == "2":
    resultado = restar(num1, num2)
elif opcion == "3":
    resultado = multiplicar(num1, num2)
elif opcion == "4":
    resultado = dividir(num1, num2)

print(f"resultado: {resultado}")