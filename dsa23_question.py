class Solution:
    def pattern17(self, n):
        for i in range(1,n+1):
            for j in range(n-i):
                print(" ",end="")
            ch="A"
            for k in range(i):
                print(ch,end="")
                ch=chr(ord(ch)+1)
            ch=chr(ord("A")+i-2)
            for k in range(i-1):
                print(ch,end="")
                ch=chr(ord(ch)-1)
            print()
obj=Solution()
n=int(input("enter the number: "))
obj.pattern17(n)
