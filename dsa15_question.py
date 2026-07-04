class solution:
    def pattern9(self,n):
        for i in range(1,n+1):
            for j in range(n-i):
                print(" ",end="")
            for k in range(i*2-1):
                print("*",end="")
            print()
        for i in range(n,0,-1):
            for j in range(n-i):
                print(" ",end="")
            for k in range(i*2-1):
                print("*",end="")
            print()
obj=solution()
n=int(input("enter any integer number: "))
obj.pattern9(n)
