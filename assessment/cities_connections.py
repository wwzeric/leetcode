# There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

# Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

# This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

# Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

# It's guaranteed that each city can reach city 0 after reorder.

 

# Example 1:


# Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
# Output: 3
# Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
# Example 2:


# Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
# Output: 2
# Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
# Example 3:

# Input: n = 3, connections = [[1,0],[2,0]]
# Output: 0

def minReorder( n, connections) -> int:

        # d=dict.fromkeys(range(1,n+1), [])
        d={i:[] for i in range(n)}
        for a in connections:
            # if a[0] not in d: 
            #     d[a[0]]=[(a[1],-1)]
            # else: 
            #     d[a[0]].append((a[1],-1))
            # if a[1] not in d: 
            #     d[a[1]]=[(a[0],1)]
            # else: 
            #     d[a[1]].append((a[0],1))
            d[a[0]].append((a[1],-1))
            d[a[1]].append((a[0],1))
       
        if d[0]: q=d[0]*1
        else: return False
        s=set()
        s.add(0)
        count=0
        while q:
            b=q.pop(0)
            
            if b[0] not in s:
                if b[1]==-1:
                    count+=1
                q+=d[b[0]]
                s.add(b[0])
        return count
