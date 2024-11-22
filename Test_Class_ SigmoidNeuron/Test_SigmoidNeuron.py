# Importation des modules nécessaires pour l'ajout du chemin parent au sys.path
import sys
import os
# Ajouter le chemin parent au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importe le module 'unittest'
import unittest
# Importe le module 'random'
import random
# Importer le fichier Travail_Préli_Sigmoid du dossier Travail_Préli_Sigmoid
from Class_SigmoidNeuron.Class_SigmoidNeuron import sigmoid

# Création de la classe de test TestSigmoid qui va tester la fonction sigmoid
class TestSigmoid(unittest.TestCase):
    def test_sigmoid_entrée(self):
        # Teste si une erreur est levée si x n'est pas un entier
        with self.assertRaises(ValueError):
            # Test avec un string
            sigmoid("string")
        
        # Teste si une erreur est levée si x n'est pas un entier
        with self.assertRaises(ValueError):
            # Test avec une liste vide 
            sigmoid([])
            
    # Test de la fonction sigmoid
    def test_sigmoid_sortie(self):
        # Teste si sigmoid(-150) est égal à 0
        self.assertAlmostEqual(sigmoid(-150), 0, places=5)
        # Teste si sigmoid(150) est égal à 1
        self.assertAlmostEqual(sigmoid(150), 1, places=5)
        # Teste si sigmoid(0) est égal à 0.5
        self.assertAlmostEqual(sigmoid(0), 0.5, places=5)
        # Teste si sigmoid(-10) est inférieur à 0.25
        self.assertLess(sigmoid(-10), 0.25)
        # Teste si sigmoid(10) est supérieur à 0.75
        self.assertGreater(sigmoid(10), 0.75)

if __name__ == '__main__':
    unittest.main()