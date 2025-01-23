# Importation des modules nécessaires pour l'ajout du chemin parent au sys.path
import sys
import os
# Ajouter le chemin parent au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importation de la classe Neuron du dossier Classe_Neuron
from Class_Neuron.class_neuron import Neuron

# Importation du module class sigmoid_neuron
from Class_SigmoidNeuron.Class_SigmoidNeuron import SigmoidNeuron

# Importation de la class NeuralNetwork du dossier Class_NeuralNetwork
from Class_NeuralNetwork.Class_NeuralNetwork import NeuralNetwork

# Importe le module 'unittest'
import unittest
# Importe le module 'random'
import random

class TestNeuralNetwork(unittest.TestCase):
    
    # Test de la méthode __init__ de la classe NeuralNetwork
    def test_longueur_neronperlayer_different_longueur_layertype(self):
        
        # Teste si une exception est levée si la longueur de neuronsPerLayer diffère de celle de layerType
        with self.assertRaises(ValueError):
            # Création d'un objet de la classe NeuralNetwork avec 3 paramètres et 2 éléments dans neuronsPerLayer et 3 éléments dans layerType
            NeuralNetwork(2, [2, 3], ["SIG", "NEU", "SIG"])
        
        # Teste si une exception est levée si la longueur de neuronsPerLayer diffère de celle de layerType
        with self.assertRaises(ValueError):
            # Création d'un objet de la classe NeuralNetwork avec 3 paramètres et 3 éléments dans neuronsPerLayer et 2 éléments dans layerType
            NeuralNetwork(2, [2, 3, 4], ["SIG", "NEU"])

if __name__ == '__main__':
    unittest.main()
    