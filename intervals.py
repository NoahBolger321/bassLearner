from mappings import Maps


def find_intervals(tabNotes, key):
    intervals = []
    intervalCounts = {}
    keyNotes = Maps.keyMap[key]
    for i in range(len(tabNotes)):
        # TODO: avoid index error
        try:
            if tabNotes[i] in keyNotes and tabNotes[i+1] in keyNotes:
                firstNote = keyNotes.index(tabNotes[i])
                secondNote = keyNotes.index(tabNotes[i+1])
                # store the numeric separation between the notes and add one to get interval number
                intervals.append(abs(secondNote - firstNote) + 1)
        except IndexError:
            print("Finished")
    # TODO: better loop variable name
    for i in intervals:
        if str(i) not in intervalCounts:
            intervalCounts[str(i)] = intervals.count(i)
    return dict(sorted(intervalCounts.items(), key = lambda x: x[1], reverse=True))
