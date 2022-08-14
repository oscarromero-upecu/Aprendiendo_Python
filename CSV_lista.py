import csv
ListaUsuario = ["Rapidos y Fueriosos","La Monja","Predator",]
with open ("Peliculas.csv","w", newline="") as peliculas:
    escribir = csv.writer(peliculas,delimiter=",")
    escribir.writerow(ListaUsuario)
    
with open("Peliculas.csv", newline="") as pelicula:  
    Leer = csv.reader(pelicula)
    for fila in Leer:
        print("Archivo CSV creado: \n",fila)
