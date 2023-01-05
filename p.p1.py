def printreverse(inp):
    inp=[i[::-1] for i in inp]
    return inp
n=input().split()
print(*printreverse(n))
