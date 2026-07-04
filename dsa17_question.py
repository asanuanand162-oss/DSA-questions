class solution:
    def pattern11(self,n):
        for i in range(n):
            if i%2==0:
                b=1
            else:
                b=0
            for j in range(i+1):
                print(b,end=" ")
                b=1-b
            print()
obj=solution()
n=int(input("enter the number: "))
obj.pattern11(n)
