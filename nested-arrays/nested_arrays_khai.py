import random

class Game:
    
    def __init__(self, rows, cols):
        '''
        Creates a game board with given number of rows and columns.
        This will be held in the form of a nested list. Initial values will be
        assigned Randomly.
        
        The top most row will be numbered 0
        '''
        
        self.board = []
        
        for row in range(rows):
            # create the inner array by using a list comphrehension. This is
            # faster and neater than appending to a list. We could have created
            # the whole thing with a 1 line nested list cophrehension; that
            # would not be very readable. So we mix the best of both worlds.
            self.board.append([random.randint(0,50) for _ in range(cols)])
            
            
    def printBoard(self):
        '''
        Prints the board. 
        The requirement states that each row should be sorrounded by square 
        brackets, which is exactly what we get when a list is passed to the
        print function
        '''
        for row in self.board:
            print(row)
            

    def getCol(self, col):
        '''
        Returns the column starting from the left. The left most column is number 0
        '''
        
        # list comprehension is the neatest and fastest way agin. The following is
        # equivalent to
        #   col = []
        #   for row in self.board:
        #       col.append(row[col])
        #   return col
        
        return [row[col] for row in self.board]
        
    def getRow(self, row):
        '''
        Returns the row starting from the top (which has number 0)
        '''
        
        return self.board[row]
     
    def getCoords(self, number):
        '''
        If the given number exists in the board, we return it's coordinates
        when multiple occurances are seen only the first one is returned. When
        the number does not occur false is returned
        '''
        for row in self.board:
            for col in row:
                if col == number:
                    # in python we can return more than one value. Such a
                    # return is automatically converted into a list.
                    return row, col 
    
        return False
    
    def getSurround(self, row, col):
        '''
        We will assume that the order is North, North East, East, South,
        South West, West, North West, North
        '''
        
        ret = []
        
        # now we try all possible combinations of row +- 1, col +- 1
        # in order. These corresponds to the 8 main points on the compass.
        if row > 0:
            ret.append(self.board[row - 1][col]) # north
            
        if row > 0 and col < len(self.board[0]) - 1:
            ret.append(self.board[row - 1][col + 1]) # north east
            
        if col < len(self.board[0]) - 1:
            ret.append(self.board[row][col + 1]) # east east
            
        if row < len(self.board) - 1 and col < len(self.board[0]) + 1 :
            ret.append(self.board[row + 1][col + 1]) # south east
            
        if row < len(self.board) - 1:
            ret.append(self.board[row + 1][col]) # south
            
        if row < len(self.board) - 1 and col > 0:
            ret.append(self.board[row + 1][col - 1]) # south west
            
        if col > 0:
            ret.append(self.board[row][col - 1]) # west
            
        if row > 0 and col > 0:
            ret.append(self.board[row - 1][col - 1]) # North west

        
        
        return ret

            
            
        
g = Game(4,4)
g.printBoard()
print("Get Col 1", g.getCol(1))
print("Get Row 1", g.getRow(1))
print("Get coords 10", g.getCoords(10))
print("get surround 1, 1", g.getSurround(1,1))
print("get surround 0, 0", g.getSurround(0,0))
print("get surround 3, 3", g.getSurround(3,3))
        
