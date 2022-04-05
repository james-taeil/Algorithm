def DFS(x,s,time) : 
    global res
    if time > m:
        return
    if x == n:
        if s > res:
            res = s
    else:
        DFS(x+1, s+pv[x] , time+pt[x]) 
        DFS(x+1, s, time)
        
if __name__=='__main__' : 
    n, m = map(int, input().split())
    pv =list()
    pt=list()
    for i in range(n) :
        a,b = map(int, input().split())
        pv.append(a)
        pt.append(b)
    res=-1
    DFS(0,0,0)
    print(res)