# Importation de la librairie math
import math

# Définition de la fonction sigmoid
def sigmoid(x):
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
    