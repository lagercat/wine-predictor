import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow_docs as tfdocs
import tensorflow_docs.modeling
import tensorflow_docs.plots

DATASET_FILE = 'winemag-data_first150k.csv'
EPOCHS = 300
DATASET_PATH = '/Users/lagercat/Devel/ml/datasets/wine-reviews/' + DATASET_FILE
TAKE_TO = 5
SEED = 42
STATS = False


def hot_code_columns(columns):
    for column in columns:
        most_common = raw_dataset[column].value_counts()[:TAKE_TO].index.tolist()
        raw_dataset[column] = raw_dataset[column].map(lambda x: x if x in most_common else 'other_' + column)


def norm(x):
    return (x - train.mean()) / train.std()


def build_model():
    new_model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=[len(train.keys())]),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(1)
    ])

    optimizer = tf.keras.optimizers.RMSprop(0.001)
    new_model.compile(loss='mse', optimizer=optimizer, metrics=['mae', 'mse'])

    return new_model


np.random.seed(SEED)
raw_dataset = pd.read_csv(DATASET_PATH, header=0).drop(
    columns=['description', 'region_1', 'Unnamed: 0',
             'region_2', 'designation']).dropna()

hot_code_columns(['country', 'variety', 'winery', 'province'])
raw_dataset = pd.get_dummies(raw_dataset, prefix='', prefix_sep='')

column_names = raw_dataset.columns.values.tolist()
msk = np.random.rand(len(raw_dataset)) < 0.75

train = raw_dataset[msk]
train_labels = train.pop('points')

test = raw_dataset[~msk]
test_labels = test.pop('points')

print('Labels of the dataset: ' + ', '.join(column_names))
print('Length of the training set ' + str(len(train)))
print('Length of the test set ' + str(len(test)))

if STATS:
    train_stats = train.describe()
    print(train_stats)

train_normed = norm(train)
test_normed = norm(test)

model = build_model()
model.summary()

history = model.fit(train_normed, train_labels, epochs=EPOCHS, validation_split=0.2, verbose=0,
                    callbacks=[tfdocs.modeling.EpochDots()])

hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch
print(hist.tail())

plotter = tfdocs.plots.HistoryPlotter(smoothing_std=2)
plotter.plot({'Basic': history}, metric="mae")
plt.ylim([0, 10])
plt.ylabel('MAE [MPG]')
plt.show()

plotter.plot({'Basic': history}, metric="mse")
plt.ylim([0, 20])
plt.ylabel('MSE [MPG^2]')
plt.show()
