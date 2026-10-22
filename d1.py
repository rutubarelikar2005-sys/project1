students = {
"Rahul": 85,
"Priya": 92,
"Amit": 76,
"Sneha": 88,
"Rohan": 95
}
marks = list(students.values())

# Function to calculate average
def average_marks(marks):
    return sum(marks) / len(marks)

# Function to find maximum 
def maximum_marks(marks):
 return max(marks)

# Function to find minimum 
def minimum_marks(marks):
   return min(marks)

print("Student Marks:")
for name, mark in students.items(): print(name, ":", mark)

print("\nAverage Marks =", average_marks(marks))
print("Maximum Marks =", maximum_marks(marks))
print("Minimum Marks =", minimum_marks(marks))
         