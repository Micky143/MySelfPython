n=int(input("enter the number:"))
def pattern3(n):
    for i in range(0,n):
        for j in range(0,n-1):
            print(" ",end='')
        n=n-1    
        for k in range(0,i+1):
            print("*",end='')
        print("\r")
    
pattern3(n)
