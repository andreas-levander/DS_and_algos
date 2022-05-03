from collections import deque
import heapq

class Vertex:
    def __init__(self, value) -> None:
        self.value = value
        self.edges = {}

    def add_edge(self, vertex: any, dist: int):
        self.edges[vertex] = dist
    
    def __repr__(self) -> str:
        return self.value
    
    def __lt__(self, other):
        return self.value < other.value

stock = Vertex('stockholm')
hel = Vertex('helsinki')
berlin = Vertex('berlin')
london = Vertex('london')
oslo = Vertex('oslo')
vasa = Vertex('vasa')

stock.add_edge(hel,1000)
stock.add_edge(berlin, 1000)
stock.add_edge(vasa, 500)
vasa.add_edge(hel, 300)
hel.add_edge(berlin, 2000)
berlin.add_edge(hel, 900)
berlin.add_edge(london, 3000)
stock.add_edge(oslo, 500)
hel.add_edge(london, 300)
london.add_edge(oslo, 800)

def BFS(start):
    visited = {}
    queue = deque()

    queue.append(start)
    visited[start.value] = True

    while queue:
        current = queue.pop()
        
        print(current.value)

        for edge in current.edges:
            if edge.value not in visited:
                queue.appendleft(edge)
                visited[edge.value] = True

print('Breath First Search:')
BFS(stock)
print('-------------------')

def DFS(vertex, visited = {}):
    print(vertex.value)
    visited[vertex.value] = True

    for edge in vertex.edges:
        if edge.value not in visited:     
            DFS(edge, visited)

print('Depth First Search:')
DFS(stock)
print('-------------------')

def dijkstra(start, end):
    shortest, prev, visited = {}, {}, {}
    pqueue = []

    heapq.heappush(pqueue, (0, start))
    
    shortest[start.value] = 0

    while len(pqueue) > 0:
        (dist, current) = heapq.heappop(pqueue)
        if current.value in visited:
            continue
        
        visited[current.value] = True

        print(dist, current.value)

        for edge, value in current.edges.items():
            current_dist = dist + value
            if edge.value not in shortest or current_dist < shortest[edge.value]:
                shortest[edge.value] = current_dist
                prev[edge.value] = current.value

            if edge.value not in visited:
                heapq.heappush(pqueue, (current_dist, edge))
                

    print(shortest)

    result = [end.value]
    
    cur = prev[end.value]

    while cur != start.value:
        result.append(cur)
        cur = prev[cur]
    
    result.append(start.value)
    result.reverse()
    print(result)


dijkstra(stock, london)
dijkstra(hel, oslo)
    
