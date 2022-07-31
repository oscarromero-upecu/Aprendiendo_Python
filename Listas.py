#listas son contenedores se representan con corchete []
ListaArtistas = ["Heroes del Silencio","Mago de Oz","Camilo"]
print(ListaArtistas)
try:
    artista = input("Ingrese un nombre de artista: ")
    print ("Correcto, gracias!")
except ValueError:
    print ("Caracter ingresado es incorrecto")
#appened agrega un item al ultimo de la lista
ListaArtistas.append(artista)
print(ListaArtistas)
