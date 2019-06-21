import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
import numpy
# fix random seed for reproducibility
numpy.random.seed(7)

df_labeled = pd.read_pickle('fullDataFrame')

