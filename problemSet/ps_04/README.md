
# SI 506: Problem Set 04

## This week's Problem Set

This week's problem set includes seven (7) problems that focus on loops and
conditional statements.

## Background
The University Career Fair is coming up next month. This year's career fair will
be held at the Michigan Union. There will be more than 100 companies attending,
and you can find more information about your potential employers through
Handshake. (https://umich.joinhandshake.com/).

For this problem set, you are provided with a list of employers that includes
basic information about the employers attending the career fair, including
names, locations, the total number of employees, websites, and their industries,
respectively. You are going to use `for` loops, `while` loops, and conditional
statements to complete the problems below.

```python
employers = [
    "Company Name, Location, Number of Employees, Website, Industry",
    "Adobe Systems, California, 25000, http://www.adobe.com, software",
    "Bloomberg, New York, 25000, http://careers.bloomberg.com, Financial",
    "Boston university, Massachusetts, 25000, http://www.bu.edu, Education",
    "Chewy, Florida, 25000, https://careers.chewy.com/us/en/c/student-program, ecommerce",
    "DHL Consulting, Florida, 200, http://www.dhl-consulting.com, Consulting",
    "Fisher Investments, Washington, 5000, http://www.fishercareers.com, financial",
    "Gartner, Connecticut, 25000, http://jobs.gartner.com, consulting",
    "Gallagher, Illinois, 25000, https://jobs.ajg.com/, Insurance",
    "Guidehouse, Virginia, 25000, https://guidehouse.com, Consulting",
    "Kohl's, Wisconsin, 25000, https://careers.kohls.com/internships, Retail",
    "Meijer, Michigan, 25000, https://jobs.meijer.com, retail",
    "Morningstar, Illinois, 10000, http://www.morningstar.com, Financial",
    "Neon Financial, Illinois, 10, https://www.neonforlife.com, Financial",
    "Northwestern Medicine, Illinois, 25000, https://jobs.nm.org/, Healthcare",
    "Point72, Connecticut, 1000, http://www.Point72.com, Financial",
    "Procter & Gamble (P&G), Ohio, 25000, https://www.pgcareers.com, Consumer Packaged Goods",
    "Samsung SDI America, Michigan, 1000, https://www.samsungsdi.com, Manufacturing",
    "Sun Communities, Michigan, 5000, http://www.suncommunities.com, Real Estate",
    "TOPIT, Texas, 10, http://www.topit.co, Software",
    "TikTok, California, 10000, https://careers.tiktok.com/campus, Software",
    "Uline, Wisconsin, 10000, https://www.uline.jobs, Wholesale Trade",
    "University of Michigan International Center, Michigan, 50, http://internationalcenter.umich.edu, Education",
    "Veeam Software, Georgia, 5000, https://careers.veeam.com, Software",
    "Welltower, Ohio, 1000, http://www.welltower.com, Real Estate"
]
```

## 1.0 Problem 01 (20 points)
Using a `for` loop, split each string element in the list `employers` to a list
and assign it back to its original position.

1. Using a `for` loop with the `range()` type, iterate over each element in
`employers`.

2. In the loop, utilize an appropriate string method to convert each element
in `employers` to a list. Assign the converted value to its original position.

    After transformation, the `employers` list *must* be structured in the same
    manner as the list below:

    ```python
    [
        ['Company Name', 'Location', 'Number of Employees', 'Website', 'Industry'],
        ['Adobe Systems', 'California', '25000', 'http://www.adobe.com', 'software'],
        ['Bloomberg', 'New York', '25000', 'http://careers.bloomberg.com', 'Financial'],
        ...
        ['Welltower', 'Ohio', '1000', 'http://www.welltower.com', 'Real Estate']]
    ```

3. After the loop terminates, extract the first element from the transformed
`employers` list and assign it to a variable named `header`.

    The `header` list *must* be structured in the same manner as the list below:

    ```python
    ['Company Name', 'Location', 'Number of Employees', 'Website', 'Industry']
    ```

## 2.0 Problem 02 (20 points)
Implement the accumulator pattern using a `for` loop and `if-else` conditional
statements, then add the employer's information to the `universities` list if it is
a university; otherwise, add it to the `other_companies` list.

1. Create an empty list and assign it a variable named `universities`.

2. Create an empty list called `other_companies`.

3. Using a `for` loop, iterate over each element in `employers`, excluding
the header row.

4. In the loop block, check whether the employer is a university. If it is a
university, add the employer's information to the `universities` list.
Otherwise, add the information to the `other_companies` list.

   :heavy_exclamation_mark: Python is a case-sensitive programming language.
   For this problem, ensure that your `if` statement performs a
   *case-insensitive* comparison of the string values.

The `universities` list you create must contain the following elements:

```python
[
    ['Boston university', 'Massachusetts', '25000', 'http://www.bu.edu', 'Education'],
    ['University of Michigan International Center', 'Michigan', '50', 'http://internationalcenter.umich.edu', 'Education']
]
```

## 3.0 Problem 03 (20 points)

Implement the accumulator pattern using a `for` loop and `if-elif-else`
conditional statements in order to classify the employers into different bins.

1. Assign an empty list to each of the following five (5) variables:
`financial`, `software`, `real_estate`, `consulting`, `other_industry`.

2. Using a `for` loop, iterate over each element in `other_companies`.

3. In the loop, extract the industry information from each company and assign
it to a variable called `industry`.

4. In the loop, check the value of the variable `industry`. If the value is
`'financial'`, `'software'`, `'real estate'`, or `'consulting'`, add *_only_*
the names of those companies to the corresponding lists you initialized in
step 1. Otherwise, add the names of the companies to the `other_industry` list.

The five lists *must* contain the following elements:

```python
# Financial
[
    'Bloomberg',
    'Fisher Investments',
    'Morningstar',
    'Neon Financial',
    'Point72'
    ]

# Software
[
    'Adobe Systems',
    'TOPIT',
    'TikTok',
    'Veeam Software'
    ]

# Real estate
[
    'Sun Communities',
    'Welltower'
    ]

# Consulting
[
     'DHL Consulting',
     'Gartner',
     'Guidehouse'
     ]

# Other companies
[
    'Chewy',
    'Gallagher',
    "Kohl's",
    'Meijer',
    'Northwestern Medicine',
    'Procter & Gamble (P&G)',
    'Samsung SDI America',
    'Uline'
    ]
```

## 4.0 Problem 04 (25 points)

Using a `for` loop and `if-elif` conditional statements, find the companies
with the least number of employees.

1. Create an empty list called `smallest_companies`.

2. Assign the Python representation of infinity to a variable called
`least_num_employees`.

3. Using a `for` loop, iterate over each element in `other_companies`.

    :warning: Do not use the `range()` type for this problem

4. In the loop, extract the number of employees in each company, and assign it
to a variable called `num_employees`.

    :bulb: Your variable `num_employees` should have been assigned an `int`
    value.

5. In the loop, compare the value in `num_employees` with the value of
`least_num_employees`. Update `least_num_employees` if the number
of employees for the company is less than the value in `least_num_employees`.
Then remove all items in the list `smallest_companies` and append *_only_* the
name of the company to `smallest_companies`.

    :bulb: Two companies in the `other_companies` list have the least number of
    employees. Hence, you should carefully construct your conditional statements
    to handle a tie.

The `smallest_companies` list *must* be structured in the same manner as
the list below:

```python
['Neon Financial', 'TOPIT']
```

## 5.0 Problem 05 (20 points)

We have provided a multiline string named `salaries`. Each line contains a
company name, a job title, and an average salary for the job. You will be asked
to convert the multiline string to a list and extract salary information in
the following problems.

```python
salaries = """Adobe; Computer Scientist; 262012
Adobe; Data Analyst; 121390
TikTok; Policy Analyst; 107240
Fisher Investments; Portfolio Analyst; 97349
Bloomberg; senior data Analyst; 166267
Procter & Gamble; Data Scientist; 142429
Adobe; Research Scientist; 248819
Chewy; Software Engineer; 153402
Morningstar; Financial Analyst; 86022
Morningstar; Software Engineer; 124599
TikTok; Software Engineer; 188801
Fisher Investments; Financial Analyst; 99365
TikTok; data Analyst; 109457
Bloomberg; Software Engineer; 182015
Procter & Gamble; Data Analyst; 103472
TikTok; Designer; 114163
"""
```

1. Utilize an appropriate string method to split the multiline string `salaries`
into a list of lines, and assign it to a variable called `salary_list`.

2. Using a `for` loop with the `range()` type, iterate over each string element
in `salary_list`.

3. In the loop, split each string element to a list and assign the new nested
list to `salary_list` in the same position as the string from which it was
constructed.

Your `salary_list` *must* be structured in the same manner as the list below:

    ```python
    [
        ['Adobe', 'Computer Scientist', '262012'],
        ['Adobe', 'Data Analyst', '121390'],
        ['TikTok', 'Policy Analyst', '107240'],
        ['Fisher Investments', 'Portfolio Analyst', '97349'],
        ...,
        ['TikTok', 'data Analyst', '109457'],
        ['Bloomberg', 'Software Engineer', '182015'],
        ['Procter & Gamble', 'Data Analyst', '103472'],
        ['TikTok', 'Designer', '114163']
    ]
    ```


## 6.0 Problem 06 (25 points)

In this problem, you will implement a `while` loop (a.k.a. an indefinite loop).

:exclamation: Beware of getting stuck in an infinite loop (mistakes do happen).
If you need to exit the infinite loop, type `CTRL + C` or `command + C` in the
terminal.

1. Assign an empty list to a variable named `da_salary`.

2. Assign zero (0) to a variable named `idx`.

3. Utilize a `while` loop to iterate over the list `salary_list`.

    :bulb: You should use the variable `idx` in your test expression for the
    `while` loop.

4. In the `while` loop, implement a conditional statement employing the
appropriate membership operator, populate `da_salary` with the
**Data Analyst's and Senior Data Analyst's salaries** from `salary_list`.
Remember to increment the value of the variable `idx` by one (1) in each
iteration.


    Your `da_salary` must include the following elements in the specified order:

    ```python
    [121390, 166267, 109457, 103472]
    ```

   :bulb: Indexing may be required to access the job title within each list.
   When performing a case-insensitive comparison of two strings, convert the
   strings to lower case before performing the comparison.

5. Utilize two built-in functions to calculate the average salary in the
`da_salary` list.

    :bulb: The built-in `sum()` function must be used to calculate the sum of
    all items in the `da_salary` list

    :bulb: The built-in `len()` function must be used to calculate the number of
    items in the `da_salary` list

## 7.0 Problem 07 (20 points)

You will implement a `while` loop with an `if` statement and the `break`
statement to solve the following problem.

1. Assign zero (0) to a variable named `idx`.

2. Utilize a `while` loop to iterate over the list `salary_list`.

    :bulb: You should use the variable `idx` in your test expression for the
    `while` loop.

3. In the loop, check each job's salary. If it is less than one hundred thousand
(100000), create a tuple named `company_salary` that contains two
elements: the company name and the job salary. Then immediately exit the while loop
completely. Similar to problem 6, you *must* increment the value of the variable
`idx` by one (1) in each iteration.

Your `company_salary` *must* be structured in the same manner as the
tuple below:

```python
('Fisher Investments', 97349)
```