class solution:
    def printNumber2(self,n):
        if n<0:
            return
        else:
            print(n,end=" ")
        self.printNumber2(n-1)
obj=solution()
n=int(input())
obj.printNumber2(n)
