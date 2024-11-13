# Identification of dictionary
Name = {}
print(Name)

# To check the type of dictionary
dictionary = {}
print(dictionary, type(dictionary) )

# Another way to create dictionary
Names = dict()
print(Names, type(Names))

# To add data in dictionary
information = {'Name' : 'Tayyaba Qamar', 'Place' : 'Ras Al Khaimah' } 
print(information)

# Adding vaue in dictionary
Name = {'Name' : 'Tayyaba Qamar' , 'Place' : 'Ras Al Khaimah'}
print(Names,type(Names))

# get() in dictionary
Name = {'Name' : 'Tayyaba Qamar' , 'Roll Number' : '6543' }
print(Names.get("student" , "Naila"))

# use of items() in dictionary
data = {'Name' : 'Tayyaba' , 'Place' : 'Rak Al Khaimah'}
print(data.items())


# To print keys in dictionary
dictionary = {'Name' : 'Tayyaba' , 'Roll number' : '5678' }
print(dictionary.keys())


# To delete any item in the dictionary
dictionary = {'Name' : 'Tayyaba' , 'Course' : 'Creative Computing' }
del dictionary ["Course"]
print(dictionary.items())

# Delete method Cont
dictionary = {'Name' : 'Tayyaba' ,
              'Place' : 'Rak Al Khaimah' ,
              'Country' : 'United Arab Emirates'}
del dictionary ["Place"]
print(dictionary.items())
print(dictionary.keys())
print(dictionary.values())


# Use of Pop Method
information = {'Names' : 'Tayyaba' ,
               'Country' : 'United Arab Emirates',
               'Roll Number' : '187644'}
print(information.pop("Country"))
print(information.keys())
print(information.values())


# Use of popitems
dictionary = {'Name' : 'Tayyaba' ,
              'fruit' : 'Banana' ,
              'Country' : 'United Arab Emirates'}
print(dictionary.popitem())
print(dictionary.keys())
print(dictionary.values())







