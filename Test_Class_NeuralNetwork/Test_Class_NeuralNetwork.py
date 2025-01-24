# Importation des modules nécessaires pour l'ajout du chemin parent au sys.path
import sys
import os
# Ajouter le chemin parent au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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
        
    # Test de la taille des listes neuronsPerLayer et layerType
    def test_type_inputsLength(self):
        
        # Teste si une exception est levée si inputsLength n'est pas un entier
        with self.assertRaises(ValueError):
            # Création d'un objet de la classe NeuralNetwork avec 3 paramètres et inputsLength n'est pas un entier
            NeuralNetwork("2", [2, 3], ["SIG", "NEU"])
            
        # Teste si une exception est levée si neuronsPerLayer n'est pas une liste 
        with self.assertRaises(ValueError):
            # Création d'un objet de la classe NeuralNetwork avec 3 paramètres et neuronsPerLayer n'est pas une liste
            NeuralNetwork(2.0, "3,5", ["SIG", "NEU"])
        
        # Test si une exception est levée si layerType n'est pas une liste
        with self.assertRaises(ValueError):
            # Création d'un objet de la classe NeuralNetwork avec 3 paramètres et layerType n'est pas une liste
            NeuralNetwork(2, [2, 3], "SIG, NEU") 

    def test_get_set_coefficient(self):
        # Création d'un objet de la classe NeuralNetwork avec 3 paramètres et 2 éléments dans neuronsPerLayer et 2 éléments dans layerType
        neuronal_network = NeuralNetwork(2, [2, 2], ["NEU", "NEU"])
        
        # Regarde chaque couche du réseau de neurones
        for layer in range(len(neuronal_network._NeuralNetwork__layers)):
            # Regarde chaque neurone de chaque couche du réseau de neurones
            for neuron in range(len(neuronal_network._NeuralNetwork__layers[layer])):
                # Regarde chaque coefficient de chaque neurone de chaque couche du réseau de neurones
                for coeff in range(1, neuronal_network._NeuralNetwork__layers[layer][neuron].getNeuronSize() + 1):
                    # Affectation d'un nombre aléatoire entre 0 et 1 à random_number
                    random_number = random.random()
                    # Changement du coefficient du neurone
                    neuronal_network._NeuralNetwork__layers[layer][neuron].setCoefficient(coeff, random_number)
                    # Test si le coefficient du neurone est égal à random_number et qu'il a bien été changé
                    self.assertEqual(neuronal_network._NeuralNetwork__layers[layer][neuron].getCoefficient(coeff), random_number)
    
    def test_get_outputs(self):
    
        # Création d'un objet de la classe NeuralNetwork avec 2 couches de 2 neurones linéaires chacune
        neuronal_network = NeuralNetwork(3, [2, 3], ["SIG", "SIG"])
        
        # Initialisation de tous les coefficients à zéro
        for layer in range(len(neuronal_network._NeuralNetwork__layers)):
            for neuron in range(len(neuronal_network._NeuralNetwork__layers[layer])):
                for coeff in range(1, neuronal_network._NeuralNetwork__layers[layer][neuron].getNeuronSize() + 1):
                    neuronal_network._NeuralNetwork__layers[layer][neuron].setCoefficient(coeff, 0.0)
        
        # Modification des coefficients spécifiques
        neuronal_network._NeuralNetwork__layers[0][1].setCoefficient(3, 1.0)
        neuronal_network._NeuralNetwork__layers[1][2].setCoefficient(2, 1.0)
        
        # Test des sorties pour une entrée spécifique
        inputs = [1.0, 0.0, 0.0]
        # Affichage des coefficients des neurones pour vérification
        for layer in range(len(neuronal_network._NeuralNetwork__layers)):
            for neuron in range(len(neuronal_network._NeuralNetwork__layers[layer])):
                coefficients = [neuronal_network._NeuralNetwork__layers[layer][neuron].getCoefficient(i + 1) for i in range(neuronal_network._NeuralNetwork__layers[layer][neuron].getNeuronSize())]
                print(f"Layer {layer}, Neuron {neuron}, Coefficients: {coefficients}")
        
        outputs = neuronal_network.getOutputs(inputs)
        
        # La valeur de sortie doit correspondre à l'entrée concernée
        self.assertEqual(outputs, [0.0, 0.0, 1.0])
    
    
if __name__ == '__main__':
    unittest.main()
    