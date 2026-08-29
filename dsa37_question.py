class Solution:
    def printNumber(self,i, N):
        if i>N:
           return
        print(i)
        self.printNumber(i+1, N)
obj= Solution()
N=int(input("enter a number: "))
obj.printNumber(1, N)
