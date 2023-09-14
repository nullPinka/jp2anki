import os

def add_word(word, filename="def_anki_deck.txt"):
    front, back = word
    write_mode = 'x+t'
    if os.path.isfile(filename):
        write_mode = 'a+t'

    # word;pos;misc;gloss;info
    with open(filename, mode=write_mode, encoding="utf-8") as deck:
        if write_mode == 'x+t':
            deck.write("word;pos;misc;gloss;info")
        if write_mode == 'a+t':
            words = deck.readlines()
            for row in words:
                if row.find(word) != -1:
                    print(front + " already exists in deck.")
                    return

        deck.write("\"" + front + "\";\"" + back["pos"] +"\";\"" + back["misc"] + "\";\"" + back["gloss"] + "\";\"" + back["info"] + "\"")

