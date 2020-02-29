import os

import pandas as pd
from matplotlib import pyplot as plt

DATASET_FILE = 'winemag-data_first150k.csv'
DATASET_FOLDER = os.environ['WINE_DATASET']
DATASET_PATH = DATASET_FOLDER + DATASET_FILE
TAKE_TO_COUNTRY = 10
TAKE_TO_VARIETY = 20
current_dir = os.path.dirname(__file__)

dataset = pd.read_csv(DATASET_PATH)

(points, prices, country, variety) = (dataset['points'].tolist(),
                                      dataset['price'].tolist(),
                                      dataset['country'],
                                      dataset['variety'])

most_common_countries = country.value_counts()[:TAKE_TO_COUNTRY].index.to_list()
country = country.map(lambda x: x if x in most_common_countries else 'other')

most_common_variety = variety.value_counts()[:TAKE_TO_VARIETY].index.to_list()
variety = variety.map(lambda x: x if x in most_common_variety else 'other')

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

country.value_counts().plot(kind='barh', figsize=(20, 10),
                            title='Country Distribution')
plt.savefig(os.path.join(current_dir, '../graphs/countries.png'), dpi=100)
plt.close()

variety.value_counts().plot(kind='barh', figsize=(20, 10),
                            title='Variety Distribution')
plt.savefig(os.path.join(current_dir, '../graphs/variety.png'), dpi=100)
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
