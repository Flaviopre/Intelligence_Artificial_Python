# Importe le module 'random'
import random

# Crée une classe 'Neuron'
class Neuron:
    # Définit la méthode __init__ qui initialise les attributs de la classe 'Neuron'
    def __init__(self, num_inputs):
        # Vérifie si le nombre d'entrées est nul et lève une exception si c'est le cas
        if num_inputs == 0:
            raise ValueError("Le nombre d'entrées ne peut pas être nul.")
        
        # Initialise le nombre d'entrées du neurone
        self.num_inputs = num_inputs
        # Initialise une liste de coefficients avec des valeurs aléatoires
        # La liste contient 'num_inputs + 1' éléments
        # Chaque élément est un nombre aléatoire flottants entre -1 et 1
        self.coefficients = [random.uniform(-1, 1) for i in range(num_inputs + 1)]
            
    # Définit la méthode getNeuronSize qui retourne le nombre d'entrées
    def getNeuronSize(self):
        return self.num_inputs
    
    # Définit la méthode getCoefficient qui retourne la valeur du coefficient à une position donnée
    def getCoefficient(self, position):
        return self.coefficients[position]