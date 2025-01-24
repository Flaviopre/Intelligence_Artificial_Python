# Importe le module 'random'
import random

# Importe le module 'numpy'
import numpy

# Crée une classe 'Neuron'
class Neuron:
    # Définit la méthode __init__ qui initialise les attributs de la classe 'Neuron'
    def __init__(self, num_inputs):
        # Vérifie si le nombre d'entrées est nul et lève une exception si c'est le cas
        if num_inputs is None:
            raise ValueError("Le nombre d'entrées ne peut pas être nul.")
        
        # Initialise le nombre d'entrées du neurone
        self.num_inputs = num_inputs
        # Initialise une liste de coefficients avec des valeurs aléatoires
        # La liste contient 'num_inputs + 1' éléments
        # Chaque élément est un nombre aléatoire flottants entre -1 et 1
        self.__coefficients = [random.uniform(-1, 1) for _ in range(num_inputs + 1)]
        print(self.__coefficients)
            
    # Définit la méthode getNeuronSize qui retourne le nombre d'entrées
    def getNeuronSize(self):
        return self.num_inputs
    
    # Définit la méthode getCoefficient qui retourne la valeur du coefficient à une position donnée
    def getCoefficient(self, position):
        # Vérifie si la position est un entier et lève une exception si ce n'est pas le cas
        if not isinstance(position, int):
            # Lève une exception de Type si la position n'est pas un entier
            raise TypeError("La position doit être un entier.")
        # Vérifie si la position est inférieure à 0 ou supérieure ou nulle et lève une exception si c'est le cas
        elif position < 0 or position >= len(self.__coefficients) or position == 0 or position is None:
            # Lève une exception de Valeur si la position est inférieure à 0 ou supérieure au nombre d'entrées ou égale à 0 ou nulle
            raise ValueError("La position doit être comprise entre 1 et " + str(self.num_inputs + 1) + ".")
        # Retourne la valeur du coefficient à la position donnée
        return self.__coefficients[position]
    
    # Définit la méthode setCoefficient qui définit la valeur du coefficient à une position donnée
    def setCoefficient(self, position, value):
        # Vérifie si la position est un entier
        if not isinstance(position, int):
            # Lève une exception de Type si la position n'est pas un entier
            raise TypeError("La position doit être un entier.")
        # Vérifie si la valeur est un flottant
        elif not isinstance(value, float):
            # Lève une exception de Type si la valeur n'est pas un flottant
            raise TypeError("La valeur doit être un flottant.")
        # Vérifie si la position est inférieure à 0 ou supérieure ou nulle
        elif position < 0 or position >= len(self.__coefficients) or position is None:
            # Lève une exception de Valeur si la position est inférieure à 0 ou supérieure au nombre d'entrées ou nulle
            raise ValueError("La position doit être comprise entre 0 et " + str(self.num_inputs) + ".")
        # Définit la valeur du coefficient à la position donnée
        self.__coefficients[position] = value
        
    # Définit la méthode getOutput qui calcule la sortie du neurone
    def getOutput(self, liste_entrees):
        
        # Vérifie si les entrées sont nulles
        if liste_entrees is None:
            # Lève une exception de Valeur si les entrées sont nulles
            raise ValueError("Les entrées ne peuvent pas être nulles.")
        
        # Vérifie si les entrées sont vides
        elif len(liste_entrees) == 0:
            # Lève une exception de Valeur si les entrées sont vides
            raise ValueError("Les entrées ne peuvent pas être vides.")
        
        # Vérifie si la longueur de la liste des entrées est égale au nombre d'entrées du neurone
        if len(liste_entrees) != self.num_inputs:
            # Lève une exception de Valeur si le nombre d'entrées n'est pas égal au nombre d'entrées du neurone
            raise ValueError("Le nombre d'entrées doit être égal à " + str(self.num_inputs + 1) + ".")
        
        # Vérifie si les entrées sont une liste
        elif not isinstance(liste_entrees, list or numpy.ndarray):
            # Lève une exception de Type si les entrées ne sont pas une liste
            raise TypeError("Les entrées doivent être une liste.")
                
        # Parcours les entrées
        for i in liste_entrees:
            # Vérifie si les entrées ne sont pas des flottants et lève une exception si ce n'est pas le cas
            if not isinstance(i, float):
                # Lève une exception de Type si les entrées ne sont pas des flottants
                raise TypeError("Les entrées doivent être des flottants.")
            # Arrête la boucle SI si une entrée est nulle
            break
        
        # Initialise la sortie du neurone à 0
        sortie_neurone = 0.0
        
        # Ajoute le dernier coefficient        
        sortie_neurone += self.__coefficients[-1]
        
        # Parcours les entrées et les coefficients en enlevant le dernier coefficient qui est notre constante
        for i in range(self.num_inputs):
            # Ajoute le produit de l'entrée et du coefficient à la sortie
            sortie_neurone += liste_entrees[i] * self.__coefficients[i]
        
        # Retourne la sortie du neurone
        return sortie_neurone
