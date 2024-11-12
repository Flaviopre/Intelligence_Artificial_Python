# Importe le module 'random'
import random
# Crée une classe 'Neuron'
class Neuron:
    # Définit la méthode __init__ qui initialise les attributs de la classe 'Neuron'
    def __init__(self, num_inputs):
        # Initialise le nombre d'entrées du neurone
        self.num_inputs = num_inputs
        # Initialise une liste de coefficients avec des valeurs aléatoires
        # La liste contient 'num_inputs + 1' éléments
        # Chaque élément est un nombre aléatoire flottants entre -1 et 1
        self.coefficients = [random.uniform(-1, 1) for i in range(num_inputs + 1)]