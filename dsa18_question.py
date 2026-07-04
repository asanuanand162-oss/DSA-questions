class solution:
    def pattern12(self,n):
        for i in range(1,n+1):
            space=2*(n-i)
            for j in range(1,i+1):
                print(j,end="")
            for k in range(space):
                print(" ",end="")
            for j in range(i,0,-1):
                print(j,end="")
            print()
obj=solution()
n=int(input("enter the number: "))
obj.pattern12(n)
