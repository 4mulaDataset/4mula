import numpy as np
import os
import pickle
import sys

from sklearn import preprocessing 
from sklearn.model_selection import KFold
from sklearn.utils import shuffle

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.callbacks import Callback, EarlyStopping, ReduceLROnPlateau
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.layers import SimpleRNN, TimeDistributed
from tensorflow.keras.layers import Dropout, BatchNormalization

from datagenerator import DataGenerator


def define_architecture(input_shape, n_classes):

  model = Sequential()
  model.add(BatchNormalization(input_shape=input_shape))
  model.add(Conv2D(30, (3,3), activation='elu', padding='same'))
  model.add(MaxPooling2D((2, 2)))
  model.add(Dropout(0.1))
  model.add(BatchNormalization())
  model.add(Conv2D(60, (3,3), activation='elu', padding='same'))
  model.add(MaxPooling2D((2, 3)))
  model.add(Dropout(0.1))
  model.add(BatchNormalization())
  model.add(Conv2D(60, (3,3), activation='elu', padding='same'))
  model.add(MaxPooling2D((4, 4)))
  model.add(Dropout(0.1))
  model.add(BatchNormalization())
  model.add(Conv2D(60, (3,3), activation='elu', padding='same'))
  model.add(MaxPooling2D((4, 4)))
  model.add(Dropout(0.1))
  model.add(TimeDistributed(SimpleRNN(30)))
  model.add(Flatten())
  model.add(Dense(n_classes, activation='softmax'))

  return model


files_dir = "../files/melspec/"

# loading and encoding labels
f = open(files_dir+"labels.pkl","rb")
all_labels = pickle.load(f)
f.close()

label_encoder = preprocessing.LabelEncoder() 
encoded_labels = label_encoder.fit_transform(all_labels)

# some definitions for training the NNs
earlyStopping = EarlyStopping(monitor="val_loss", patience=20,
  verbose=0, restore_best_weights=True)
reduce_lr = ReduceLROnPlateau()

example_data = np.load(files_dir + "/0.npy")
input_layer = (example_data.shape[0], example_data.shape[1], 1)
n_examples = len(encoded_labels)
n_classes = len(np.unique(encoded_labels))

params = {"dim": (example_data.shape[0], example_data.shape[1]),
          "batch_size": 32,
          "n_classes": n_classes,
          "n_channels": 1,
          "gen_dir": files_dir,
          "shuffle": True}


kf = KFold(n_splits=10, shuffle=True, random_state=42)
val_kf = KFold(n_splits=9, shuffle=True, random_state=42)

acc = []
k = 0
for train_index, test_index in kf.split(range(n_examples)):

  this_tr, this_val = next(val_kf.split(train_index))

  # Generators
  training_generator = DataGenerator(train_index[this_tr],
    encoded_labels,
    **params)
  val_generator = DataGenerator(train_index[this_val],
    encoded_labels,
    **params)
  test_generator = DataGenerator(test_index,
    encoded_labels,
    **params)

  model = define_architecture(input_layer, n_classes)
  model.compile(optimizer=tf.keras.optimizers.Adam(),
    loss="categorical_crossentropy",
    metrics=["accuracy"])

  model.fit(x = training_generator,
    validation_data = val_generator,
    callbacks = [earlyStopping, reduce_lr],
    epochs = 50)

  score, this_acc = model.evaluate(x=test_generator)
  acc.append(this_acc)

  k += 1

print(np.mean(acc))
print(np.std(acc))
