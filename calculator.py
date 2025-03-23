num1 = float(input("הכנס את המספר הראשון: "))
num2 = float(input("הכנס את המספר השני: "))
print("בחר פעולה: +  -  *  /")
operation = input("הכנס פעולה: ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "אי אפשר לחלק באפס!"
else:
    result = "פעולה לא חוקית"

print("התוצאה היא:", result)