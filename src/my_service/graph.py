from collections import defaultdict


squars = [x**2 for x in range(10)]
print(squars)

def apply_twice(func, arg):
    return func(func(arg))

def add_five(x) -> int:
    return x + 5;

print(apply_twice(add_five, 10))

def test():
    word_count = defaultdict(int)

    words = ["apple", "banana", "orange", "banana", "apple"]

    for word in words:
        word_count[word] += 1

    print(word_count)

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def dfs_util(self, v, visited):
        visited.add(v)
        print(v, end=" ")

        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)
    
    def dfs(self, start):
        visited = set()
        self.dfs_util(start, visited)
    
        
if __name__ == "__main__": # type: ignore
    test()
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 1)
    graph.dfs(0)


