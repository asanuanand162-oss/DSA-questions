class solution:
    def pattern14(self,n):
        for i in range(n):
            ch="A"
            for j in range(i+1):
                print(ch,end=" ")
                ch=chr(ord(ch)+1)
            print()
obj=solution()
n=int(input("enter the number: "))
obj.pattern14(n)

