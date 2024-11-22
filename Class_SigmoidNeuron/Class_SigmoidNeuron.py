# Importation de la librairie math
import math

# Importation des modules nécessaires pour l'ajout du chemin parent au sys.path
import sys
import os
# Ajouter le chemin parent au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importer le fichier Travail_Préli_Sigmoid du dossier Travail_Préli_Sigmoid
from Class_Neuron.class_neuron import Neuron

# Définition de la fonction sigmoid
def sigmoid(x):
    # Vérifie que x est un entier
    if not isinstance(x, (int, float)):
        # Lève une erreur si x n'est pas un entier
        raise ValueError("x doit être un nombre")
    # Si x est supérieur à 100
    if x > 100:
        # Retourne 1.0
        return 1.0
    # Sinon si x est inférieur à -100
    elif x < -100:
        # Retourne 0.0
        return 0.0
    # Sinon
    else:
        # Retourne 1 / (1 + exp(-x))
        return 1 / (1 + math.exp(-x))

# Création de la classe SigmoidNeuron
class SigmoidNeuron(Neuron):
    # Constructeur de la classe
    def __init__(self, num_inputs):
        # Appelle le constructeur de la classe mère
        super().__init__(num_inputs)
        # Initialise le nombre d'entrées du neurone
        self.num_inputs = num_inputs    