import os, sys
import pygame
import Piece
from pygame.locals import *
from Piece import Piece

#setting variables
WIDTH = 40
HEIGHT = 40
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (204, 204, 204)

#creating grid
grid = []
for row in range(8):
    grid.append([])
    for column in range(8):
        grid[row].append(0)

pygame.init()

#create screen
WINDOW_SIZE = [320, 320]
screen = pygame.display.set_mode(WINDOW_SIZE)
screen.fill(BLACK)

#create board 'surface'
gameBoard = pygame.Surface(screen.get_size())
gameBoard = gameBoard.convert()
gameBoard.fill(WHITE)

#window title
pygame.display.set_caption("Chess")
print("Welcome to Chess!")
print("Loading game...")

done = False
clock = pygame.time.Clock()

#loading images...
bbishop = pygame.image.load("images/bbishop.png").convert_alpha()
bbishop = pygame.transform.scale(bbishop, (40,40))
bking = pygame.image.load("images/bking.png").convert_alpha()
bking = pygame.transform.scale(bking, (40,40))
bknight = pygame.image.load("images/bknight.png").convert_alpha()
bknight = pygame.transform.scale(bknight, (40,40))
bpawn = pygame.image.load("images/bpawn.png").convert_alpha()
bpawn = pygame.transform.scale(bpawn, (40,40))
bqueen = pygame.image.load("images/bqueen.png").convert_alpha()
bqueen = pygame.transform.scale(bqueen, (40,40))
brook = pygame.image.load("images/brook.png").convert_alpha()
brook = pygame.transform.scale(brook, (40,40))
wbishop = pygame.image.load("images/wbishop.png").convert_alpha()
wbishop = pygame.transform.scale(wbishop, (40,40))
wking = pygame.image.load("images/wking.png").convert_alpha()
wking = pygame.transform.scale(wking, (40,40))
wknight = pygame.image.load("images/wknight.png").convert_alpha()
wknight = pygame.transform.scale(wknight, (40,40))
wpawn = pygame.image.load("images/wpawn.png").convert_alpha()
wpawn = pygame.transform.scale(wpawn, (40,40))
wqueen = pygame.image.load("images/wqueen.png").convert_alpha()
wqueen = pygame.transform.scale(wqueen, (40,40))
wrook = pygame.image.load("images/wrook.png").convert_alpha()
wrook = pygame.transform.scale(wrook, (40,40))

#create blank piece for empty spaces
blankSpace = Piece('empty', None, None, 'neither')

#creating black/white squares on board
for row in range(8):
    for column in range(8):
        color = WHITE
        grid[row][column] = blankSpace
        if (row % 2) == 0:
            if ((column % 2) == 0):
                color = GREY
        if ((row % 2) != 0):
            if ((column % 2) != 0):
                color = GREY
        pygame.draw.rect(gameBoard, color, [WIDTH * column, HEIGHT * row, WIDTH, HEIGHT])

##print('finished drawing board')

#function to move piece from one grid to another
#x = column y = row
def movePiece(theRow, theColumn, newRow, newColumn):
    movedPiece = getattr(grid[theRow][theColumn], 'pcType')
    movedOwner = getattr(grid[theRow][theColumn], 'owner')
    setattr(grid[theRow][theColumn], 'xCoord', newColumn)
    setattr(grid[theRow][theColumn], 'yCoord', newRow)
                        
    ##print('set attributes finished')
    grid[newRow][newColumn] = grid[theRow][theColumn]
    grid[theRow][theColumn] = blankSpace
    
    #filling in square to erase piece.  simulate movement
    if (theRow % 2) == 0:
        if ((theColumn % 2) == 0):
            color = GREY
        else:
            color = WHITE
    if ((theRow % 2) != 0):
        if ((theColumn % 2) != 0):
            color = GREY
        else:
            color = WHITE
            
    pygame.draw.rect(gameBoard, color, [WIDTH * theColumn, HEIGHT * theRow, WIDTH, HEIGHT])
    
    if (newRow % 2) == 0:
        if ((newColumn % 2) == 0):
            color = GREY
        else:
            color = WHITE
    if ((newRow % 2) != 0):
        if ((newColumn % 2) != 0):
            color = GREY
        else:
            color = WHITE
    pygame.draw.rect(gameBoard, color, [WIDTH * newColumn, HEIGHT * newRow, WIDTH, HEIGHT])
    print('width: ', WIDTH * theColumn)
    print('height: ', HEIGHT * theRow)
    
    #filling in piece at new location.  simulate movement
    if (movedOwner == 'black'):
        if (movedPiece == 'pawn'):
            gameBoard.blit(bpawn, (WIDTH * newColumn, HEIGHT * newRow))
        if (movedPiece == 'rook'):
            gameBoard.blit(brook, (WIDTH * newColumn, HEIGHT * newRow))
        if (movedPiece == 'knight'):
            gameBoard.blit(bknight, (WIDTH * newColumn, HEIGHT * newRow))
        if (movedPiece == 'bishop'):
            gameBoard.blit(bbishop, (WIDTH * newColumn, HEIGHT * newRow))
        if (movedPiece == 'queen'):
            gameBoard.blit(bqueen, (WIDTH * newColumn, HEIGHT * newRow))
        if (movedPiece == 'king'):
            gameBoard.blit(bking, (WIDTH * newColumn, HEIGHT * newRow))
    if (movedOwner == 'white'):
        if (movedPiece == 'pawn'):
            gameBoard.blit(wpawn, (WIDTH * newColumn, HEIGHT * newRow))
        if (movedPiece == 'rook'):
            gameBoard.blit(wrook, (WIDTH * newColumn, HEIGHT * newRow))
        if (movedPiece == 'knight'):
            gameBoard.blit(wknight, (WIDTH * newColumn, HEIGHT * newRow))
        if (movedPiece == 'bishop'):
            gameBoard.blit(wbishop, (WIDTH * newColumn, HEIGHT * newRow))
        if (movedPiece == 'queen'):
            gameBoard.blit(wqueen, (WIDTH * newColumn, HEIGHT * newRow))
        if (movedPiece == 'king'):
            gameBoard.blit(wking, (WIDTH * newColumn, HEIGHT * newRow))

#drawing black pieces
gameBoard.blit(brook, (0,0))
gameBoard.blit(bknight, (40,0))
gameBoard.blit(bbishop, (80,0))
gameBoard.blit(bking, (120,0))
gameBoard.blit(bqueen, (160,0))
gameBoard.blit(bbishop, (200,0))
gameBoard.blit(bknight, (240,0))
gameBoard.blit(brook, (280,0))
gameBoard.blit(bpawn, (0,40))
gameBoard.blit(bpawn, (40,40))
gameBoard.blit(bpawn, (80,40))
gameBoard.blit(bpawn, (120,40))
gameBoard.blit(bpawn, (160,40))
gameBoard.blit(bpawn, (200,40))
gameBoard.blit(bpawn, (240,40))
gameBoard.blit(bpawn, (280,40))

#drawing white pieces
gameBoard.blit(wpawn, (0,240))
gameBoard.blit(wpawn, (40,240))
gameBoard.blit(wpawn, (80,240))
gameBoard.blit(wpawn, (120,240))
gameBoard.blit(wpawn, (160,240))
gameBoard.blit(wpawn, (200,240))
gameBoard.blit(wpawn, (240,240))
gameBoard.blit(wpawn, (280,240))
gameBoard.blit(wrook, (0,280))
gameBoard.blit(wknight, (40,280))
gameBoard.blit(wbishop, (80,280))
gameBoard.blit(wqueen, (160,280))
gameBoard.blit(wking, (120,280))
gameBoard.blit(wbishop, (200,280))
gameBoard.blit(wknight, (240,280))
gameBoard.blit(wrook, (280,280))
##print('finished drawing pieces')



#creating black objects
bRook1 = Piece('rook', 0, 0, 'black')
grid[0][0] = bRook1
bRook2 = Piece('rook', 7, 0, 'black')
grid[0][7] = bRook2
bKnight1 = Piece('knight', 1, 0, 'black')
grid[0][1] = bKnight1
bKnight2 = Piece('knight', 6, 0, 'black')
grid[0][6] = bKnight2
bBishop1 = Piece('bishop', 2, 0, 'black')
grid[0][2] = bBishop1
bBishop2 = Piece('bishop', 5, 0, 'black')
grid[0][5] = bBishop2
bQueen = Piece('queen', 4, 0, 'black')
grid[0][4] = bQueen
bKing = Piece('king', 3, 0, 'black')
grid[0][3] = bKing
bPawn1 = Piece('pawn', 0, 1, 'black')
grid[1][0] = bPawn1
bPawn2 = Piece('pawn', 1, 1, 'black')
grid[1][1] = bPawn2
bPawn3 = Piece('pawn', 2, 1, 'black')
grid[1][2] = bPawn3
bPawn4 = Piece('pawn', 3, 1, 'black')
grid[1][3] = bPawn4
bPawn5 = Piece('pawn', 4, 1, 'black')
grid[1][4] = bPawn5
bPawn6 = Piece('pawn', 5, 1, 'black')
grid[1][5] = bPawn6
bPawn7 = Piece('pawn', 6, 1, 'black')
grid[1][6] = bPawn7
bPawn8 = Piece('pawn', 7, 1, 'black')
grid[1][7] = bPawn8
##print('finished creating black objects')

#creating white objects
wRook1 = Piece('rook', 0, 7, 'white')
grid[7][0] = wRook1
wRook2 = Piece('rook', 7, 7, 'white')
grid[7][7] = wRook2
wKnight1 = Piece('knight', 1, 7, 'white')
grid[7][1] = wKnight1
wKnight2 = Piece('knight', 6, 7, 'white')
grid[7][6] = wKnight2
wBishop1 = Piece('bishop', 2, 7, 'white')
grid[7][2] = wBishop1
wBishop2 = Piece('bishop', 5, 7, 'white')
grid[7][5] = wBishop2
wQueen = Piece('queen', 4, 7, 'white')
grid[7][4] = wQueen
wKing = Piece('king', 3, 7, 'white')
grid[7][3] = wKing
wPawn1 = Piece('pawn', 0, 6, 'white')
grid[6][0] = wPawn1
wPawn2 = Piece('pawn', 1, 6, 'white')
grid[6][1] = wPawn2
wPawn3 = Piece('pawn', 2, 6, 'white')
grid[6][2] = wPawn3
wPawn4 = Piece('pawn', 3, 6, 'white')
grid[6][3] = wPawn4
wPawn5 = Piece('pawn', 4, 6, 'white')
grid[6][4] = wPawn5
wPawn6 = Piece('pawn', 5, 6, 'white')
grid[6][5] = wPawn6
wPawn7 = Piece('pawn', 6, 6, 'white')
grid[6][6] = wPawn7
wPawn8 = Piece('pawn', 7, 6, 'white')
grid[6][7] = wPawn8
##print('finished creating white objects')


selected = 0
turn = 0
pos = None
column = None
row = None
newColumn = None
newRow = None
newPos = None
print("Start game!")
print("White begins first")
#event loop
while not done:
    while True:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    break
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if selected == 0:
                        pos = pygame.mouse.get_pos()
                        column = pos[0] // WIDTH
                        row = pos[1] // HEIGHT
                        getattr(grid[row][column], 'owner')
                        if (turn % 2 == 0):
                            pygame.display.set_caption("Chess -- White's move. Please select piece...")
                            print("White's Move")
                            if (getattr(grid[row][column], 'owner') == 'white'):
                                ##print("turn: ", turn)
                                print("Valid White Selection -- Click piece again to deselect")
                                pygame.display.set_caption("Chess -- Select Movement -- Click piece to deselect")
                                turn = turn + 1
                                selected = 1
                                break
                            else:
                                print("Invalid White Selection")
                                continue
                        if (turn % 2 == 1):
                            pygame.display.set_caption("Chess -- Black's Move")
                            print("Black's Move")
                            if (getattr(grid[row][column], 'owner') == 'black'):
                                ##print("turn: ", turn)
                                print("Valid Black Selection --  Click piece again to deselect")
                                pygame.display.set_caption("Chess -- Select Movement -- Click piece to deselect")
                                turn = turn + 1
                                selected = 1
                                break
                            else:
                                print("Invalid Black Selection")
                                continue
                    if selected == 1:
                        selected = 0
                        pos = pygame.mouse.get_pos()
                        newColumn = pos[0] // WIDTH
                        newRow = pos[1] // HEIGHT
                        
                        #Deselect selected piece
                        if newColumn == column and newRow == row:
                            selected = 0
                            turn = turn + 1

                        #checks if selected movement grid is valid movement by piece
                        elif grid[row][column].isLegalMove(newColumn, newRow):
                            ##print('test')
                            ##print('owner old: ', getattr(grid[row][column], 'owner'))
                            ##print('owner new: ', getattr(grid[newRow][newColumn], 'owner'))
                            
                            #if selected movement grid is your own piece
                            if getattr(grid[row][column], 'owner') == getattr(grid[newRow][newColumn], 'owner'):
                                selected = 1
                                print("Can't move on your own piece.  Please try again")
                                
                            #if selected movement piece is a pawn
                            elif (getattr(grid[row][column], 'pcType') == 'pawn'):
                                ##print('in pawn')
                                if (turn % 2 == 1): #white pawn
                                    ##print('white pawn')
                                    if (getattr(grid[newRow][newColumn], 'pcType') != 'empty'):
                                        ##print('not empty')
                                        if (getattr(grid[newRow][newColumn], 'owner') == 'black') and (column != newColumn):
                                             movePiece(row, column, newRow, newColumn)
                                        else:
                                            selected = 1
                                            print("Invalid pawn movement.  Please try again")
                                    else:
                                        if (column == newColumn):
                                            movePiece(row, column, newRow, newColumn)
                                        else:
                                            selected = 1
                                            print("Invalid pawn movement. Please try again")
                                
                                if (turn % 2 == 0): #black pawn
                                    ##print('black pawn')
                                    if (getattr(grid[newRow][newColumn], 'pcType') != 'empty'):
                                        if (getattr(grid[newRow][newColumn], 'owner') == 'white') and (column != newColumn):
                                             movePiece(row, column, newRow, newColumn)
                                        else:
                                            selected = 1
                                            print("Invalid pawn movement.  Please try again")
                                    else:
                                        if (column == newColumn):
                                            movePiece(row, column, newRow, newColumn)
                                        else:
                                            selected = 1
                                            print("Invalid pawn movement. Please try again")
                                            
                            #check for collision
                                #specifically rooks
                            elif (getattr(grid[row][column], 'pcType') == 'rook') or (getattr(grid[row][column], 'pcType') == 'queen'):
                                collisionPass = 0
                                if (row - newRow) == 0:
                                    ##print("in row")
                                    if column > newColumn:
                                        for rangeColumn in range(newColumn+1, column):
                                            if (getattr(grid[row][rangeColumn], 'pcType') != 'empty'):
                                                selected = 1
                                                collisionPass = 1
                                                print("Invalid move.  Another piece in the way")
                                                break
                                        if collisionPass == 0:
                                            movePiece(row, column, newRow, newColumn)
                                    if newColumn > column:
                                        for rangeColumn in range(column+1, newColumn):
                                            if (getattr(grid[row][rangeColumn], 'pcType') != 'empty'):
                                                selected = 1
                                                collisionPass = 1
                                                print("Invalid move. Another piece in the way")
                                                break
                                        if collisionPass == 0:
                                            movePiece(row, column, newRow, newColumn)
                                if (column - newColumn) == 0:
                                    ##print("in column")
                                    if row > newRow:
                                        ##print("first row")
                                        print("%d %d", row, newRow)
                                        for rangeRow in range(newRow+1, row):
                                            ##print("grid:")
                                            if (getattr(grid[rangeRow][column], 'pcType') != 'empty'):
                                                selected = 1
                                                collisionPass = 1
                                                print("Invalid move. Another piece in the way")
                                                break
                                        if collisionPass == 0:
                                            movePiece(row, column, newRow, newColumn)
                                    if newRow > row:
                                        print("second row")
                                        for rangeRow in range(row+1, newRow):
                                            if (getattr(grid[rangeRow][column], 'pcType') != 'empty'):
                                                selected = 1
                                                collisionPass = 1
                                                print("Invalid move. Another piece in the way")
                                                break
                                        if collisionPass == 0:
                                            movePiece(row, column, newRow, newColumn)
                                            
                                #specifically bishops
                            elif (getattr(grid[row][column], 'pcType') == 'bishop') or (getattr(grid[row][column], 'pcType') == 'queen'):
                                collisionPass = 0
                                ##print("in bishop")
                                ##print(" ", row, column, newRow, newColumn)
                                if newRow > row and newColumn > column:
                                    ##print("in if")
                                    for x in range(1, newRow - row):
                                        ##print("in for")
                                        if (getattr(grid[row+x][column+x], 'pcType') != 'empty'):
                                            selected = 1
                                            collisionPass = 1
                                            print("Invalid move. Another piece in the way")
                                            break
                                    if collisionPass == 0:
                                        movePiece(row, column, newRow, newColumn)
                                        
                                if newRow > row and newColumn < column:
                                    for x in range(1, newRow - row):
                                        if(getattr(grid[row+x][column-x], 'pcType') != 'empty'):
                                            selected = 1
                                            collisionPass = 1
                                            print("Invalid move. Another piece in the way")
                                            break
                                    if collisionPass == 0:
                                        movePiece(row, column, newRow, newColumn)

                                if newRow < row and newColumn > column:
                                    for x in range(1, newColumn - column):
                                        if(getattr(grid[row-x][column+x], 'pcType') != 'empty'):
                                            selected = 1
                                            collisionPass = 1
                                            print("Invalid move. Another piece in the way")
                                            break
                                    if collisionPass == 0:
                                        movePiece(row, column, newRow, newColumn)

                                if newRow < row and newColumn < column:
                                    for x in range(1, column - newColumn):
                                        if(getattr(grid[row-x][column-x], 'pcType') != 'empty'):
                                            selected = 1
                                            collisionPass = 1
                                            print("Invalid move. Another piece in the way")
                                            break
                                    if collisionPass == 0:
                                        movePiece(row, column, newRow, newColumn)
                                
                            
                            #movement to empty space
                            else:
                                movePiece(row, column, newRow, newColumn)

                        #selected movement grid is not valid    
                        else:
                            selected = 1
                            print("Invalid move.  Please try again")
                        
            screen.blit(gameBoard, (0,0))
            clock.tick(60)
            pygame.display.flip()
            
        except AttributeError:
            print("No chess piece in selected grid.  Please select another")
                    
        
pygame.quit()

    
