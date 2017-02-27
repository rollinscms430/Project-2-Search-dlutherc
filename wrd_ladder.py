#Project 2 - Problem 2, Word Ladder
#David Costantino, AI Spring 2017

"""
    I used breadth first search to prevent wasting search time looking through
    states that were not going to lead to the goal state.  This will find the 
    first correct ladder the quickest.    
    
    I noticed a pattern in the correct selection of words.  As the search gets 
    closer to the goal state, the successive words begin to resemble the goal state.
    There are many children for 'dog' for example.  Only one word, 'cog', resembles
    the goal 'cat'.  A function that picks the word closest to the goal, would
    would prevent the program from unnecessarily searching the other 12 terms
    and speed the output of the solution. (I'm still working on that algorithm)

"""
from copy import deepcopy

#queue to hold the nodes to be checked
queue = []

#dictionary for words.txt and previously visited states, respectively
d = {}
visited = {}

#goal state of the search
goal = 'brains'

class State(object):
    
    
    """Represents the state of the ladder
    
       Attributes:  
        ladder:  represents the current list of moves
    """
    
    def __init__(self, ladder):
        self.ladder = ladder
        
        
        
    def add_word(self, word):
        new_ladder = deepcopy(self.ladder)
        new_ladder.append(word)
        
        return State(new_ladder)
        

#strip new line and set up initial dictionary  - goes in search()
def init_dict(file):
    f = open(file)
    for word in f:
        word = word.strip()
        d.setdefault(word, [])


#check for to see if we're done
def found_goal(state):   
    if state.ladder[len(state.ladder) - 1 ] == goal:
        return True
    
    return False


#Find the children of the current state
def expand_node(state):
    start = state.ladder[len(state.ladder) - 1]#returns last word in the ladder object
    
    #compare the current state with the rest of the word
    #to find adjacencies
    for word in d:
        if word != start:
            if len(word) == len(start):
                for i in range(len(start)):#start=node
                    slice_word = start[:i] + start[i+1:]#slice the start word
                    slice_cn = word[:i] + word[i+1:] #possibly the next wrung in the ladder
                    
                    #check if the child state has been visited already
                    #if not, update new state and visited with that child
                    if slice_word == slice_cn:
                        if word not in visited:
                            visited[word] = 1
                            new_state = state.add_word(word)
                            queue.append(new_state)
            
def solve(word):
    
    #initialize settings
    ladder = [word]
    init_state = State(ladder)
    queue.append(init_state)
    
    
    #search while states are in the queue
    while len(queue) > 0:
        
        current_state = queue.pop(0)
        
        #check if done
        if found_goal(current_state):
            print current_state.ladder
        
        #check the next state in the queue
        expand_node(current_state)
        
        
        
if __name__ == '__main__':
    
    init_dict('words.txt')
    solve('snakes')
        
    
        