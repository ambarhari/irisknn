import numpy as np
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
import pandas as pd
import sys

# Mengambil input dari PHP
angka1 = float(sys.argv[1])
angka2 = float(sys.argv[2])
angka3 = float(sys.argv[3])
angka4 = float(sys.argv[4])
# Load the pre-trained model
model = tf.keras.models.load_model('../models/iris.h5')
# Select a single data point for prediction
x_new = np.array([[angka1, angka2, angka3, angka4]])  # example data point
# Predict the class of the new data point
predicted_probabilities = model.predict(x_new)
predicted_class = np.argmax(predicted_probabilities, axis=-1)
if predicted_class == 0:
    print("Setosa")
elif predicted_class == 1:
    print("Versicolor")
elif predicted_class == 2:
    print("Virginica")
else:
    print("Hasil klasifikasi tidak valid.")