# Grade

## Anagrams

Good. It would be nice to remove single word lists from the output.

## Word Ladders

Good. It's a little slow, probably because it loops through the entire dictionary to expand a node, looking for all of the words
that are one letter away from the current word. This works, but it would be faster to just generate all of the words that are one
letter away (this would require 26 * the number of letters in the word operations) and keep only the ones that are in the dictionary.

## Boggle

Nice! Very good, clean solution. Separating the search code from the node expansion is a ncie way of organizing things.

## Total

100 / 100
