import sys, pygame #sys es para poder controlar funciones de sistema

pygame.init()#siempre que suas funciones de pygame esto tiene que ir ariiba de todo

zise=800,600#el tamaño de la pantalla
screen=pygame.display.set_mode(tuple(zise))#tiene que ser una tupla

pygame.display.set_caption("parchisparapobres")#nombre de la pantalla
imagen=pygame.image.load("tablero.png")#el tablero
color=pygame.Color(130,180,150)
pygame.draw.line(screen,color,(60,80),(160,100),8)

print (color.r)
print (color.g)
print (color.b)

while True:#es el metodo de la ventana

    for event in pygame.event.get():#aca van todos los eventos que sucedan, sea tirar dados, moverse, cerrar la ventana
        if event.type==pygame.QUIT:#para cerrar y que no crashee
            pygame.quit()#el metodo de salida
            sys.exit()#metodo de salida del sistema
    screen.blit(imagen,(0,0))#posicion de la imagen dentro de la ventana
    pygame.display.update()#para que sucedan los eventos