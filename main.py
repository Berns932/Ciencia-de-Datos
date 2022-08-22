#Bernardo Jardinez Arriaga
#222759-A
# 08-22-2022
#Brief: Generar un programa que permita calcular el promedio para un i número de valores introducidos
#       por el usuario.

n=0 #Sirve de contador
total=0 #Lo utilizó para guardar el promedio final
x=0 #Guarda los valores ingresados por el usuario
suma=0 #Se va haciendo la suma
i= input ("Dime cuántos números promediar: ")
i=int(i)

for n in range (0,i,1): #Sirve para hacer la suma
    x = input("Dame un número: ")
    suma=suma+int(x)

total= suma/i #Sirve para calcular el promedio

print("El promedio de los 20 números es: ", total)
