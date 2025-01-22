# Importation des modules nécessaires pour l'ajout du chemin parent au sys.path
import sys
import os
# Ajouter le chemin parent au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importe le module 'unittest'
import unittest

# Importer le fichier Classe_Learning du dossier Classe_Learning
from Classe_Learning.Classe_Learning import Learning

# Véirifier le raiseError lors de la création de la classe Learning
class TestLearning(unittest.TestCase): 
    
    # Test des entrées et des sorties si égale 
    def test_input_output_égale(self):
        # Création des inputs avec une liste de listes (matrice)
        inputs = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]]
        # Création des outputs avec une liste monodimensionnelle qui ets une liste basique
        outputs = [0.1, 0.2, 0.3]
        # Création de l'instance de la classe Learning
        learning_instance = Learning(3, inputs ,outputs)
        # Teste si la première dimension de inputs est égale à celle de outputs
        self.assertEqual(len(learning_instance._Learning__inputs), len(learning_instance._Learning__outputs))
    
    # Test des entrées et des sorties si différente et lève une erreur
    def test_input_output_différent(self):
        # Création des inputs avec une liste de listes (matrice)
        inputs = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]]
        # Création des outputs avec une liste monodimensionnelle qui ets une liste basique
        outputs = [0.1, 0.2]
        # Regarde l'erreur levée
        with self.assertRaises(ValueError):
            # Création de l'instance de la classe Learning
            learning_instance = Learning(0, inputs ,outputs)

    def test_inputs_outputs_erreur(self):
        # Création des inputs avec un string qui n'est pas une liste
        inputs = "abc"
        # Création des outputs avec une liste monodimensionnelle qui ets une liste basique
        outputs = [0.1, 0.2, 0.3]
        # Regarde l'erreur levée
        with self.assertRaises(ValueError):
            # Création de l'instance de la classe Learning
            learning_instance = Learning(0, inputs ,outputs)
                # Création des inputs avec une liste de listes (matrice)
        inputs = [[0.1, 0.2, 0.3] , [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]]
        # Création des outputs avec un string qui n'est pas une liste
        outputs = "abc"
        # Regarde l'erreur levée
        with self.assertRaises(ValueError):
            # Création de l'instance de la classe Learning
            learning_instance = Learning(0, inputs ,outputs)

    
    def test_inputs_taille_neurone_différente(self):
        # Création des inputs avec une liste de listes (matrice)
        inputs = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]]
        # Création des outputs avec une liste monodimensionnelle qui ets une liste basique
        outputs = [0.1, 0.2, 0.3]
        # Regarde l'erreur levée
        with self.assertRaises(ValueError):
            # Création de l'instance de la classe Learning
            learning_instance = Learning(2, inputs ,outputs)
        # Création des inputs avec une liste de listes (matrice)
        inputs = [[0.1, 0.2], [0.4, 0.5], [0.7, 0.8]]
        # Création des outputs avec une liste monodimensionnelle qui ets une liste basique
        outputs = [0.1, 0.2, 0.3]
        # Regarde l'erreur levée
        with self.assertRaises(ValueError):
            # Création de l'instance de la classe Learning
            learning_instance = Learning(2, inputs ,outputs)
        
if __name__ == '__main__':
    unittest.main()     