# Importation des librairies nécessaires math, random et matplotlib.pyplot
import math
import random
import matplotlib.pyplot as plt

# Importation des modules nécessaires pour l'ajout du chemin parent au sys.path
import sys
import os
# Ajouter le chemin parent au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importation de la classe Neuron du dossier Classe_Neuron
from Class_Neuron.class_neuron import Neuron

# Importation de la classe Learning du dossier Classe_Learning
from Classe_Learning.Classe_Learning import Learning

# Importer le fichier Travail_Préli_Sigmoid du dossier Travail_Préli_Sigmoid
from Class_SigmoidNeuron.Class_SigmoidNeuron import sigmoid
from Class_SigmoidNeuron.Class_SigmoidNeuron import SigmoidNeuron

# Description: Premier neurone avec 7 entrées et 1 sortie représentant un neurone qui apprend àun affichage de 7 segments
# Entrées: 7 entrées représentant les 7 segments
entrees = [ [1.0,1.0,1.0,1.0,1.0,1.0,0.0] ,\
[0.0,1.0,1.0,0.0,0.0,0.0,0.0] ,\
[1.0,1.0,0.0,1.0,1.0,0.0,1.0] ,\
[1.0,1.0,1.0,1.0,0.0,0.0,1.0] ,\
[1.0,1.0,1.0,0.0,0.0,1.0,1.0] ,\
[1.0,0.0,1.0,1.0,0.0,1.0,1.0] ,\
[1.0,0.0,1.0,1.0,1.0,1.0,1.0] ,\
[1.0,1.0,1.0,0.0,0.0,0.0,0.0] ,\
[1.0,1.0,1.0,1.0,1.0,1.0,1.0] ,\
[1.0,1.0,1.0,1.0,0.0,1.0,1.0] ]

# Sorties: 10 sorties représentant les chiffres de 0 à 9
sorties = [ 0, 0, 0, 0, 1, 0, 0 ,0 ,0 ,0]

# Création de la classe Neuron avec 7 entrées
neuron = SigmoidNeuron(7)

# Création de l'instance de la classe Learning
learning = Learning(neuron, entrees, sorties)

# Calcul des erreur a l'aide de la méthode simpleTraining
errors=learning.simpleTraining()

# Affichage du graphique de l'évolution de l'erreur moyenne
plt.plot(errors)
# Affichage du titre du graphique et des labels des axes
plt.title("Évolution de l'erreur moyenne")
# Affichage du titre de l'axe des abscisses
plt.xlabel("Époques")
# Affichage du titre de l'axe des ordonnées
plt.ylabel("Erreur moyenne")
# Affichage de la grille
plt.show()