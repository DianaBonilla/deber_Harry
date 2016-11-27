##ESCUELA POLITECNICA NACIONAL
##ESCUELA DE FORMACION DE TECNOLOGOS
##PROGRAMACION AVANZADA
##AUTOR:DIANA BONILLA-VALERIA OCHOA
##TITULO: PRACTICA DE MANEJO DE ARCHIVOS

print("\t\t\t     Escuela Politécnica Nacional")
print("\t\t\t Escuela de Formación de Tecnólogos")
print("\t\t\t\t  Programación Avanzada")
print("\t\t\t\tDiana Bonilla - Valeria Ochoa")
print("Cuenta el numero de ocurrencias de palabras en un archivo")
p= "Quirrell"
##def creartxt():
##    archivo = open('HarryPotter.txt','a')
##    archivo.close()

def contarPalabras():
    archivo=open('HarryPotter.txt','r')
    data=archivo.readlines()
    archivo.close()
    contador=0
    cont=0

    for renglon in data:
        for palabra in renglon.split(' '):
            if palabra == "Hagrid":
                contador +=2
                print(str(contador),palabra)
##                if palabra == "Harry":
##                    cont+=1
##                    print("Hay: ", str(cont),"con la palabra Harry")
                
            
def grabartxt():
    archivo = open('NumPalaHarry.txt','a')
    archivo.write("hola")
    archivo.close()

##creartxt()
contarPalabras()
grabartxt()
