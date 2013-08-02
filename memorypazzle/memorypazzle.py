import random
import sys
import pygame
from pygame.locals import *

AQUA      =  (  0, 255, 255)
BLACK     =  (  0,   0,   0)
BLUE      =  (  0,   0, 255)
FUCHSIA   =  (255,   0, 255)
GRAY      =  (128, 128, 128)
GREEN     =  (  0, 128,   0)
LIME      =  (  0, 255,   0)
MAROON    =  (128,   0,   0)
NAVYBLUE  =  (  0,   0, 128)
OLIVE     =  (128, 128,   0)
PURPLE    =  (128,   0, 128)
RED       =  (255,   0,   0)
SILVER    =  (192, 192, 192)
TEAL      =  (  0, 128, 128)
WHITE     =  (255, 255, 255)
YELLOW    =  (255, 255,   0)

class game(object):

    def __init__(self, wWidth = 640, wHeight = 480, fullscreen = 0, depth = 32):

        pygame.init()
        self.display = pygame.display.set_mode((wWidth, wHeight), fullscreen, depth)
        pygame.display.set_caption('Memory game')
        self.fpsClock = pygame.time.Clock()
        
        self.FPS = 30
        self.revealSpeed = 8 #speed boxes' sliding reveals and covers
        self.boxSize = 40 #box's width & height in pixels
        self.gapSize = 10 #gap's size between boxes in pixels
        self.boardWidth = 10 #number of columns of icons
        self.boardHeight = 7 #number of rows of icons
        assert (self.boardWidth * self.boardHeight) % 2 == 0, 'Needs to have even number of boxes'
        self.xMargin = int((wWidth - (self.boardWidth * (self.boxSize + self.gapSize))) / 2)
        self.yMargin = int((wHeight - (self.boardHeight * (self.boxSize + self.gapSize))) / 2)
        #colors
        self.bgColor = NAVYBLUE
        self.lightBgColor = GRAY
        self.boxColor = WHITE
        self.hightLightColor = BLUE
        #shapes
        self.donut = 'donut'
        self.square = 'square'
        self.diamond = 'diamond'
        self.lines = 'lines'
        self.oval = 'oval'
        self.allShapes = (self.donut, self.square, self.diamond, self.lines, self.oval)
        self.allColors = (RED, GREEN, BLUE, YELLOW, SILVER, PURPLE, AQUA)
        
        assert len(self.allColors) * len(self.allShapes) * 2 >= self.boardWidth * self.boardHeight, \
            "Board is too big for thr number of shapes/colors defined."
        #controls
        self.mousex = 0
        self.mousey = 0
        
        self.mainBoard = self.getRandomizedBoard()
        self.revealedBoxes = self.generateRevealedBoxesData(False)
        self.mouseClicked = False
        self.firstSelection = None #stores (x,y) of the first box clicked

        self.boxx = 0
        self.boxy = 0

        self.mainBoard = self.getRandomizedBoard()
        
        self.display.fill(self.bgColor)
        self.startGameAnimation(self.mainBoard)

    def init(self):
        pass

    def quit(self):
        pass

    def getRandomizedBoard(self):
        # Get a list of every possible shape in every possible color
        icons = []
        for color in self.allColors:
            for shape in self.allShapes:
                icons.append((shape, color))

        random.shuffle(icons) # randomize the order of the icons list
        numIconsUsed = int(self.boardWidth * self.boardHeight / 2) # how many icons need
        icons = icons[:numIconsUsed] * 2 # make two of each
        random.shuffle(icons)
        
        #create the board data structure, with randomly placed icons
        board = []
        for x in range(self.boardWidth):
            column = []
            for y in range(self.boardHeight):
                column.append(icons[0])
                del icons[0] #remove the icon as we assign it
                board.append(column)
            return board
        
    def generateRevealedBoxesData(self, val):
        revealedBoxes = []
        for i in range(self.boardWidth):
            revealedBoxes.append([val] * self.boardHeight)
        return revealedBoxes

    def splitIntoGroupsOf(self, groupSize, theList):
        #splits a list into a list of lists, where the inner lists have
        #the most groupSize number of items
        result = []
        for i in xrange(0, len(theList), groupSize):
            result.append(theList[i:i + groupSize])
        return result

    def leftTopCoordsOfBox(self, boxx, boxy):
        #convert board coords to pixel coords
        print("From LTCOB: boxx = " + str(boxx) + " ; boxSize = " + str(self.boxSize) + \
                  " ; gapSize = " + str(self.gapSize) + " ; xmargin = " + str(self.xMargin))

        left = boxx * (self.boxSize + self.gapSize) + self.xMargin
        print("left = " + str(left))
        print("boxy = " + str(boxy) + " boxSize + gapSize ; ymargin = " + str(self.yMargin))
        top = boxy * (self.boxSize + self.gapSize) + self.yMargin
        print("top = " + str(top))
        return (left, top)

    def getBoxAtPixel(self, x, y):
        for boxx in range(self.boardWidth):
            for boxy in range(self.boardHeight):
                left, top = self.leftTopCoordsOfBox(boxx, boxy)
                boxRect = pygame.Rect(left, top, self.boxSize, self.boxSize)
                if boxRect.collidepoint(x, y):
                    return (boxx, boxy)
        return (None, None)

    def drawIcon(self, shape, color, boxx, boxy):
        quarter = int(self.boxSize * 0.25)
        half    = int(self.boxSize * 0.5)

        left, top = self.leftTopCoordsOfBox(boxx, boxy) # get pixel coords from board coords
        #draw shapes
        if shape == self.donut:
            pygame.draw.circle(self.display, color, (left + half, top + half), half - 5)
            pygame.draw.circle(self.display, self.bgColor, (left + half, top + half), quarter - 5)
        elif shape == self.square:
            pygame.draw.rect(self.display, color, 
                             (left + quarter, top + quarter, self.boxSize - half, self.boxSize - half)) 
        elif shape == self.diamond:
            pygame.draw.polygon(self.display, color, ((left + half, top), 
                                                      (left + self.boxSize - 1, top + half),
                                                      (left + half, top + self.boxSize - 1),
                                                      (left, top + half)))
        elif shape == self.lines:
            for i in xrange(0, self.boxSize, 4):
                pygame.draw.line(self.display, color, (left, top + i), (left + i, top))
                pygame.draw.line(self.display, color, (left + i, top + self.boxSize - 1), 
                                 (left + self.boxSize - 1, top + i))
        elif shape == self.oval:
            pygame.draw.ellipse(self.display, color, (left, top + quarter, self.boxSize, half))

    def getShapeAndColor(self, board, boxx, boxy):
        #shape value for x, y spot is stored in board[x][y][0]
        #color value for x, y spot is stored in board[x][y][1]
        return board[boxx][boxy][0], board[boxx][boxy][1]

    def drawBoxCovers(self, board, boxes, coverage):
        #Draws boxes being covered/revealed. "boxes" is a list
        #of two-item lists, which have the x & y spot of the box/
        for box in boxes:
            left, top = self.leftTopCoordsOfBox(box[0], box[1])
            pygame.draw.rect(self.display, self.bgColor, (left, top, self.boxSize, self.boxSize))
            shape, color = self.getShapeAndColor(board, box[0], box[1])
            self.drawIcon(shape, color, box[0], box[1])
            if coverage > 0: #only draw the cover if there is an coverage
                pygame.draw.rect(self.display, self.boxColor, (left, top, coverage, self.boxSize))
        pygame.display.update()
        self.fpsClock.tick(self.FPS)

    def revealBoxesAnimation(self, board, boxesToReveal):
        #do the box reveal animation
        for coverage in range(self.boxSize, (-self.revealSpeed) - 1, -self.revealSpeed):
            self.drawBoxCovers(board, boxesToReveal, coverage)

    def coverBoxesAnimation(self, board, boxesToCover):
        #do the box cover animation
        for coverage in range(0, self.boxSize + self.revealSpeed, self.revealSpeed):
            self.drawBoxCovers(board, boxesToCover, coverage)

    def drawBoard(self, board, revealed):
        #draws all of the boxes in their covered or revealed state
        for boxx in range(self.boardWidth):
            for boxy in range(self.boardHeight):
                left, top = self.leftTopCoordsOfBox(boxx, boxy)
                if not revealed[boxx][boxy]:
                #Draw a covered box
                    pygame.draw.rect(self.display, self.boxColor, (left, top, self.boxSize, self.boxSize))
                else:
                    #Draw a revealed icon
                    shape, color = self.getShapeAndColor(board, boxx, boxy)
                    drawIcon(shape, color, boxx, boxy)
                    
    def drawHighlightBox(self, boxx, boxy):
        left, top = self.leftTopCoordsOfBox(boxx, boxy)
        pygame.draw.rect(self.display, self.hightLightColor, 
                         (left - 5, top - 5, self.boxSize + 10, self.boxSize + 10), 4)
        
    def startGameAnimation(self, board):
        #Randomly reveal the boxes 8 at a time
        coveredBoxes = self.generateRevealedBoxesData(False)
        boxes = []
        for x in range(self.boardWidth):
            for y in range(self.boardHeight):
                boxes.append((x, y))
        random.shuffle(boxes)
        boxGroups = self.splitIntoGroupsOf(8, boxes)
        
        self.drawBoard(board, coveredBoxes)
        for boxGroup in boxGroups:
            self.revealBoxesAnimation(board, boxGroup)
            self.coverBoxesAnimation(board, boxGroup)

    def gameWonAnimation(self, board):
        #flash the background color when player has won
        coveredBoxes = self.generateRevealedBoxesData(True)
        color1 = self.lightBgColor
        color2 = self.bgColor

        for i in xrange(13):
            color1, color2 = color2, color1
            self.display.fill(color1)
            self.drawBoard(board, coveredBoxes)
            pygame.display.update()
            pygame.time.wait(300)
        
    def hasWon(revealedBoxes):
        #Returns True if all the boxes have been revealed, otherwise False
        for i in revealedBoxes:
            if False in i:
                return False #return False if any boxes are covered
        return True


    def handleEvents(self):
        self.mouseClicked = False
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                self.mousex, self.mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                self.mousex, self.mousey = event.pos
                self.mouseClicked = True
            else:
                print(event)


    def updateState(self):
        self.boxx, self.boxy = self.getBoxAtPixel(self.mousex, self.mousey)
        if self.boxx != None and self.boxy != None:
            if not self.revealedBoxes[self.boxx][self.boxy]:
                self.drawHighlightBox(self.boxx, self.boxy)
            if not self.revealedBoxes[self.boxx][self.boxy] and self.mouseClicked:
                self.revealBoxesAnimation(self.mainBoard, [(self.boxx, self.boxy)])
                self.revealedBoxes[self.boxx][self.boxy] = True

                if self.firstSelection == None: #the current box was the first box clicked
                    self.firstSelection = (self.boxx, self.boxy)
                else: #the current box was the second box clicked
                    #Check if there is a match between the two icons
                    self.firstIconShape, self.firstIconColor = self.getShapeAndColor(
                        self.mainBoard, self.firstSelection[0], self.firstSelection[2])
                    self.secondIconShape, self.secondIconColor = self.getShapeAndColor(
                        self.mainBoard, self.boxx, self.boxy)
                    if self.firstIconShape != self.secondIconShape or firstIconColor != secondIconColor:
                        #icons don't match. Re-cover up both selections
                        pygame.time.wait(1000) #1 sec
                        self.coverBoxesAnimation(self.mainBoard,
                                                 [(self.firstSelection[0], self.firstSelection[1]), 
                                                 (self.boxx, self.boxy)])
                        self.revealedBoxes[self.firstSelection[0]][firstSelection[1]] = False
                        self.revealedBoxes[self.boxx][self.boxy] = False
                    elif self.hasWon(self.revealedBoxes): #check if all pairs found
                        self.gameWonAnimation(self.mainBoard)
                        pygame.time.wait(2000)
                        
                        #reset the board
                        self.mainBoard = self.getRandomizedBoard()
                        self.revealedBoxes = self.generateRevealedBoxesData(False)

                        #Show the fully unrevealed board for a second.
                        self.drawBoard(self.mainBoard, self.revealedBoxes)
                        pygame.display.update()
                        pygame.time.wait(1000)

                        #replay the start game animation.
                        self.startGameAnimation(self.mainBoard)
                    self.firstSelection = None
        pygame.display.update()

                        


    def drawScreen(self):
        self.display.fill(self.bgColor)
        self.drawBoard(self.mainBoard, self.revealedBoxes)

        pygame.display.update()
        self.fpsClock.tick(self.FPS)




def main():
    memgame = game()
    while True:
        memgame.handleEvents()
        memgame.updateState()
        memgame.drawScreen()

if __name__ == '__main__':
    main()
