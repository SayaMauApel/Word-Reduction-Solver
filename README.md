 Word-Reduction-Solver
To understand the Word Reduction Solver you must first understand the principle behind it. The goal of this program is to find a word that if you remove any letter it remains a word example:
"seat" a random word pulled from a massive dictionary turns into "eat" "sat" "set" "sea" the program then checks these outputted words to see if there part of the dictionary aswell. If they are all apart of the dictionary it will print the information to console if even one word fails this check it will not print. The word that gets printed in this example will be "seat" not the following words as those e.g "eat" turn into "at" "et" "ea". as only one of those words counts as a valid word "eat" will not be printed. 

As you can see accuracy largely depends on dictionary size unfortunately my program as of 27/05/2026 isn't made to support multiple txt files at once that is something that will come at a later date. You may also recongise that the word file I've provided is from SCOWL. This is normally used for spell checkers and has things like "/" and other characters that would otherwise break my program entirely. So I made a seperate program I'll include in this repo titled "Clean-Dictionary". This script cleans the file of unicode characters, "/" and anything else that might cause issue it's also extremely easy to update if needed. It's advised to run the cleaner program before you run the Word Reduction Solver to lower the chance of running into any avoidable errors this only has to be done once to a file.

Results: 
ash
peat
may
bye
spay
seat
coops
shoot
pear

The longest word(s) so far discovered with my program are "shoot and coops" 5 letter words. This is out of an 80,000 letter wordlist meaning there is (approximately) a 0.01125% chance any particular word contains
what I am looking for. I currently aspire to find a 7 letter word if such a thing even exists fitting my criteria that is my goal for this project.

If you have any questions regarding the program or would like to contact me I accept all inquiries at magic.devmail@gmail.com

Copyright 2000-2026 by Kevin Atkinson

Permission to use, copy, modify, distribute, and sell any part of the English
Speller Database (ESDB, previously known as SCOWLv2), or word lists
created from it, is hereby granted without fee, provided that the above
copyright notice appears in all copies and that both the above copyright
notice and this notice appear in supporting documentation.  Kevin Atkinson
makes no representations about the suitability of this database for any
purpose.  It is provided "as is" without express or implied warranty.

ESDB is derived from many sources, most of which are in the Public Domain.
Data from the Corpus of Contemporary American English (COCA) was also used.

All data from COCA comes from 3-gram data that is not freely available;
however, the usage is within the rights given by the NDA that was signed when
purchasing the data.  More information on COCA is available at
https://www.english-corpora.org/coca/.

The primary source of words for ESDB comes from 12dicts and ENABLE2K.  Both
are in the Public Domain, but Alan Beale <biljir@pobox.com> deserves special
credit as he is the author of 12dicts and a major contributor to ENABLE2K.  In
addition, he gave me an incredible amount of feedback and created a number of
special lists in order to help improve the overall quality of ESDB.

===




