from tkinter import * 
import tkinter as tk

app = Tk()
#initialize the canvas
canvas_width = 600
canvas_height = 600
app.geometry("600x600")


canvas = tk.Canvas(app,height = canvas_height,width = canvas_width,bg="white")
canvas.pack()
step = 1

grid =[] # the entire grid is a matrix
number_of_squaresH  = canvas_width // 20
number_of_squaresV  = canvas_height // 20

dirI = [-1,1,0,0,-1,-1,1,1]
dirJ = [0,0,-1,1,-1,1,-1,1]

path = []
start_i=0
start_j=0
class PriorityQueue: #actually a normal queue but I should make it a priority one:P
    def __init__(self):
        self.values = []

    def empty(self):
        if len(self.values) ==0:
            return True
        else :return False

    def add(self,x):
        self.values.append(x)

    def delete(self):
        del self.values[0]
    def get(self):
        return self.values[0]
queue = PriorityQueue() 

class Rectangle: # represents every element of the grid
    def __init__(self,x1,y1,x2,y2,color,i,j):
        self.x1 = x1 
        self.y1 = y1
        self.y2 = y2
        self.x2 = x2
        self.i = i
        self.j = j
        self.color = color 
        self.visited = False
        self.previous =None  
    def update(self):
        canvas.create_rectangle(self.x1,self.y1,self.x2,self.y2,fill=self.color)
        
def createGrid():
    x ,y = 0 ,0
    index = 0
    for i in range(1,number_of_squaresV+1):
        row = []
        for j in range(1,number_of_squaresH+1):
            x1 = x + 20 
            index += 1
            rect  = Rectangle(x,y,x1,y+20,"white",i-1,j-1)
            rect.update()
            row.append(rect)
            x = x1
            if  j == number_of_squaresH:
                y = y + 20
                x = 0
                grid.append(row) # creates the grid one row at a time so I can create the matrix as well
  
def leftClick(event):
    canvas.focus_set()
    x = event.x # takes the input of the user
    y = event.y
    global step
    global end_i
    global end_j

    for i in range(number_of_squaresV):
        for j in range(number_of_squaresH):
            if x > grid[i][j].x1 and x <= grid[i][j].x2 and y > grid[i][j].y1 and y <= grid[i][j].y2:
                if step == 1:
                    grid[i][j].color ="green"
                    i_start = i
                    j_start = j 
                    queue.add(grid[i][j])
                    grid[i][j].previous = 0
                    step += 1        
                elif step == 2:
                    grid[i][j].color ="red"
                    end_i = i
                    end_j = j
                    step+= 1
                elif step == 3 and grid[i][j].color != "green" and grid[i][j].color!= "red" :
                    grid[i][j].color = "grey"
                grid[i][j].update()
def keyEvent(event):
    if step == 3 and event.keysym == "Return":
        Lee()

createGrid()
canvas.bind("<Key>", keyEvent)
canvas.bind("<Button-1>",leftClick)
canvas.pack()

def isOk(i,j):
    if i < 0 or i > 29 or j < 0 or j > 29:# checks if i and j are stil within the grid
        return False
    return True

def Lee():
    ok = False
    while not queue.empty() and ok == False:
        node = queue.get()
        current_i = node.i
        current_j = node.j
        grid[current_i][current_j].visited = True
        for k in range(8):
            new_i = current_i + dirI[k]
            new_j = current_j + dirJ[k]
            if isOk(new_i,new_j) and grid[new_i][new_j].color != 'grey' and grid[new_i][new_j].visited == False :
                grid[new_i][new_j].previous = grid[current_i][current_j]
                grid[new_i][new_j].visited = True

                if new_i == end_i and new_j == end_j:
                    ok = True
                    print("found it")
                queue.add(grid[new_i][new_j])
        queue.delete()        
    if ok == False:
        print("no path")
    if ok == True:
        current_node = grid[end_i][end_j]
        while current_node.previous != 0  :
            current_node = current_node.previous
            if current_node.color == "green":
                break
            current_node.color= "yellow"
            current_node.update()

app.mainloop()

