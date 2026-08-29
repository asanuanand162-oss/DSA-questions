class Solution:
    def printName(self, name, count, N):
        if count == N:
           return
        print(name)
        self.printName(name, count + 1, N)
obj= Solution()
N=int(input("enter a number: "))
name =input("enter name: ")
obj.printName(name, 0, N)
