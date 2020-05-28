import numpy as np
import os
import pandas as pd
import pickle

# creating a dir for separate each melspectrogram to generator
if not (os.path.exists("../files/melspec/")):
    os.mkdir("../files/melspec/")

df = pd.read_parquet('../files/4mula_small.parquet')

melspecs = df["melspectrogram"]
labels = df["main_genre"]

f = open("../files/melspec/labels.pkl","wb")
pickle.dump(np.array(labels),f)
f.close()

i = 0
for m in melspecs:
	this_m = np.concatenate(m).reshape((128,-1))
	this_m = np.hstack((this_m,np.zeros((128,1292-this_m.shape[1]))))
	np.save("../files/melspec/"+str(i)+".npy", this_m)
	i += 1

