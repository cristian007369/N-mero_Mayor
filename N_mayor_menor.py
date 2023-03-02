#Programa para determinar que número es mayor
print("---------------------------------------")
print("------------Tarea No.1-----------------")
print("---------------------------------------")
#imput
a=int(input("Digite un número Entero positivo para X: " ))
while a<0:
    a=int(input("Por favor, el número X tiene que ser positivo: "))

b=int(input("Digite otro número Entero positivo para Y: " ))
while b<0:
    b=int(input("Y tiene que ser un número positivo: "))

#output
if a>b:
    print(str(a) + " es mayor que " + str(b))
else:
    print(str(b) + " es mayor que " + str(a))