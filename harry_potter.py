##ESCUELA POLITECNICA NACIONAL
##ESCUELA DE FORMACION DE TECNOLOGOS
##PROGRAMACION AVANZADA
##AUTOR:DIANA BONILLA-VALERIA OCHOA
##TITULO: OCURRENCIAS DE UNA PALABRA

print("\t\t\t     Escuela Politécnica Nacional")
print("\t\t\t Escuela de Formación de Tecnólogos")
print("\t\t\t\t  Programación Avanzada")
print("\t\t\t\tDiana Bonilla - Valeria Ochoa")
print("Cuenta el numero de ocurrencias de palabras en un archivo")
##p= "Quirrell"
##def creartxt():
##    archivo = open('HarryPotter.txt','a')
##    archivo.close()

def contarPalabras():
    palabra = str(input("Ingrese la palabra: "))
    archivo=open('HarryPotter.txt','r')
##    data=archivo.readlines()
##    archivo.close()
    contador=0
##    cont=0

####    for renglon in data:
####        for palabra in renglon.split(' '):
####            if palabra == "Hagrid":
####                contador +=1
####                print(str(contador),palabra)
##                if palabra == "Harry":
##                    cont+=1
##                    print("Hay: ", str(cont),"con la palabra Harry")
                
    lines = archivo.readlines()
    for line in lines:
        palabras = line.split(" ")
        for p in palabras:
            if p == palabra:
                contador = contador + 1
    print(contador,palabra)
##def grabartxt():
##    archivo = open('NumPalaHarry.txt','a')
##    archivo.write("hola")
##    archivo.close()

##creartxt()
contarPalabras()
##grabartxt()
