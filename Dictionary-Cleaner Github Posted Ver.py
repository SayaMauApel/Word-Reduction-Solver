file_path = r"" #Add your file path here to your dictionary file. I used the 2of12inf.txt file from the original project, but you can use any text file with words in it. Just make sure to update the file path accordingly.

with open(file_path) as seat:
    reader = [w.strip() for w in seat.read().split()]

Dictionary = {
    w.replace("/", " ").replace("%", " ")
    for w in reader
    if w.isascii()
}

output_path = r"" #Add your output file path here. This will be where the cleaned dictionary is saved.

with open(output_path, "w") as out: #This loop will overwrite any file placed in the output path, so be careful when choosing the output file path.
    for word in Dictionary:
        out.write(word + "\n")
