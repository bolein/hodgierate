from __future__ import division, print_function, absolute_import

import tflearn
from tflearn.data_utils import to_categorical, pad_sequences
from tflearn.datasets import imdb
import numpy as np
import model
from data import loader
from sklearn.model_selection import train_test_split

# # IMDB Dataset loading
# train, test, _ = imdb.load_data(path='imdb.pkl', n_words=10000,
#                                 valid_portion=0.1)
# trainX, trainY = train
# testX, testY = test
# testY


x, y = loader.load_data()
# y = [y - 1 for y in y]

# Data preprocessing
# Sequence padding
x = pad_sequences(x, maxlen=model.MAX_SEQ_LENGTH, value=0.)
# Converting labels to binary vectors
y = to_categorical(y, nb_classes=2)

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

# Training

dnn = model.DNN()
epochs = 1
best_val_score = 0

for epoch in range(epochs):
    dnn.fit(X_train, y_train, n_epoch=1, validation_set=(X_test, y_test),
            show_metric=True, batch_size=32, snapshot_epoch=True)

    # print('---------- EPOCH {} validation score: {}'.format(epoch, val_score))
    #
    # if val_score > best_val_score:
    #     # Manually save model
    #     best_val_score = val_score
    #     dnn.save("model.tfl")
