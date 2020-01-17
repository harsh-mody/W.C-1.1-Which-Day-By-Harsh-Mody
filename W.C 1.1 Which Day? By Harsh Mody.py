enteredDate = int(input("Please Enter The Value Of Date : "))
enteredMonth = int(input("Please Enter The Value Of Month : "))
enteredYear = int(input("Please Enter The Value Of Year : "))
numberOfDaysGapFromFirstDayToEnteredDate = 0
currentYear = 1
currentMonth = 1
currentDate = 1
if currentYear != enteredYear:
    numberOfDaysGapFromFirstDayToEnteredDate = numberOfDaysGapFromFirstDayToEnteredDate + (365 * (enteredYear -
                                                                                                  currentYear))
if currentMonth != enteredMonth:
    numberOfDaysGapFromFirstDayToEnteredDate = numberOfDaysGapFromFirstDayToEnteredDate + (31 * (enteredMonth -
                                                                                                 currentMonth))
if currentDate != enteredDate:
    numberOfDaysGapFromFirstDayToEnteredDate = numberOfDaysGapFromFirstDayToEnteredDate + (enteredDate - currentDate)
print("The Index Of The Day Of Week Is : ", numberOfDaysGapFromFirstDayToEnteredDate%7)

