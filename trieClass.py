#LastName: Arnot
#FirstName: Bradley
#Email: bradarnot@gmail.com
#Comments: 

from __future__ import print_function
import sys

class MyTrieNode:
    # Initialize some fields 
  
    def __init__(self, isRootNode):
        self.isRoot = isRootNode
        self.isWordEnd = False # is this node a word ending node
        self.count = 0 # frequency count
        self.next = {} # Dictionary mappng each character from a-z to the child node


    # Adds Word w to the Trie
    def addWord(self,w):
        assert(len(w) > 0)
        current = self
        for i in range(0, len(w)):
            success = False
            for key in current.next:
                if key == w[i]:
                    success = True
                    next = current.next[key]

            if success:
                current = next
            else:
                newNode = MyTrieNode(False)
                newNode.isWordEnd = False
                current.next[w[i]] = newNode
                current = current.next[w[i]]
        current.count += 1
        current.isWordEnd = True
        
        return

    def lookupWord(self,w):
        # Return frequency of occurrence of the word w in the trie
        # returns a number for the frequency and 0 if the word w does not occur.
        current = self
        for i in range(0,len(w)):
            success = False
            for key in current.next:
                if key == w[i]:
                    success = True
                    next = current.next[key]
            if success:
                current = next
            else:
                return 0
        
        return current.count
    
    def printTrie(self):
        if self.isRoot:
            print()
            print("TRIE_________________________________________________")
        for key in self.next:
            print("Node value: " + key + " " + str(self.next[key]))
            self.next[key].printTrie()
        if self.isRoot:
            print("END TRIE_____________________________________________")
            print()


    def __str__(self):
        return str("Trie Node " + ("Not the root " if self.isRoot else "Not root ") + ("is word end " if self.isWordEnd else "is not word end ") + ("there are " + str(self.count) + " occurrences ") + ("children include [" + "".join((str(key2) +  " ")for key2 in self.next) + "]"))

    # Depth First Seach
    def dfs(self):
        words = []
        for key in self.next:
            if self.next[key].isWordEnd:
                newWord = (key, self.next[key].count)
                words.append(newWord)
            prevWords = self.next[key].dfs()
            for i in range(0, len(prevWords)):
                prevWords[i] = (key + prevWords[i][0], prevWords[i][1])
            words.extend(prevWords)
        return words

    def autoComplete(self,w):
        #Returns possible list of autocompletions of the word w
        #Returns a list of pairs (s,j) denoting that
        #         word s occurs with frequency j

        current = self
        for i in range(0,len(w)):
            success = False
            for key in current.next:
                if key == w[i]:
                    success = True
                    next = current.next[key]
            if success:
                current = next
            else:
                return []

        # Search for all words after prefix
        words = current.dfs()
        for i in range(0, len(words)):
                words[i] = (w + words[i][0], words[i][1])

        if current.isWordEnd:
            words.append((w, current.count))

        return words
    
    
            
# Simple test program
if (__name__ == '__main__'):
    t= MyTrieNode(True)
    lst1=['test','testament','testing','ping','pin','pink','pine','pint','testing','pinetree','hello','he']

    for w in lst1:
        t.addWord(w)

    j = t.lookupWord('testy') # should return 0
    print("This number should be 0 :: ", j)
    j2 = t.lookupWord('telltale') # should return 0
    print("This number should be 0 :: ", j2)
    j3 = t.lookupWord ('testing') # should return 2
    print("This number should be 2 :: ", j3)

    #t.printTrie()

    lst3 = t.autoComplete('pi')

    print('Completions for \"pi\" are : ')
    print(lst3)
    
    lst4 = t.autoComplete('tes')
    print('Completions for \"tes\" are : ')
    print(lst4)

    lst5 = t.autoComplete('he')
    print('Completions for \"he\" are : ')
    print(lst5)

 
    
    
     
