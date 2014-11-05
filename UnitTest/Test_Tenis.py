# -*- coding: utf8 -*-
#!/usr/bin/env python

import unittest
from tennis import tennis


class Test_Tenis(unittest.TestCase):

    def setUp(self):
        self.tenis = tennis()

    def test_mostrar_score_0_0(self):
        self.assertEqual('[0-0]', self.tenis.mostrar_score())

    def test_anotaJugador_1_0(self):
        self.assertEqual('', self.tenis.anotar(1, 0))

    def test_mostrar_score_1_0(self):
        self.tenis.anotar(1, 0)
        self.assertEqual('[15-0]', self.tenis.mostrar_score())

    def test_anotaJugador_1_1(self):
        self.assertEqual('', self.tenis.anotar(1, 1))

    def test_mostrar_score_1_1(self):
        self.tenis.anotar(1, 1)
        self.assertEqual('[15-15]', self.tenis.mostrar_score())

    def test_anotaJugador_2_1(self):
        self.assertEqual('', self.tenis.anotar(2, 1))

    def test_mostrar_score_2_1(self):
        self.tenis.anotar(2, 1)
        self.assertEqual('[30-15]', self.tenis.mostrar_score())

    def test_anotaJugador_2_2(self):
        self.assertEqual('', self.tenis.anotar(2, 2))

    def test_mostrar_score_2_2(self):
        self.tenis.anotar(2, 2)
        self.assertEqual('[30-30]', self.tenis.mostrar_score())

    def test_anotaJugador_3_2(self):
        self.assertEqual('', self.tenis.anotar(3, 2))

    def test_mostrar_score_3_2(self):
        self.tenis.anotar(3, 2)
        self.assertEqual('[40-30]', self.tenis.mostrar_score())

    def test_anotaJugador_3_3(self):
        self.assertEqual('deuse', self.tenis.anotar(3, 3))

    def test_mostrar_score_3_3(self):
        self.tenis.anotar(3, 3)
        self.assertEqual('[40-40]', self.tenis.mostrar_score())

    def test_anotaJugador_4_3(self):
        self.assertEqual('[advantage-40]', self.tenis.anotar(4, 3))

    def test_anotaJugador_4_5(self):
        self.assertEqual('[50-advantage]', self.tenis.anotar(4, 5))

    def test_mostrar_score_4_3(self):
        self.tenis.anotar(4, 3)
        self.assertEqual('[50-40]', self.tenis.mostrar_score())

    def test_anotaJugador_5_3(self):
        self.assertEqual('[set-40]', self.tenis.anotar(5, 3))

    def test_anotaJugador_3_4(self):
        self.assertEqual('[40-set]', self.tenis.anotar(3, 5))

    def test_mostrar_score_5_3(self):
        self.tenis.anotar(5, 3)
        self.assertEqual('[60-40]', self.tenis.mostrar_score())

if __name__ == "__main__":
    unittest.main()
