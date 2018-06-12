t = int(input())
for ti in range(t):
    p, q, r = tuple(map(int, input().rstrip().split()))
    print((r - q - 1) if (r - q) > (q - p) else (q - p - 1))
