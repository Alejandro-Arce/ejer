paginas = [
    "Pagina 0 ) erace una vez... \n ¿Que quieres hacer? \n1... \n2... \n3...",
    "Pagina 1 ) erace una vez... \n ¿Que quieres hacer? \n1... \n2... \n3...",
    "Pagina 2 ) erace una vez... \n ¿Que quieres hacer? \n1... \n2... \n3...",
]


def showPagina(NumPagina):
    text =paginas[NumPagina ]
    print(text)
    respuesta = input()
    showPagina(int(respuesta))

showPagina(0)
