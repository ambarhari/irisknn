import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
import sys

# Read CSV file
csv_file_path = sys.argv[1]
data = pd.read_csv(csv_file_path, index_col=0)

# Convert labels from string to integer
encoder = LabelEncoder()
labels = encoder.fit_transform(data["Species"])

# Split data into features and labels
features = data.drop(columns=["Species"]).values

# Define model architecture
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dense(3, activation="softmax")
])

# Compile model
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# Train model
model.fit(features, labels, epochs=10)

# Save model as H5 file
h5_file_path = sys.argv[2]
model.save(h5_file_path)
