n = int(input()) 
a = [] 
b = [[1, 2, 4, 6, 8, 9], [3, 4, 8], [1, 4, 7, 9], [1, 3, 5, 7], [2, 4, 5, 8], [1, 2, 5, 8, 9], [3, 5, 6, 8, 9], 
[1, 3, 6], [1, 2, 4, 5, 6, 8, 9], [1, 2, 4, 5, 7]] 
c = [0] * 10 
for i in range(n): 
    a.append(int(input())) 
for j in range(len(b[a[i]])): 
    c[b[a[i]][j]] = 1 
for i in range(10): 
    ok = True 
for j in range(len(b[i])): 
    if not c[b[i][j]]: 
        ok = False 
if ok: 
    print(i)