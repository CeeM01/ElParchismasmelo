from random import randint

mensaje_modo = ('Escriba 1 en la consola para elegir modo real. El resultado de los dados será aleatorio.\n'
                'Escriba 2 en la consola para elegir modo desarrollador. El programa recibirá el resultado de los dados.')
advertencia_modo = "ATENCION: Solo se aceptan los numeros 1 o 2 como respuesta."

mensaje_dados = "Introduzca el resultado del lanzamiento para el dado"
advertencia_dados = "ATENCION: Solo se acepta un número del 1 al 6 como resultado del dado."
posible_dado = ["1", "2", "3", "4", "5", "6"]

mensaje_opcion = "Escriba el numero de la opcion que desea elegir."
advertencia_opcion = "ATENCION: Solo se acepta un numero de opcion entre 1 y 12."
posible_opcion = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

print("MODO DE JUEGO:")
print(mensaje_modo)
modo = input()
while modo !="1" and modo !="2":
    print(advertencia_modo)
    print(mensaje_modo)
    modo = input()

equipos = ["amarillo", "azul", "rojo", "verde"]

inicio_torres = {"amarillo": 68, "azul": 17, "rojo": 34, "verde": 51}

fichas_amarillo = {"amarillo1": 5, "amarillo2": 5, "amarillo3": 5, "amarillo4": 5}
fichas_azul = {"azul1": 22, "azul2": 22, "azul3": 22, "azul4": 22}
fichas_rojo = {"rojo1": 36, "rojo2": 36, "rojo3": 36, "rojo4": 36}
fichas_verde = {"verde1": 56, "verde2": 56, "verde3": 56, "verde4": 56}
las_fichas = [fichas_amarillo, fichas_azul, fichas_rojo, fichas_verde]

i = 0
jugando = True
while jugando:  # Para que los turnos roten mientras dura el juego
    turno = equipos[i]  # Asigna el turno segun el indice en la lista de equipos
    print("Turno del equipo {}.".format(turno))
    if modo == "1":
        dado1 = randint(1, 6)
        print("En dado1 sale {}.".format(dado1))
        dado2 = randint(1, 6)
        print("En dado2 sale {}.".format(dado2))
    else:
        print(mensaje_dados+"1.")
        dado1 = input()
        while dado1 not in posible_dado:
            print(advertencia_dados)
            print(mensaje_dados+"1.")
            dado1 = input()
        dado1 = int(dado1)

        print(mensaje_dados+"2.")
        dado2 = input()
        while dado2 not in posible_dado:
            print(advertencia_dados)
            print(mensaje_dados+"2.")
            dado2 = input()
        dado2 = int(dado2)

    fichas = las_fichas[i]
    opcion = 0
    opciones = {}
    for dados in range(3):
        if dados == 0:
            movimiento = dado1
        elif dados == 1:
            movimiento = dado2
        else:
            movimiento = dado1 + dado2

        for ficha in fichas:
            opcion += 1
            print("Opción {}: Mover {} casillas con la ficha {}. Pasaria de la casilla {} a la casilla {}.".format(opcion, movimiento, ficha, fichas[ficha], fichas[ficha] + movimiento))
            opciones[opcion] = ficha, (fichas[ficha] + movimiento)

    print()
    print(mensaje_opcion)
    usuario_elige = input()
    while usuario_elige not in posible_opcion:
        print(advertencia_opcion)
        print(mensaje_opcion)
        usuario_elige = input()

    print(fichas)                                                ## esto es ver en el diccionario las posiciones de las fichas antes de que se mueva
    ficha_que_mueve, nueva_posicion = opciones[int(usuario_elige)]
    fichas[ficha_que_mueve] = nueva_posicion
    print(fichas)                                                ## esto es para ver en el diccionario las posiciones de las fichas despues de haber movido

    # Cuando se acaba el turno de un equipo pasa el siguiente. Si el que jugó es el ultimo equipo, vuleve a jugar el primero
    if i != len(equipos) - 1:
        i += 1
    else:
        i = 0

    jugando = False
