class Solution:
    def pattern18(self, n):
        for i in range(1,n+1):
            ch=chr(ord("A")+n-i)
            for j in range(i):
                print(ch,end=" ")
                ch=chr(ord(ch)+1)
            print()
obj=Solution()
n=int(input("enter the number: "))
obj.pattern18(n)

