# -*- coding: utf8 -*-
#!/usr/bin/env python

"""
SIMULANDO UN JUEGO DE TENNIS
>>> mostrar_score()
'[0-0]'
>>> anotar(1,0)
''
>>> mostrar_score()
'[15-0]'
>>> anotar(1,1)
''
>>> mostrar_score()
'[15-15]'
>>> anotar(2,1)
''
>>> mostrar_score()
'[30-15]'
>>> anotar(2,2)
''
>>> mostrar_score()
'[30-30]'
>>> anotar(3,2)
''
>>> mostrar_score()
'[40-30]'
>>> anotar(3,3)
'deuse'
>>> mostrar_score()
'[40-40]'
>>> anotar(4,3)
'[advantage-40]'
>>> mostrar_score()
'[50-40]'
>>> anotar(5,3)
'[set-40]'
>>> mostrar_score()
'[60-40]'

"""


class tennis():

    def __init__(self):
        self.player1 = 0
        self.player2 = 0
        self.vuelta1 = 0
        self.vuelta2 = 0
        self.puntos1 = 0
        self.puntos2 = 0
        self.extra1 = 0
        self.extra2 = 0
        self.info = ""

    def cambiarPuntaje(self, play1, play2):
        self.puntos1 = 10
        self.puntos2 = 10

        if play1 < 2:
            self.player1 = 15 * play1
        else:
            self.player1 = self.puntos1 * (play1 + 1)

        if play2 < 2:
            self.player2 = 15 * play2
        else:
            self.player2 = self.puntos2 * (play2 + 1)

    def anotar(self, play1, play2):
        self.cambiarPuntaje(play1, play2)
        if self.player1 >= 40 and self.player2 >= 40:
            gana = self.player1 - self.player2
            if self.definirGanador(gana) == 0:
                self.validarPuntaje(self.player1, self.player2)
        return self.info

    def definirGanador(self, gana):
        if gana == 20:
            self.info = "[set-" + str(self.player2) + "]"
            return 1
        elif gana == -20:
            self.info = "[" + str(self.player1) + "-set]"
            return 1
        return 0

    def validarPuntaje(self, player1, player2):
        self.info = "[" + str(self.player1) + "-advantage]"
        if self.player1 == self.player2:
            self.info = "deuse"
        elif self.player1 > self.player2:
            self.info = "[advantage-" + str(self.player2) + "]"

    def mostrar_score(self):
        return "[" + str(self.player1) + "-" + str(self.player2) + "]"
'''
t=tennis()
t.anotar(1,0)
t.anotar(2,0)

print t.mostrar_score()
'''
