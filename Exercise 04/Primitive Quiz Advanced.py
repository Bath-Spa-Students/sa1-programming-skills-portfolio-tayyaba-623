""""
## Exercise 4: Primitive Quiz - 30 Marks

In this exercise, you'll create a simple program that asks the user a question, evaluates their answer, and provides feedback.

### Steps:
1. Write a program that asks the user "What is the capital of France?" and waits for their response.
2. If the user's answer is correct (i.e., "Paris"), the program should print a message saying the answer is correct.
3. If the answer is incorrect, the program should print a message saying the answer is wrong.

### Advanced Requirements:
Ignore Capitalization: Modify your program to accept answers regardless of the capitalization (e.g., "paris", "Paris", and "PaRis" should all be considered correct).
Multiple Questions: Extend the program into a quiz that asks for the capitals of 10 European countries. Provide feedback for each question.
"""
# 10 European countries and their capital
Countries = {
        "France" : "Paris",
        "Andorra" : "Andorra la Vella",
        "Austria" : "Vienna",
        "Belarus" : "Minsk",
        "Belgium" : "Brussels",
        "Bulgaria" : "Sofia",
        "Croatia" : "Zagreb",
        "Cyprus" : "Nicosia",
        "Czech Republic" : "Prague",
        "Denmark" : "Copenhagen"
}
 
for country, capital in Countries.items():
# Taking input from the user
    answer = input(f"What is the capital of {country}? ").strip().lower()
# if-else statement
    if answer == capital.lower():
     print("Correct answer")
    else:
     print(f"Incorrect the correct answer is {capital}")
