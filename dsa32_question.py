class Solution:
    def gdc(self, n1,n2):
        for i in range(1,min(n1,n2)+1):
            if n1%i==0 and n2%i==0:
                gdc=i
        print(gdc)
obj=Solution()
n1=int(input("enter a first number: "))
n2=int(input("enter a second number: "))
obj.gdc(n1,n2)
            

