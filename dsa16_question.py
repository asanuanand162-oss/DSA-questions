class solution:
    def pattern10(self,n):
        for i in range(n):
            for j in range(i+1):
                print("*",end="")
            print()
        for i in range(n-1,0,-1):
            for j in range(i):#as the j is starting from 0
                print("*",end="")
            print()
obj=solution()
n=int(input("enter any integer number: "))
obj.pattern10(n)

