# Importation des modules nécessaires pour l'ajout du chemin parent au sys.path
import sys
import os
import numpy as np
# Ajouter le chemin parent au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Création de la classe Learning qui va permettre d'entraîner un neurone
class Learning:
    # Constructeur de la classe Learning avec 3 paramètres
    def __init__(self, neuron, inputs, outputs):
        # Vérifications de la taille des entrées  et des dimensions        
        if inputs.shape[0] != outputs.shape[0]:
            raise ValueError("La première dimension de inputs doit être égale à celle de outputs.")