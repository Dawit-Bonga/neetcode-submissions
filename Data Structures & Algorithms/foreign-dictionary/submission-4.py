class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        indegree = {}
        adj_list = defaultdict(set)

        for word in words:
            for c in word:
                indegree[c] = 0
        


        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            
            for j in range(len(w2)):
                if j >= len(w1):
                    break
                
                if w1[j] != w2[j]:
                    if w2[j] not in adj_list[w1[j]]:
                        indegree[w2[j]] += 1
                        adj_list[w1[j]].add(w2[j])
                    break
        
        q = deque()
        for char in indegree.keys():
            if indegree[char] == 0:
                q.append(char)
        print(q)
        final = []
        while q:
            node = q.popleft()
            final.append(node)

            for nei in adj_list[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        print(final)
        return "".join(final) if len(indegree) == len(final) else ""



