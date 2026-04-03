# we have to first create a TrieNode that has a hashmap and a boolean to indicate if it's the end of the word or not

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # the current pointer starts at the root
        # check for every character in the word if it is in the children hashmpa
        # if it's not there, then we make a Trie node with the charcter being the key, and the empty Trie node being the value
        # else if it's there, we just update our current pointer to be wehre our character key is
        # and then set the end of the word to be true but out of the loop
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endofword = True



    def search(self, word: str) -> bool:
        # here we also start our current pointer to the root
        # and check again for chatacter in word
        # check if that charcater is in our children, if not, we return false
        # if it's there, we set our current to the character key in our children
        # then at the end of it all we return where our current pointer will be but return what's at the endword
        curr = self.root

        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.endofword


        
    def startsWith(self, prefix: str) -> bool:
        # again start our current at the root
        # go for character in the prefix
        # we search if the character is in the children, if not, we return false
        # if it's there, we shift the current pointer to where the character is in the dict and we keep on doing that in the for loop
        # and at the end of it all, we return True
        curr = self.root

        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return True

        
        