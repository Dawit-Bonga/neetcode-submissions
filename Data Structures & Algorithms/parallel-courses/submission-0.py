class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for a,b in relations:
            indegree[a] = 0
            indegree[b] = 0
        for a,b in relations:
            graph[a].append(b)
            indegree[b] += 1
        
        q = deque()
        for i, degree in indegree.items():
            if degree == 0:
                q.append(i)
        
        numSemesters = 0
        coursesTaken = 0
        while q:
            print(q)
            for _ in range(len(q)):
                curr = q.popleft()
                coursesTaken += 1

                for nei in graph[curr]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)
            numSemesters += 1
        
        return numSemesters if coursesTaken == n else -1




