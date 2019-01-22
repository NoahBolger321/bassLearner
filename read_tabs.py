import os
from mappings import Maps

# read tab lines
root = os.path.dirname(os.path.abspath(__file__))


def read_lines(rootPath, fileName):
    path = "{}/tablature/{}".format(rootPath, fileName)
    with open(path, 'r') as tabText:
        tabLines = tabText.readlines()
    tabLines = [t.strip() for t in tabLines if t.strip() != '']
    return tabLines


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
                elif note in Maps.commonChars:
                    try:
                        surrNotes = (Maps.stringMap[tabLines[n+j][i-1] + string], Maps.stringMap[tabLines[n+j][i+1] + string])
                        nuances.setdefault(note, []).append(surrNotes)
                    except KeyError:
                        continue
    return {'notes': notes, 'nuances': nuances}


def note_frequency(listNotes, frequencies):
    for note in list(set(listNotes)):
        frequencies[note] = listNotes.count(note)
    return frequencies
