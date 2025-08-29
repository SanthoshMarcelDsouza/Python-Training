# grocery = ["bread", "milk", "eggs", "butter","Buns","curd","12"]  # list of grocery items
# print("Grocery List:", grocery)
# grocery.sort()
# print("Grocery List:", grocery)
 
# # replcaing the element in the list
# index = grocery.index('butter')
# print("Index of 'butter':", index)
# grocery[index] = 'jam'  # updating butter to jam
# print("Updated Grocery List:", grocery)
 
# grocery.pop()   # pop will remove the lst item from the list
# print("Grocery List after pop():", grocery)
 
# grocery.extend(['cookies', 'chocolates','milk'])  # adding multiple items to the list
# print("Grocery List after extend():", grocery)
 
# backup_list = grocery.copy()  # copying the list
# print("Copied Grocery List:", backup_list)
 
# changed_list = [item.upper() for item in grocery]   # list comprehension to convert items to uppercase
# print("Changed Grocery List to Uppercase:", changed_list)
 
# print("First item in the grocery list:", grocery[0])  # accessing the first item
# print("Last item in the grocery list:", grocery[-1])  # accessing the last item
 
# print("Number of items in the grocery list:", len(grocery))  # length of the list
 
# print("first two items, grocery[:2]", grocery[:2])
 
# grocery.insert(2, 'rice')  # inserting 'rice' at index 2
# print("Grocery List after insert():", grocery)
 
# grocery.remove('milk')  # removing 'milk' from the list
# print("Grocery List after remove():", grocery)
 
# del grocery[3]  # deleting item at index 3
# print("Grocery List after del:", grocery)
 
# print("is eggs are there in the list or not?", 'eggs' in grocery)  # checking if 'eggs' is in the list
 
# grocery.extend(['milk', 'chocolates','milk'])
# print("Number of times 'milk' appears in the list:", grocery.count('milk'))  # count occurrences of 'milk'
 
# grocery.reverse()  # reversing the list
# print("Reversed Grocery List:", grocery)
 
# grocery.clear()  # clearing the list
# print("Cleared Grocery List:", grocery)



studentScores = []
studentScores.append(85)
studentScores.append(90)
studentScores.append(78)
studentScores.append(92)
studentScores.append(88)
print("Student Scores after creation:",studentScores)

studentScores.insert(2,80)
print("Score after inserting after index 2", studentScores)

studentScores.remove(90)
print("Score after removing 90", studentScores)

studentScores.sort()
print("Score after sorting", studentScores)

studentScores.reverse()
print("Score after Reverse", studentScores)

print("Minimum Score", min(studentScores))

print("Minimum Score", max(studentScores))

print("Is 90 present", 90 in studentScores)

print("Total count of Score", len(studentScores))

print("Slice First three Score", studentScores[:3])

print("Last element", studentScores[-1])

print("New Copied list", studentScores.copy())


print(f"Grades are assigned for  {studentScores} as below:")
for score in studentScores:
    if score > 90:
         print(f"Score {score} is grade A")
    elif score > 80: 
        print(f"Score {score} is grade B")
    elif score > 70: 
        print(f"Score {score} is grade C")
    elif score > 60: 
        print(f"Score {score} is grade C")
    else:
         print(f"Score {score} is grade D")
