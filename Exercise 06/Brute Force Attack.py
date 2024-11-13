"""
## Exercise 6: Brute Force Attack - 30 Marks

Write a program that simulates a password entry system. The correct password is defined as 12345. The program should keep asking the user to enter the password until they provide the correct one.

### Basic Requirements:
1. Define the correct password.
2. Use a while loop to repeatedly ask the user for the password until the correct one is entered.
3. Output an appropriate message when the correct password is entered.

### Optional Requirements:

Modify the program to include a maximum of 5 password attempts. If the user enters the wrong password, inform them of the remaining attempts. If the maximum number of attempts is reached, inform the user that the authorities have been alerted.
"""
# Correct password
password= "12345"
# Attempts
total_attempts= 5
# While loop
while total_attempts > 0:
   answer= input("Enter the password:")
# Checking the answer
   if answer == password:
       print("Correct password")
       break 
   else:
        total_attempts -=1
        if total_attempts > 0:
            print("Attempt left", total_attempts)
else:
        print("Authorities have been alerted ")
        

     
