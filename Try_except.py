a = input("Ingrese un numero: ")
try:
    a= int(a)
    print ("Correcto, gracias!")
except ValueError:
    print ("Valor ingresado es incorrecto")
