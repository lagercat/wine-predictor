from matplotlib import pyplot as plt
import pandas as pd


DATASET_PATH = "/home/malessebastian/datasets/wine/winemag-data-130k-v2.csv"
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
plt.savefig('graphs/ratings.png')
plt.close()


plt.hist(prices, bins=binsForPrices)
plt.xlabel("Prices")
plt.ylabel("Number")
plt.title("Distribution of wine Prices")
plt.savefig('graphs/prices.png')
plt.close()


plt.hist(country, width=1)
plt.xlabel("Country")
plt.ylabel("Number")
plt.title("Distribution of wine's country of origin")
fig = plt.gcf()
fig.set_size_inches(28.5, 20.5)
plt.savefig('graphs/countries.png', dpi=100)
plt.close()


plt.hist(variety)
plt.xlabel("Variety")
plt.ylabel("Number")
plt.title("Distribution of wine variety")
plt.savefig('graphs/variety.png')
plt.close()


plt.plot(prices, points, 'ro')
plt.axis([0, 250, 80, 100])
plt.xlabel("Prices")
plt.ylabel("Rating")
plt.title("Prices against rating")
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
plt.savefig('graphs/priceAndRating.png', dpi=100)
plt.close()



