import os

import pandas as pd
from matplotlib import pyplot as plt

DATASET_FILE = 'winemag-data_first150k.csv'
DATASET_FOLDER = os.environ['WINE_DATASET']
DATASET_PATH = DATASET_FOLDER + DATASET_FILE
current_dir = os.path.dirname(__file__)

dataset = pd.read_csv(DATASET_PATH)

(points, prices, country, variety) = (dataset['points'].tolist(),
                                      dataset['price'].tolist(),
                                      dataset['country'].tolist(),
                                      dataset['variety'].tolist())

binsForPoints = [x for x in range(80, 101, 2)]
binsForPrices = [x for x in range(0, 251, 5)]

plt.hist(points, bins=binsForPoints)
plt.xlabel("Rating")
plt.ylabel("Number")
plt.title("Distribution of Wine Rating")
plt.savefig(os.path.join(current_dir, '../graphs/ratings.png'))
plt.close()

plt.hist(prices, bins=binsForPrices)
plt.xlabel("Prices")
plt.ylabel("Number")
plt.title("Distribution of wine Prices")
plt.savefig(os.path.join(current_dir, '../graphs/prices.png'))
plt.close()

plt.hist(country, width=1)
plt.xlabel("Country")
plt.ylabel("Number")
plt.title("Distribution of wine's country of origin")
fig = plt.gcf()
fig.set_size_inches(28.5, 20.5)
plt.savefig(os.path.join(current_dir, '../graphs/countries.png'), dpi=100)
plt.close()

plt.hist(variety)
plt.xlabel("Variety")
plt.ylabel("Number")
plt.title("Distribution of wine variety")
plt.savefig(os.path.join(current_dir, '../graphs/variety.png'))
plt.close()

plt.plot(prices, points, 'ro')
plt.axis([0, 250, 80, 100])
plt.xlabel("Prices")
plt.ylabel("Rating")
plt.title("Prices against rating")
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
plt.savefig(os.path.join(current_dir, '../graphs/priceAndRating.png'), dpi=100)
plt.close()
