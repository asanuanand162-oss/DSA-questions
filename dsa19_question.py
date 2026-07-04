class solution:
    def pattern13(self,n):
        count=1
        for i in range(n):
            for j in range(i+1):
                print(count,end=" ")
                count+=1
            print()
obj=solution()
n=int(input("enter the number: "))
obj.pattern13(n)
