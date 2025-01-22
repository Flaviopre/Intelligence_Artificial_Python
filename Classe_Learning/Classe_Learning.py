# Importation des modules nécessaires pour l'ajout du chemin parent au sys.path
import sys
import os
# Ajouter le chemin parent au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Création de la classe Learning qui va permettre d'entraîner un neurone
class Learning:
    # Constructeur de la classe Learning avec 3 paramètres
    def __init__(self, neuron, inputs, outputs):
        # Vérifications de la taille des entrées  et des dimensions        
        if inputs[0] != outputs:
            raise ValueError("La première dimension de inputs doit être égale à celle de outputs.")
        # Attributs privés de la classe Learning
        self.__neuron = neuron
        self.__inputs = inputs
        self.__outputs = outputs
    
    # Méthode privée pour calculer l'erreur
    def __computeError(self, index):
        # Calcul de la sortie du neurone pour le jeu d'entrées donné
        predicted_output = self.__neuron.getOutput(self.__inputs[index])
        # Calcul de l'erreur quadratique
        error = (predicted_output - self.__outputs[index]) ** 2
        return error