class Solution:
    def reverse(self, n):
        r=0
        while n>0:
            digit=n%10
            r=r*10+digit
            n//=10
        print(r)
obj=Solution()
n=int(input("enter a number: "))
obj.reverse(n)
            
