n=int(input("enter the number:"))
"""
This function is to print the star pattern in the fan's blade format

OUTPUT:

*   *****
**  ****
*** ***
******
*********
   ******
  *** ***
 ****  **
*****   *
"""
for i in range(1,n+1):
    if i==n:                                                        #It will print the straight line of the stars
        print("*"*(n+n-1),end='')
    else:
        for j in range(i):
            print("*",end='')
        for k in range(n-(i+1)):
            print("  ",end='')
        for l in range((n+1)-i):
            print("*",end='')
    print()
for p in range(2,n+1):
    for q in range(n-p):
        print("  ",end='')
    for r in range(p):
        print("*",end='')
    for s in range(p-2):
        print("  ",end='')
    for t in range((n+1)-p):
        print("*",end='')
    print()
