def mergesort (s):
    n = len(s)
    if (n <= 1):
        return s
    else:
        mid = n // 2
        u = mergesort(s[0:mid])
        v = mergesort(s[mid:n])
        return merge(u, v)
    
def merge(u, v):
    s = []
    i = j = 0
    while i < len(u) and j < len(v):
        if u[i] < v[j]:
            s.append(u[i])
            i += 1
        else:
            s.append(v[j])
            j += 1
    if i < len(u):
        s += u[i : len(u)]
    else:
        s += v[j : len(v)]
    return s