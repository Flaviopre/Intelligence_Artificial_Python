from Class_Neuron import Neuron
# Importe le module 'unittest'
import unittest
# Crée une classe 'TestNeuron' qui hérite de la classe 'unittest.TestCase'
class TestNeuron(unittest.TestCase):
    # Définit la méthode 'test_init' pour tester l'initialisation d'un neurone
    def test_init(self):
        # Crée un neurone avec 3 entrées
        test1 = Neuron(3)
        # Vérifie que le nombre d'entrées du neurone est égal à 3
        self.assertEqual(test1.num_inputs, 3)
        # Vérifie que la longueur de la liste de coefficients est égale à 4
        self.assertEqual(len(test1.coefficients), 4)
        # Vérifie que les coefficients sont bien compris entre -1 et 1
        for i in test1.coefficients:
            self.assertGreaterEqual(i, -1)
            self.assertLessEqual(i, 1)
            
    # Définit la méthode 'test_compute' pour tester le calcul d'un neurone        
    if __name__ == '__main__':
        unittest.main()   
        