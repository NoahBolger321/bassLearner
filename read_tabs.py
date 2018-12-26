import os
from string_map import stringMap

# read tab lines
root = os.path.dirname(os.path.abspath(__file__))
path = "{}/tablature/bitesDust.txt".format(root)
with open(path, 'r') as tabText:
    tabLines = tabText.readlines()

# TODO: use threading to read 4 strings simultaneously
# print notes
tabLines = [t.strip() for t in tabLines if t.strip() != '']
for line in tabLines:
    string = line[0]
    for note in line:
        if note.isdigit():
            print(stringMap.map[note + string])
