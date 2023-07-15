from Helper.ButtonHelper import Button

# Colour coordinate node's colour
RED = "#F65353"
PURPLE = "#726FC8"
GREEN = "#69B27A"
BLUE = "#58B1FF"
ORANGE = "#FFB347"
WHITE = "#FFFFFF"
BLACK = "#4C5270"
GRAY = "#9B9B9B"
SELECTEDBUTTON = "#00A67E"
UNSELECTEDBUTTON = "#4C5270"

WIDTH = 1200
HEIGHT = 750
ROWS = 70
GAP = 15

#Sidebar buttons
lblTitle = Button(0, 0, 150, 60, WHITE, UNSELECTEDBUTTON, "PATHFINDING")
dropAlgorithm = Button(0, 60, 150, 45, WHITE, UNSELECTEDBUTTON, "Algorithm: ")
btnAStar = Button(0, 105, 150, 45, WHITE, UNSELECTEDBUTTON, "A*")
btnDjikstra = Button(0, 150, 150, 45, WHITE, UNSELECTEDBUTTON, "Dijkstra")
btnDFS = Button(0, 195, 150, 45, WHITE, UNSELECTEDBUTTON, "Depth First Search")
dropWalls = Button(0, 240, 150, 45, WHITE, UNSELECTEDBUTTON, "Walls")
dropExtraNodes= Button(0, 285, 150, 45, WHITE, UNSELECTEDBUTTON, "Extra Nodes")
btnVisualise = Button(0, 330, 150, 45, WHITE, UNSELECTEDBUTTON, "Visualise")
btnClearBoard = Button(0, 375, 150, 45, WHITE, UNSELECTEDBUTTON, "Clear Board")
btnClearWall = Button(0, 420, 150, 45, WHITE, UNSELECTEDBUTTON, "Clear Walls")
btnClearPath = Button(0, 465, 150, 45, WHITE, UNSELECTEDBUTTON, "Clear Path")
dropSpeed = Button(0, 510, 150, 45, WHITE, UNSELECTEDBUTTON, "Speed: ")
btnHelp = Button(0, 555, 150, 45, WHITE, UNSELECTEDBUTTON, "Help")

#Legend symbols
legendStart = Button(25, 608, 15, 15, BLACK, RED, "", border=True)
legendTarget = Button(25, 628, 15, 15, BLACK, PURPLE, " ", border=True)
legendPrelimary = Button(25, 648, 15, 15, BLACK, BLACK, " ", border=True)
legendUnvisited = Button(25, 668, 15, 15, BLACK, WHITE, " ", border=True)
legendVisited1 = Button(15, 688, 15, 15, BLACK, GREEN, " ", border=True)
legendVisited2 = Button(35, 688, 15, 15, BLACK, BLUE, " ", border=True)
legendPath = Button(25, 708, 15, 15, BLACK, ORANGE, " ", border=True)
legendWall = Button(25, 728, 15, 15, BLACK, BLACK, " ", border=True)