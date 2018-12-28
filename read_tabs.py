import os
from string_map import stringMap
from collections import Counter

# read tab lines
root = os.path.dirname(os.path.abspath(__file__))
path = "{}/tablature/bitesDust.txt".format(root)
with open(path, 'r') as tabText:
    tabLines = tabText.readlines()
tabLines = [t.strip() for t in tabLines if t.strip() != '']


# loop through each grouping of strings, retrieve notes, print mapped note if fret recorded (dynamic # of strings)
def get_notes(notes, num_strings):
    for n in range(0, len(tabLines), num_strings):
        for i in range(1, len(tabLines[n])):
            for j in range(0, num_strings):
                note = tabLines[n+j][i]
                string = tabLines[n+j][0]
                if note.isdigit():
                    notes.append(stringMap.map[note + string])
    return notes


def note_frequency(listNotes, frequencies):
    for note in list(set(listNotes)):
        frequencies[note] = listNotes.count(note)
    return frequencies


# storage for all notes, and frequencies of notes
notesArr = []
freqDict = {}
allNotes = get_notes(notesArr, 4)
noteFreq = note_frequency(allNotes, freqDict)
print(dict(sorted(noteFreq.items(), key=lambda x: x[1], reverse=True)))
