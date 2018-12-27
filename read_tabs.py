import os
from string_map import stringMap

# read tab lines
root = os.path.dirname(os.path.abspath(__file__))
path = "{}/tablature/bitesDust.txt".format(root)
with open(path, 'r') as tabText:
    tabLines = tabText.readlines()

# TODO: read notes into list in order for nearest neighbour algorithm
tabLines = [t.strip() for t in tabLines if t.strip() != '']
# loop through each grouping of strings, retrieve notes, print mapped note if fret recorded
for n in range(0, len(tabLines), 4):
    for i in range(1, len(tabLines[n])):
        gNote = tabLines[n][i]
        dNote = tabLines[n+1][i]
        aNote = tabLines[n+2][i]
        eNote = tabLines[n+3][i]
        if gNote.isdigit():
            string = tabLines[n][0]
            print(stringMap.map[gNote + string])
        elif dNote.isdigit():
            string = tabLines[n+1][0]
            print(stringMap.map[dNote + string])
        elif aNote.isdigit():
            string = tabLines[n+2][0]
            print(stringMap.map[aNote + string])
        elif eNote.isdigit():
            string = tabLines[n+3][0]
            print(stringMap.map[eNote + string])
