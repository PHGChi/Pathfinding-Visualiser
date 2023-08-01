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
LIGHTGRAY = "#C6C6C6"
DARKGREEN = "#00A67E"

# Main features size
WIDTH = 1200
HEIGHT = 750

# Related to grid
ROWS = 70
COLS = 50
GAP = 15

# Related to sidebar
SIDEBARWIDTH = 450
BUTTONWIDTH = 150
BUTTONHEIGHT = 45
TITLEHEIGHT = 60
FIRSTLINE = 50
SECONDLINE = 250
MIDDLE = (SIDEBARWIDTH - BUTTONWIDTH)//2

# Sidebar buttons
lblTitle = Button(MIDDLE, 0, BUTTONWIDTH, TITLEHEIGHT, BLACK, WHITE, "PATHFINDING", "Title")
btnVisualise = Button(FIRSTLINE, TITLEHEIGHT + GAP, BUTTONWIDTH, BUTTONHEIGHT, WHITE, GREEN, "Visualise", "Normal")
btnClearBoard = Button(SECONDLINE, TITLEHEIGHT + GAP, BUTTONWIDTH, BUTTONHEIGHT, WHITE, BLACK, "Clear Board", "Normal")
btnClearWall = Button(FIRSTLINE, TITLEHEIGHT + BUTTONHEIGHT + 2 * GAP, BUTTONWIDTH, BUTTONHEIGHT, WHITE, BLACK, "Clear Walls", "Normal")
btnClearPath = Button(SECONDLINE, TITLEHEIGHT + BUTTONHEIGHT + 2 * GAP, BUTTONWIDTH, BUTTONHEIGHT, WHITE, BLACK, "Clear Path", "Normal")
lblAlgorithm = Button(MIDDLE, TITLEHEIGHT + 2 * BUTTONHEIGHT + 3 * GAP, BUTTONWIDTH, BUTTONHEIGHT, BLACK, WHITE, "Algorithm: A*", "Heading")
btnAStar = Button(FIRSTLINE, TITLEHEIGHT + 3 * BUTTONHEIGHT + 4 * GAP, BUTTONWIDTH, BUTTONHEIGHT, WHITE, BLACK, "A*", "Normal")
btnDjikstra = Button(SECONDLINE, TITLEHEIGHT + 3 * BUTTONHEIGHT + 4 * GAP, BUTTONWIDTH, BUTTONHEIGHT, WHITE, BLACK, "Dijkstra", "Normal")
btnDFS = Button(FIRSTLINE, TITLEHEIGHT + 4 * BUTTONHEIGHT + 5 * GAP, BUTTONWIDTH, BUTTONHEIGHT, WHITE, BLACK, "Depth First Search", "Normal")
btnBidirectional = Button(SECONDLINE, TITLEHEIGHT + 4 * BUTTONHEIGHT + 5 * GAP, BUTTONWIDTH, BUTTONHEIGHT, WHITE, BLACK, "Bidirectional", "Normal")
lblMaze = Button(MIDDLE, TITLEHEIGHT + 5 * BUTTONHEIGHT + 6 * GAP, BUTTONWIDTH, BUTTONHEIGHT, BLACK, WHITE, "Maze Generator", "Heading")
btnRecursiveDivsion = Button(FIRSTLINE, TITLEHEIGHT + 6 * BUTTONHEIGHT + 7 * GAP, BUTTONWIDTH, BUTTONHEIGHT, WHITE, BLACK, "Recursive Division", "Normal")
btnPrims = Button(SECONDLINE, TITLEHEIGHT + 6 * BUTTONHEIGHT + 7 * GAP, BUTTONWIDTH, BUTTONHEIGHT, WHITE, BLACK, "Prim's MST", "Normal")
btnKruskal = Button(FIRSTLINE, TITLEHEIGHT + 7 * BUTTONHEIGHT + 8 * GAP, BUTTONWIDTH, BUTTONHEIGHT, WHITE, BLACK, "Kruskal", "Normal")
btnRandom = Button(SECONDLINE, TITLEHEIGHT + 7 * BUTTONHEIGHT + 8 * GAP, BUTTONWIDTH, BUTTONHEIGHT, WHITE, BLACK, "Randomised", "Normal")

btnHelp = Button(420, TITLEHEIGHT + 8 * BUTTONHEIGHT + 10 * GAP, 15, 15, BLACK, WHITE, "?", "Help", border=True)

# Legend symbols
lblLegend = Button(MIDDLE, 585, BUTTONWIDTH, BUTTONHEIGHT, BLACK, WHITE, "Legend", "Heading")
legendStart = Button(85, 645, 15, 15, BLACK, RED, "", "Legend", border=True)
legendTarget = Button(185, 645, 15, 15, BLACK, PURPLE, " ", "Legend", border=True)
legendUnvisited = Button(285, 645, 15, 15, BLACK, WHITE, " ", "Legend", border=True)
legendVisited1 = Button(75, 675, 15, 15, BLACK, GREEN, " ", "Legend", border=True)
legendVisited2 = Button(95, 675, 15, 15, BLACK, BLUE, " ", "Legend", border=True)
legendPath = Button(185, 675, 15, 15, BLACK, ORANGE, " ", "Legend", border=True)
legendWall = Button(285, 675, 15, 15, BLACK, BLACK, " ", "Legend", border=True)