# Interes_compuesto: Hacer el diagrama e flujo y el programa en python, que lea un capital c y que averigue e imprima en cuantos meses se duplica, 
# si lo colocamos a un interes compuesto de 5% mensual. 

print("\n----------------------------------------------------------------------")
print("--------Calcular la cantidad de meses para duplicar el capital--------")
print("----------------------------------------------------------------------\n")

#input 
c=int(input("\nIngrese el capital "))
t=2*c

#processing 
m=0

while c<=t:
    c=(c*0.05)+c
    m=m+1

# output
print("\nLa cantidad de meses a las cuales el capital se duplico es de: "+str(m))
print(" ")