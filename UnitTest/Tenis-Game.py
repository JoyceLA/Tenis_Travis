# -*- coding: utf8 -*-



"""
	SIMULANDO UN JUEGO DE TENNIS
	>>> ingresarTotalJuegos(2)
	>>> mostrar_score()
	'[0-0]'
	>>> anotar(1,0)
	''
	>>> mostrar_score()
	'[15-0]'
	>>> anotar(0,1)
	''
	>>> mostrar_score()
	'[15-15]'
	>>> anotar(1,0)
	''
	>>> mostrar_score()
	'[30-15]'
	>>> anotar(0,1)
	''
	>>> mostrar_score()
	'[30-30]'
	>>> anotar(1,0)
	''
	>>> mostrar_score()
	'[40-30]'
	>>> anotar(0,1)
	'deuse'
	>>> mostrar_score()
	'[40-40]'
	>>> anotar(1,0)
	'[advantage-40]'
	>>> mostrar_score()
	'[50-40]'
	>>> anotar(1,0)
	'[set-40]'
	>>> mostrar_score()
	'[60-40]'

	
	>>> mostrar_score()
	'[0-0]'
	>>> anotar(1,0)
	''
	>>> mostrar_score()
	'[15-0]'
	>>> anotar(0,1)
	''
	>>> mostrar_score()
	'[15-15]'
	>>> anotar(1,0)
	''
	>>> mostrar_score()
	'[30-15]'
	>>> anotar(0,1)
	''
	>>> mostrar_score()
	'[30-30]'
	>>> anotar(1,0)
	''
	>>> mostrar_score()
	'[40-30]'
	>>> anotar(0,1)
	'deuse'
	>>> mostrar_score()
	'[40-40]'
	>>> anotar(1,0)
	'[advantage-40]'
	>>> mostrar_score()
	'[50-40]'
	>>> anotar(1,0)
	'[set-40]'
	>>> mostrar_score()
	'[60-40]'
	

	>>> mostrar_score()
	'[0-0]'
	>>> anotar(1,0)
	''
	>>> mostrar_score()
	'[15-0]'
	>>> anotar(0,1)
	''
	>>> mostrar_score()
	'[15-15]'
	>>> anotar(1,0)
	''
	>>> mostrar_score()
	'[30-15]'
	>>> anotar(0,1)
	''
	>>> mostrar_score()
	'[30-30]'
	>>> anotar(1,0)
	''
	>>> mostrar_score()
	'[40-30]'
	>>> anotar(0,1)
	'deuse'
	>>> mostrar_score()
	'[40-40]'
	>>> anotar(1,0)
	'[advantage-40]'
	>>> mostrar_score()
	'[50-40]'
	>>> anotar(1,0)
	'[set-40]'
	>>> mostrar_score()
	'[60-40]'
	

	
"""
total = 0
numjuego = 0

	
player1 = 0
player2 = 0
vuelta1 = 0
vuelta2 = 0
puntos1 = 0
puntos2 = 0
extra1 = 0
extra2 = 0
info = ""

def ingresarTotalJuegos(cantidad): 
	numjuego,total
	numjuego = cantidad
	total = cantidad


def mostrar_score():
	print "["+str(player1)+"-"+str(player2)+"]"

def anotar(play1, play2):
	info = ""
	global player1,player2,vuelta1,vuelta2,puntos1,puntos2,extra1,extra2,gameP1,gameP2
	
	
	if vuelta1 <= 1:
		puntos1 = 15
	if vuelta2 <= 1:
		puntos2 = 15
	if vuelta1 >= 2:
		puntos1 = 10
	if vuelta2 >=2:
		puntos2 = 10
	
	if play1 == 1: #Anoto el jugador 1
		player1 += puntos1
		vuelta1 += 1
	elif play2 == 1: #Anoto el jugador 2
		player2 += puntos2
		vuelta2 += 1

	gana1  = 0
	gana2 = 0
	start = numjuego
	if player1 >= 40 or player2 >= 40:
		
		game = player1 - player2
		
		if game == (20*total):
			print "GANO EL JUGADOR 1"
		elif (-1*game) == (20*total):
			print "GANO EL JUGADOR 2"
		if player1 == player2:
			info= "deuse"
		elif player1 > player2:
			info=  "[advantage-"+str(player2)+"]"
			gana1 = player1-player2
		
		elif player1 < player2:
			info=  "["+str(player1)+"-advantage]"
			gana2 = player2-player1
		
		if gana1 == 20:
			info=  "[set-"+str(player2)+"]"
			numjuego -= 1
			
		elif gana2== 20:
			info=  "["+str(player1)+"-set]"
			numjuego -=1
			print "NUMERO "+str(numjuego)+info

		
		
	
		
		
	
	









		
