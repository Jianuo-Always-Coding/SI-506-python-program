# SI 506 Lecture 03

# 1.0 COMMENTS

# A single line comment <-- commences with hash (#) character

# Block comment
# A single line comment
# Yet another single line comment
# And yet another single line comment

# x = 5
# y = 2
# sum = x + y

welcome = 'Welcome to SI 506' # string


# 3.0 VARIABLES

num = 506

welcome_message = 'Welcome to SI 506'

uniqnames = ['arwhyte', 'brooksch', 'collemc', 'csev', 'cteplovs']

chorus = """Hail! to the victors valiant
Hail! to the conquering heroes
Hail! Hail! to Michigan
the leaders and best!
"""

# 4.0 VARIABLE NAMING RULES AND CONVENTIONS

# 4.1 Good

# Choose lowercase
uniqname = 'arwhyte'

# Separate words with underscore (_)
course_code = 'SI 506'

# Use plural form to indicate a set or sequence
course_codes = ['SI 504', 'SI 506', 'SI 507']

# Ok to use recognizable abbreviations like num[ber], val[ue] or var[iable].
num = 24

# "is_", "has_" Boolean true/false
is_enrolled = False
has_mask = True

# All caps designates a module level constant (special case)
BASE_URL = 'https://si506.org/'

# Function definition specifying two parameters x and y (a foreshadowing of the weeks ahead)
def multiply(x, y):
    return x * y # arithmetic

# Call the function and pass two numeric arguments
product = multiply(14, 24)

print(f"\n4.1 product = {product}\n") # formatted string literal (f-string)

# For loop incorporating a counter < i > value
course_codes = ['SI 564', 'SI 574', 'SI 579', 'SI 582']
i = 1 # counter
for code in course_codes:
    print(f"{i}. {code}")
    i += 1 # addition assignment (increment)

print('\n') # pad with newline escape character

# Alternative: call built-in function enumerate()
for i, code in enumerate(course_codes, start=1):
    print(f"{i}. {code}")


# 4.3 Ugly (illegal)

# Illegal: keyword used as a variable name (language-specific identifiers reserved by Python)

# class = 'SI 506' # use clazz # TODO UNCOMMENT

# Illegal: variable name commences with a numeric value.

# 506_umsi = 'SI 506' # TODO UNCOMMENT

# Illegal: variable name commences with a special character (e.g., `@`, `%`, `$`, `&`, `!`)

# $number = 506 # TODO UNCOMMENT

# Illegal: variable name includes a dash (`-`).

# course-list = ['SI 506', 'SI 507', 'SI 618'] # TODO UNCOMMENT

# Illegal: variable name includes whitespace.

# course name = 'SI 506' # illegal; uncomment to test


# 5.0 BUILT-IN FUNCTIONS (print(), type(), len())

# 5.1 print(): print passed in object to the screen

# Passing a hard-coded string.
print('\n5.1.1 SI 506 rocks!') # \n = newline escape character

# Passing a variable name which points to a string.
print(f"\n5.1.2 Print welcome_message = {welcome_message}") # formatted string literal

# Passing a variable name which points to a multiline string.
print(f"\n5.1.3 Print multiline str = {chorus}")


# 5.2 type(): determine object's data type

data_type = type(num)
print(f"\n5.2.1 num type = {data_type}") # returns <class 'int'>

data_type = type(welcome_message)
print(f"\n5.2.2 welcome_message type = {data_type}") # returns <class 'str'>

data_type = type(uniqnames)
print(f"\n5.2.3 uniqnames type = {data_type}") # returns <class 'list'>


# 5.3 len(): check length of sequence (i.e., number of elements)

# TODO UNCOMMENT
# len = 10 # Shadowing built-in function name (avoid)
# Generates TypeError: 'int' object is not callable when len() is called below.

# Count characters in string (including whitespace).
char_count = len(welcome_message)
print(f"\n5.3.1 Welcome_message length = {char_count}")

# Count number of elements in list.
uniqname_count = len(uniqnames)
print(f"\n5.3.2 uniqnames length = {uniqname_count}")


# 5.4 CHALLENGE 01

print(f"\n5.4 Challenge 01") # f-string

# Variable assignment
attractions = ['Detroit Observatory', 'Museum of Art', 'Museum of Natural History']
print(f"\n5.4.2 Attractions = {attractions}")

# Return data type and print to screen (2 lines permitted)
attractions_type = type(attractions)
print(f"\n5.4.4 Data type = {attractions_type}")

# Return length and print to screen (one line only)
# print(len(attractions))
print(f"\n5.4.5 Length = {len(attractions)}")


# 6.0. BASIC ARITHMETIC (addition, subtraction, multiplication, division)

# 6.2 Challenge 02

# Counts
lecturer_count = 1
gsi_count = 6
ia_count = 2 # not considered instructors
lab_count = 12
student_count = 301

# 6.2.1 Addition (+ operator)
team_count = lecturer_count + gsi_count + ia_count
print(f"\n6.2.1: teaching_team_count = {team_count}")

# 6.2.2 Subtraction (- operator)
instructor_count = team_count - ia_count
print(f"\n6.2.2: instructor_count = {instructor_count}")

# 6.2.3 Multiplication (* operator)
max_enrollment = lab_count * 25 # approximate
print(f"\n6.2.3: max_enrollment = {max_enrollment}")

# 6.2.4 Floor division (// operator)
students_per_gsi = student_count // gsi_count
print(f"\n6.2.4 Student:Teacher ratio = {students_per_gsi}")

# 6.2.5 Max enrolled percentage
max_enrolled_pct = student_count / max_enrollment * 100
print(f"\n6.2.5 Max enrolled percent = {max_enrolled_pct:.2f}")
