n, m = map(int, input().split())

no_listen = []
no_see = []

for _ in range(n):
    no_listen.append(input())

for _ in range(m):
    no_see.append(input())

no_see_listen = sorted(list(set(no_listen) & set(no_see)))

print(len(no_see_listen))
for name in no_see_listen:
    print(name)

