class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        prereqs = defaultdict(set)
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for a,b in prerequisites:
            indegree[b] += 1
            graph[a].append(b)  
            prereqs[b].add(a)
        

        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        while q:
            node = q.popleft()
            for neighbor in graph[node]:
                prereqs[neighbor] |= prereqs[node]
                prereqs[neighbor].add(node)
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        final = []

        for preq, course in queries:
            if preq in prereqs[course]:
                final.append(True)
            else:
                final.append(False)
        
        return final

