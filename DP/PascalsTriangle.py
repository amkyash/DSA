def pas(n):
    #First Row
    res=[[1]]
    
    #for the rest of rows
    for i in range(n-1):
        #creating temp row  for adding Extra 0 at start and end
        temp=[0]+ res[-1]+[0]
        row=[]

        for j in range( len(res[-1]) + 1 ):
            row.append(temp[j]+temp[j+1])
        res.append(row)
    return res

if __name__== "__main__":
    n=int(input())
    print(pas(n))
