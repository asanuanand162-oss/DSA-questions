class Solution:
    def pattern5(self, n):
        for i in range(n,-1,-1):
            for j in range(i):
                print("*",end="")
            print()
obj=Solution()
n=int(input("enter a number of rows: "))
obj.pattern5(n)
