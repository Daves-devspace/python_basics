#python
import math


def split_check(total,number_of_people):
    if number_of_people <=1:
        raise ValueError("More than 1 person is required to split the check")
    return math.ceil(total/number_of_people)
#exception
try:
     total_due= float(input("What is the total?  "))
     number_of_people = int(input("How many people?  "))
     amount_due = split_check(total_due, number_of_people)
except ValueError:
     print("oh no!Thats not a valid value.Try again...")
     #print("({})" .format())
else:
      print("Each person owes ksh",format(amount_due))