# Importation des modules nécessaires pour l'ajout du chemin parent au sys.path
import sys
import os
# Ajouter le chemin parent au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importe la classe 'Neuron' du module 'Class_Neuron.class_neuron'
from Class_Neuron.class_neuron import Neuron
# Importe le module 'unittest'
import unittest

# Crée une classe 'Vérification_Neuron' pour tester la classe Neuron
class Vérification_Neuron(unittest.TestCase):
    # Définit la méthode 'test_Vérification_Nombre_Entrées' pour tester le nombre d'entrées d'un neurone
    def test_Vérification_Nombre_Entrées (self):
        # Crée un neurone avec 3 entrées
        test1 = Neuron(3)
        # Vérifie que le nombre d'entrées du neurone est égal à 3
        self.assertEqual(test1.num_inputs, 3)
        
    # Définit la méthode 'test_Vérification_Nombre_Entrées_Nul' pour tester l'initialisation d'un neurone avec 0 entrée
    def test_Vérification_Nombre_Entrées_Nul(self):
        # Vérifie que l'initialisation d'un neurone avec 0 entrée lève une exception
        with self.assertRaises(ValueError):
            Neuron(0)
            
    # Définit la méthode 'test_vérification_liste_coefficients' pour tester la liste de coefficients d'un neurone
    def test_Vérification_Liste_Coefficients(self):
        # Crée un neurone avec 3 entrées
        test1 = Neuron(3)
        # Vérifie que la longueur de la liste de coefficients est égale à 4
        self.assertEqual(len(test1.coefficients), 4)

    # Définit la méthode 'test_Vérification_Coefficients' pour tester les valeurs des coefficients d'un neurone
    def test_Vérification_Coefficients(self):
        # Crée un neurone avec 3 entrées
        test1 = Neuron(3)
        # Vérifie que les coefficients sont bien compris entre -1 et 1
        for coef in test1.coefficients:
            self.assertTrue(coef >= -1 and coef <= 1)

    # Définit la méthode 'test_Vérification_Neuron_Size' pour tester le nombre d'entrées d'un neurone
    def test_Vérification_Neuron_Size(self):
        test1 = Neuron(3)
        self.assertEqual(test1.getNeuronSize(), 3)
        
    # Définit la méthode 'test_Vérification_Position' pour tester la position d'un coefficient
    def test_Vérification_Méthode_getCoefficient(self):
        test1 = Neuron(3)
        valeur_sans_méthode = test1.coefficients[2]
        valeur_avec_méthode = test1.getCoefficient(2)
        self.assertEqual(valeur_sans_méthode, valeur_avec_méthode)

    # Définit la méthode 'test_Vérification_Position' pour tester la position d'un coefficient
    def Vérification_Entier_Méthode_getCoefficient(self):
        def test_Vérification_Entier_Méthode_getCoefficient(self):
            test1 = Neuron(3)
            with self.assertRaises(ValueError):
                test1.getCoefficient("a")
            with self.assertRaises(ValueError):
                test1.getCoefficient(1.5)
            with self.assertRaises(ValueError):
                test1.getCoefficient(None)

# Définit la méthode 'test_compute' pour tester le calcul d'un neurone        
if __name__ == '__main__':
    unittest.main()   
