def gbfs(GRAPH,start,end):
    explored=[]
    queue=[start]
    while queue:
        print(queue)
        node =queue.pop(0)
        if node not in explored:
            explored.append(node)
            if node == end:
                break
            neighbors = GRAPH[node]
            neighbors.sort(key=Lambda :a[1])
            print(neighbors)
            queue=neighbors.pop(0)
    print(explored)

GRAPH={

}

Start = input("Enter Starting node")
End = input("Enter Ending node")
print("\nGBFS from Starting node to Goal node")

gbfs(GRAPH, Start, End)
