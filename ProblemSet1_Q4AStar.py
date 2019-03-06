from collections import defaultdict
from math import radians, cos, sin, asin, atan2, sqrt
import queue

class Graph: 
  
   
    def __init__(this): 
  
        #Dictionary To Store Entire Graph
        this.graph = defaultdict(list)

        #Dictionary To Hold if Verticie Has Been Visited
        this.visited = defaultdict(bool) 

         # Create an open,closed and expanded list for A*
        this.openlist = queue.PriorityQueue()
        this.closedlist = []
        this.expanded = []
        this.readopenlist = []
       
        # Check if we reached goal state
        this.foundgoal = False;

        this.Start = "";
        this.Goal = "";

        this.miles = 0;
  
    # method to add edge to Node 
    def addEdge(this,u,v,g,h): 
        this.graph[u].append((v,g+h,g))
        this.visited[u] = False 

    # method to set the Goal State
    def setGoal(this,v):
        this.Goal = v  

    def peak(this, pq):
        return pq.get()[2] 

    # method to calculate Heuristic
    def getH(this,lat1, lon1, lat2, lon2):
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = (sin(dlon / 2))**2 + cos(lon1) * cos(lon2) * (sin(dlat / 2))**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        r = 6371
        return r * c

    # Print if we reached a goal state
    def foundState(this, s):
        print(s, " Has been reached and is a Goal State")
           
    # method to run A-Star
    def AStar(this, s): 
  
        print("****AStar Find Cities****")
        print("****Adding Root Node****\n") 

        #Put Root Node in queue and mark as visited
        this.openlist.put((0,s,0))
        this.readopenlist.append(s)
        print(s, " Is the Starting City") 

        this.visited[s] = True
        print("****Finding Cities****")


        # Loop to find other nodes
        while this.openlist: 
  
            # Get Node with lowest Heurisitc
        
            s = this.openlist.get()
            this.readopenlist.remove(s[1])

            
            # If Node is a goal state end program
            if s[1] == this.Goal:
                this.foundState(s[1])
                foundgoal = True
                this.expanded.append(s[1])
                break

            # Add current Node to closed and expanded lists
            this.closedlist.append(s) 
            this.expanded.append(s[1])
            print (s[1], "Is The Next City To Visit\n") 
  
            
            # Find neighbor edges to Node and mark as visited
            for i in this.graph[s[1]]: 
                v = i[0]
                if this.visited[v] == False: 
                    this.openlist.put((i[1]-s[0],v,i[2]))
                    this.readopenlist.append(v)
                    this.visited[v] = True
                          
        if (not foundgoal):
            print("Goal State Not Found")
        print("Cities Visited: ", this.expanded)
        print("Miles Traveled: ", s[0])           

# Driver code 
grid = [
    [0, -1, 713, 1018, -1, 1374, -1, 213, -1, 875, -1, -1, -1],
    [-1, 0, -1, -1, 831, 1240, 959, -1, 403, -1, 1374, 357, 579],
    [713, -1, 0, 355, 920, 803, -1, 851, -1, 262, 940, -1, -1],
    [1018, -1, 355, 0, 700, -1, 1395, 1123, -1, 466, -1, -1, 987],
    [-1, 831, 920, 700, 0, 663, 1021, -1, 949, 796, 879, 586, 371],
    [1374, 1240, 803, -1, 663, 0, -1, -1, -1, 547, 225, 887, 999],
    [-1, 959, -1, 1395, 1021, -1, 0, -1, 678, -1, -1, 1114, 701],
    [213, -1, 851, 1123, -1, -1, -1, 0, -1, 1038, -1, -1, -1],
    [-1, 403, -1, -1, 949, -1, 678, -1, 0, -1, 1645, 653, 600],
    [875, -1, 262, 466, 796, 547, -1, 1038, -1, 0, 679, 1272, 1162],
    [-1, 1374, 940, -1, 879, 225, -1, -1, 1645, 679, 0, -1, 1200],
    [-1, 357, -1, -1, 586, 887, 1114, -1, 653, 1272, -1, 0, 504],
    [-1, 579, -1, 987, 371, 999, 701, -1, 600, 1162, 1200, 504, 0],
]
cities = ['New York', 'Los Angeles', 'Chicago', 'Minneapolis', 'Denver', 'Dallas', 'Seattle', 'Boston', 'San Francisco', 'St. Louis', 'Houston', 'Phoenix', 'Salt Lake City']
coords = [[40.730610, -73.935252], [34.052235, -118.243683], [41.881832, -87.623177], [44.986656, -93.258133], [39.742043, -104.991531], [32.897480, -97.040443], [47.608013, -122.335167], [42.361145, -71.057083], [37.7749, -122.4194], [38.627003, -90.199402], [29.7604, -95.3698], [33.448376, -112.074036], [40.7608, -111.8910]] 

Start = input('start city: ')
Goal = input('goal city: ')

index = cities.index(Goal)
goalLon = coords[index][0]
goalLat = coords[index][1]


g = Graph() 
for i in range(0, len(grid)):
    lat = coords[i][0]
    lon = coords[i][1]
    for j in range(0, len(grid[i])):
         if grid[i][j] > 0:
             h = g.getH(lat,lon,goalLat,goalLon)
             g.addEdge(cities[i],cities[j],grid[i][j],h)

g.setGoal(Goal)
g.AStar(Start)