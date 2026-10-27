#taking input from the user and pretinting it out on the screen 

first_name = "tony"
last_name = "stark"
age = 53
height = 1.85 
superhero_name = input("what is ur superhero name? ") 
print("tony's first name is " , first_name , "and, his last name is " , last_name , "and, his age is" , str(age) , "and his super hero name is" , superhero_name , 'and his height is' , str(height) , "cm")  
#practicing "TYPECASTING"

saras_age = input("what is sara's age?")
saras_new_age = int(saras_age) + 3
print(saras_new_age)
print(float(saras_new_age))

#type conversion is the process of convertingthe data type of a value of a variable to another type as well but the major difference in btw typecasting and type conversion is that the typecasting is done by the user while the type conversion is done by the python interpreter, automatically. 


 
#  #Problem: Product Price Calculator

# Statement:
# Write a program that asks the user for:

# Product name (text)
# Price per unit in PKR (decimal number)
# Quantity (whole number)
# Tax percentage (decimal number)

# Then calculate and print:

# Subtotal (price × quantity)
# Tax amount
# Final total

# Rules:

# Use input() for all four values
# Use float() and int() to convert them
# Use str() when joining numbers with text using +
# Print the data type of each variable at the end using type()

product_name = input("enter the product name : ")
price_per_unit = float(input("enter the price per unit in PKR : "))
product_quantity = int(input("enter the product quantity : "))
tax_percentage = float(input("enter the tax percentage : "))  
sub_total = price_per_unit * product_quantity
tax_amount = (sub_total * tax_percentage) / 100 
final_total = sub_total + tax_amount 
print ("the product name is " , product_name , "the privce per unit of the profuct is" , str(price_per_unit) , "the product quatity is" , product_quantity , "the taxt percntage is" , str(tax_percentage) ) , "the sub total is " , str(sub_total) , "the tex amount is " , str(tax_amount) , " and the dinal total is " , str(final_total) 
print ('the data type of product name is ' , type(product_name)) 

#checking the immutability of the strings. 
his_name = "tony stark"
print(his_name.upper())
print(his_name)

