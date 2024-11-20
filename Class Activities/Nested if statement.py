# Nested if-else statement
# Taking input from the user
salary = (int(input("Enter your salary:")))
# Nested if-else statement
if salary >= 40000:
    year_of_experience = (float(input("Enter your year of experience:")))
    
    if year_of_experience >= 3:
        print("You are eligible for this job")
    
    else:
        print("Your experience is less than 3")
    
else:
    print("You should earn 40k to eligible for this job")

    
