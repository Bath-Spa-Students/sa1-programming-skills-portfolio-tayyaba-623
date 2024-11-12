#Elif statement
c=55
d=7
#if Statement
if c<d:
    print("C is less than d")
#elif Statement
elif c==d:
    print("C and d are equal")  
#else Statement
else:
    print("C is greater than d")
      
#To get input from user
score= int(input("Enter your scores:"))
#if statement
if score>=90:
    print("Your grade is A.")
#elif statement
elif score>=80:
    print("Your grade is B.")
#elif statement
elif score>=70:
    print("Your grade is C.")
#elif statement
elif score>=50:
    print("Yoyr grade is D.")
#else statement
else:
    print("Your grade is F.")