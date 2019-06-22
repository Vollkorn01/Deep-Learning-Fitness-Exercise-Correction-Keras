import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# fix random seed for reproducibility
np.random.seed(7)

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
X = np.nan_to_num(X)
print(X)

# one hot encoding of labels
onehot_encoder = OneHotEncoder(sparse=False)
Y = Y.reshape(len(Y), 1)
Y = onehot_encoder.fit_transform(Y)
print('ENCODED')
print(Y)

# split in train / test set
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=42, shuffle=False)  # maybe add shuffle=False


# create model
model = Sequential()
model.add(Dense(36, input_dim=36, activation='relu'))
model.add(Dense(18, activation='relu'))
model.add(Dense(9, activation='relu'))
model.add(Dense(3, activation='softmax'))  # we use Softmax, so the outputs represent accuracies that add up to 1


# Compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


# Fit the model
model.fit(X_train, y_train, epochs=100, batch_size=10)

eval_model=model.evaluate(X_train, y_train)
eval_model

y_pred=model.predict(X_test)
y_pred =(y_pred > 0.5)

cm = confusion_matrix(y_test.argmax(axis=1), y_pred.argmax(axis=1))
print(cm)

def print_confusion_matrix(confusion_matrix, class_names, figsize=(10, 7), fontsize=14):
    """Prints a confusion matrix, as returned by sklearn.metrics.confusion_matrix, as a heatmap.

    Arguments
    ---------
    confusion_matrix: numpy.ndarray
        The numpy.ndarray object returned from a call to sklearn.metrics.confusion_matrix.
        Similarly constructed ndarrays can also be used.
    class_names: list
        An ordered list of class names, in the order they index the given confusion matrix.
    figsize: tuple
        A 2-long tuple, the first value determining the horizontal size of the ouputted figure,
        the second determining the vertical size. Defaults to (10,7).
    fontsize: int
        Font size for axes labels. Defaults to 14.

    Returns
    -------
    matplotlib.figure.Figure
        The resulting confusion matrix figure
    """
    df_cm = pd.DataFrame(
        confusion_matrix, index=class_names, columns=class_names,
    )
    fig = plt.figure(figsize=figsize)
    try:
        heatmap = sns.heatmap(df_cm, annot=True, fmt="d")
    except ValueError:
        raise ValueError("Confusion matrix values must be integers.")
    heatmap.yaxis.set_ticklabels(heatmap.yaxis.get_ticklabels(), rotation=0, ha='right', fontsize=fontsize)
    heatmap.xaxis.set_ticklabels(heatmap.xaxis.get_ticklabels(), rotation=45, ha='right', fontsize=fontsize)
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.interactive(False)
    plt.show()
    return fig

print_confusion_matrix(cm, ['too low', 'correct', 'too high'])