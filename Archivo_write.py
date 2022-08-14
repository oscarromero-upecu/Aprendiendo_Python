def EscribirArchivo():
    archivoLista = ["Bienvenido","a mi primer","archivo Phyton",]
    with open ("archivoPhyton.txt","w") as archivoBienvenida:
        for string in archivoLista:
            archivoBienvenida.write("{}\n".format(string))

