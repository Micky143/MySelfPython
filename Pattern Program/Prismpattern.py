n=int(input("enter the number:"))
"""
Output:
**********
****  ****
***    ***
**      **
*        *
"""
for  i in range(0,n):
    
    for j in range(n,0,-1):
        print("*",end='')
    
    for s in range(0,i):
        print("  ",end='' )
    for r in  range(0,i):
        print("  ",end='')
    for k in range(n,0,-1):
        print("*",end='')
    n=n-1
    print("\r")
    
    


    
