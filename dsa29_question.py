class Solution:
    def countDigit(self, n):
        count=0
        while n>0:
            count+=1
            n//=10
        print(count)
obj=Solution()
n=int(input("enter a number: "))
obj.countDigit(n)
            
