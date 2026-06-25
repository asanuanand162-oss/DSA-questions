class Solution:
    def whileLoop(self, d : int) -> int:
        # Your code goes here
        n=50
        sum=0
        while n>0:
            sum+=d
            n-=1
            d+=10
        print(sum)
obj=Solution()
d=int(input("enter a number:"))
obj.whileLoop(d)
