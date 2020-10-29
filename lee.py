class PriorityQueue(): #actually a normal queue but I should make it a priority one:P
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
# checks if the position is valid
def isOK(i,j):
    if i < 0 or i > 5 or j <0 or j > 4 :
        return False
    if maze[i][j] == "#":
        return False
    return True
def Lee():
    queue =PriorityQueue()
    dirI = [-20,20,0,0]
    dirJ = [0,0,-20,20]
    

moves = []  
#initialize the matrix that holds the shortest path
for i in range(0,6):
    a.append([-1,-1,-1,-1,-1])

l1 = queue.get()
a[l1[0]][l1[1]] = 0 #the shortest path to the start is 0

ok = False
while  not queue.empty() and ok == False:
    l1 = queue.get()
    prev_i = l1[0]
    prev_j = l1[1]
    for k in range(0,4):
        new_i = prev_i + dirI[k]
        new_j = prev_j + dirJ[k]

        if isOK(new_i,new_j) and a[new_i][new_j]== -1:
            a[new_i][new_j] = a[prev_i][prev_j]+1
            if maze[new_i][new_j] == "F":
                ok = True
                final_i = new_i
                final_j = new_j
            queue.add([new_i,new_j])
    queue.delete()
# if the maze has solution 

if ok == True:
    x = a[final_i][final_j]
    while x != 0 :
        for k in range(0,4):
            new_i = final_i + dirI[k]
            new_j = final_j + dirJ[k]
            if isOK(new_i,new_j) and a[new_i][new_j] == x-1:
                final_i= new_i
                final_j = new_j
                if maze[new_i][new_j] != 'S':
                    maze[new_i][new_j] = "+"
                x -=1 