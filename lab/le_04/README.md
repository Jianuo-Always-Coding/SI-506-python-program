# SI 506: Lab Exercise 04

## This week's Lab Exercise

This week's lab exercise includes five (5) problems that focus on loops and
conditional statements.

## Background
The University Career Fair is coming up next month. This year's career fair will
be held at the Michigan Union. There will be more than 100 companies attending,
and you can find more information about potential employers through
Handshake. (https://umich.joinhandshake.com/).

For this lab exercise, you are provided with a list of employers that includes
basic information about the employers attending the career fair, including
names, locations, the total number of employees, position types, and their industries, respectively. You are going to use `for` loops, `while` loops, and conditional statements to complete the problems below.

```python
employers = [
    ['Adobe Systems', 'California', '25000', ('Job', 'Internship'), 'software'],
    ['Advantage Health Centers', 'Michigan', '100', ('Job', 'Internship'), 'healthcare'],
    ['Amtrak', 'Various Locations', '25000', ('Job', 'Internship'), 'Transportation'],
    ['Blue Cross Blue Shield of Michigan', 'Michigan', '25000', ('Job', 'Internship'), 'Insurance'],
    ['Boston University', 'Massachusetts', '25000', ('Fellowship', 'Internship'), 'Education'],
    ['Elevance Health', 'Indiana', '25000', ('Internship', 'Fellowship'), 'healthcare'],
    ['Epic', 'Wisconsin', '20000', ('Internship', 'Job'), 'Software'],
    ['fairlife, LLC', 'Illinois', '1000', ('Job', 'Internship'), 'food'],
    ['Fan Duel', 'Florida', '1000', ('Internship', 'Job'), 'Software'],
    ['Gallagher', 'Illinois', '25000', ('Job',), 'Insurance'],
    ['GM Financial', 'Texas', '10000', ('Job', 'Internship'), 'automotive'],
    ['Mayo Clinic', 'Minnesota', '25000', ('Job', 'Internship'), 'Healthcare'],
    ['Northwestern Medicine', 'Illinois', '25000', ('Job', 'Fellowship'), 'Healthcare'],
    ['Optum', 'Minnesota', '25000', ('Job', 'Internship'), 'Healthcare'],
    ['Penske Truck Leasing', 'Pennsylvania', '10000', ('Job', 'Internship'), 'transportation'],
    ['Progressive', 'Wisconsin', '25000', ('Internship', 'Job'), 'insurance'],
    ['TikTok', 'California', '10000', ('Job', 'Internship'), 'Software'],
    ['Thomson Reuters', 'Minnesota', '25000', ('Internship', 'Job'), 'Software'],
    ['University of Michigan International Center', 'Michigan', '50', ('Internship', 'Fellowship'), 'Education'],
]
```

## 1.0 Problem 01 (3 points)
1. Loop over the `employers` list using the `range` type and convert the number of employees from type `str` to type `int`. Take the converted number and assign it back to the original position in `employers`.

:bulb: Convert each number encountered to an integer and access the list element using list indexing to update the number of employees.

## 2.0 Problem 02 (4 points)
Implement an `if` statement inside a `for` loop to identify how many large employers have 'Fellowship' positions in the `employers` list. *For this problem, large employer is considered having 20000 employees or more*.

Loop over the `employers` list and utilize a conditional statement that checks if the employer's position type includes 'Fellowship' and employs 20000 people or more. Increment the counter `large_fellowship` by one (`1`) if the employer fulfills the conditional statement.

:bulb: For this problem, you can safely assume that the 'Fellowship' string in the "employers" list does not have any other case format.

## 3.0 Problem 03 (4 points)
Implement an `if` statement inside a `for` loop to check for mid-sized employers in the `employers` list. *For this problem, mid-size is inclusively the number of employees between 1000 and 5000*.

Loop over the `employers` list; if the employer has the number of employees anywhere from 1000 to 5000 (inclusive), append the name of the employer to a list called `mid_size_employers`.

## 4.0 Problem 04 (4 points)
Implement an `if-elif-else` statement inside a `for` loop and count the employers based on their industry.
Loop over the `employers` list and if the category is 'software', increment a variable called `software_count` by one. If the category is 'healthcare', increment a variable called `health_count` by one. If the category is 'education', increment a variable called `edu_count` by one. If the category is 'transportation', increment a variable called `transport_count` by one. If the category is 'insurance', increment a variable called `insurance_count` by one. Otherwise, increment a variable called `other_count` by one.

:bulb: Recall that you can utilize the built-in function print() to check on the values being counted in the variables. When satisfied with your conditional statements you can comment out print() or remove the expression from your code.

## 5.0 Problem 05 (5 points)
In this problem, you will implement a `while` loop (a.k.a. an indefinite loop) to calculate the average number of employees in the healthcare industry in the `employers` list.

:exclamation: Beware of getting stuck in an infinite loop (mistakes do happen).
If you need to exit the infinite loop, type `CTRL + C` or `command + C` in the terminal.

1. The variable `idx` is assigned to the value 0. While this value is less than the length of the `employers` list the `while` loop will execute. Remember to increment the value of the variable `idx` by one (1) during each iteration of the loop.
2. Implement an `if` statement within the `while` loop that checks if the industry of an employer is 'healthcare'.
3. If the employer's industry is healthcare then add employee count to the variable `num_employees`.
4. Once the `while` loop is complete, calculate the average number of employees using the variable `num_employees` as the numerator and `healthcare_count` calculated in Problem 04 as the denominator.

:bulb: You must use a floor division to solve this problem.
