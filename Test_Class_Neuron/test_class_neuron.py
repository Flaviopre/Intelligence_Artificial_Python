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
            Neuron(None)
            
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
        # Vérifie que le nombre d'entrées du neurone est égal à 3
        self.assertEqual(test1.getNeuronSize(), 3)
    
        # Définit la méthode 'test_Vérification_Position' pour tester les paramètres d'entrée de la fonction 
    def test_Vérification_Entier_Méthode_getCoefficient(self):
        test1 = Neuron(3)
        # Vérifie que la méthode lève une exception si la position n'est pas un entier
        with self.assertRaises(TypeError):
            test1.getCoefficient("string")
        # Vérifie que la méthode lève une exception si la position est un flottant
        with self.assertRaises(TypeError):
            test1.getCoefficient(1.5)
        # Vérifie que la méthode lève une exception si la position est nulle
        with self.assertRaises(TypeError):
            test1.getCoefficient(None)
        # Vérifie que la méthode lève une exception si la position est supérieure au nombre d'entrées
        with self.assertRaises(ValueError):
            test1.getCoefficient(6)
        # Vérifie que la méthode lève une exception si la position est inférieure à 1
        with self.assertRaises(ValueError):
            test1.getCoefficient(-6)
        # Vérifie que la méthode lève une exception si la position est égale à 0
        with self.assertRaises(ValueError):
            test1.getCoefficient(0)
        # Vérifie que la méthode lève une exception si la position est inférieure à 1 mais dans la plage des entrées
        with self.assertRaises(ValueError):
            test1.getCoefficient(-1)
                
    # Définit la méthode 'test_Vérification_Position' pour tester la position d'un coefficient
    def test_Vérification_Méthode_getCoefficient(self):
        test1 = Neuron(3)
        # Garde en mémoire la valeur du coefficient à la position 2
        valeur_sans_méthode = test1.coefficients[2]
        # Récupère la valeur du coefficient à la position 2 avec la méthode getCoeff
        valeur_avec_méthode = test1.getCoefficient(2)
        # Vérifie que les deux valeurs sont égales
        self.assertEqual(valeur_sans_méthode, valeur_avec_méthode)
    
    # Définit la méthode 'test_entier_setCoefficient'pour tester les paramètres d'entrée de la fonction 
    def test_Vérification_Entier_Méthode_setCoefficient(self):
        test1 = Neuron(3)
        # Vérifie que la méthode lève une exception si la position n'est pas un entier
        with self.assertRaises(TypeError):
            test1.setCoefficient("string", 1.5)
        # Vérifie que la méthode lève une exception si la valeur n'est pas un flottant
        with self.assertRaises(TypeError):
            test1.setCoefficient(1.5, 1.5)
        # Vérifie que la méthode lève une exception si la valeur est une chaîne de caractères
        with self.assertRaises(TypeError):
            test1.setCoefficient(1, "string")
        # Vérifie que la méthode lève une exception si la position est supérieure au nombre d'entrées
        with self.assertRaises(ValueError):
            test1.setCoefficient(6, 1.5)
        # Vérifie que la méthode lève une exception si la position est inférieure à 1 
        with self.assertRaises(ValueError):
            test1.setCoefficient(-6, 1.5)
    
    # Définit la méthode 'test_Modification_Coefficient' pour tester la modification d'un coefficient avec la méthode setCoeffcient
    def test_Modification_Coefficient_setCoefficient(self):
        verif = Neuron(3)
        # Garde en mémoire la valeur du coefficient à la position 2
        résultat_sans_méthode_set_coeff = verif.coefficients[2]
        # Modifie la valeur du coefficient à la position 2
        verif.setCoefficient(2, 0.5)
        # Récupère la valeur du coefficient à la position 2 nouvellement modifiée
        résultat_avec_méthode_setcoeff = verif.coefficients[2]
        # Vérifie que les deux valeurs sont différentes car elles ont été modifiées
        self.assertNotEqual(résultat_sans_méthode_set_coeff, résultat_avec_méthode_setcoeff)
        # Vérifie que la valeur du coefficient à la position 2 est égale à 0.5
        self.assertEqual(résultat_avec_méthode_setcoeff, 0.5)
    
    # Définit la méthode 'test_sortie_neurone' pour tester l'entrée de la fonction getOutput
    def test_sortie_neurone(self):
        test1 = Neuron(3)
        # Vérifie que la méthode lève une exception si le nombre d'entrées n'est pas égal au nombre d'entrées du neurone
        with self.assertRaises(ValueError):
            test1.getOutput([1, 2])
        # Vérifie que la méthode lève une exception si les entrées ne sont pas une liste
        with self.assertRaises(TypeError):
            test1.getOutput(1)
        # Vérifie que la méthode lève une exception si les entrées sont nulles
        with self.assertRaises(ValueError):
            test1.getOutput(None)
        # Vérifie que la méthode lève une exception si les entrées sont vides
        with self.assertRaises(ValueError):
            test1.getOutput([])

        
# Définit la méthode 'test_compute' pour tester le calcul d'un neurone        
if __name__ == '__main__':
    unittest.main()   
