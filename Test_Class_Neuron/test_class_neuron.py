# Importation des modules nécessaires pour l'ajout du chemin parent au sys.path
import sys
import os
# Ajouter le chemin parent au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importe la classe 'Neuron' du module 'Class_Neuron.class_neuron'
from Class_Neuron.class_neuron import Neuron
# Importe le module 'unittest'
import unittest

# Crée une classe 'Vérification_Nombre_Entrées' pour tester le nombre d'entrées d'un neurone
class Vérification_Nombre_Entrées(unittest.TestCase):
    # Définit la méthode 'test_init' pour tester l'initialisation d'un neurone
    def test_init(self):
        # Crée un neurone avec 3 entrées
        test1 = Neuron(3)
        # Vérifie que le nombre d'entrées du neurone est égal à 3
        self.assertEqual(test1.num_inputs, 3)

# Crée une classe 'Vérification_Liste_Coefficients' pour tester le nombre de coefficients dans la liste d'un neurone
class Vérification_Liste_Coefficients(unittest.TestCase):
    # Définit la méthode 'test_init' pour tester l'initialisation d'un neurone
    def test_init(self):
        # Crée un neurone avec 3 entrées
        test1 = Neuron(3)
        # Vérifie que la longueur de la liste de coefficients est égale à 4
        self.assertEqual(len(test1.coefficients), 4)

# Crée une classe 'Vérification_Coefficients' pour tester les valeurs des coefficients d'un neurone
class Vérification_Coefficients(unittest.TestCase):
    # Définit la méthode 'test_init' pour tester l'initialisation d'un neurone
    def test_init(self):
        # Crée un neurone avec 3 entrées
        test1 = Neuron(3)
        # Vérifie que les coefficients sont bien compris entre -1 et 1
        for coef in test1.coefficients:
            self.assertTrue(coef >= -1 and coef <= 1)

# Crée une classe 'Vérification_Neuron_Size' pour tester la méthode 'getNeuronSize' d'un neurone
class Vérification_Neuron_Size(unittest.TestCase):
    def test_getNeuronSize(self):
        test1 = Neuron(3)
        self.assertEqual(test1.getNeuronSize(), 3)

# Définit la méthode 'test_compute' pour tester le calcul d'un neurone        
if __name__ == '__main__':
    unittest.main()   
