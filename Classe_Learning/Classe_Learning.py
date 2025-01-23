# Importation des modules nécessaires pour l'ajout du chemin parent au sys.path
import sys
import os
# Ajouter le chemin parent au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importation de la classe Neuron du dossier Classe_Neuron
from Class_Neuron.class_neuron import Neuron

# Importation du module random
import random

# Création de la classe Learning qui va permettre d'entraîner un neurone
class Learning:
    # Constructeur de la classe Learning avec 3 paramètres
    def __init__(self, neuron, inputs, outputs):
        # Si le nombre de sous-listes dans inputs diffère du nombre d'éléments dans outputs, une exception est levée.        
        if len(inputs) != len(outputs):
            raise ValueError("La première dimension de inputs doit être égale à celle de outputs.")
        # Attributs privés de la classe Learning
        self.__neuron = neuron
        # Si inputs n'est pas une liste de listes, une exception est levée.
        if not isinstance(inputs, list):
            # Si inputs n'est pas une liste de listes, une exception est levée.
            raise ValueError("inputs doit être une liste de listes.")
        # Si outputs n'est pas une liste, une exception est levée.
        if not isinstance(outputs, list):
            # Si outputs n'est pas une liste, une exception est levée.
            raise ValueError("outputs doit être une liste.")
        self.__inputs = inputs
        self.__outputs = outputs
        if len(inputs[0]) != self.__neuron.getNeuronSize():
            print("inputs size: ", len(inputs[0]))
            print("neuron size: ", self.__neuron.getNeuronSize())
            raise ValueError("Le nombre d'entrées du neurone doit être égal à la taille des entrées.")
    
    # Méthode privée pour calculer l'erreur
    def __computeError(self, index):
        # Calcul de la sortie du neurone pour le jeu d'entrées donné
        predicted_output = self.__neuron.getOutput(self.__inputs[index])
        # Calcul de l'erreur quadratique
        error = (predicted_output - self.__outputs[index]) ** 2
        # Retourne l'erreur
        return error
    
    def __computeAverageError(self):
        return sum(self.__computeError(i) for i in range(len(self.__inputs))) / len(self.__inputs)
    
    # Méthode publique pour entraîner le neurone
    def simpleTraining(self, epochs = 1000):
        # Initialisation de l'erreur
        error = []
        # Boucle pour chaque époque d'entraînement
        for _ in range(epochs):
            # Calcul de l'erreur moyenne actuelle
            avg_error = self.__computeAverageError()
            # Ajout de l'erreur moyenne actuelle à la liste des erreurs
            error.append(avg_error)

            # Choix d'un coefficient aléatoire à mettre à jour
            index = random.randint(1, self.__neuron.getNeuronSize())
            # Sauvegarde de l'ancienne valeur du coefficient
            old_value = self.__neuron.getCoefficient(index)

            # Modification aléatoire du coefficient
            coeff_ml = random.uniform(-0.1, 0.1)
            # Mise à jour du coefficient avec la nouvelle valeur
            new_value = self.__neuron.getCoefficient(index) + coeff_ml
            self.__neuron.setCoefficient(index, new_value)

            # Calcul de la nouvelle erreur
            new_avg_error = self.__computeAverageError()

            # Réinitialisation si l'erreur augmente
            if new_avg_error > avg_error:
                # Réinitialisation de la valeur du coefficient
                self.__neuron.setCoefficient(index, old_value)
        # Retourne la liste des erreurs
        return error
    
    def memoryLearning(self, epochs=1000):
        # Initialisation de l'erreur
        error = []
        # Initialisation du coefficient aléatoire entre 0 et 0.1
        coeff_ml = random.uniform(0, 0.1)
        # Initialisation du booléen aléatoire
        bool_ml= random.choice([True, False])
        
        # Boucle pour chaque époque d'entraînement
        for _ in range(epochs):
            # Calcul de l'erreur moyenne actuelle
            avg_error = self.__computeAverageError()
            # Ajout de l'erreur moyenne actuelle à la liste des erreurs
            error.append(avg_error)

            # Choix d'un coefficient aléatoire à mettre à jour
            index = random.randint(1, self.__neuron.getNeuronSize())
            # Sauvegarde de l'ancienne valeur du coefficient
            old_value = self.__neuron.getCoefficient(index)

            # Modification du coefficient en fonction du booléen
            if bool_ml:
                # Ajout du coefficient aléatoire à la valeur du coefficient actuel
                new_value = old_value + coeff_ml
            # Sinonl
            else:
                # Soustraction du coefficient aléatoire à la valeur du coefficient actuel
                new_value = old_value - coeff_ml
            # Mise à jour du coefficient avec la nouvelle valeur
            self.__neuron.setCoefficient(index, new_value)

            # Calcul de la nouvelle erreur
            new_avg_error = self.__computeAverageError()

            # Réinitialisation si l'erreur augmente ou reste la même
            if new_avg_error >= avg_error:
                # Réinitialisation de la valeur du coefficient
                self.__neuron.setCoefficient(index, old_value)
                # Choix d'un nouveau coefficient aléatoire entre 0 et 0.1
                coeff_ml = random.uniform(0, 0.1)
                # Choix d'un nouveau booléen aléatoire
                bool_ml = random.choice([True, False])
            # Sinon    
            else:
                # Augmenter la valeur absolue de la modification de 10 %
                coeff_ml *= 1.1

        # Retourne la liste des erreurs
        return error
    
