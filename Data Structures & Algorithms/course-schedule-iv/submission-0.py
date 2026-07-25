class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        in_degree = [0] * numCourses
        graph = defaultdict(set)

        for src, dst in prerequisites:
            in_degree[dst] += 1
            graph[src].add(dst)
        
        def bfs(start, end):
            q = deque([start])
            visited = set()

            while (q):
                curr = q.popleft()
                visited.add(curr)
                if curr == end:
                    return True

                for nei in graph[curr]:
                    if nei not in visited:
                        q.append(nei)
            
            return False
            
        answer = []
        for src, dst in queries:
            answer.append(bfs(src, dst))
        return answer
