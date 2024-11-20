"""
## Exercise 10: Is it even? - 35 Marks

Write a program that tests if a value is even or odd. Follow the instructions outlined below:

### Instructions:
* The program should ask the user for a number from within the main function.
* The entered number should be passed to a function that determines if the value is even or odd.
* The function should return a message indicating whether the number is even or odd.
* The message returned by the function should be printed from within the main function.

"""
# Taking input from the user
Number = int(input("Enter a number:"))
def Even_OR_Odd(Number):
# if-else statement
     if Number % 2 == 0:
        print("Even number")
     else:
        print("Odd number") 
# Calling the Function
Even_OR_Odd(Number)
