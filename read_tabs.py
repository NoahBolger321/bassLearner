import os
from mappings import Maps

# read tab lines
root = os.path.dirname(os.path.abspath(__file__))
path = "{}/tablature/bitesDust.txt".format(root)
with open(path, 'r') as tabText:
    tabLines = tabText.readlines()
tabLines = [t.strip() for t in tabLines if t.strip() != '']


# loop through each grouping of strings, retrieve notes, print mapped note if fret recorded (dynamic # of strings)
def get_notes(notes, nuances, tabLines, num_strings):
    for n in range(0, len(tabLines), num_strings):
        for i in range(1, len(tabLines[n])):
            for j in range(0, num_strings):
                note = tabLines[n+j][i]
                string = tabLines[n+j][0]
                if note.isdigit():
                    notes.append(Maps.stringMap[note + string])
                # check for special characters and map surrounding notes in list of tuples
                # TODO: determine how to store surrounding notes
                elif note in Maps.commonChars:
                    nuances.setdefault(note, []).append((tabLines[n+j][i-1], tabLines[n+j][i+1]))
    return {'notes': notes, 'nuances': nuances}


def note_frequency(listNotes, frequencies):
    for note in list(set(listNotes)):
        frequencies[note] = listNotes.count(note)
    return frequencies
