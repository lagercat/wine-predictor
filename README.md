# 🍷 Predicting wine ratings with Tensorflow

This is a small project I did just so that I brush up
my data science skills.

## The dataset
The dataset I used can be found [here](https://www.kaggle.com/zynicide/wine-reviews).
It does have some bottle necks caused by the collection of the data, it happens that
the author scraped only wines with a score higher than 80.

## Graphs
There are various graphs(in the graphs/ directory) which I plotted 
to help with my understanding of the dataset. 
Some of them are a work in progress and will be
cleaned.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to
install the requirements of the project.

```bash
pip install -r requirements.txt
```

Note that you will also need to put the path of your 
folder to your dataset in an env variable called `WINE_DATASET`.

## Possible applications
Because of the nature of the data, I think even an ideal 
model would have restricted use cases in a real 
life application(maybe sell it to a posh winery in France?).
However, this kind of prediction based on online ratings is
quite notorious in some industries(like the music industry).

## License
[MIT](https://choosealicense.com/licenses/mit/)