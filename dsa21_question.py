class solution:
    def pattern15(self,n):
        for i in range(n,0,-1):
            ch="A"
            for j in range(i):
                print(ch,end="")
                ch=chr(ord(ch)+1)
            print()
obj=solution()
n=int(input("enter the number: "))
obj.pattern15(n)


