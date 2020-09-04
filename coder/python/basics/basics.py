# Introduction to Python language with multiple examples

                                        # Example 1 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Example 1 :: Using Variables in Python
# In python we dont have to declare the type of variable before assigning it any value.
# But in languages like C, C++ or Java etc.. we need define first then assign value...

var_x = 100 # Integer
var_y = 200 # Integer
x=True # Boolean
y=False # Boolean
a=110.50 # Float
b=-200 # Integer 
c={1:10,2:25,3:30,4:50} # Dictionary
d=[1,2,3,4,5] # Lists/Array
e=(1,2,3,4,5) # Tuple
f= -100.125 # Float

'''
# To find the memory location of each object using id(object) - this will give memory location as integer.
'''

print("\n")
print("Example 1 Output :: ")
print("\n")
print(id(var_x)) # Returns Memory location
print(id(var_y)) # Returns Memory location
print(id(x)) # Returns Memory location
print(id(y)) # Returns Memory location
print(id(a)) # Returns Memory location
print(id(b)) # Returns Memory location
print(id(c)) # Returns Memory location
print(id(d)) # Returns Memory location
print(id(e)) # Returns Memory location

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


                                        # Example 2
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Example 2 :: Using Variables in Python

'''
	The below definition means that var_x is a variable and it points/references a memory location
	that has value as 500 ~
	In python when we assign a variable like var_x = 500, Whatever is there to the left side of the
	" = " symbol represents the stack memory and that to the right represents the heap memory.

	Which means , when var_x = 500
	var_x - > Stack Memory
	500 -> Heap Memory

	* Python Stores all the objects in the heap memory only.

	What's stack memory and heap memory ?

	https://gribblelab.org/CBootCamp/7_Memory_Stack_vs_Heap.html

	# Note: In Python its not needed to pre-define a variable type before assigning values.
	We can dynamically assign values to any variables.

	In python we find the family/type of object using __class__ or type() built-in function.

'''

print("\n")
print("Example 2 Output :: ")
print("\n")


var_x = 500 # Type is integer
print(var_x) # 500
# In python we find the family/type of object using __class__ or type() built-in function.
print(var_x.__class__) # Returns type of object
print(type(var_x)) # Returns type of object

# Same variable can be reassigned to another value.
# Note: In Python its not needed to pre-define a variable type before assigning values.
var_x = "Arun Chandramouli"
print(var_x) # Arun Chandramouli
print(var_x.__class__) # Returns type of object
print(type(var_x)) # Returns type of object


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


                                        # Example 3
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Example 3 :: Using Variables in Python

print("\n")
print("Example 3 Output :: ")
print("\n")

some_var = 100.50
print(some_var)
del some_var
#print(some_var) # Will result in an exception since the variable is deleted.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

                                        # Example 4
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Example 4 :: Using simple functions in python for getting variable details.

# Write a simple function to find memory location and type of given variable.

def print_mem_location_type_of_variable(variable):
	'''
		Find memory location and type of variable
		:param variable: Variable to be explained.	
		The class of the variable can be found in 2 ways:
			print(variable.__class__)	
			print(type(variable))
	'''
	print("Memory location of variable {} is {} ".format(variable,id(variable)))
	print("Variable {} belongs to class {} ".format(variable,type(variable)))

def return_mem_location_type_of_variable(variable):
	'''
		Find memory location and type of variable
		:param variable: Variable to be explained.	
		The class of the variable can be found in 2 ways:
			print(variable.__class__)	
			print(type(variable))
	'''
	print("Memory location of variable {} is {} ".format(variable,id(variable)))
	print("Variable {} belongs to class {} ".format(variable,type(variable)))
	return id(variable),variable.__class__

print("\n")
print("Example 4 Output :: ")
print("\n")

# Test the function with various objects.
print_mem_location_type_of_variable(1000)
print(return_mem_location_type_of_variable("Arun"))
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 



                                        # Example 5
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Example 5 :: Using simple functions in python for getting variable details.
# In Python we can store the function is a variable.

# Write a simple function to find memory location and type of given variable.
def return_mem_location_type_of_variable(variable):
	'''
		Find memory location and type of variable
		:param variable: Variable to be explained.	
		The class of the variable can be found in 2 ways:
			print(variable.__class__)	
			print(type(variable))
	'''
	print("Memory location of variable {} is {} ".format(variable,id(variable)))
	print("Variable {} belongs to class {} ".format(variable,type(variable)))
	return id(variable),variable.__class__

print("\n")
print("Example 5 Output :: ")
print("\n")

# Test the function with various objects.
result = return_mem_location_type_of_variable("Arun")
print(result)
result = return_mem_location_type_of_variable(100)
print(result)
result = return_mem_location_type_of_variable(100.50)
print(result)

result = return_mem_location_type_of_variable(True)
print(result)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 



                                        # Example 6
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Example 6 :: Using simple functions in python for getting variable details.
# In Python we can store the function is a variable. 
# Even if the function is deleted, the variable will still work and produce results.

# Write a simple function to find memory location and type of given variable.
def hello_world(name):
	'''
		Find memory location and type of variable
		:param name: Name to the printed.	
		The class of the variable can be found in 2 ways:
			print(variable.__class__)	
			print(type(variable))
	'''
	return "Hello World ! {} ".format(name)

print("\n")
print("Example 6 Output :: ")
print("\n")

# Test the function with various objects.
result = hello_world("Arun Chandramouli")
print(result) # Print "Arun Chandramouli"
del hello_world # Function objects gets deleted
print(result) # It will still print the value as "Arun Chandramouli"

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

                                        # Example 7
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Example 7 :: Using simple functions in python for getting variable details.
# In Python we can store the function is a variable. 
# Even if the function is deleted, the variable will still work and produce results.

# Write a simple function to find memory location and type of given variable.
def hello_world(name):
	'''
		Find memory location and type of variable
		:param name: Name to the printed.	
		The class of the variable can be found in 2 ways:
			print(variable.__class__)	
			print(type(variable))
	'''
	return "Hello World ! {} ".format(name)

print("\n")
print("Example 7 Output :: ")
print("\n")

# Store the function object in a variable and delete the original function.
# The variable can still give results...

test_result = hello_world
print(test_result("Arun"))
del hello_world
print(test_result("Arun !!"))
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 