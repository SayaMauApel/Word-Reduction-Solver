import random

Seat = r"word.txt" # you just use the word.txt file the one you used listWord to fetch the word and you use that word with this logic

NUMBER_TO_SAVE = 20 # amount of reducible word you want to save into the plausible.txt

with open(Seat, encoding="utf-8") as seat:
    dictionary = set(
        w.strip().lower()
        for w in seat.read().split()
    )

def is_reducible(word, dictionary):
    if len(word) != 7:
        return False

    for i in range(len(word)):
        candidate = word[:i] + word[i + 1:]

        if candidate not in dictionary:
            return False

    return True

reducible_words = [
    word for word in dictionary
    if is_reducible(word, dictionary)
]

if reducible_words:

    random.shuffle(reducible_words)

    selected_words = reducible_words[:NUMBER_TO_SAVE]

    with open("plausible.txt", "w", encoding="utf-8") as out_file:
        for word in selected_words:
            out_file.write(word + "\n")
    print(f"██████████████████████████████████████████████████████████████")
    print(f"We found {len(reducible_words)} possible reducible words.") # this is possible reducible not 100% gureenty
    print(f"Saved {len(selected_words)} words to plausible.txt")
    print(f"██████████████████████████████████████████████████████████████")
    print("\nPossible reducibles:")
    for i, word in enumerate(selected_words, 1):
        print(f"{i}: {word}")

else:

    with open("plausible.txt", "w", encoding="utf-8"):
        pass

    print("There is no possible reducible in this file.")