from turtle import *
bgpic("parchis.gif")
register_shape('fichaunalgif.gif')
register_shape('fichaandesgif.gif')
register_shape('fichadistrigif.gif')
register_shape('fichajavegif.gif')
ListadeTortugas = [["azul1","azul2","azul3","azul4"],["rojo1","rojo2","rojo3","rojo4"],["amarillo1","amarillo2","amarillo3","amarillo4"],["verde1","verde2","verde3","verde4"]]
Listadeposiciondebase = [[(240,240),(180,180),(240,180),(180,240)],[(-240,240),(-180,180),(-240,180),(-180,240)],[(240,-240),(180,-180),(240,-180),(180,-240)],[(-240,-240),(-180,-180),(-240,-180),(-180,-240)]]
Listadecolor = ['MidnightBlue','DarkRed','DarkGoldenrod','ForestGreen']
unal = ListadeTortugas[0]
andes = ListadeTortugas[1]
distri = ListadeTortugas[2]
javeriana = ListadeTortugas[3]

for color in range(4):
	for posicion in range(4):
		ListadeTortugas[color][posicion]=Turtle()
		ListadeTortugas[color][posicion].speed(15)
		ListadeTortugas[color][posicion].color(Listadecolor[color])
		unal[posicion].shape("fichaunalgif.gif")
		andes[posicion].shape("fichaandesgif.gif")
		ListadeTortugas[color][posicion].shape("fichaandesgif.gif")
		ListadeTortugas[color][posicion].shape("fichaandesgif.gif")
		ListadeTortugas[color][posicion].up()
		ListadeTortugas[color][posicion].goto(Listadeposiciondebase[color][posicion])
mainloop()