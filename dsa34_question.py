class Solution:
    def divisor(self, n):
        lst=[]
        for i in range(1,n+1):
            if n%i==0:
                lst.append(i)
        print(lst)
obj=Solution()
n=int(input("enter a number: "))
obj.divisor(n)
