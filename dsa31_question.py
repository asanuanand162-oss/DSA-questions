class Solution:
    def palindrom(self, n):
        original=n
        r=0
        while n>0:
            digit=n%10
            r=r*10+digit
            n//=10
        if r==original:
            print("palindrome number")
        else:
            print("not palindrom number")
obj=Solution()
n=int(input("enter a number: "))
obj.palindrom(n)
            
