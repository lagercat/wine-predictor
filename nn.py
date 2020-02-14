import tensorflow as tf
from tensorflow import keras

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DATASET_FILE = "winemag-data_first150k.csv"
DATASET_PATH = "/Users/lagercat/Devel/ml/datasets/wine-reviews/" + DATASET_FILE
SEED = 42

np.random.seed(SEED)

raw_dataset = pd.read_csv(DATASET_PATH, header=0)
labels = raw_dataset.columns.values.tolist()

msk = np.random.rand(len(raw_dataset)) < 0.75

train = raw_dataset[msk]
test = raw_dataset[~msk]

print("Labels of the dataset: " + ", ".join(labels))
print("Length of the training set " + str(len(train)))
print("Length of the test set " + str(len(test)))
