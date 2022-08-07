from collections import deque

n, m, v = map(int, input().split())

adj = [[] for _ in range(n + 1)]
isvisited_dfs = [False] * (n + 1)
isvisited_bfs = [False] * (n + 1)
result_dfs = []
result_bfs = []

for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

for i in range(n + 1):
    adj[i].sort()

def dfs(now_pos):
    isvisited_dfs[now_pos] = True
    result_dfs.append(now_pos)
    for next_pos in adj[now_pos]:
        if isvisited_dfs[next_pos]:
            continue
        else:
            dfs(next_pos)

def bfs(v):
    q = deque([v])
    isvisited_bfs[v] = True
    while q:
        for e in adj[q[0]]:
            if isvisited_bfs[e]:
                continue
            else:
                isvisited_bfs[e] = True
                q.append(e)
        result_bfs.append(q.popleft())

dfs(v)
bfs(v)
print(' '.join(list(map(str, result_dfs))))
print(' '.join(list(map(str, result_bfs))))

