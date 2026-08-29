class solution:
    def sum(self,n):
        if n==1:
            return 1
        else:
            return n+self.sum(n-1)
obj=solution()
n=int(input())
print(obj.sum(n))
