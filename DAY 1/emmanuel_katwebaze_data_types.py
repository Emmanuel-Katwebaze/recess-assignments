#Floats, strings, int, decimal, char, booleans
print("******** TYPE OF ********")
w = 40 #int type
print(type(w))
z = "Hello world" #string type
print(type(z))
y = 1j #complex type
print(type(y))
print("****************")

#LISTS
#They are used to store multiple items in a single variable
#Lists are ordered, changeable, and allows duplicate values
print("******** LISTS ********")
Afternoon = ["Emma", "Katwebaze", "Joseph"]
print(Afternoon)
#Duplicates in Lists
Afternoon = ["Emma", "Katwebaze", "Joseph", "Emma", "Maria","Gabriel"]
print(Afternoon)
#List length
print(len(Afternoon))
#List type
print(type(Afternoon))

#print List items using index
print("****************")
print(Afternoon[0])
print(Afternoon[2])
print(Afternoon[3])
print(Afternoon[-2])

#Accessing a range of items, get's from the startIndex to minus one of the last index
print("****************")
print(Afternoon[3:6])
print(Afternoon[:3])
print(Afternoon[1:])

#print List items using a loop
print("******* Access Elements with for loop *********")
for i in Afternoon:
    print(i)
    
#appending
Afternoon.append("Taylor")
print(Afternoon)

#Remove a particular item
Afternoon.remove("Joseph")
print(Afternoon)

#Add list items using the insert method
Afternoon.insert(0, "Shidah")
print(Afternoon)

#Remove a  particular item using index
Afternoon.pop(0)
print(Afternoon)

#TUPLES
#They are used to store items in a single variable
#They are ordered and unchangeable
print("******** TUPLES ********")
phones = ("samsung", "iphone", "techno")
print(phones)

#Allow for duplicate values
phones = ("samsung", "iphone", "techno", "techno","samsung")
print(phones)

#Exercise use the len() with this tuple example
print("******** Tuple length ********")
print(len(phones))

#Tuple showing different data types
print("****************")
Tuple1 = ("matooke", "rice", "tomatoes", "beans")
Tuple2 = (100, 200, 300, 500)
print(Tuple1)
print(Tuple2)
print(type(Tuple2))

#Exercise How to access tuples
print("****************")
print(Tuple1[0])
print(Tuple1[-2])

#Add items to a tuple
print("****************")
phones = ("samsung", "iphone", "Techno")
print(phones)
z = list(phones)
z.append("Nokia")
phones = tuple(z)
print(phones)

#second method to add items
print("****************")
extra_phone = ("Sony",)
phones+=extra_phone
new_stock = phones + extra_phone
print(phones)
print(new_stock)

#SETS
#store multiple items in a single variable
#unchangeable but one can remove and add new items
#don't allow duplicates
print("******** SETS  ********")
setone = {"rice", "matooke", "irish" }
print(setone)

#Duplicates in Sets
setone = {"rice", "matooke", "irish", "Irish" }
print(setone)

#Exercise find the length of your set, data type, accessing items in a set, add items in a set, add two sets together
phone_set = {"samsung", "iphone", "Techno"}
print(phone_set)
#Length of set
print("length of the Phone set: ")
print(len(phone_set))

#Set datatypes
print("The set datatype is:")
print(type(phone_set))

#Accessing set items
print("******** phone set  ********")
for phone in phone_set:
    print(phone)
    
if "iphone" in phone_set:
  print("The element 'iphone' is present in the set.")

#Adding items in a set
phone_set.add("Sony")
print("Modified set after adding")
print(phone_set)

#Joining sets
extra_set = {"Motorolla"}
print("Combined Set:")
print(phone_set.union(extra_set))
