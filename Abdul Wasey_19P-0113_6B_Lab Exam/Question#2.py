from queue import PriorityQueue #priority Que is a datastructre, that organises item based on a item I set , think of it like a dictionary of lists or somthing

class State(object):  #this is base class that is going to be used to store all the imperative stuff that we will use for the A* algorithm

    def __init__(self, value, parent, #this is so that we dont have a inital start state and no values we can then initialize and give it 0 values
                 start = 0,
                 goal = 0):

        self.children = [] # all nerighbouring tiles to current tile
        self.parent = parent
        self.value = value
        self.dist = 0

        if parent:#if parent is plugged in, copy the parent's path to our path
            self.start  = parent.start #[:] it copies the parent list to self list, if this were not present the duplication would continue
            self.goal   = parent.goal #we store our value and making track of where we're at
            self.path   = parent.path[:]
            self.path.append(value)
        else: # if there is no parent
            self.path   = [value]#we are starting a path with list of objects starting with our current value 
            self.start  = start
            self.goal   = goal

    def GetDistance(self): #simple function 1 defined below
        pass

    def CreateChildren(self):  #simple function 2 defined below
        pass

class State_String(State):
    def __init__(self,value,parent,
                 start = 0,
                 goal = 0):

        super(State_String, self).__init__(value, parent, start, goal) #initaling the base class in the constructor
        self.dist = self.GetDistance()#function called from below, this function would meausre our distance from our goal

    def GetDistance(self):

        if self.value == self.goal: #if goal has been reached
            return 0
        dist = 0
        for i in range(len(self.goal)): #we will go through each letter of the goal
            letter = self.goal[i]  #we get the letter
            try:
                dist += abs(i - self.value.index(letter)) #we find the index of that letter in our current value and subtract that from where we are currently at
            except:
                dist += abs(i - self.value.find(letter)) #we find the index of that letter in our current value and subtract that from where we are currently at
        return dist #distance of letter from its target placement

    def CreateChildren(self):
        if not self.children: # if there are no children then we create children, this is just a extra precaution inorder to avoid extra children
            for i in range(len(self.goal)-1):
                val = self.value
                val = val[:i] + val[i+1] + val[i] + val[i+2:]
                child = State_String(val, self) #child created with value and self(parent created)
                self.children.append(child)# we add that child to our children list

class AStar_Solver:
    def __init__(self, start , goal):
        self.path          = [] # it is going to store the final path from the start state to the end state
        self.visitedQueue  = []  # it is going to keep track of all children visited so we dont end up visiting children twice
        self.priorityQueue = PriorityQueue()
        self.start         = start
        self.goal          = goal

    def Solve(self):
        startState = State_String(self.start,
                                  0,
                                  self.start,
                                  self.goal)

        count = 0 #id for each child being created
        self.priorityQueue.put((0,count,startState)) #put is basically like add , 0 is the priority number ,

        while(not self.path and self.priorityQueue.qsize()):#while the path is empty and while the priority que has a size
            closestChild = self.priorityQueue.get()[2]#grab the start state , the two here gets the 3rd item in the tupple which in this case is startState
            closestChild.CreateChildren() # now that we have the state we can create children for that state
            self.visitedQueue.append(closestChild.value) #adds the closed child to the vsitied que list, visitedQueue is made to keep track of all children we've visited

            for child in closestChild.children:
                if child.value not in self.visitedQueue:
                    count +=1
                    if not child.dist:#if child's distance is at zero adn does not exist
                        self.path = child.path
                        break# this would take us out of the for loop into the while loop
                    self.priorityQueue.put((child.dist,count,child))

        if not self.path:#if we still have not found a path yet then we know that the priority que condition from the while loop broke, there were no more children in the priority que
            print("Goal of %s is not possible!" % (self.goal))

        return self.path

#main function 

if __name__ == "__main__":
    start1 = "SACDBFEG"
    goal1  = "SABCDEFG"
    print("Here we go")

    a = AStar_Solver(start1, goal1)
    a.Solve()

    for i in range(len(a.path)): #just outputting the results
        print("{0}) {1}".format(i, a.path[i]))