def bfs(graph,root):
    visited=[]
    queue=[]
    queue.append(root)

    while queue:
        print(queue)
        vertex = queue.pop(0)
        print(vertex)
        if vertex == 'G':
            return
        
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                queue.append(neighbour)
def dfs(visited,graph,node):
    if node not in visited:
        print(node)
        if node =='G':
            return
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)

if __name__== '__main__':
    graph= {
        'A':['B','C','D'],
        'B':['E','F'],
        'E':['H'],
        'F':['H'],
        'H':[],
        'C':['F','G'],
        'D':['G'],
        'G':['I','J','K'],
        'I':[],
        'J':[],
        'K':[]
        
    }
    
    print(graph)
    print("Following is breadth First Traversal: ")
    bfs(graph,'A')

    print(graph)
    print("Following is Depth-First Traversal: ")
    visited=set()
    dfs(visited,graph,'A')