def bfs_matrix(graph, start_node, total_nodes, k):
    visited = [False] * total_nodes
    queue = []

    visited[start_node] = True #start node is the index
    queue.append(start_node)   

    # "1st" level is level 0
    level = 0
    visited_count = 0

    while queue and visited_count < k:
        level_size = len(queue) # queue tracks the size of the level
                                # so we use this to tell when we're finished processing a level
                                # thus telling us which level we're currently on

        for _ in range(level_size):       # _ is a placeholder variable. Just makes writing slightly easier....

            current_node = queue.pop(0) 
            connection = 0 

            while connection < total_nodes:

                if graph[current_node][connection] == 1 and visited[connection] == False:

                    queue.append(connection)   # queue stores everything on the current level
                    visited[connection] = True # track visited nodes
                    visited_count += 1         

                    if visited_count >= k:     # if we've reached target, return level + 1
                        return level + 1

                connection += 1                # increment the next node we're checking for connection

        level += 1                             # track new level

    return level

#MAIN CALLING ROUTINE

adjacency_matrix1 = [
    [0,0,0,0,0,1], #0
    [0,0,1,1,0,0], #1
    [0,1,0,1,1,0], #2
    [0,1,1,0,1,1], #3
    [0,0,1,1,0,0], #4
    [1,0,0,1,1,0]  #5
]

adjacency_matrix2 = [
    [0,1,1,1,0,0], #0
    [1,0,0,0,0,1], #1
    [1,0,0,1,0,0], #2
    [1,0,1,0,1,0], #3
    [0,0,0,1,0,1], #4
    [0,0,0,0,1,0]  #5
]

adjacency_matrix3 = [
    [0,1,1,0,1,0,0], #0
    [1,0,0,1,0,0,0], #1
    [1,0,0,0,1,0,0], #2
    [0,1,0,0,0,0,1], #3
    [1,0,1,0,0,1,0], #4
    [0,0,0,0,1,0,0], #5
    [0,0,0,1,0,0,0], #6
]

adjacency_matrix4 = [
    [0,1,1,0,0,0,0,0], #0
    [1,0,0,1,1,0,0,0], #1
    [1,0,0,0,0,1,0,0], #2
    [0,1,0,0,1,0,1,0], #3
    [0,1,0,1,0,0,0,1], #4
    [0,0,1,0,0,0,1,0], #5
    [0,0,0,1,0,1,0,1], #6
    [0,0,0,0,1,0,1,0]  #7
]

adjacency_matrix5 = [
    [0,1,1,0,0], #0
    [1,0,1,1,1], #1
    [1,1,0,0,1], #2
    [0,1,0,0,1], #3
    [0,1,1,1,0]  #4
]


level = bfs_matrix(adjacency_matrix5, 0, len(adjacency_matrix5), 3)
print(level)


