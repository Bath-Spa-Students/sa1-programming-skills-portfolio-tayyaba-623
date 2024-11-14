"""
## Exercise 5: Days of the Month - 30 Marks

Write a program that tells a user how many days there are in a specific month. Use a dictionary to map the month numbers (1-12) to the number of days in each month.

### Instructions:
1. Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
2. Input Handling: Ask the user to input the month number.
3. Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month.

### Advanced Requirement:
Leap Year Adjustment: Modify the program to account for leap years. For February, ask the user if the year is a leap year and adjust the number of days accordingly.
"""
# months
months= {
        1:  31,
        2:  28,
        3:  31,
        4:  30,
        5:  31,
        6:  30,
        7:  31,
        8:  31,
        9:  30,
        10: 31,
        11: 30,
        12: 31,
                }
# Taking input from the user
user_answer=int(input("Enter any month number from 1 to 12:"))
# if-else statement
if user_answer <= 12:
    print(f"Month {user_answer} has {months[user_answer]} days")
else:
    print("Invalid. Please enter a month between 1 and 12")



