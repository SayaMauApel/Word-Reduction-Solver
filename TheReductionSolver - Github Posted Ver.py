import os
Seat = r"C:\Users\User\source\repos\WordReductionSolver\WordReductionSolver\2of12inf.txt"

def merge_files(folder, output_path): #Function that merges all text files in a folder into one text file.
    merged = []

    for filename in os.listdir(folder): #Iterates through all files in the specified folder and checks if they are text files. If they are, it reads their contents and appends them to a list.
        if filename.endswith(".txt"):
            with open(os.path.join(folder, filename), "r") as f:
                merged.append(f.read())

    with open(output_path, "w") as out: 
        out.write("\n".join(merged))

        merge_files(r"C:\Users\User\source\repos\WordReductionSolver\WordReductionSolver\MergedTxtFiles", "merged_output.txt") #Calls the merge_files function and specifies the folder containing the text files to be merged and the output path for the merged file.

with open(Seat) as seat:
    Reader = [w.strip() for w in seat.read().split()]

Dictionary = set(Reader) 
Counter = 0
for words in Dictionary:
    Counter += 1
print(Counter) #Prints the number of words in the dictionary to the console. 

for Current_Word in Dictionary: #Loop that iterates through the dictionary and checks if the word can be reduced by one letter and still be in the dictionary.
    Active = True
    for i in range(len(Current_Word)):  #Goes over each index position in the current word.
        reduced = Current_Word[:i] + Current_Word[i+1:] #Loop that iterates through the letters of the current word and creates a new word with one letter removed.
        if reduced not in Dictionary:
            Active = False
            break

    if Active == True:
        open("reducible_words.txt", "a").write(Current_Word + "\n" )  #Writes the current word to a new file if it can be reduced by one letter and still be in the dictionary.
        
        
        
        
        #print(Current_Word) prints finished word to console comeback to later...
