class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # build graph
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for start, dest in sorted(tickets)[::-1]:
            graph[start].append(dest)
            indegree[dest] += 1
        

        final = []
        def dfs(src):
            while graph[src]:
                destination = graph[src].pop()
                dfs(destination)
            final.append(src)


        beginning = "JFK"
        dfs(beginning)
        print(final)
        return final[::-1]

        