# Importe le module 'random'
import random

# Crée une classe 'Neuron'
class Neuron:
    # Définit la méthode __init__ qui initialise les attributs de la classe 'Neuron'
    def __init__(self, num_inputs):
        # Vérifie si le nombre d'entrées est nul et lève une exception si c'est le cas
        if num_inputs == None:
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
        # Vérifie si la position est un entier et lève une exception si ce n'est pas le cas
        if not isinstance(position, int):
            # Lève une exception de Type si la position n'est pas un entier
            raise TypeError("La position doit être un entier.")
        # Vérifie si la position est inférieure à 0 ou supérieure au nombre d'entrées ou égale à 0 ou nulle et lève une exception si c'est le cas
        elif position < 0 or position >= len(self.coefficients) or position == 0 or position == None :
            # Lève une exception de Valeur si la position est inférieure à 0 ou supérieure au nombre d'entrées ou égale à 0 ou nulle
            raise ValueError("La position doit être comprise entre 1 et " + str(self.num_inputs) + ".")
        # Retourne la valeur du coefficient à la position donnée
        return self.coefficients[position]
    
    # Définit la méthode setCoefficient qui modifie la valeur du coefficient à une position donnée
    def setCoefficient(self, position, value):
        # Vérifie si la position est un entier et lève une exception si ce n'est pas le cas
        if not isinstance(position, int):
            # Lève une exception de Type si la position n'est pas un entier
            raise TypeError("La position doit être un entier.")
        # Vérifie si la valeur est un flottant et lève une exception si ce n'est pas le cas
        elif not isinstance(value, float):
            # Lève une exception de Type si la valeur n'est pas un flottant
            raise TypeError("La valeur doit être un flottant.")
        # Vérifie si la position est inférieure à 0 ou supérieure au nombre d'entrées ou égale à 0 ou nulle et lève une exception si c'est le cas
        elif position < 0 or position >= len(self.coefficients) or position == 0 or position == None:
            # Lève une exception de Valeur si la position est inférieure à 0 ou supérieure au nombre d'entrées ou égale à 0 ou nulle
            raise ValueError("La position doit être comprise entre 1 et " + str(self.num_inputs) + ".")
        # Modifie la valeur du coefficient à la position donnée
        self.coefficients[position] = value
        