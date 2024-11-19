"""
Write a loop that prompts the user to enter a series of pizza toppings until they enter a
'quit' value. As they enter each topping,
Print a message saying you’ll add that topping to their pizza.
"""
# While loop
while True:
# Taking input from the user
    Pizza_topping = input("Enter a pizza topping:")
    if  Pizza_topping == "Quit": 
        print("Thank you for ordering the food")
# To break the loop
        break 
    print("Topping will add to your pizza.")
