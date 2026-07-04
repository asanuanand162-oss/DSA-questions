class solution:
    def pattern16(self,n):
        ch="A"
        for i in range(n):
            for j in range(i+1):
                print(ch,end="")
            print()
            ch=chr(ord(ch)+1)
obj=solution()
n=int(input("enter the number: "))
obj.pattern16(n)


