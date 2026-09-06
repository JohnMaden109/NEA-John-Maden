import time

BOARD_SIZE = 8

class Piece:
    def __init__(self, colour, row, column):
        self.colour = colour
        self.row = row
        self.column = column

    def get_position(self):
        return self.row, self.column
    
    def set_position(self, newrow, newcolumn):
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
             else:
                print('Captured: ', grid[newrow][newcolumn].icon)
 
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
             else:
                print('Captured: ', grid[newrow][newcolumn].icon)
 
        return True

class King(Piece):
    def __init__(self, colour, row, column):
        super().__init__(colour, row, column)

        if colour == 'white':
            self.icon = '♚'
        else:
            self.icon = '♔'

    def legalmove(self, newrow, newcolumn, grid):
        valid = False

        if newrow in (self.row + 1, self.row - 1) and newcolumn == self.column:
            valid = True

        elif newrow == self.row and newcolumn in (self.column + 1, self.column - 1):
            valid = True

        elif newrow in (self.row + 1, self.row - 1) and newcolumn in (self.column + 1, self.column - 1):
            valid = True

        if not valid:
            print('Invalid move for a king.')
            return False

        target = grid[newrow][newcolumn]
        if target != ' ':
            if target.colour == self.colour:
                print('You cannot capture your own piece.')
                return False
            else:
                print('Captured: ', target.icon)

        return True


class Board:
    def __init__(self):
        self.grid = [[' ' for i in range(BOARD_SIZE)] for i in range(BOARD_SIZE)]

    def setup(self):
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

    def movepiece(self, startrow, startcolumn, newrow, newcolumn):
        piece = self.grid[startrow][startcolumn]

        if piece == ' ':
            return False
        else:

            if piece.legalmove(newrow, newcolumn, self.grid) == True:
                self.grid[startrow][startcolumn] = ' '
                self.grid[newrow][newcolumn] = piece
    
                piece.set_position(newrow, newcolumn)

                self.displayboard()
                print('Move Successful')
            else:
                print('Illegal Move.')
                return False
            

    def displayboard(self):

        print('\n')

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

    def checkturn(self, startrow, startcolumn, newrow, newcolumn):
        piece = self.board.grid[startrow][startcolumn]

        if piece != ' ' and piece.colour == self.turn:

            if self.board.movepiece(startrow, startcolumn, newrow, newcolumn) == False:
                return False
            else:
                if self.turn == 'white':
                    self.turn = 'black'
                else:
                    self.turn = 'white'
        else:
            print('broski it is not ur turn, it is actually',self.turn,"'s turn")
            return False

def main():
    game = Game()
    
    game.board.setup()
    game.board.displayboard()

    while game.run == True:
        try:
            print('\n')
            print('it is',game.turn,"'s turn.")
            startrow = int(input('ENTER START ROW: ')) - 1
            startcolumn = int(input('ENTER START COLUMN: ')) - 1
            newrow = int(input('ENTER NEW ROW: ')) - 1
            newcolumn = int(input('ENTER NEW COLUMN: ')) - 1
            print('\n')

            game.checkturn(startrow, startcolumn, newrow, newcolumn)
        except(ValueError):
            print('Not a correct guy mate.')
            continue



    


main()
