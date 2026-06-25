class Solution:
    def whichWeekDay(self, day):
        match day:
            case 1:
                print("monday")
            case 2:
                print("tuesday")
            case 3:
                print("Wednesday")
            case 4:
                print("thursday")
            case 5:
                print("friday")
            case 6:
                print("saturday")
            case 7:
                print("sunday")
            case _:
                print("invalid")
obj=Solution()
day=int(input("enter number (1-7): "))
obj.whichWeekDay(day)
