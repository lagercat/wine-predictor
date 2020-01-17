from matplotlib import pyplot as plt
import pandas as pd


DATASET_PATH = "/home/malessebastian/datasets/wine/winemag-data-130k-v2.csv"
dataset = pd.read_csv(DATASET_PATH)

(points, prices) = (dataset['points'].dropna().tolist(),
                    dataset['price'].dropna().tolist())

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
plt.title("Distribution of Wine Prices")
plt.savefig('graphs/prices.png')
plt.close()
