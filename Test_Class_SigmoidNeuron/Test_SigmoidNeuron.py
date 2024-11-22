# Importation des modules nécessaires pour l'ajout du chemin parent au sys.path
import sys
import os
# Ajouter le chemin parent au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importe le module 'unittest'
import unittest
# Importer le fichier Travail_Préli_Sigmoid du dossier Travail_Préli_Sigmoid
from Class_SigmoidNeuron.Class_SigmoidNeuron import sigmoid
from Class_SigmoidNeuron.Class_SigmoidNeuron import SigmoidNeuron

#Importation de la librairie random
import random

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

# Création de la classe de test TestSigmoidNeuron qui va tester la classe SigmoidNeuron
class TestSigmoidNeuron(unittest.TestCase):
    # Test de la méthode __init__
    def test_init(self):
        # Création d'un neurone avec 3 entrées
        sigmoid_neuron = SigmoidNeuron(3)
        # Teste si le nombre d'entrées du neurone est égal à 3
        self.assertEqual(sigmoid_neuron.num_inputs, 3)
        
    def test_getOutput_sortie_0(self):
        # Création d'un neurone avec un nombre d'entrées aléatoires
        nb_aléatoire = random.randint(5, 10)
        # Création d'un neurone avec un nombre d'entrées aléatoires
        sigmoid_neuron = SigmoidNeuron(nb_aléatoire)
        # Boucle qui parcourt la liste des coefficients du neurone
        for i in range(0, nb_aléatoire + 1):
            # Met le coefficient à 0    
            sigmoid_neuron.setCoefficient(i, 0.0)
        # Création d'une liste d'entrées aléatoires entre -10 et 10
        entré_getOutput = [random.uniform(-10.0, 10.0) for i in range(nb_aléatoire)]
        # Calcul de la sortie du neurone avec les entrées aléatoires et les coefficients à 0
        sortie_getOutput_SigmoidNeuron = sigmoid_neuron.getOutput_SigmoidNeuron(entré_getOutput)
        # Teste si la sortie du neurone est égale à 0.5
        self.assertAlmostEqual(sortie_getOutput_SigmoidNeuron, 0.5, places=5)
        
    def test_getOutput_sortie_positif(self):
        # Création d'un neurone avec un nombre d'entrées aléatoires
        nb_aléatoire = random.randint(5, 10)
        # Création d'un neurone avec un nombre d'entrées aléatoires
        sigmoid_neuron = SigmoidNeuron(nb_aléatoire)
        # Boucle qui parcourt la liste des coefficients du neurone
        for i in range(0, nb_aléatoire + 1):
            # Mettre tous les coefficients en positif
            sigmoid_neuron.setCoefficient(i, random.uniform(0, 1))
        # Creation d'une liste d'entrées aléatoires entre 0 et 10 donc positifs
        entré_getOutput = [random.uniform(0, 10) for i in range(nb_aléatoire)]
        # Calcul de la sortie du neurone avec les entrées aléatoires positives et les coefficients positifs
        sortie_getOutput_SigmoidNeuron = sigmoid_neuron.getOutput_SigmoidNeuron(entré_getOutput)
        # Teste si la sortie du neurone est positive ou égale à 0
        self.assertGreater(sortie_getOutput_SigmoidNeuron, 0.0)
    
    def test_getOutput_sortie_négatif(self):
        # Création d'un neurone avec un nombre d'entrées aléatoires
        nb_aléatoire = random.randint(5, 10)
        # Création d'un neurone avec un nombre d'entrées aléatoires
        sigmoid_neuron = SigmoidNeuron(nb_aléatoire)
        # Boucle qui parcourt la liste des coefficients du neurone
        for i in range(0, nb_aléatoire + 1):
            # Mettre tous les coefficients en négatif
            sigmoid_neuron.setCoefficient(i, random.uniform(-1, 0))
        # Creation d'une liste d'entrées aléatoires entre -10 et 10 donc négatifs
        entré_getOutput = [random.uniform(-10, 0) for i in range(nb_aléatoire)]
        # Calcul de la sortie du neurone avec les entrées aléatoires négatives et les coefficients négatifs
        sortie_getOutput_SigmoidNeuron = sigmoid_neuron.getOutput_SigmoidNeuron(entré_getOutput)
        # Teste si la sortie du neurone est négative ou égale à 0
        self.assertGreater(sortie_getOutput_SigmoidNeuron, 0.0)
         
if __name__ == '__main__':
    unittest.main()     