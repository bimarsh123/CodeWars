def PersistenceBugger(n):
    count=0
    while(int(n)>9):
        count+=1
        a=str(n)
        result = 1
        for i in a:
            result*=i
        n=result
    return count
