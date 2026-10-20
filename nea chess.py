import time

BOARD_SIZE = 8 # constant which shows the size of the grid.

class Piece:
    def __init__(self, colour, row, column):
        self.colour = colour
        self.row = row
        self.column = column

    def get_position(self): # checks the position of the piece on the board.
        return self.row, self.column 
    
    def set_position(self, newrow, newcolumn): # sets the position of the piece on the corresponding tile based on newrow and newcolumn.
        self.row = newrow
        self.column = newcolumn

class Pawn(Piece):
    def __init__(self, colour, row, column):
        super().__init__(colour,row,column)

        if colour == 'white':
            self.icon = '♟'
            self.direction = -1
        else:
            self.icon = '♙'
            self.direction = 1

    def legalmove(self, newrow, newcolumn, grid):

        differencerow = self.row - newrow
        differencecolumn = self.column - newcolumn

        if differencecolumn == differencerow or differencecolumn == -differencerow:
            diagonal = True
        else:
            diagonal = False

        if diagonal == True:
            print('DIAGONAL')
            if grid[newrow][newcolumn] == ' ' or grid[newrow][newcolumn].colour == self.colour:
                print('cannot capture')
            else:
                if newrow == self.row + self.direction:
                    print('Diagonal Move')
                    return True
        
        if newcolumn == self.column:
            if newrow == self.row + self.direction and grid[newrow][newcolumn] == ' ':
                return True

            if self.row == 1 and newrow == self.row + self.direction + 1:
                nextrow = self.row + self.direction
                if grid[nextrow][self.column] == ' ' and grid[newrow][newcolumn] == ' ':
                    return True

            if self.row == 6 and newrow == self.row + self.direction - 1:
                nextrow = self.row + self.direction
                    
                if grid[nextrow][self.column] == ' ' and grid[newrow][newcolumn] == ' ':
                    return True

        return False  

class Rook(Piece):
    def __init__(self, colour, row, column):
        super().__init__(colour,row,column)

        if colour == 'white':
            self.icon = '♜'
        else:
            self.icon = '♖'

    def legalmove(self, newrow, newcolumn, grid):
        if newcolumn == self.column or newrow == self.row:
            if newrow != self.row:

                if newrow > self.row:
                    direction = 1
                else:
                    direction = -1

                for i in range(self.row + direction, newrow, direction):

                    if grid[i][self.column] != ' ':
                        print('Piece is in the way')
                        return False
                return True

            if newcolumn != self.column:

                if newcolumn > self.column:
                    direction = 1
                else:
                    direction = -1

                for i in range(self.column + direction, newcolumn, direction):

                    if grid[self.row][i] != ' ':
                        print('Piece is in the way')
                        return False
                return True
         
        return False

class Knight(Piece):
    def __init__(self, colour, row, column):
        super().__init__(colour,row,column)

        if colour == 'white':
            self.icon = '♞'
        else:
            self.icon = '♘'

    def legalmove(self, newrow, newcolumn, grid):
        x = [1,2,2,1,-1,-2,-2,-1]
        y = [2,1,-1,-2,-2,-1,1,2]

        for i in range(BOARD_SIZE):
            possiblex = self.row + x[i]
            possibley = self.column + y[i]

            if newrow == possiblex and newcolumn == possibley:

                targetsquare = grid[newrow][newcolumn]

                if targetsquare == ' ' or targetsquare.colour != self.colour:
                    try:
                        if targetsquare != self.colour:
                            return True
                    except:
                        pass
                    return True
                else:
                    print('Piece is in the way.')
                    return False
                    
            return False

class Bishop(Piece):
    def __init__(self, colour, row, column):
        super().__init__(colour,row,column)

        if colour == 'white':
            self.icon = '♝'
        else:
            self.icon = '♗'

    def legalmove(self, newrow, newcolumn, grid):
        valid = False
        differencerow = self.row - newrow
        differencecolumn = self.column - newcolumn

        if differencerow < 0:
            distancerow = -differencerow
        else:
            distancerow = differencerow

        if differencecolumn == differencerow or differencecolumn == -differencerow:
            valid = True

            for i in range(1,distancerow):

                directionrow = i
                directioncolumn = i

                if differencerow > 0:
                    directionrow *= -1

                if differencecolumn > 0:
                    directioncolumn *= -1

                targetsquare = grid[self.row + directionrow][self.column + directioncolumn]    

                if targetsquare != ' ':
                    print('There is a ', targetsquare.icon, '   Blocking.')
                    return False

        if not valid:
            return False

        if valid == True and grid[newrow][newcolumn] != ' ':
             if grid[newrow][newcolumn].colour == self.colour:
                print('you cannot capture your own piece.')
                return False
 
        return True 

class Queen(Piece):
    def __init__(self, colour, row, column):
        super().__init__(colour,row,column)

        if colour == 'white':
            self.icon = '♛'
        else:
            self.icon = '♕'

    def legalmove(self, newrow, newcolumn, grid):
        valid = False
        diagonalmove = False
        orthogonalmove = False
        differencerow = self.row - newrow
        differencecolumn = self.column - newcolumn

        if differencerow < 0:
            distancerow = -differencerow
        else:
            distancerow = differencerow

        if differencecolumn == differencerow or differencecolumn == -differencerow:
            diagonalmove = True
            valid = True
        elif newcolumn == self.column or newrow == self.row:
            orthogonalmove = True
            valid = True

        if diagonalmove == True:
            for i in range(1,distancerow):

                directionrow = i
                directioncolumn = i

                if differencerow > 0:
                    directionrow *= -1

                if differencecolumn > 0:
                    directioncolumn *= -1

                targetsquare = grid[self.row + directionrow][self.column + directioncolumn]    

                if targetsquare != ' ':
                    print('There is a ', targetsquare.icon, '   Blocking.')
                    return False
    
        elif orthogonalmove == True:
            if newrow != self.row:

                if newrow > self.row:
                    direction = 1
                else:
                    direction = -1

                for i in range(self.row + direction, newrow, direction):

                    targetsquare = grid[i][self.column]

                    if targetsquare != ' ':
                        print('There is a ', targetsquare.icon, '   Blocking.')
                        return False

            if newcolumn != self.column:

                if newcolumn > self.column:
                    direction = 1
                else:
                    direction = -1

                for i in range(self.column + direction, newcolumn, direction):

                    targetsquare = grid[self.row][i]

                    if targetsquare != ' ':
                        print('There is a ', targetsquare.icon, '   Blocking.')
                        return False
                 
        if not valid:
            return False

        if valid == True and grid[newrow][newcolumn] != ' ':
             if grid[newrow][newcolumn].colour == self.colour:
                print('you cannot capture your own piece.')
                return False
 
        return True

class King(Piece):
    def __init__(self, colour, row, column):
        super().__init__(colour, row, column)
        self.moved = False
        self.g = Game()
        self.castle = False

        if colour == 'white':
            self.icon = '♚'
        else:
            self.icon = '♔'

    def legalmove(self, newrow, newcolumn, grid):
        valid = False

        if self.castle == False:
            if newrow in (self.row + 1, self.row - 1) and newcolumn == self.column:
                valid = True

            elif newrow == self.row and newcolumn in (self.column + 1, self.column - 1):
                valid = True

            elif newrow in (self.row + 1, self.row - 1) and newcolumn in (self.column + 1, self.column - 1):
                valid = True

            if not valid:
                print('Invalid move..')
                return False

            target = grid[newrow][newcolumn]
            if target != ' ':
                if target.colour == self.colour:
                    print('You cannot capture your own piece.')
                    return False

        return True

PROMOTION_PIECES = [[1,Rook],[2,Bishop],[3,Knight],[4,Queen]] # constant used specifically for when the pawns are promoted, done by assigning each piece class to a index

class Board:
    def __init__(self):
        self.grid = [[' ' for i in range(BOARD_SIZE)] for i in range(BOARD_SIZE)]

    def setup(self): # sets the class pieces on each corresponding cell
        for i in range(BOARD_SIZE):
            whitepawn = Pawn('white',6,i)
            self.grid[6][i] = whitepawn

        for i in range(BOARD_SIZE):
            whiterook = Rook('white',7,i)   
            if i == 0 or i == BOARD_SIZE-1:
                self.grid[7][i] = whiterook

        for i in range(BOARD_SIZE):
            whiteknight = Knight('white',7,i)
            if i == 1 or i == BOARD_SIZE-2:
                self.grid[7][i] = whiteknight

        for i in range(BOARD_SIZE):
            whitebishop = Bishop('white',7,i)
            if i == 2 or i == BOARD_SIZE-3:
                self.grid[7][i] = whitebishop

        whitequeen = Queen('white',7,3)
        self.grid[7][3] = whitequeen                       

        whiteking = King('white',7,4)
        self.grid[7][4] = whiteking

        for i in range(BOARD_SIZE):
            blackpawn = Pawn('black',1,i)
            self.grid[1][i] = blackpawn

        for i in range(BOARD_SIZE):
            blackrook = Rook('black',0,i)
            if i == 0 or i == BOARD_SIZE-1:
                self.grid[0][i] = blackrook

        for i in range(BOARD_SIZE):
            blackknight = Knight('black',0,i)
            if i == 1 or i == BOARD_SIZE-2:
                self.grid[0][i] = blackknight

        for i in range(BOARD_SIZE):
            blackbishop = Bishop('black',0,i)
            if i == 2 or i == BOARD_SIZE-3:
                self.grid[0][i] = blackbishop

        blackqueen = Queen('black',0,3)
        self.grid[0][3] = blackqueen    

        blackking = King('black',0,4)
        self.grid[0][4] = blackking 

    def movepiece(self, startrow, startcolumn, newrow, newcolumn): # Moves the piece to the allocated position depending on whether or not the move you're trying to do is legal or not.
        piece = self.grid[startrow][startcolumn]
        captured = False
        piececaptured = ' '

        if piece == ' ':
            return False
        else:

            if piece.legalmove(newrow, newcolumn, self.grid) == True:
                if self.grid[newrow][newcolumn] != ' ':
                    piececaptured = self.grid[newrow][newcolumn]
                    captured = True

                self.grid[startrow][startcolumn] = ' '
                self.grid[newrow][newcolumn] = piece

                if self.grid[newrow][newcolumn].icon == '♟' or self.grid[newrow][newcolumn].icon == '♙':
                    print('Pawn has been moved')
                    if newrow == BOARD_SIZE - 1 or newrow == 0:
                        print('PROMOTION: ')
                        print('1: rook')
                        print('2: bishop')
                        print('3: knight')
                        print('4: queen')
                        choice = int(input('enter your choice: '))

                        for i in PROMOTION_PIECES:
                            if i[0] == choice:
                                print(i[1])
                                self.grid[newrow][newcolumn] = i[1]('white', newrow,newcolumn)

                piece.set_position(newrow, newcolumn)

                print('Move Successful')
                return True, captured, piececaptured
            else:
                print('Illegal Move.')
                return False, captured, piececaptured

    def displayboard(self):

        xnums = ('  '+'   '.join(str(i+1)for i in range(BOARD_SIZE)))
        print(xnums)

        num = 1
        for row in self.grid:
            game_row = []
            for i in row:
                if i == ' ':
                    game_row.append(' ')
                else:
                    game_row.append(i.icon)

            print(' -- ' * BOARD_SIZE)
            print(num, (' | '.join(game_row)))
            num += 1

class Game:
    def __init__(self):
        self.board = Board()
        self.turn = 'white'
        self.run = True
        self.timewhite = 1800
        self.timeblack = 1800

        self.whitecaptured = []
        self.blackcaptured = []

        self.white_kingside = True
        self.white_queenside = True
        self.black_kingside = True
        self.black_queenside = True

    def get_castlingrights(self):
        return self.white_queenside, self.white_kingside, self.black_queenside, self.black_kingside

    def get_status(self):
        return self.run

    def set_status(self):
        if self.run == True:
            self.run = False
        else:
            self.run = True
        return self.run

    def checkturn(self, startrow, startcolumn, newrow, newcolumn): # Checks whether the turn will work or not
        piece = self.board.grid[startrow][startcolumn]

        if piece != ' ' and piece.colour == self.turn:

            valid, captured, piececaptured = self.board.movepiece(startrow, startcolumn, newrow, newcolumn)
            if valid == False:
                return False
            elif captured == True:
                if piececaptured != ' ':
                    if piececaptured.icon == '♚':
                        print('black winner')
                        self.set_status()
                    elif piececaptured.icon == '♔':
                        print('white winner')
                        self.set_status()

                    if self.turn == 'white':
                        self.whitecaptured.append(piececaptured.icon)
                    else:
                        self.blackcaptured.append(piececaptured.icon)

                print('Captured')

            if self.turn == 'white':
                self.turn = 'black'
            else:
                self.turn = 'white' 
            
        else:
            print('it is not your turn, it is ',self.turn,"'s turn")
            return False

def main():
    game = Game()
    
    game.board.setup()
    
    timeblack = game.timeblack
    timewhite = game.timewhite


    while game.timewhite > 0 and game.timeblack > 0 and game.run == True:
        wmins = timewhite // 60
        wsecs = timewhite % 60
            
        bmins = timeblack // 60
        bsecs = timeblack % 60
                    
        formatw = f'{wmins:02}:{wsecs:02}'
        formatb = f'{bmins:02}:{bsecs:02}'

        print('GAME STATUS: ', game.run)
        print('White: ')
        print(*game.whitecaptured)
        print(formatw)
        print('Black: ')
        print(*game.blackcaptured)
        print(formatb)
            
        try:
            start = time.time()
            game.board.displayboard()
            print('it is',game.turn,"'s turn.")
            startrow = int(input('ENTER START ROW: ')) - 1

            startcolumn = int(input('ENTER START COLUMN: ')) - 1

            newrow = int(input('ENTER NEW ROW: ')) - 1

            newcolumn = int(input('ENTER START COLUMN: ')) - 1

            print('\n')
            game.checkturn(startrow, startcolumn, newrow, newcolumn)
        except(ValueError, TypeError):
            print('INVALID INPUT.')

        end = time.time()
        difference = round((end - start),0)
        if game.turn == 'white':
            timewhite -= difference
        else:
            timeblack -= difference
        
main()  