n=int(input("enter the number"))
def pattern1(n):
    
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end=' ')
        print("\r")
        
pattern1(n)
