with open ("archivoPhyton.txt","r") as archivoRead:
    stringArchivo = archivoRead.read()
    print ("Normal:\n",stringArchivo)

    lineasInvertidas= stringArchivo[::-1]
    print ("Invertido:\n",lineasInvertidas)
   
       
        
