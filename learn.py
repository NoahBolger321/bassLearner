from sklearn import preprocessing as pp
from sklearn.neighbors import KNeighborsClassifier
from read_tabs import read_lines, get_notes
from itertools import cycle, islice
from mappings import Maps
import os

# TODO: add more features to data set including(key, nuances and intervals)

# get document root
root = os.path.dirname(os.path.abspath(__file__))

# initialize label encoder and classifier
labelEnc = pp.LabelEncoder()
knn = KNeighborsClassifier()

# read in the test and prediction notes
dani = read_lines(root, "daniCalifornia.txt")
bitesDust = read_lines(root, "bitesDust.txt")
trainNotes = get_notes([], {}, dani, 4)['notes']
predictNotes = get_notes([], {}, bitesDust, 4)['notes']

# create labels from list of notes, transform to integers
labelEnc.fit(Maps.allNotes)
shapedList = list(islice(cycle(list(labelEnc.classes_)), 100))

# transform train and test notes into integers
train_y = labelEnc.transform(shapedList)
train_x = labelEnc.transform(trainNotes)
test_x = labelEnc.transform(predictNotes)

# train model on 100 notes and generate prediction based on prediction notes
knn.fit(train_x[0:100].reshape(-1, 1), train_y)
prediction = knn.predict(test_x.reshape(-1, 1))
print(predictNotes)
print(labelEnc.inverse_transform(prediction))
