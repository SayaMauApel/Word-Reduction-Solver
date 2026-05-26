Seat = r""  #Add your file path here to your dictionary file. I used the 2of12inf.txt file from the original project, but you can use any text file with words in it. Just make sure to update the file path accordingly.

with open(Seat) as seat:
    Reader = [w.strip() for w in seat.read().split()]

Dictionary = set(Reader) 

for Current_Word in Dictionary: #Loop that iterates through the dictionary and checks if the word can be reduced by one letter and still be in the dictionary.
    Placeholder1 = True
    for i in range(len(Current_Word)):  #Goes over each index position in the current word.
        reduced = Current_Word[:i] + Current_Word[i+1:] #Loop that iterates through the letters of the current word and creates a new word with one letter removed.
        if reduced not in Dictionary:
            Placeholder1 = False
            break

    if Placeholder1 == True:
        print(Current_Word)
