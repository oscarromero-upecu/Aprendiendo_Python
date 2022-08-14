Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
tupla = tuple()
tupla
()
tupla2 = ("casa","56")
tupla2
('casa', '56')
tupla3=("hogar",)
tupla3
('hogar',)
tupla2[1]
'56'
hogar in tupla3
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    hogar in tupla3
NameError: name 'hogar' is not defined
"hogar" in tupla3
True
# diccionario
dic=dict()
dic
{}
frutas = ("Manzana": "Roja", "Banana":"Amarilla")
SyntaxError: invalid syntax
frutas = ("Manzana": "Roja", "Banana": "Amarilla")
SyntaxError: invalid syntax
frutas = ("Manzana" : "Roja", "Banana": "Amarilla")
SyntaxError: invalid syntax
frutas = ("Manzana":"Roja","Banana":"Amarilla")
SyntaxError: invalid syntax
frutas["Manzana"]="Roja"
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    frutas["Manzana"]="Roja"
NameError: name 'frutas' is not defined
frutas = dict()
frutas["Manzana"]="Roja"
frutas
{'Manzana': 'Roja'}
frutas[tupla3]="Azul"
frutas
{'Manzana': 'Roja', ('hogar',): 'Azul'}
persona = ("Pedro": "Arriba Tijuana", "Jose":"No manches wey")
SyntaxError: invalid syntax
persona = dict("Pedro": "Arriba Tijuana", "Jose":"No manches wey")
SyntaxError: invalid syntax
Persona["Jose"]="Arriba Mexico"
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    Persona["Jose"]="Arriba Mexico"
NameError: name 'Persona' is not defined
Persona = dict()
Persona["Jose"]="Arriba Mexico"
Persona["Pedro"]="Abajo cabrones"
Persona
{'Jose': 'Arriba Mexico', 'Pedro': 'Abajo cabrones'}
jose in Persona
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    jose in Persona
NameError: name 'jose' is not defined
"Jose" in Persona
True
"Arriba Mexico" in Persona
False
nombre = input("Ingrese el nombre")
Ingrese el nombre
if nombre in Persona
SyntaxError: expected ':'
Persona = ("Pedro": "Arriba Tijuana", "Jose":"No manches wey")
SyntaxError: invalid syntax
lugares=[]
quito=(23424.3,23456.6)
guayaquil=(232423.44,23424.5)
lugares.append(quito,guayaquil)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    lugares.append(quito,guayaquil)
TypeError: list.append() takes exactly one argument (2 given)
lugares.append(quito)
lugares.append(guayaquil)
lugares
[(23424.3, 23456.6), (232423.44, 23424.5)]
listaUno=["Marcelo","Carlos"]
listaDos=("Juan","Pedro")
nombres=(listaUno,ListaDos)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    nombres=(listaUno,ListaDos)
NameError: name 'ListaDos' is not defined. Did you mean: 'listaDos'?
nombres=(listaUno,listaDos)
nombres
(['Marcelo', 'Carlos'], ('Juan', 'Pedro'))
nombres[0]
['Marcelo', 'Carlos']
nombres[0][1]
'Carlos'
nombre=""" Pedro esta usando mas de una linea
nombre
"""
nombre
' Pedro esta usando mas de una linea\nnombre\n'
nombre[3]
'd'
nombre[-1]
'\n'
autor = "Musica latina"
nombre + autor
' Pedro esta usando mas de una linea\nnombre\nMusica latina'
nombre+autor.upper()
' Pedro esta usando mas de una linea\nnombre\nMUSICA LATINA'
nombre.split('')
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    nombre.split('')
ValueError: empty separator
nombre.split("")
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    nombre.split("")
ValueError: empty separator
nombre.split(" ")
['', 'Pedro', 'esta', 'usando', 'mas', 'de', 'una', 'linea\nnombre\n']
",".join(nombre)
' ,P,e,d,r,o, ,e,s,t,a, ,u,s,a,n,d,o, ,m,a,s, ,d,e, ,u,n,a, ,l,i,n,e,a,\n,n,o,m,b,r,e,\n'
nombre[:3]
' Pe'
nombre[:4]
' Ped'
