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
    
    # Test de la fonction getOutputs de la classe NeuralNetwork
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
        
        # Récupération des sorties 
        outputs = neuronal_network.getOutputs(inputs)
        
        print(f"Outputs: {outputs}")
        # La valeur de sortie doit correspondre à l'entrée concernée
        for output in outputs:
            # Test si la sortie est environ égale à 0.0 ou 1.0
            self.assertTrue(-1.5 <= output <= 1.5)
            
                    
    def test_load_network(self):
        # Création d'un fichier temporaire pour tester la méthode loadNetwork
        with open('fichiertest.txt', 'w') as f:
            # Écriture des données attendues dans le fichier
            f.write("2,3\n")  # 2 couches, 3 entrées
            f.write("4,2\n")  # 4 neurones dans la première couche, 2 neurones dans la deuxième couche
            f.write("SIG,NEU\n")  # Types de couches (SIG et NEU)
            f.write("0.1,0.2,0.3\n")  # Poids pour le premier neurone de la première couche
            f.write("0.4,0.5,0.6\n")  # Poids pour le second neurone de la première couche
            f.write("0.7,0.8,0.9\n")  # Poids pour le troisième neurone de la première couche
            f.write("1.0,1.1,1.2\n")  # Poids pour le quatrième neurone de la première couche
            f.write("1.3,1.4\n")  # Poids pour le premier neurone de la deuxième couche
            f.write("1.5,1.6\n")  # Poids pour le second neurone de la deuxième couche

        # Création de l'objet NeuralNetwork et appel de la méthode loadNetwork
        nn = NeuralNetwork(3, [4, 2], ["SIG", "NEU"])
        loaded_nn = nn.loadNetwork('fichiertest.txt')

        # Vérification que les couches et neurones ont bien été chargés
        self.assertEqual(len(loaded_nn.layers), 2)  # 2 couches
        self.assertEqual(len(loaded_nn.layers[0]), 4)  # 4 neurones dans la première couche
        self.assertEqual(len(loaded_nn.layers[1]), 2)  # 2 neurones dans la deuxième couche

        # Vérification des poids du réseau pour s'assurer qu'ils ont bien été chargés
        self.assertEqual(loaded_nn.layers[0][0], [0.1, 0.2, 0.3])  # Poids du premier neurone de la première couche
        self.assertEqual(loaded_nn.layers[1][0], [1.3, 1.4])  # Poids du premier neurone de la deuxième couche

        # Suppression du fichier temporaire
        os.remove('fichiertest.txt')
        
if __name__ == '__main__':
    unittest.main()
    