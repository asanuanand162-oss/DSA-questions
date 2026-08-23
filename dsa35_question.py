class Solution:
    def prime(self, n):
        count=0
        for i in range(1,n+1):
            if n%i==0:
                count+=1
        if count==2:
            print(f"the number is prime")
        else:
            print(f"the number is not prime")
            
obj=Solution()
n=int(input("enter a number: "))
obj.prime(n)
