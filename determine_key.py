import os
from mappings import Maps
from read_tabs import get_notes, note_frequency

# read tab lines
root = os.path.dirname(os.path.abspath(__file__))
path = "{}/tablature/hysteria.txt".format(root)
with open(path, 'r') as tabText:
    tabLines = tabText.readlines()
tabLines = [t.strip() for t in tabLines if t.strip() != '']

notesArr = []
freqDict = {}
allNotes = get_notes(notesArr, tabLines, 4)
noteFreq = note_frequency(allNotes, freqDict)


# find key of tab by summing note frequencies and scoring each key
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
print(keyOfTab)
