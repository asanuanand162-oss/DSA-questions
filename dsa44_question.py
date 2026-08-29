class solution:
    def fibo(self,n):
        if n==0:
            return 1
        elif n==1:
            return 1
        return self.fibo(n-1)+self.fibo(n-2)  
obj=solution()
n=int(input())
for i in range(n):
    print(obj.fibo(i))
