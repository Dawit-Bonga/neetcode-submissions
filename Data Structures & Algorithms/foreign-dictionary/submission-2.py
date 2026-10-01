class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #so it's either "" or every string in word sorted so I might need to sort by making
        indegree = defaultdict(int)

        adj_list = defaultdict(set)

        for word in words:
            for char in word:
                indegree[char] = 0

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            prev = None
            w = None

            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            for j in range(len(w2)):
                if j >= len(w1):
                    break
                elif w1[j] != w2[j]:
                    w = w2[j]
                    prev = w1[j]
                    break
                
            if w:
                if w not in adj_list[prev]:
                    adj_list[prev].add(w)
                    indegree[w] += 1

        q = deque()
        for char in indegree.keys():
            if indegree[char] == 0:
                q.append(char)
        final = []
        while q:
            node = q.popleft()

            final.append(node)

            for c in adj_list[node]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)

        return "".join(final) if len(final) == len(indegree) else ""

            
                