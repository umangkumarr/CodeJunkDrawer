
def matrixRotation(matrix, r):
    mat=[]
    k=min(m,n)//2
    for i in range(k):
        temp=[]
        for j in range(i,n-1-i):
            temp.append(matrix[i][j])
        for j in range(i, m-1-i):
            temp.append(matrix[j][n-i-1])
        for j in range(n-1-i,i,-1):
            temp.append(matrix[m-1-i][j])
        for j in range(m-1-i,i,-1):
            temp.append(matrix[j][i])
        mat.append(temp)
    for i in range(k):
        row = mat[i]
        idx=r%len(row)
        def inc():
            return (idx+1)%len(row)
        for j in range(i,n-1-i):
            matrix[i][j]=row[idx]
            idx=inc()
        for j in range(i, m-1-i):
            matrix[j][n-1-i]=row[idx]
            idx=inc()
        for j in range(n-1-i,i,-1):
            matrix[m-i-1][j]=row[idx]
            idx=inc()
        for j in range(m-i-1,i,-1):
            matrix[j][i]=row[idx]
            idx=inc()
    for tt in matrix:
        print(*tt)