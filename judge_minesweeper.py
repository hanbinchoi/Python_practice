matrix=[]

col,row=map(int,input().split())


for i in range(row):
    matrix.append(list(input()))

for i in range(row):
    
    for j in range(len(matrix[i])):
        count=0
        if(matrix[i][j]=='*'):
            print('*',end='')
        else:
            if i==0:
                
                if j==0:                    
                    if matrix[i+1][j] =='*':
                        count+=1
                    if matrix[i][j+1] =='*':
                        count+=1
                    if matrix[i+1][j+1] =='*':
                        count+=1
                        
                elif j==len(matrix[i]-1):
                    if matrix[i+1][j]=='*':
                        count+=1
                    if matrix[i][j-1]=='*':
                        count+=1
                    if matrix[i+1][j-1]=='*':
                        count+=1

                else:
                    if matrix[i+1][j]=='*':
                        count+=1
                        
                    if matrix[i][j-1]=='*':
                        count+=1
                    if matrix[i][j+1]=='*':
                        count+=1

                    if matrix[i-1][j-1]=='*':
                        count+=1
                    if matrix[i+1][j+1]=='*':
                        count+=1

            if
        print(count,end='')
    print()
