frase = ["Hola","soy","Oscar"]
i=0
for string in frase:
    aux = frase[i].upper()
    frase.append(aux)
    i+=1
    print (frase)
    if i%3 == 0:
        break
    
    
