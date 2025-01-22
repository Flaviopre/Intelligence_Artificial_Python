# Importation des modules nécessaires pour l'ajout du chemin parent au sys.path
import sys
import os
# Ajouter le chemin parent au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importation de la classe Neuron du dossier Classe_Neuron
from Class_Neuron.class_neuron import Neuron

# Création de la classe Learning qui va permettre d'entraîner un neurone
class Learning:
    # Constructeur de la classe Learning avec 3 paramètres
    def __init__(self, neuron, inputs, outputs):
        # Si le nombre de sous-listes dans inputs diffère du nombre d'éléments dans outputs, une exception est levée.        
        if len(inputs) != len(outputs):
            raise ValueError("La première dimension de inputs doit être égale à celle de outputs.")
        # Attributs privés de la classe Learning
        self.__neuron = Neuron(neuron)
        # Si inputs n'est pas une liste de listes, une exception est levée.
        if not isinstance(inputs, list):
            # Si inputs n'est pas une liste de listes, une exception est levée.
            raise ValueError("inputs doit être une liste de listes.")
        # Si outputs n'est pas une liste, une exception est lev
        if not isinstance(outputs, list):
            # Si outputs n'est pas une liste, une exception est levée.
            raise ValueError("outputs doit être une liste.")
        self.__inputs = inputs
        self.__outputs = outputs
    
    # Méthode privée pour calculer l'erreur
    def __computeError(self, index):
        # Calcul de la sortie du neurone pour le jeu d'entrées donné
        predicted_output = self.__neuron.getOutput(self.__inputs[index])
        # Calcul de l'erreur quadratique
        error = (predicted_output - self.__outputs[index]) ** 2
        return error