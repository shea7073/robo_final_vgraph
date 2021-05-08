# Sean Shea
# Grad Robotics Final, Vgraph implementation
# May 7, 2021

world = [[True, False, False, False, False, False],
         [False, False, False, False, False, False],
         [False, False, True, True, False, False],
         [False, False, True, True, False, False],
         [False, False, False, False, False, False],
         [False, False, False, False, False, True]]

# written assuming the world map is square

def vgraph(grid):
    graph = {}
    vertex_counter = 0
    vertex_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(len(grid)):
        for j in range(len(grid)):
            counter = 0
            current = grid[i][j]
            if current:
                if i > 0:
                    above = grid[i-1][j]
                else:
                    above = None
                if j > 0:
                    left = grid[i][j-1]
                else:
                    left = None
                if j < (len(grid) - 1):
                    right = grid[i][j+1]
                else:
                    right = None
                if i < (len(grid) - 1):
                    below = grid[i+1][j]
                else:
                    below = None
                if not above:
                    counter += 1
                if not left:
                    counter += 1
                if not right:
                    counter += 1
                if not below:
                    counter += 1
                if counter >= 2:
                    graph[vertex_names[vertex_counter]] = {'coordinates': (i, j)}
                    vertex_counter += 1
    for start_vertex in graph:
        for possible_connection in graph:
            if graph[start_vertex] == graph[possible_connection]:
                # meaning start and end are the same node
                pass
            startx, starty = graph[start_vertex]['coordinates']
            endx, endy = graph[possible_connection]['coordinates']
            #equation of the line
            if endx - startx == 0:
                slope = 'undefined'
                y_intercept = None
            else:
                slope = (endy - starty) / (endx - startx)
                y_intercept = starty - (slope*startx)
                # y = slope*x = y_intercept
        # The goal here was to find which vertices were reachable from
        # each other vertex without intersecting another vertex
        # which would have resulted in perfect edges of vgraph

print(vgraph(world))
