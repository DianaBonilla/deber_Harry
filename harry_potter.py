##ESCUELA POLITECNICA NACIONAL
##ESCUELA DE FORMACION DE TECNOLOGOS
##ALGORITMOS FUNDAMENTALES
##AUTOR:DIANA BONILLA-VALERIA OCHOA
##TITULO: PRACTICA DE MANEJO DE ARCHIVOS

print("\t\t\t     Escuela Politécnica Nacional")
print("\t\t\t Escuela de Formación de Tecnólogos")
print("\t\t\t\t  Programación Avanzada")
print("\t\t\t\tDiana Bonilla - Valeria Ochoa")
print("Cuenta el numero de ocurrencias de palabras en un archivo")
##def creartxt():
##    archivo = open('HarryPotter.txt','a')
##    archivo.close()
    
def grabartxt():
    archivo = open('HarryPotter.txt','a')
    archivo.write('Hola')
    archivo.close()

##creartxt()
grabartxt()
