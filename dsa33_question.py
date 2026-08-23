class Solution:
    def armstrong(self, n):
        num=c=n
        sum=0
        count=0
        while c>0:
            count+=1
            c//=10
        while n>0:
            digit=n%10
            sum+=digit**count
            n//=10
        if num==sum:
            print("given number is armstrong")
        else:
            print("given number is not armstrong")
obj=Solution()
n=int(input("enter a first number: "))
obj.armstrong(n)
