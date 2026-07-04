class Solution:
    def pattern1(self, n):
        for i in range(n):
            for j in range(i+1):
                print("*",end="")
            print()
obj=Solution()
n=int(input("enter a number of rows: "))
obj.pattern1(n)
