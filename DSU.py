class DSU:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
    
    def get_parent(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.get_parent(self.parent[x])
            return self.parent[x]
    
    def get_size(self, x):
        parent = self.get_parent(x)
        return self.size[parent]
    
    def union(self, x, y):
        x = self.get_parent(x)
        y = self.get_parent(y)
        if self.get_size(x) < self.get_size(y):
            x, y = y, x
        self.parent[y] = x
        self.size[x] = self.size[x] + self.size[y]