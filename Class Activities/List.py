#Homogeneous List
names= ["Tayyaba" , "University" , "Hello"]
#print the variable 
print(names)


#Hetrogeneous List
Country= ["Canada" , "24" , "3.5"]
#print the variable 
print(Country)


#Repitition Operator * is use to repeat the data
Fruits= ["Banana", "Apple", "Grapes"]
Fruits_names= Fruits * 4
#print the variable Fruits_names
print(Fruits_names)


#Positive Indexing starts from 0
#Example 1
numbers=[2,4,5,8,9,0]
print(numbers[0])

#Example 2
list=[6,9,3,6,2]
#Print the variable name as list
print(list[4])


#Negative Indexing starts from -1 
numbers=[4,8,1,5,9,3,6,7]
#Print the variable name as numbers
print(numbers[-5])


#len function 
numbers=[2,8,5,9,6,4,1,3]
print("Number of elements in the list is:" ,len(numbers))


#Mutability 
numbers =[5,8,3,2]
numbers[2]=1
print(numbers)


#Concatenating Lists
#First variable
numbers_1=[2,6,2,4]
#Second variable
numbers_2=[5,8,1]
numbers_3=numbers_1 + numbers_2
#print the variable 
print(numbers_3)


#List Slicing
list_1=[4,8,2,4,0,5,3,1]
numbers=list_1[3:5]
print(numbers)

#To find the elements in the list we are supposed to use if operator 
#Example 1
list=[2,5,3,7,5,1,4,8,9]
if 9 in list:
    print("Found")
else:
    print("Not found")


#Example 2 of if operator
numbers=[3,5,6]
if 7 in numbers:
    print("Found")
else:
    print("Not Found")


#not in operator
list3=[3,6,8,2,9,0,1]
if 9 not in list3:
    print("yes")
else:
    print("No")
 

#build in functions (append)
new_numbers=[4,9,3,1]
#Adding an element in the list 
new_numbers.append(10)
#print the variable
print(new_numbers)


#buid in functions (index) 
list5=[4,8,9,0]
#finding the index number of 0
print(list5.index(0))


#build in functions (sort)
list5=[7,9,2,4]
list5.sort()
#Print the varaible name as list5
print(list5)


#build in functions (reverse)
new_list=[5,9,0,5]
new_list.reverse()
#Print the variable name as new_list
print(new_list)


#build in function (remove)
list3=[4,6,2,7,8,1,9]
list3.remove(1)
#Print the variable
print(list3)


#finding the min and max number
new_list1=[5,9,0,3,8,7,2,1]
print(max(new_list1))
print(min(new_list1))


