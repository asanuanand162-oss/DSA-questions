class Solution:
    def studentGrade(self, marks):
        if marks>=90:
            print("Grade A")
        elif marks>=70:
            print("Grade B")
        elif marks>=50:
            print("Grade C")
        elif marks>=35:
            print("Grade D")
        else:
            print("fail")
obj=Solution()
marks=int(input("enter your marks: "))
obj.studentGrade(marks)
