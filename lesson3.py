#if statements
#store data list,tuple dictionary,set
#loops

entered_value=input("Enter the score:")
if not entered_value.isnumeric():
    print("please enter a valid number")
    exit(0)

score= int(entered_value)
if score >= 78:
    print("A")
elif score >= 71 and score <=77:
    print("A-")
elif score >= 64 and score <=70:
    print("B+")
elif score >= 57 and score <=63:
    print("B")
elif score >= 50 and score <=56:
    print("B-")
elif score >= 43 and score <=49:
    print("C+")
elif score >= 36 and score <=42:
    print("C")
elif score >= 29 and score <=35:
    print("C-")
elif score >= 22 and score <=28:
    print("D+")
else:
    print("D")
