class Solution:
    def pattern19(self, n):
        s=0
        for i in range(n):
            for j in range(n-i):
                print("*",end="")
            for k in range(s):
                print(" ",end="")
            for j in range(n-i):
                print("*",end="")
            print()
            s+=2
        for i in range(1,n+1):
            for j in range(i):
                print("*",end="")
            for k in range(2*(n-i)):
                print(" ",end="")
            for j in range(i):
                print("*",end="")
            print()
obj=Solution()
n=int(input("enter a number: "))
obj.pattern19(n)
