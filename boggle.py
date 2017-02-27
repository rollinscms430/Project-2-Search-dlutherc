#Project 2 - Problem 3, Boggle
#David Costantino, AI Spring 2017

"""
    This program uses recursive search which aids in performance.  When it 
    checks through the prefix dictionary, it will back out of useless word
    sequences.  
"""



from copy import deepcopy

#creates dictionaries to hold words.txt and prefixes to enhance the search
d = {}
prefix_dict = {}

#create the boggle board
board = [['u','n', 't', 'h'] ,
         ['g', 'a', 'e', 's'],
         ['s', 'r', 't', 'r'],
         ['h', 'm', 'i', 'a']]


class State(object):
    
    """
        Represents the current state of the board
        
        Attributes:
        position: represents the position of the needed tile
        sequence: represents
        
    """
    
    def __init__(self, position, sequence):
        
        self.position = position
        self.sequence = sequence
        
        
    def add_position(self, position):
        
        new_position = deepcopy(self.position)
        new_position.append(position)
            
        new_sequence = deepcopy(self.sequence)
        new_sequence += board[position[0]][position[1]]
        
        return State(new_position, new_sequence)
        
        
    





#strip new line and set up initial dictionary 
def init_dict(file):
    f = open(file)
    for word in f:
        word = word.strip()
        d.setdefault(word, [])
        
        
#create a dictionary of prefixes to cross check potential words
#prefix_dict cuts off searches that have no chance of success, improving the search
def init_prefix(d):
    
    for word in d:
        prefix = "" #empty string to fill w/prefixes
        for i in range(len(word)):
            prefix += word[i]
            if prefix not in prefix_dict:
                prefix_dict[prefix] = True
                
#generate children of selected tile
def gen_children(state):
    
    current_position = state.position[len(state.position) - 1]#find last position to find neighbors
    
    #ensure the boundaries of the board are respected by the search
    for i in range(max(0, current_position[0] - 1), min(len(board) - 1, current_position[0] + 2)):#row
        for j in range(max(0, current_position[1] - 1), min(len(board[i]) - 1, current_position[1] + 2)):#column
            
            #add child to new_state and search the new_state recursively
            position = (i, j)
            if position != current_position:
                new_state = state.add_position(position)
            
                recursive_search(new_state)
        
    

#searches the word dictionary for words and prints them. 
#checks to prefix dictionary to eliminate unnecessary searching
def recursive_search(state):
    
    if state.sequence in d:
        print state.sequence
        
    if state.sequence in prefix_dict:
        gen_children(state)



def solve(board):
    
    #searches through the game board and finds the valid words
    for i in range(len(board)):
        for j in range(len(board[i])):
            
            init_position = [(i, j)]
            
            init_sequence = board[i][j]
            
            state = State(init_position, init_sequence)
            
            recursive_search(state)

    



if __name__ == '__main__':
    
    init_dict('words.txt')
    init_prefix(d)
    
    solve(board)
            
            