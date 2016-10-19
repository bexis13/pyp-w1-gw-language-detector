# -*- coding: utf-8 -*-
import unittest

from language_detector import (detect_language, LANGUAGES)


class TestLanguageDetector(unittest.TestCase):

    def test_detect_language_spanish_with_module_language_specification(self):
        text = """
                Lionel Andrés Messi Cuccittini (Rosario, 24 de junio de 1987),
                conocido como Leo Messi, es un futbolista argentino11 que juega
                como delantero en el Fútbol Club Barcelona y en la selección
                argentina, de la que es capitán. Considerado con frecuencia el
                mejor jugador del mundo y calificado en el ámbito deportivo como el
                más grande de todos los tiempos, Messi es el único futbolista en la
                historia que ha ganado cinco veces el FIFA Balón de Oro –cuatro de
                ellos en forma consecutiva– y el primero en
                recibir tres Botas de Oro.
                """
        result = detect_language(text, LANGUAGES)
        self.assertEqual(result, 'Spanish')


    def test_detect_language_german_with_module_language_specification(self):
        text =  """
                Messi spielt seit seinem 14. Lebensjahr für den FC Barcelona.
                Mit 24 Jahren wurde er Rekordtorschütze des FC Barcelona, mit 25
                der jüngste Spieler in der La-Liga-Geschichte, der 200 Tore
                erzielte. Inzwischen hat Messi als einziger Spieler mehr als 300
                Erstligatore erzielt und ist damit Rekordtorschütze
                der Primera División.
                """
        result = detect_language(text, LANGUAGES)
        self.assertEqual(result, 'German')
    
    def test_detect_language_english_with_module_language_specification(self):
        text = """
                Shakespeare was born and brought up in Stratford-upon-Avon,
                Warwickshire. At the age of 18, he married Anne Hathaway, 
                with whom he had three children: Susanna, and twins Hamnet and Judith.
                Sometime between 1585 and 1592, he began a successful career in London 
                as an actor, writer, and part-owner of a playing company called the Lord
                Chamberlain's Men, later known as the King's Men.
                """
        result = detect_language(text, LANGUAGES)
        self.assertEqual(result, 'English')

