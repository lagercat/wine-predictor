import matplotlib

matplotlib.use('Agg')

from matplotlib import pyplot as plt
import pandas as pd
from collections import Counter
from functools import reduce


DATASET_PATH = "/home/malessebastian/datasets/wine/winemag-data-130k-v2.csv"
POINTS_INDEX = 4
PRICE_INDEX = 5
dataset = pd.read_csv(DATASET_PATH)

(points, prices) = (dataset['points'].dropna().tolist(),
        dataset['price'].dropna().tolist())
num_bins = 10

plt.hist(prices, bins=num_bins)
plt.xlabel("Prices")
plt.ylabel("Number")
plt.title("Distribution of Wine Prices")
plt.savefig('graphs/test.png')
plt.close()
