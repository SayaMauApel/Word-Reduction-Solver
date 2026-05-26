 Word-Reduction-Solver
To understand the Word Reduction Solver you must first understand the principle behind it. The goal of this program is to find a word that if you remove any letter it remains a word example:
"seat" a random word pulled from a massive dictionary turns into "eat" "sat" "set" "sea" the program then checks these outputted words to see if there part of the dictionary aswell. If they are all apart of the dictionary it will print the information to console if even one word fails this check it will not print. The word that gets printed in this example will be "seat" not the following words as those e.g "eat" turn into "at" "et" "ea". as only one of those words counts as a valid word "eat" will not be printed. 

As you can see accuracy largely depends on dictionary size unfortunately my program as of 27/05/2026 isn't made to support multiple txt files at once that is something that will come at a later date. You may also recongise that the word file I've provided is from SCOWL. This is normally used for spell checkers and has things like "/" and other characters that would otherwise break my program entirely. So I made a seperate program I'll include in this repo titled "Clean-Dictionary". This script cleans the file of unicode characters, "/" and anything else that might cause issue it's also extremely easy to update if needed. It's advised to run the cleaner program before you run the Word Reduction Solver to lower the chance of running into any avoidable errors this only has to be done once to a file.






