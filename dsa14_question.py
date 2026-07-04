class solution:
    def pattern7(self,n):
        for i in range(n,0,-1):
            for j in range(n-i):
                print(" ",end="")
            for k in range(i*2-1):
                print("*",end="")
            print()
obj=solution()
n=int(input("enter any integer number: "))
obj.pattern7(n)

