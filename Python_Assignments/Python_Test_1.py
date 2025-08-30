# Write a Python program that manages a list of student scores. Perform the following operations step-by-step:
# Create an empty list to store scores.
# Append the scores: 85, 90, 78, 92, 88
# Insert the score 80 at index 
# Remove the score 92 from the list
# Sort the scores in ascending order
# Reverse the list
# Find and print the maximum and minimum score
# Check if 90 is in the list
# Print the total number of scores
# Slice and print the first three scores 
# find the last element from the list
# replace the score with new score on the index 2
# create a new copied list also

 

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
