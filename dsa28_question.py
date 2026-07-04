class Solution:
    def pattern22(self, n):
        s=2*n-1
        for i in range(s):
            for j in range(s):
                top=i
                left=j
                right=s-1-j
                bottom=s-1-i
                m=min(left,right,top,bottom)
                print(n-m,end=" ")
            print()
obj=Solution()
n=int(input("enter the number: "))
obj.pattern22(n)
