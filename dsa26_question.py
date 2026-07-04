class Solution:
    def pattern20(self, n):
        for i in range(1,n+1):
            for j in range(i):
                print("*",end="")
            for k in range(2*(n-i)):
                print(" ",end="")
            for j in range(i):
                print("*",end="")
            print()
        for i in range(n-1,0,-1):
            for j in range(i):
                print("*",end="")
            for k in range(2*(n-i)):
                print(" ",end="")
            for j in range(i):
                print("*",end="")
            print()
obj=Solution()
n=int(input("enter the number: "))
obj.pattern20(n)
