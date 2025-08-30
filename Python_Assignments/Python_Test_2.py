
#Test-2
# Create a tuple named product containing the following items: "Laptop", 50000, Black ,'Samsung' and "Electronics". Print the tuple.
# Access and print the second element of the tuple product. 
# Slice and print the last two elements of the product tuple. 
# Check whether "Electronics" is present in the product tuple and print a message. 
# Create a tuple of 5 product prices: (1000, 1500, 1200, 1100, 900). Count how many times 1000 appears. 
# Find and print the maximum and minimum price from the prices tuple. 
# Use a loop to print each item from the product tuple on a new line. 
# Convert the product tuple to a list. Change the price to 55000, then convert it back to a tuple. Print the updated tuple.
# Add a new item "In Stock" to the product tuple (simulate adding by concatenation).
# Remove "Electronics" from the product tuple (by converting to list, removing, and converting back). 
# Unpack the tuple product into three variables and print each variable. 
# Create a nested tuple that contains three product tuples inside it. Access and print the name of the second product in the nested tuple.
 

product = ("Laptop", 50000, "Black" ,'Samsung',"Electronics")
print(product)

print(product[2])
print(product[-2:])

print("Is Electronics is present in products tuple", ("Electronics" in product))

productPrice = (1000, 1500, 1200, 1100, 900)
print(productPrice)
print("Minimum of Products:",(min( productPrice)))
print("Maximum of Products:",max( productPrice))

print("List of prodcuts:")
for pr in product:
    print(pr)


product_list = list(product)
product_list[1] = 55000

product = tuple(product_list)
print("Products:",product)

product = product + ("In Stock",)
print("Products:",product)


product_list = list(product)
product_list.remove("Electronics")

product = tuple(product_list)
print("Products:",product)


name, price,color,*rest = product
print("Name",name,"Price",price,"Color",color)


product1 = ("Laptop", 50000, "Black" ,'Samsung',"Electronics")
product2 = ("Mobile", 6000, "Red" ,'Oppo',"Electronics")
product3 = ("Tablet", 80000, "Blue" ,'APple',"Electronics")

NestedProducts= (product1,product2,product3)
print(NestedProducts)

prod2 = NestedProducts[1]
print("Name",prod2[0])

print("Name",NestedProducts[1][0])