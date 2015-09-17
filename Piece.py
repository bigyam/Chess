import math
class Piece:
    def __init__(self, pcType, xCoord, yCoord, owner):
        self.pcType = pcType
        self.xCoord = xCoord
        self.yCoord = yCoord
        self.owner = owner
        if self.pcType == 'pawn':
            self.hasMoved = False

    def isLegalMove(self, x, y):
        if self.pcType == 'pawn':
            if self.hasMoved == False:
                if self.owner == 'black':
                    if ((y - self.yCoord) <= 2) and ((x - self.xCoord) == 0) and ((y - self.yCoord) != 0):
                        self.hasMoved = True
                        return True
                    elif (math.fabs(x - self.xCoord) == 1) and (self.yCoord - y == -1):
                        self.hasMoved = True
                        return True
                    else:
                        return False
                else:
                    if ((y - self.yCoord) >= -2) and ((x - self.xCoord) == 0) and ((y - self.yCoord) != 0):
                        self.hasMoved = True
                        return True
                    elif (math.fabs(x - self.xCoord) == 1) and (self.yCoord - y == 1):
                        self.hasMoved = True
                        return True
                    else:
                        return False
            else:
                if self.owner == 'black':
                    if ((y - self.yCoord) == 1) and ((x - self.xCoord) == 0):
                        return True
                    elif (math.fabs(x - self.xCoord) == 1) and (self.yCoord - y == -1):
                        return True
                    else:
                        return False
                else:
                    if ((y - self.yCoord) == -1) and ((x - self.xCoord) == 0):
                        return True
                    elif (math.fabs(x - self.xCoord) == 1) and (self.yCoord - y == 1):
                        return True
                    else:
                        return False
                    
        if self.pcType == 'rook':
            if ((x - self.xCoord) != 0) and ((y - self.yCoord) == 0):
                return True
            elif ((x - self.xCoord) == 0) and ((y - self.yCoord) != 0):
                return True
            else:
                return False
            
        if self.pcType == 'knight':
            if ((x - self.xCoord) == 1) or ((x - self.xCoord) == -1):
                if ((y - self.yCoord) == 2) or ((y - self.yCoord) == -2):
                    return True
                else:
                    return False
            elif ((y - self.yCoord) == 1) or ((y - self.yCoord) == -1):
                if ((x - self.xCoord) == 2) or ((x - self.xCoord == -2)):
                    return True
                else:
                    return False
            else:
                return False

        if self.pcType == 'bishop':
            if ((math.fabs(y - self.yCoord)) == (math.fabs(x - self.xCoord))):
                return True
            else:
                return False

        if self.pcType == 'queen':
            if ((math.fabs(y - self.yCoord)) == (math.fabs(x - self.xCoord))) or (((x - self.xCoord) != 0) and ((y - self.yCoord) == 0)) or (((x - self.xCoord) == 0) and ((y - self.yCoord) != 0)):
                return True
            else:
                return False

        if self.pcType == 'king':
            if (((x - self.xCoord) != 0) or ((y - self.yCoord) != 0)) and ((math.fabs(y - self.yCoord) < 2) and (math.fabs(x - self.xCoord) < 2)):
                return True
            else:
                return False
