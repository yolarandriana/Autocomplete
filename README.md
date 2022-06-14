# Autocomplete

Yola Randrianantoanina
Department of Linguistics, Stony Brook University
LIN637: Computational Linguistics II
Dr. Jeffrey Heinz
May 20, 2022

Introduction 
The goal of this project was to make an autocomplete function for singleton words in Python. It would uses a prefix tree that incorporates statistics to determine the upcoming letter (e.g. if “#a” is 30% likely to be followed by “pple”, 70% likely to be followed by “ntidote”, then the function would predict “ntidote”). 

Background 
My main goal in choosing a final project was to create something that can be used by disabled people to make technology more accessible. When we think of accessibility in computational linguistics, I’ve noticed that we tend to think of accommodations for disabilities that directly affect language use, such as blindness and deafness. The value of accessibility for the blind and deaf is immeasurable, but other disabilities can have indirect effects which make use of language technology more difficult as well. For example, if someone experiences chronic pain in their arms or hands, long periods of typing could cause flare-ups of pain. An autocomplete tool can help them cut down on time spent typing and hopefully avoid painful flare-ups. 

Finding data
Going into my final project, I was hoping to use a highly phonetically consistent language such as Finnish or Serbo-Croatian so that this endeavor would be phonologically relevant (not just orthographically). However, this goal was compromised when I realized that finding sufficient data for these languages would be difficult. I then chose to use English because of the ample datasets available for that language. I found a dataset created by Thorsten Brants and Alex Franz which is aptly named Web 1T 5-gram Version 1 LDC2006T13. This dataset is a dictionary of English words along with unigrams, bigrams, trigrams, fourgrams, and fivegrams of the word combinations. This dataset also included the rate of incidence of that information, which was key to not only finding out the possible results of each word beginning but also calculating the likelihood of each outcome.

It should be noted that, by downloading (or in some cases, compiling) the appropriate dataset, this code can be applied to other languages very easily. 

The large size of this dataset means that the function is very slow. The vast majority of the runtime is spent inserting each English word into the Trie. Additonally, Python made mistakes computing the maximum among such large numbers (representing the rate of occurrence). For example, finding that 999999 is greater than 1111111. So, I split the words into dictionaries based on the number of digits in their corresponding numbers to make the max() function accurate. Then I used loops to iterate through each dictionary and insert the words into the Trie such that words with the highest rate of occurrence were added first. 

Trie object
The first part of my code worked to create a class Trie object. This is Python’s translation of a prefix tree using nested dictionaries containing singleton letters and one number (to indicate the rate of incidence of that word). Then I created a function called search() which scans the prefix tree for a given string and returns True if the string can be found in a word in the dictionary. 

startstop()
After creating search(), I created a function called startstop() which adds start and end markers to its input. For example, startstop(“apple”) will return “$apple&”). This is used when adding words to the dictionary. I did this so that the program has a clear indication of the start and end of words and does not suggest something like “pineapple” when the user inputs “ap.” 

auto()
This function takes a tree and the user’s input and identifies the corresponding dictionaries (within the large nested dictionary of all words) that contain words the user could have been starting to write, known as “curry.” Curry is formed by continually redefining itself to include each letter of the prefix inputted. For example, if the user inputs “app,” curry first equals current[‘$’] (because ‘$’ is added to the beginning of each dictionary entry and current is equal to the tree.child). It then equals current[‘$][‘a’], then current[‘$][‘a’][‘p’], and so on. 

words()
The main crux of this project is the words() function. This function performs a depth first search to parse through the nested dictionary in the way it is meant to be read. It appends the values it finds to a list, “preds” and continues when it finds the end marker, “&.” 

main()
The main function asks the user to input the first letter of a word and creates a list of strings by splitting the tokens by the “ “ space symbol. It uses a for loop to iterate through each token and apply the auto() function to each one. If the string does not exist as the beginning of any words in the dictionary, like “lkjtnhsjbd” for example, then the program will print out nothing. If it does exist as a prefix in English, main() will tell the user the remaining letters of the top five most likely words that they were beginning to write. It does this by iterating through the list returned by words() and deleting unsightly non-letter characters and delineating word boundaries with the tab symbol.


Possible Improvements
Ideally, I would like the program to continually assess the input as it’s being typed (so never “entered”) like it does on Apple products. I tried using curses, pygame, sys, tty, getch, and blessed to do try to put my terminal into cbreak or raw mode. However, none of these processes worked and were irrelevant to the scope of this class, so I unfortunately decided to simply have the user press “Enter” to submit their input. If I had access to Windows, I would try using msvcrt but I only had access to a Macbook. I spent a great chunk of time and energy on this particular problem that I wish I had spent on other aspects of the program. 

Additionally, encoding a part-of-speech tagger and some phrase structure rules would make the assessment more accurate because then it would take context and grammaticality into account. However, this could make the process of converting the code to work for a non English language more cumbersome and arduous. However, I believe this tradeoff would be worth it for the improved accuracy. 

Finally, taking capitalization into account would make this code more professional. I would do this by triggering capitalization with periods or preserving the capitalization inputted by the user. A part-of-speech tagger that recognizes proper nouns could also be used for this purpose. 
