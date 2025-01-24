import numpy as np
import random

# Importation de la librairie math

# Importation des modules nécessaires pour l'ajout du chemin parent au sys.path
import sys
import os
# Ajouter le chemin parent au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importer le fichier Travail_Préli_Sigmoid du dossier Travail_Préli_Sigmoid
from Class_Neuron.class_neuron import Neuron
# Importation de la class NeuralNetwork du dossier Class_NeuralNetwork
from Class_NeuralNetwork.Class_NeuralNetwork import NeuralNetwork

# Importe le module 'unittest'
import unittest
# Importe le module 'random'


# Fonction pour générer des fichiers d'exemple et de coefficients
def generate_example_files():
    # Générer les coefficients du réseau (fichier Coefficients.txt)
    with open('Coefficients.txt', 'w') as f:
        f.write("2,625\n")  # Exemple: 2 couches, 625 entrées
        f.write("64,26\n")  # 64 neurones dans la première couche, 26 neurones dans la couche de sortie
        f.write("NEU,SIG\n")  # Type de couche : Neuron pour la première, SigmoidNeuron pour la deuxième
        for _ in range(64):
            f.write(','.join([str(random.random()) for _ in range(625)]) + '\n')
        for _ in range(26):
            f.write(','.join([str(random.random()) for _ in range(64)]) + '\n')

    # Générer les exemples de tests (fichier SignesTests.txt)
    with open('SignesTests.txt', 'w') as f:
        for _ in range(338):  # 338 exemples
            label = chr(random.randint(ord('a'), ord('z')))  # Lettre aléatoire entre 'a' et 'z'
            pixels = [random.randint(0, 255) for _ in range(625)]  # 625 valeurs de pixels
            f.write(f"{label},{','.join(map(str, pixels))}\n")

# Fonction pour charger les données d'exemple
def load_test_data(filename):
    examples = []
    labels = []
    
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            label = parts[0]
            pixels = list(map(int, parts[1:]))
            examples.append(np.array(pixels) / 255.0)  # Normalisation
            labels.append(label)
    
    return examples, labels

# Fonction pour afficher les lettres mal reconnues
def recognize_and_display_misrecognized_characters(coefficients_file, test_file):
    # Charger le réseau de neurones depuis le fichier Coefficients.txt
    nn = NeuralNetwork(625, [64, 26], ["NEU", "SIG"])  # Réseau avec 625 entrées, 64 neurones dans la première couche et 26 neurones de sortie
    nn.loadNetwork(coefficients_file)
    
    # Charger les exemples de test depuis le fichier SignesTests.txt
    examples, labels = load_test_data(test_file)
    
    # Reconnaître les lettres et obtenir celles qui ont été mal reconnues
    misrecognized = []
    for i, example in enumerate(examples):
        output = nn.getOutputs(example)
        predicted_label = chr(np.argmax(output) + ord('a'))  # Lettre prédite
        if predicted_label != labels[i]:
            output = nn.getOutputs(example.tolist())
    
    # Afficher les lettres mal reconnues
    print(f"Nombre de lettres mal reconnues: {len(misrecognized)}")
    for correct, predicted in misrecognized:
        print(f"Lettres mal reconnue : {correct} -> Prédiction : {predicted}")

# Générer les fichiers et effectuer la reconnaissance
if __name__ == "__main__":
    generate_example_files()  # Générer les fichiers
    recognize_and_display_misrecognized_characters('Coefficients.txt', 'SignesTests.txt')  # Vérifier les résultats
