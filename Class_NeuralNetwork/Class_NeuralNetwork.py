# Importation des modules nécessaires pour l'ajout du chemin parent au sys.path
import sys
import os
# Ajouter le chemin parent au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importation de la classe Neuron du dossier Classe_Neuron
from Class_Neuron.class_neuron import Neuron

# Importation du module class sigmoid_neuron
from Class_SigmoidNeuron.Class_SigmoidNeuron import SigmoidNeuron

# Création de la classe NeuralNetwork qui va permettre de créer un réseau de neurones 
class NeuralNetwork:
    # Constructeur de la classe NeuralNetwork avec 3 paramètres 
    def __init__(self, inputsLength, neuronsPerLayer, layerType):
        
        # Si le nombre d'éléments dans neuronsPerLayer diffère du nombre d'éléments dans layerType, une exception est levée.
        if len(neuronsPerLayer) != len(layerType):
            # Si le nombre d'éléments dans neuronsPerLayer diffère du nombre d'éléments dans layerType, une exception est levée.
            raise ValueError("neuronsPerLayer and layerType must have the same length")
        
        # Si inputsLength n'est pas un entier, une exception est levée.
        if type(inputsLength) != int:
            # Si inputsLength n'est pas un entier, une exception est levée.
            raise ValueError("inputsLength must be an integer")
        
        # Si neuronsPerLayer n'est pas une liste, une exception est levée.
        if type(neuronsPerLayer) != list:
            # Si neuronsPerLayer n'est pas une liste, une exception est levée.
            raise ValueError("neuronsPerLayer must be a list")
        
        # Si layerType n'est pas une liste, une exception est levée.
        if type(layerType) != list:
            # Si layerType n'est pas une liste, une exception est levée.
            raise ValueError("layerType must be a list")
        
        # Attributs privés de la classe NeuralNetwork
        self.__layers = []
        # Si inputsLength n'est pas un entier, une exception est levée.
        previousLayerSize = inputsLength
        
        # Boucle pour chaque élément dans neuronsPerLayer
        for i in range(len(neuronsPerLayer)):
            # Si layerType[i] n'est pas "SIG" ou "NEU", une exception est levée.
            layer = []
            # Boucle pour chaque élément dans neuronsPerLayer[i]
            for _ in range(neuronsPerLayer[i]):
                # Si layerType[i] est "SIG", neuron est un SigmoidNeuron, sinon neuron est un Neuron
                if layerType[i] == "SIG":
                    # Si layerType[i] est "SIG", neuron est un SigmoidNeuron
                    neuron = SigmoidNeuron(previousLayerSize)
                # Si layerType[i] est "NEU", neuron est un Neuron
                else:
                    # Si layerType[i] est "NEU", neuron est un Neuron
                    neuron = Neuron(previousLayerSize)
                # Ajout de neuron à layer
                layer.append(neuron)
            # Ajout de layer à self.__layers    
            self.__layers.append(layer)
            # previousLayerSize prend la valeur de neuronsPerLayer[i] 
            previousLayerSize = neuronsPerLayer[i]
        return layer
            
    # Méthode publique pour obtenir le nombre de couches avec 4 paramètres la taille des entrées, le nombre de neurones par couche, le type de couche et le type de neurone
    def getCoefficient(self, layer, neuron, position):
        # Retourne le coefficient de la couche, du neurone et de la position donnés
        return self.__layers[layer][neuron].weights[position]

    # Méthode publique pour obtenir le nombre de couches avec 4 paramètres la taille des entrées, le nombre de neurones par couche, le type de couche et le type de neurone
    def setCoefficient(self, layer, neuron, position, value):
        # Met à jour le coefficient de la couche, du neurone et de la position
        self.__layers[layer][neuron].weights[position] = value

    # Méthode publique pour obtenir le nombre de couches avec 4 paramètres la taille des entrées, le nombre de neurones par couche, le type de couche et le type de neurone
    def getOutputs(self, inputs):
        # Retourne les sorties du réseau de neurones pour les entrées données
        for layer in self.__layers:
            # Création d'une liste vide outputs
            outputs = []
            # Boucle pour chaque neurone dans layer
            for neuron in layer:
                # Ajout de la sortie du neurone pour les entrées données à outputs
                outputs.append(neuron.getOutput(inputs))
            # Les entrées deviennent les sorties
            inputs = outputs
        # Retourne les sorties
        return inputs