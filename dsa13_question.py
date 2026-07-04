class solution:
    def pattern7(self,n):
        for i in range(1,n+1):
            for j in range(n-i):
                print(" ",end="")
            for k in range(i*2-1):
                print("*",end="")
            print()
obj=solution()
n=int(input("enter any integer number: "))
obj.pattern7(n)
