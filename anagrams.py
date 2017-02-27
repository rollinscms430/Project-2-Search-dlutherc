#Project 2 - Problem 1, Anagrams
#David Costantino, AI Spring 2017


#create the dictionary
d = {}

#open words.txt
file = open('words.txt')

#run through 'file', strip out the \n character, and sort each word string alphabetically
for word in file: 
    word = word.strip()
    sorted_word = "".join(sorted(word)) #is this the most sophistcated way to do this?
    
    #add sorted_word/word as a key/pair list if not already in the dictionary
    if sorted_word not in d:
        d.setdefault(sorted_word, [word])
    #if sorted_word is already a key, append to its value
    else:
        d[sorted_word].append(word)


#if a key has more than 1 value, it is an anagram and should be printed
for key in d:
    if len(d[key]) > 1:
        print d[key]
    
    
    
    

    
    

    
    