class Solution:
    def forLoop(self, low : int, high : int) -> int:
        # Your code goes here
        sum=0
        for i in range(low,high+1):
            sum+=i
        print( sum)
obj=Solution()
low=int(input("enter the lowest value: "))
high=int(input("enter the highest value: "))
obj.forLoop(low,high)
