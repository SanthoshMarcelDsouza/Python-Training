grocery = ["bread", "milk", "eggs", "butter","Buns","curd","12"]  # list of grocery items
print("Grocery List:", grocery)
grocery.sort()
print("Grocery List:", grocery)
 
# replcaing the element in the list
index = grocery.index('butter')
print("Index of 'butter':", index)
grocery[index] = 'jam'  # updating butter to jam
print("Updated Grocery List:", grocery)
 
grocery.pop()   # pop will remove the lst item from the list
print("Grocery List after pop():", grocery)
 
grocery.extend(['cookies', 'chocolates','milk'])  # adding multiple items to the list
print("Grocery List after extend():", grocery)
 
backup_list = grocery.copy()  # copying the list
print("Copied Grocery List:", backup_list)
 
changed_list = [item.upper() for item in grocery]   # list comprehension to convert items to uppercase
print("Changed Grocery List to Uppercase:", changed_list)
 
print("First item in the grocery list:", grocery[0])  # accessing the first item
print("Last item in the grocery list:", grocery[-1])  # accessing the last item
 
print("Number of items in the grocery list:", len(grocery))  # length of the list
 
print("first two items, grocery[:2]", grocery[:2])
 
grocery.insert(2, 'rice')  # inserting 'rice' at index 2
print("Grocery List after insert():", grocery)
 
grocery.remove('milk')  # removing 'milk' from the list
print("Grocery List after remove():", grocery)
 
del grocery[3]  # deleting item at index 3
print("Grocery List after del:", grocery)
 
print("is eggs are there in the list or not?", 'eggs' in grocery)  # checking if 'eggs' is in the list
 
grocery.extend(['milk', 'chocolates','milk'])
print("Number of times 'milk' appears in the list:", grocery.count('milk'))  # count occurrences of 'milk'
 
grocery.reverse()  # reversing the list
print("Reversed Grocery List:", grocery)
 
grocery.clear()  # clearing the list
print("Cleared Grocery List:", grocery)


student = ('Ravi',34,"Delhi","India","IT","Delhi")
print("student tuple, student", student)
 
print("Nmae",student[0])
print(" address details:", student[2:4])
 
if "A" in student:     #Mmeberhsip Test
    print("A is present in the tuple")
   
for a in student:
    print("value:", a)
   
print("Length of the tuple:", len(student))
 
print(" Occuracingin the the student tuple", student.count("Delhi"))
 
print("Index of IT in the tuple:", student.index("IT"))
 
# Tuple to list conversion
student_list = list(student)
student_list.append("WIPRO Technologies")
student_list[3] = "Bangalore"
print( "The list is ", student_list)
 
# convert back to tuple fromthe list
student = tuple(student_list)
print("The modified tuple is ", student)
 
project_codes = ('P001', 'P002', 'P003') # another tuple
complete_tuple = student + project_codes  # concatenation of tuples
print("The complete tuple after concatenation is ", complete_tuple)
 
#tuple within the tuple = nested tuples
studdent_nested = (student, project_codes)
print("The nested tuple is ", studdent_nested)
print("Accessing nested tuple element:", studdent_nested[0][1])  # accessing
print("Accessing nested 2nd tuple element:", studdent_nested[1][1])  # accessing
print(student)
 
#Unpacking the tuple
name, age, city, country, dept, state, org = student
print("Unpacked Values - Name:", name, ", Age:", age, ", City:", city, ", Country:", country, ", Dept:", dept, ", State:", state)
 
scores = (56,89,23,90,87,66)
print("Minimum score:", min(scores))
print("Maximum score:", max(scores))
print("Sum of scores:", sum(scores))
 
#extended tuple unpacking
a, b, c, *rest = scores
print("a:", a)
print("b:", b)  
print("c:", c)
print("rest:", rest)  # rest will be a list of remaining elements
 
# comparision of tuples
print((3,4,5) == (3,4,5))
print((6,7,4) == (6,7,1))
 
s = list(scores)
s.sort
 
# comparision of tuples
print((3,4,5) > (3,4,5))
print((6,7,4) > (6,7,1))


##################################################
s1 = "Samsung LED is good TV and is available in mutiple colors"
s2 = '                    Brand is good                                             '
s3 = """This is a good rband in the market
You can see multiple products of multiple categories
Available in all the major retail stores
you can buy online also.
"""
 
print([s1, s2, s3])
 
print(s1[2])
print(s1[0:6])
print(s1[0:10:2])  # step value
print(s1[-1])  # last character
print(s1[-4:])  # negative indexing including the last chafacter
print(s1[-4:-2])  # negative indexing eclusign the last character
print(s1[-5])  # negative indexing to fetch the 5th indexed character from last
print(s1[::-1])  # reversing the string
 
print("Length of the string s1:", len(s1))
 
print( s1 * 4) # repeating the string
 
print(s2.upper()) # converting to upper case
print(s2.lower()) # converting to lower case
print(s2.strip()) # removing leading and trailing spaces
print(s1.replace("is", "are")) # replacing the string
print(s3.split(" ")) # splitting the string based on space
print(s1.startswith("Sam")) # checking the starting of the string
print(s1.endswith("LED ")) # checking the ending of the string
print(s1.find("LED")) # finding the index of the substring
print(s1.count("in")) # counting the occurrence of a substring
 
v = "black, white, grey,darkblack"
res = v.split(",") # splitting the string based on comma
print(res)
x = "::".join(res) # joining the list elements with hyphen
print(x)
 
print("is" in s1) # membership test
reverse_Str = ''.join(reversed(s1)) # reversing the string using reversed() function
print(reverse_Str)
 
 

product = {
    "name": "Laptop",
    "brand": "Dell",
    "price": 80000,
    "specs": {
        "RAM": "16GB",
        "Storage": "512GB SSD",
        "Processor": "Intel i7"
    }
}
 
print("Product Name:", product["name"])  # passing the key to print the attribute value
print("Product Brand:", product.get("brand"))  # another way to access the value using get()
print("Product Price:", product["price"])
print("Product Specs:", product["specs"])
print("Product RAM:", product["specs"]["RAM"])  # accessing nested dictionary value
 
product["stock"] = 50  # adding a new key-value pair
print("Updated Product Dictionary:", product)
 
if "brand" in product:
    print("Brand is present in the product dictionary", product["brand"])
else:
    print(" The brand  key doesnt exst in the product dictionary")
   
print(product.keys()) # printing all the keys
 
product["price"] = 75000  # updating the price
print("Updated Price:", product["price"])
print(product)
 
for key, value in product.items():  # iterating through the dictionary
    print(f"{key}: {value}")
   
product.pop("stock")
print(product)
 
keys = list(product.keys())
print(product[keys[0]]) # accessing value using the first key from the keys list
 
values = product.values()
print("All values in the product dictionary:", type(values))
 
a= product.copy()  # copying the dictionary
print("Copied Product Dictionary:", a)
 
del product["price"]
 
# merging two dictionaries objects
warranty = {
    "Name": "Laptop",
    "brand": "Dell",
    "period": "2 year",
    "extended": "1 year",
}
 
product.update(warranty)
print("Merged Product Dictionary with Warranty:", product)
 
product.clear()  # clearing the dictionary
print("Cleared Product Dictionary:", product)



products = {"laptop", "mobile", "tablet", "desktop", "smartwatch"}
print(products)
 
products.add("earbuds")  # adding an item to the set
products.add("earbuds")  # adding an item to the set
products.add("earbuds")  # adding an item to the set
print("After adding earbuds:", products)
 
products.remove("tablet")  # removing an item from the set
print("After removing tablet:", products)
 
prod = {"camera", "speaker","mobile", "laptop"}
result = products.union(prod)  # union of two sets
print("Union of products and prod:", result)
 
result = products.intersection(prod)  # intersection of two sets
print("Intersection of products and prod:", result)
 
print(products)
print(prod)
 
if products == prod:
    print("Both sets are equal")
else:
    print("Both sets are not equal")
   
products.pop() # pop will remove a random item from the set
print("After pop():", products)
 
result2 = products.difference(prod)  # difference of two sets
print("Difference of products and prod:", result2)
 
result3 = products^prod  # symemtric difference of two sets means the uncommon elements from both the sets
print("symmnetric Difference of products and prod:", result3)
 
a = products.discard("desktop")  # discard will remove the item if present else will do nothing
print("After discarding desktop:", products)
 
products.update(prod)
print(products)
 
products.clear()  # clearing the set
print("After clearing the set:", products)
 
del products   # deleting the entire set

 