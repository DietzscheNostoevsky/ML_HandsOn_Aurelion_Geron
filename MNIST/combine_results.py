import numpy as np
import tensorflow as tf
from tensorflow import keras

# Load the models and their weights
model1 = keras.models.load_model('model1.h5')
model2 = keras.models.load_model('model2.h5')

# Combine the weights from both models
for layer1, layer2 in zip(model1.layers, model2.layers):
    weights1 = layer1.get_weights()
    weights2 = layer2.get_weights()
    new_weights = []
    for w1, w2 in zip(weights1, weights2):
        new_weights.append(np.mean([w1, w2], axis=0))
    layer1.set_weights(new_weights)

# Save the combined model
model1.save('combined_model.h5')
