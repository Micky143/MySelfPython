n=int(input("enter the number:"))
"""
Output:
        1
      123
    12345
  1234567
123456789
  1234567
    12345
      123
        1

"""
for i in range(n):
        for j in range(n-i):
            print("  ",end='')
           
        for k in range(i*2-1):
            print(k+1,end='')
        print()
for i in range(n,0,-1):
        for j in range(n-i):
            print("  ",end='')
           
        for k in range(i*2-1):
            print(k+1,end='')
        print()

