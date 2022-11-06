from random import randint
from turtle import *
bgpic("./parchis.gif")
register_shape("fichajavegif.gif")
register_shape("fichaunalgif.gif")
register_shape("fichaandesgif.gif")
register_shape("fichadistrigif.gif")
register_shape("dado1.gif")
register_shape("dado2.gif")
register_shape("dado3.gif")
register_shape("dado4.gif")
register_shape("dado5.gif")
register_shape("dado6.gif")
ListadeTortugas = [["azul1","azul2","azul3","azul4"],["rojo1","rojo2","rojo3","rojo4"],["amarillo1","amarillo2","amarillo3","amarillo4"],["verde1","verde2","verde3","verde4"]]
Listadeposiciondebase = [[(260,260),(210,210),(260,210),(210,260)],[(-260,260),(-210,210),(-260,210),(-210,260)],[(260,-260),(210,-210),(260,-210),(210,-260)],[(-260,-260),(-210,-210),(-260,-210),(-210,-260)]]
Lisadeimg_dado = ['dado1.gif','dado2.gif','dado3.gif','dado4.gif','dado5.gif','dado6.gif']
primero = ListadeTortugas[0]
segundo = ListadeTortugas[3]
tercero = ListadeTortugas[2]
cuarto = ListadeTortugas[1]
for x in range(len(primero)):
    primero[x] = Turtle()
    primero[x].speed(15)
    primero[x].shape("fichajavegif.gif")
    primero[x].up()
    primero[x].goto(Listadeposiciondebase[1][x])
for x in range(len(segundo)):
    segundo[x] = Turtle()
    segundo[x].speed(15)
    segundo[x].shape("fichaunalgif.gif")
    segundo[x].up()
    segundo[x].goto(Listadeposiciondebase[3][x])
for x in range(len(tercero)):
    tercero[x] = Turtle()
    tercero[x].speed(15)
    tercero[x].shape("fichaandesgif.gif")
    tercero[x].up()
    tercero[x].goto(Listadeposiciondebase[2][x])
for x in range(len(cuarto)):
    cuarto[x] = Turtle()
    cuarto[x].speed(15)
    cuarto[x].shape("fichadistrigif.gif")
    cuarto[x].up()
    cuarto[x].goto(Listadeposiciondebase[0][x])

#DADOS
img_dado1 = Turtle()
img_dado2 = Turtle()
img_dado1.up()
img_dado1.goto(20,0)
img_dado1.shape("dado1.gif")
img_dado2.up()
img_dado2.goto(-20,0)
img_dado2.shape("dado1.gif")
def animacion_dados():
	img_dado1.shape(Lisadeimg_dado[0])
	delay(300)
	img_dado2.shape(Lisadeimg_dado[3])
	delay(300)
	img_dado1.shape(Lisadeimg_dado[5])
	delay(300)
	img_dado2.shape(Lisadeimg_dado[2])
	delay(300)
	img_dado1.shape(Lisadeimg_dado[1])
	delay(300)
	img_dado2.shape(Lisadeimg_dado[4])
	delay(300)
	img_dado1.shape(Lisadeimg_dado[4])
	delay(300)
	img_dado2.shape(Lisadeimg_dado[1])
	delay(300)
	img_dado1.shape(Lisadeimg_dado[2])
	delay(300)
	img_dado2.shape(Lisadeimg_dado[5])
	delay(300)
	img_dado1.shape(Lisadeimg_dado[3])
	delay(300)
	img_dado2.shape(Lisadeimg_dado[0])
	delay(300)
	dado1 = randint(1, 6)
	dado2 = randint(1, 6)
	img_dado1.shape(Lisadeimg_dado[dado1-1])
	img_dado2.shape(Lisadeimg_dado[dado2-1])

animacion_dados()

mainloop()