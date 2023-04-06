import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import ModelCheckpoint

# Load the data
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Preprocess the data
x_train = x_train / 255.0
x_test = x_test / 255.0

# Define the model
model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Set up checkpointing
checkpoint_path = '/content/drive/MyDrive/Colab Notebooks/checkpoints/colab_training/cp-{epoch:04d}.ckpt'
checkpoint_callback = ModelCheckpoint(
    filepath=checkpoint_path, save_weights_only=True, save_freq='epoch')

# Train the model
model.fit(x_train, y_train, epochs=10, validation_data=(
    x_test, y_test), callbacks=[checkpoint_callback])
