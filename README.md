# Letter Boxed Solver
A solver for the NYT game, Letter Boxed, in python.
## Description
[Letter Boxed](https://www.nytimes.com/puzzles/letter-boxed) is a daily word game from the New York Times. The goal is to create words out of the 12 given letters, which are arranged into the shape of a box with three letters on each side. The rules are as follows:
1. Letters from the same side may not be used consecutively.
2. The last letter of one word must also be the first letter of the next word.
The game ends when the player uses all twelve letters of the box to form words. The base game usually suggests that players solve the puzzle in 4-5 words, but there is always at least one solution that is only two words long.

This program provides the user with a list of two word solutions to a Letter Boxed puzzle. The user may choose to input their own puzzle or they may use a demo puzzle. User's puzzles should be inputted with the format *ABC-DEF-GHI-JKL* or *abc-def-ghi-jkl*. 

The basic algorithm of the program uses a trie to create a dictionary of words from the file words.txt, which I found from [this](https://boardgames.stackexchange.com/questions/38366/latest-collins-scrabble-words-list-in-text-file) stack exchange forum post. Then, we use a DFS to create a list of words that satisfy rule no. 1. Then we search through those words to find two word solutions that use all 12 letters at least once and that satisfy rule no. 2. 
## Future Work
This project might be improved in a number of ways. First, we could be more selective when choosing solutions and rule out solutions that add extra letters (like an "s" to the end of a word when it already contains an "s"). We could also give the user the option to search for solutions of a specified word length (i.e. three word or four word solutions). I also believe this program would work well as an application where the format of the original puzzle is maintained. Users could enter the letters into the sides of a box, and then the app could draw lines between the letters as it shows the solution, just like in the original game.
## Acknowledgements
The idea of using a trie data structure came from a [blog post](http://writeasync.net/?p=5622#comments) by Brian Rogers.
