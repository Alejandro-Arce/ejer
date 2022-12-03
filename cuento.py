#programa de libro con eleccion (el usuario va elijiendo el runbo de la historia)
#primero comiensa en la pagina 0 y elige en cual continuar.
paginas = [
    "Pagina 0 ) erace una vez... \n ¿Que quieres hacer? \n1... \n2... \n3...",
    "Pagina 1 ) erace una vez... \n ¿Que quieres hacer? \n1... \n2... \n3...",
    "Pagina 2 ) erace una vez... \n ¿Que quieres hacer? \n1... \n2... \n3...",
]

#se define showPagina como el numero de pagina, el texto sera indicado por el numero de la pagina escogida se imprime la eleccion y...
#el numero de la pagina escogida es conbertida a numero entero.

def showPagina(NumPagina):
    text =paginas[NumPagina ]
    print(text)
    respuesta = input()
    showPagina(int(respuesta))

showPagina(0)
