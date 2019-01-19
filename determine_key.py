import os
from mappings import Maps
from read_tabs import get_notes, note_frequency
from intervals import find_intervals

# read tab lines
root = os.path.dirname(os.path.abspath(__file__))
path = "{}/tablature/hysteria.txt".format(root)
with open(path, 'r') as tabText:
    tabLines = tabText.readlines()
tabLines = [t.strip() for t in tabLines if t.strip() != '']

notesArr = []
nuancesDict = {}
freqDict = {}
notesRetrieved = get_notes(notesArr, nuancesDict, tabLines, 4)
allNotes = notesRetrieved['notes']
nuances = notesRetrieved['nuances']
noteFreq = note_frequency(allNotes, freqDict)


# find key of tab by summing note frequencies and scoring each key
# TODO: determine whether key is major or minor depending on most common intervals
def find_key(counts, allKeys):
    scoredKeys = {}
    for key, notes in allKeys.items():
        score = 0
        for note, count in counts.items():
            if note in notes:
                score += count
        scoredKeys[key] = score
    return dict(sorted(scoredKeys.items(), key=lambda x: x[1], reverse=True))


# TODO: determine key by score, explore defining characteristics to strengthen determination
keyOfTab = find_key(noteFreq, Maps.keyMap)
# get intervals by passing in all notes and the most likely key
intervals = find_intervals(allNotes, list(keyOfTab.keys())[0])
print(keyOfTab)
print(intervals)
print(nuances)
