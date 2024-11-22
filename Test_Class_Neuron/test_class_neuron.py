# Importation des modules nécessaires pour l'ajout du chemin parent au sys.path
import sys
import os
# Ajouter le chemin parent au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importe la classe 'Neuron' du module 'Class_Neuron.class_neuron'
from Class_Neuron.class_neuron import Neuron
# Importe le module 'unittest'
import unittest
# Importe le module 'random'
import random

# Crée une classe 'Vérification_Neuron' pour tester la classe Neuron
class Vérification_Neuron(unittest.TestCase):
    # Définit la méthode 'test_Vérification_Nombre_Entrées' pour tester le nombre d'entrées d'un neurone
    def test_Vérification_Nombre_Entrées(self):
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
        self.assertEqual(len(test1._Neuron__coefficients), 4)

    # Définit la méthode 'test_Vérification_Coefficients' pour tester les valeurs des coefficients d'un neurone
    def test_Vérification_Coefficients(self):
        # Crée un neurone avec 3 entrées
        test1 = Neuron(3)
        # Vérifie que les coefficients sont bien compris entre -1 et 1
        for coef in test1._Neuron__coefficients:
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
            test1.getCoefficient('string')
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
        # Garde en mémoire la valeur du coefficient à la position 2 sans la méthode getCoeff
        valeur_sans_méthode = test1._Neuron__coefficients[2]
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
        résultat_sans_méthode_set_coeff = verif._Neuron__coefficients[2]
        # Modifie la valeur du coefficient à la position 2
        verif.setCoefficient(2, 0.5)
        # Récupère la valeur du coefficient à la position 2 nouvellement modifiée
        résultat_avec_méthode_setcoeff = verif._Neuron__coefficients[2]
        # Vérifie que les deux valeurs sont différentes car elles ont été modifiées
        self.assertNotEqual(résultat_sans_méthode_set_coeff, résultat_avec_méthode_setcoeff)
        # Vérifie que la valeur du coefficient à la position 2 est égale à 0.5
        self.assertEqual(résultat_avec_méthode_setcoeff, 0.5)
    
    # Définit la méthode 'test_Vérification_Entrée_getOutput' pour tester l'entrée de la fonction getOutput
    def test_Vérification_Entrée_getOutput(self):
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

    # Définit la méthode 'test_Sortie_getOutput' pour tester la méthode getOutput
    def test_Sortie_getOutput_Constante(self):
        # Choisi un nombre aléatoire entre 5 et 10
        nombre_al_entre_5_et_10 = random.randint(5, 10)
        # Crée un neurone avec un nombre aléatoire d'entrées entre 5 et 10
        test1_sans_fonction = Neuron(nombre_al_entre_5_et_10)
        # Choisis le dernier coefficient du neurone
        test_Sortie_getCoefficients = test1_sans_fonction.getCoefficient(nombre_al_entre_5_et_10)
        
        # Crée une liste de zéros de la taille du nombre aléatoire entre 5 et 10
        liste_test_0 = [0.0 for _ in range(nombre_al_entre_5_et_10)]
        # Récupère la sortie du neurone avec la liste de zéros
        test_Sortie_getOutput_0 = test1_sans_fonction.getOutput(liste_test_0)
    
        # Vérifie que la sortie du neurone est égale au dernier coefficient du neurone dans ce cas 
        self.assertEqual(test_Sortie_getOutput_0, test_Sortie_getCoefficients)
    
    def test_Sortie_getOutput_coeff_0(self):
        # Choisi un nombre aléatoire entre 5 et 10
        nombre_al_entre_5_et_10 = random.randint(5, 10)
        # Crée un neurone avec un nombre aléatoire d'entrées entre 5 et 10
        test1 = Neuron(nombre_al_entre_5_et_10)
        
        # Boucle qui parcourt la liste des coefficients du neurone
        for i in range(0, nombre_al_entre_5_et_10 + 1):
            # Met le coefficient à 0    
            test1.setCoefficient(i, 0.0)
        
        # Crée une liste d'entrées remplie aléatoirement
        liste_entrées = [random.uniform(-1, 1) for _ in range(nombre_al_entre_5_et_10)]
        
        # Teste chaque coefficient en le remplaçant par une valeur aléatoire
        # Parcours la liste des coefficients du neurone en partant de 1 jusqu'à nombre_al_entre_5_et_10 + 1
        for i in range(0, nombre_al_entre_5_et_10):
            # Modifie la valeur du coefficient à 1 à la position i
            test1.setCoefficient(i, 1.0)
            # Récupère la sortie du neurone avec la liste d'entrées
            sortie = test1.getOutput(liste_entrées)
            # Vérifie que la sortie du neurone est égale à la valeur aléatoire multipliée par la valeur de la liste d'entrées à la position i - 1 plus le biais
            self.assertAlmostEqual(sortie, liste_entrées[i], places=5)
            print("La valeur de sortie est : ", sortie, "Le calcul correct est : ", liste_entrées[i])
            # Remet le coefficient à zéro
            test1.setCoefficient(i, 0.0)

    # Définit la méthode 'test_Sortie_getOutput_dernier_coeff' pour tester la sortie du neurone avec le dernier coefficient modifié
    def test_Sortie_getOutput_dernier_coeff(self):
        # Choisi un nombre aléatoire entre 5 et 10
        nombre_al_entre_5_et_10 = random.randint(5, 10)
        # Crée un neurone avec un nombre aléatoire d'entrées entre 5 et 10
        test1 = Neuron(nombre_al_entre_5_et_10)
        # Teste le dernier coefficient en plaçant toutes les entrées à zéro
        # Modifie la valeur du dernier coefficient qui vaudra 0 à la position donnée par nombre_al_entre_5_et_10 + 1  
        test1.setCoefficient(nombre_al_entre_5_et_10, 0.5)
        # Récupère la sortie du neurone avec la liste de zéros
        sortie = test1.getOutput([0.0 for _ in range(nombre_al_entre_5_et_10)])
        # Vérifie que la sortie du neurone est égale à 0.5 dans ce cas
        self.assertAlmostEqual(sortie, 0.5, places=5)

# Définit la méthode 'test_compute' pour tester le calcul d'un neurone        
if __name__ == '__main__':
    unittest.main()