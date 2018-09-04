n=int(input("enter the number:"))

"""
Program to print the hollow diamond
      
     
"""
for i in range(1,n+1):
    for j in range(n-i):
        print("  ",end='')
    for k in range(i*2):
        if k==0 or k==i*2-1:
            print("*",end='')
        else :

            print("  ",end='')
        
    print()
for i in range(n-1,0,-1):
    for j in range(n-i):
        print("  ",end='')
    for k in range(i*2):
        if k==0 or k==i*2-1:
            print("*",end='')
        else :

            print("  ",end='')
        
    print()
