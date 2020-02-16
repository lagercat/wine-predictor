import numpy as np
import pandas as pd

DATASET_FILE = 'winemag-data_first150k.csv'
DATASET_PATH = '/Users/lagercat/Devel/ml/datasets/wine-reviews/' + DATASET_FILE
TAKE_TO = 5
SEED = 42
STATS = False


def hot_code_columns(columns):
    for column in columns:
        most_common = raw_dataset[column].value_counts()[:TAKE_TO].index.tolist()
        raw_dataset[column] = raw_dataset[column].map(lambda x: x if x in most_common else 'other_' + column)


np.random.seed(SEED)
raw_dataset = pd.read_csv(DATASET_PATH, header=0).drop(
    columns=['description', 'region_1', 'Unnamed: 0',
             'region_2', 'designation']).dropna()

hot_code_columns(['country', 'variety', 'winery', 'province'])
raw_dataset = pd.get_dummies(raw_dataset, prefix='', prefix_sep='')

column_names = raw_dataset.columns.values.tolist()
msk = np.random.rand(len(raw_dataset)) < 0.75

train = raw_dataset[msk]
train_label = train.pop('points')

test = raw_dataset[~msk]
test_label = test.pop('points')

print('Labels of the dataset: ' + ', '.join(column_names))
print('Length of the training set ' + str(len(train)))
print('Length of the test set ' + str(len(test)))

if STATS:
    train_stats = train.describe()
    print(train_stats)
