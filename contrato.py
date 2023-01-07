mi_archivo = open("contra.txt", "r")
resutado = ""
for fila in mi_archivo:
    resutado += fila 

with open("contra.txt", "w") as text_file:
    text_file.write(resutado)