Word Reduction Solver is a python script that filters text, metadata along with any English terms and searches for what I like to call reducible words.

What is a reducible word? Well it's a word that if you take out any single letter it remains a valid word e.g seat turns into eat, sat, sea, set. because all of these words are valid English words we place seat in a special file titled File to maintain a list of all 
reducible words that we've found.

Where are we getting our source material? well originally we used open source online dictionaries we scoured over 80,000 verifiable words and here were the results: ash, peat, may, bye, spay, seat, coops, shoot, pear.  See just how little that is? Me and Obsan the 
creators of this project believe that to be a little bad luck and far to small of a source material. Because of this we switched over to a far more difficult source material https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2
this comes from a wiki dump like this https://dumps.wikimedia.org/ these contain millions of words and let us find hundreds of thousands of reducible words.

How does the program work? To save you the technical explanation I'll simplify slightly. The program works by looking at the current dictionary taking the first word splitting it into it's components. looking at the seat example again seat would become 
eat, sat, set, sea. we then check to see if all of the words eat, sat, set, sea are in the dictionary somewhere else if yes then seat is considered a reducible word if not we move onto the next word we do this until we've checked every word.

What have we accomplished so far? To our knowledge as of 8/28/2026 there isn't any projects doing what we've done on a scale above 10,000 words. for reference we (Me and Obsan) have discovered over 580,000 reducible words and searched an estimated 6 million words. 
To put that into perspective our 100% verifiable words come from our old dictionary of 80,000 this dictionary has a 0.01125% chance of any random word you pull from it being reducible by our program. Our newer one on the other hand boasts odds as high as 9.67%.
it does this by using English words that are translations from other languages words, using old terminology and mostly forgotten words this version uses a significant portion of all English words to achieve this success rate.

As for how to run the program To be continued. For now please visit https://github.com/SayaMauApel/Word-Reduction-Solver/tree/Legacy-Main-80k-wordlist?tab=readme-ov-file our legacy version utilizing 80,000 words if you'd like to see immediate results.


















This is a python script it's purpose is to filter anything from words, logos, xml data any text at all really in English. Specifically what where filtering for is words within words take the word seat for instance. If we split the word seat into every variant of the word
minus one letter it turns into: Eat, Sat, Set, Sea. Because no matter which letter you remove from the word it remains a word our program will filter for it and document them. This is a phenomenon without a name though I call them reducible words as the name suggests it
means words that can have any letter removed and remain a valid word. This is likely rarer then you think. Using SCOWL a large dictionary comprised of English words that can be found here: https://github.com/engramtech/scowl checking over 80,000 unique words I was only
able to find an abysmal 9 reducible words. This version of the program can be found in a branch titled legacy-main. Not willing to give up I gathered a friend to create what you see now. In this updated version containing brand names, old English words and much more we 
were able to extrapolate over 580,000 reducible words by scanning the entirety of a Wiktionary dump containing millions and millions of words. We call this project the word reduction solver and the results speak for themselves.
