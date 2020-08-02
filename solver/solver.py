from .apps import SolverConfig
from .trie import TrieNode

directions = [
    (1,0),
    (0,1),
    (-1,0),
    (0,-1),
    (1,-1),
    (-1,-1),
    (-1,1),
    (1,1)
]

class solveWordHunt():
    def __init__(self, letters, size):
        self.board = []
        self.size = size
        temp = []
        
        for i, v in enumerate(letters):
            temp.append(v)
            if((i+1)%size == 0):
                self.board.append(temp)
                temp = []

        self.visited = [
            [False for i in range(size)] for j in range(size)
        ]

        self.ans = []

        for i in range(size):
            for j in range(size):
                self.recurse(i, j, "", "", self.visited, SolverConfig.dictionaryTrie)
        
        def sortAns(e):
            return len(e[0])
        
        self.ans.sort(key=sortAns, reverse=True)

        for row in self.ans:
            row[1] = row[1].split()

    def recurse(self, row, col, word, path, visited, currNode):
        if row < 0 or row >= self.size or col < 0 or col >= self.size:
            return
        if visited[row][col]:
            return
        
        letter = self.board[row][col]
        
        if not letter in currNode.children:
            return
        word += letter
        visited[row][col] = True

        if len(word) > 3 and currNode.children[letter].word_finished:
            self.ans.append([word, path+" "+str(row*self.size+col)])
        
        for dir in directions:
            x = dir[0]
            y = dir[1]
            if row+x >=0 and row+x < self.size and col+y >= 0 and col+y < self.size:
                if not visited[row+x][col+y]:
                    self.recurse(row+x, col+y, word, path+" "+str(row*self.size+col), visited, currNode.children[letter])

        visited[row][col] = False


if __name__=="__main__":
    solveWordHunt("asdfasdfasdfasdf", 4)