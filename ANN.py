import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
import numpy
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder

# fix random seed for reproducibility
numpy.random.seed(7)

import os
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"   # see issue #152
os.environ["CUDA_VISIBLE_DEVICES"] = ""

dataset = pd.read_pickle('fullDataFrame')
dataset = dataset.replace(r'\\n',' ', regex=True)
dataset['label'] = dataset['label'].astype(int)
print(dataset)
dataset = dataset.values

X = dataset[:, 0:36]
Y = dataset[:, 37]
Y = Y.astype(int)

print(X)
print(Y)
print('datatype: ' + str(Y.dtype))


# Feature Scaling
sc = StandardScaler()
X = sc.fit_transform(X)
print(X)

# one hot encoding of labels
onehot_encoder = OneHotEncoder(sparse=False)
Y = Y.reshape(len(Y), 1)
Y = onehot_encoder.fit_transform(Y)
print('ENCODED')
print(Y)


# create model
model = Sequential()
model.add(Dense(12, input_dim=36, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(3, activation='sigmoid'))


# Compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


# Fit the model
model.fit(X, Y, epochs=150, batch_size=10)