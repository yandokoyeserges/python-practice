class KriskalMST:
    def _ini_(self,vertices):
        self.V=vertices
        self.graph=[]

    def add_edge(self,u,v,w):
        self.graph.append([u,v,w])

    def find_parent(self,parent,i):
        if parent == i:
            return i
        return self.find_parent(parent,parent[i])

    def union(self,parent,rank,x,y):
        xroot=self.find_parent(parent,x)
        yroot=self.find_parent(parent,y)

        if rank[xroot]<rank[yroot]:
            parent[xroot]=yroot
        elif rank[xroot]>rank[yroot]:
            parent[yroot]=xroot
        else:
            parent[yroot] = xroot
            rank[xroot] +=1

    def kriskal_mst(self):
        result=[]
        i,e=0,0
        self.graph=sorted(self.graph,key=lambda item:item[2])
        parent=[]
        rank=[]
        for node in range(self.V):
          parent.append(node)
          rank.append(0)

        while e<self.V-1:
            u,v,w=self.graph[i]
            i=i+1
            x=self.find_parent(parent,u)
            y=self.find_parent(parent,v)

            if x!=y:
                e=e+1
                result.append([u,v,w])
                self.union(parent,rank,x,y)
        minimum_cost=0
        print("Edges in the constructed MST:")
        for u,v,weight in result:
            minimum_cost +=weight
            print(f"{u}____{v}=={weight}")
        print(f"minimum spanning tree is:{minimum_cost}")
#example usage
g=KriskalMST()
g.add_edge(0,1,10)
g.add_edge(0,2,6)
g.add_edge(0,3,5)
g.add_edge(0,1,10)
g.add_edge(1,3,15)
g.add_edge(2,3,4)
g.kriskal_mst()












