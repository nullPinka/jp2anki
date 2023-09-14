import io
import nagisa
from jamdict import Jamdict
import sys
import word2anki

jam = Jamdict()

sentence = input("Input here: ")
sentence = "これはテスト"

matching = []

# Segments sentence into words. Wataki returns a list of words, each word is a string of the word
# Can have this return part of speech things too. Look into that for narrowing down entries
# Parts of speech are not translated...
for word in nagisa.wakati(sentence):
    # search up the word using jamdict
    # jam.lookup(word) returns a list of entries, sort through each of those
    for entry in jam.lookup(word).entries:
        # Validate that an entry exactly matches what has been looked up, then adds it to matching array
        for i in range(0, len(entry.to_dict()["kana"])):
            if word == entry.to_dict()["kana"][i]["text"]:
                matching.append((entry.to_dict()["kana"][i]['text'], entry.to_dict()['senses']))

for dic in matching:
    # word + result of 'sense'
    # main definitions stored in SenseGloss and SenseInfo
    # part of speech in pos
    word, meaning = dic

    # word2anki format is (word (JP) : str, {"pos" : "", "misc" : "", "gloss" : "", "info" : ""})

    front, back = (word, {"pos": "", "misc" : "", "gloss": "", "info" : ""})
    for defin in meaning:
        for pos in defin["pos"]:
            if pos not in back["pos"]:
                back["pos"] += pos + " "
                back["pos"] += ";;"

        if "misc" in defin:
            for misc in defin["misc"]:
                back["misc"] += misc + " "
            back["misc"] += ";;"

        if "SenseGloss" in defin:
            for gloss in defin["SenseGloss"]:
                back["gloss"] += gloss["text"] + " "
            back["gloss"] += ";;"
        
        if "SenseInfo" in defin:
            for info in defin["SenseInfo"]:
                back["info"] += info
            back["info"] += ";;"

    print((front, back))
