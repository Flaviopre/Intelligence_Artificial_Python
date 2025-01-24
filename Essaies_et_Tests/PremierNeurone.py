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

# Création de la liste entrees_bruitees en ajoutant une valeur aléatoire comprise entre -0.1 et +0.1
entrees_bruitees = [[x + random.uniform(-0.1, 0.1) for x in entree] for entree in entrees]

# Création de l'instance de la classe Learning avec entrees_bruitees
learning_bruitees = Learning(neuron, entrees_bruitees, sorties)

# Calcul des erreurs à l'aide de la méthode simpleTraining sur entrees_bruitees
errors_bruitees = learning_bruitees.simpleTraining()

# Vérification des résultats de l'apprentissage sur entrees_bruitees 
results_bruitees = []
# Pour chaque entrée dans entrees_bruitees
for entree in entrees_bruitees:
    # Calcul de la sortie du neurone 
    output = neuron.getOutput(entree)
    # Si la sortie est supérieure à 0.5, le résultat est 1, sinon 0
    result = 1 if output > 0.5 else 0
    # Ajout du résultat à la liste results
    results_bruitees.append(result)

# Affichage des résultats de l'apprentissage sur entrees_bruitees        
print("Résultats de l'apprentissage sur entrees_bruitees:", results_bruitees)
for res in results_bruitees:
    # Si res est différent de 0 et 1, une exception est levée
    if res != 0 and res != 1:
        # Exception levée valeur incorrecte
        raise ValueError("Les résultats doivent être 0 ou 1")

# Affichage du graphique de l'évolution de l'erreur moyenne sur entrees_bruitees
plt.plot(errors_bruitees)
# Affichage du titre du graphique et des labels des axes
plt.title("Évolution de l'erreur moyenne sur entrees_bruitees")
# Affichage du titre de l'axe des abscisses
plt.xlabel("Époques")
# Affichage du titre de l'axe des ordonnées
plt.ylabel("Erreur moyenne")
# Affichage de la grille
plt.grid(True)
# Affichage du graphique 
plt.show()

# Création d'un nouvel objet de la classe SigmoidNeuron avec 7 entrées
neuron_initial = SigmoidNeuron(7)

# Parcourir les coefficients du neurone initial en utilisant la méthode getCoefficient
for _ in range(1, neuron_initial.getNeuronSize() + 1):
    # Sauvegarde des coefficients initiaux du neurone dans la liste initial_coefficients 
    initial_coefficients = [neuron_initial.getCoefficient(i) for i in range(1, neuron_initial.getNeuronSize() + 1)]

# Réalisation de l'apprentissage avec les données initiales
learning_initial = Learning(neuron_initial, entrees, sorties)
# Utilisation de la méthode simpleTraining afin de calculer les erreurs
errors_initial = learning_initial.simpleTraining()

# Remplacement des coefficients du neurone par ceux sauvegardés
for i in range(neuron_initial.getNeuronSize()):
    # Affichage des coefficients initiaux
    print("Initial coefficients: ", initial_coefficients[i])
    # Définition des coefficients du neurone initial 
    neuron_initial.setCoefficient(i + 1, initial_coefficients[i])

# Utilisation de la méthode memoryLearning
errors_memory = learning_initial.memoryLearning()

# Construction de la figure avec l'évolution de l'erreur selon les deux algorithmes
# Affichage des erreurs de la mémoire
plt.plot(errors_memory, label='Avec mémoire')
# Affichage des erreurs initiales
plt.plot(errors_initial, label='Simple')
# Affichage du titre du graphique et des labels des axes
plt.title("Comparaison de l'évolution de l'erreur moyenne")
# Affichage du titre de l'axe des abscisses
plt.xlabel("Époques")
# Affichage du titre de l'axe des ordonnées
plt.ylabel("Erreur moyenne")
# Affichage de la légende
plt.legend()
# Affichage de la grille
plt.grid(True)
# Affichage du graphique
plt.show()
