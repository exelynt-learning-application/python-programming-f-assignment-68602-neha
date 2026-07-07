# Student Details Program

print("===== Student Details Program =====")

# User Input
student_name = input("Enter Student Name: ")
age = int(input("Enter Age: "))
course_fee = float(input("Enter Course Fee: "))
is_enrolled = input("Is the student enrolled? (True/False): ")

# Convert input to Boolean
if is_enrolled.lower() == "true":
    is_enrolled = True
else:
    is_enrolled = False

# Display Student Details
print("\n----- Student Details -----")
print("Student Name :", student_name)
print("Age          :", age)
print("Course Fee   :", course_fee)
print("Enrolled     :", is_enrolled)

# Display Data Types
print("\n----- Data Types -----")
print("Name Type       :", type(student_name))
print("Age Type        :", type(age))
print("Course Fee Type :", type(course_fee))
print("Enrolled Type   :", type(is_enrolled))

# Update Values
age = age + 1
course_fee = course_fee + (course_fee * 0.18)   # Add 18% tax
is_enrolled = not is_enrolled

# Display Updated Details
print("\n----- Updated Student Details -----")
print("Student Name :", student_name)
print("Updated Age  :", age)
print("Updated Fee  :", course_fee)
print("Enrolled     :", is_enrolled)

# Display Updated Data Types
print("\n----- Updated Data Types -----")
print("Name Type       :", type(student_name))
print("Age Type        :", type(age))
print("Course Fee Type :", type(course_fee))
print("Enrolled Type   :", type(is_enrolled))
