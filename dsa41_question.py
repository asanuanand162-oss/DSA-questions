class solution:
    def fact(self,n):
        if n==0:
            return 1
        elif n==1:
            return 1
        else:
            return n*self.fact(n-1)
obj=solution()
n=int(input())
print(obj.fact(n))
