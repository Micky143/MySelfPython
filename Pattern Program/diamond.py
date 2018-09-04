n=int(input("enter the number:"))
"""
Shorter way to print the diamond pattern
def pattern5(n):
    for i in range(n):
        print ("  "*(n-i-1) + "*"*(2*i+1))
    for i in range(n-1,-1,-1):
        print ('  '*(n-i-1) + "*"*(2*i+1))

Output:
     *
    ***
   *****
  *******
 *********
  *******
   *****
    ***
     *
"""


for i in range(n):
        for j in range(n-i):
            print("  ",end='')
           
        for k in range(i*2-1):
            print("*",end='')
        print()
for i in range(n,0,-1):
        for j in range(n-i):
            print("  ",end='')
           
        for k in range(i*2-1):
            print("*",end='')
        print()


