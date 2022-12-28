
# SI 506: Problem Set 02

## This week's Problem Set

This week's problem set includes four problems that focus on strings, lists, and string/list operations.

:bulb: In order to check your work, try using the built-in function `print()` to print out the results.

:bulb: Feel free to refer to w3school's [List/Array methods page](https://www.w3schools.com/python/python_ref_list.asp).

## Background

The University of Michigan offers numerous resources that can help you and other students in their well-being journeys. This week's problem utilizes a different string representation of the wellbeing resources encountered in the lab exercise. You will be working with the multi-line string variable `wellbeing_resources` to start with:

```python
wellbeing_resources = 'Counseling and Psychological Services (CAPS)|734-764-8312, '\
'SilverCloud|, '\
'Dean of Students Office|734-764-7420, '\
'Office of Student Conflict Resolution|734-936-6308, '\
'Services for Students with Disabilities (SSD)|734-763-3000, '\
'Maize and Blue Cupboard (MBC)|734-936-2794, '\
'Ginsberg Center for Community Service Learning|734-763-3548, '\
'Sexual Assault Prevention and Awareness Center (SAPAC)|734-764-7771, '\
'Multi-ethnic Student Affairs (MESA)|734-763-9044, '\
'Spectrum Center|734-763-4186'
```

As we noted in the lab exercise we hope that through this exercise, in addition to obtaining an understanding of strings and list operations, you also gain awareness of the numerous resources that UMich offers for your benefit as listed in the SI 506 [Syllabus](https://si506.org/syllabus/). You can explore more about them at https://wellbeing.studentlife.umich.edu/

## 1.0 Problem 01 (30 Points)

1. You have been provided with a variable containing a single string expressed across multiple lines named `wellbeing_resources`. Review each resource and note which character(s) delineate (separate) each resource.
Call the appropriate string method to return a list of resource elements. Assign the return value of the string method to the variable `wellbeing`.

:bulb: This is what the value assigned to `wellbeing` must match after calling the string method:
```python
['Counseling and Psychological Services (CAPS)|734-764-8312', 'SilverCloud|', 'Dean of Students Office|734-764-7420', 'Office of Student Conflict Resolution|734-936-6308', 'Services for Students with Disabilities (SSD)|734-763-3000', 'Maize and Blue Cupboard (MBC)|734-936-2794', 'Ginsberg Center for Community Service Learning|734-763-3548', 'Sexual Assault Prevention and Awareness Center (SAPAC)|734-764-7771', 'Multi-ethnic Student Affairs (MESA)|734-763-9044', 'Spectrum Center|734-763-4186']
```

2. Create a new list variable named `health` and assign to it the first two elements of `wellbeing` using list slicing.

    :warning: In order to pass the autograder you *must* use list slicing in one statement.

3. Create a new list variable named `academic` and assign to it the third, fourth, and fifth elements of `wellbeing` using list slicing.

    :warning: In order to pass the autograder you *must* use list slicing in one statement.

4. Create a new list variable named `community` and assign to it the sixth and seventh elements of `wellbeing` using list slicing and negative index values.

    :warning: In order to pass the autograder, you *must* use both list slicing and negative index values in one statement.

5. Create a new list variable named `marginalized_comm` and assign to it the last three elements of `wellbeing` using list slicing and negative indexing.

    :warning: In order to pass the autograder, you *must* use both list slicing and negative index values in one statement.

## 2.0 Problem 02 (40 Points)

1. Call the appropriate list method to extend `health` with `addl_health_resources`.

    :bulb: This is what the value assigned to `health` must match after calling the list method:
    ```python
    ['Counseling and Psychological Services (CAPS)|734-764-8312', 'SilverCloud|',
    'UMSI Embedded CAPS Psychologist|Ashley Evearitt', 'Wolverine Wellness|734-763-1320']
    ```

2. Call the appropriate list method to add `uhs` as the last `health` element.

3. Call the appropriate list method to insert `trotter` as the second `marginalized_comm` element.

    :bulb: The second element does not necessarily mean the second index.

4. Using list indexing and string concatenation methods, mutate `addl_academic_resources` by concatenating each element with the respective phone numbers in `addl_academic_resource_numbers`.

    :bulb: This is what the value assigned to `addl_academic_resources` must match after concatenating the strings:
    ```python
    ["Sweetland Center for Writing|734-764-0429", "Office of the Ombuds|734-763-3545"]
    ```
5. Call the appropriate list method to extend `academic` with `addl_academic_resources`.

    :bulb: Your output must match the following:
    ```python
    ['Dean of Students Office|734-764-7420', 'Office of Student Conflict Resolution|734-936-6308', 'Services for Students with Disabilities (SSD)|734-763-3000', 'Sweetland Center for Writing|734-764-0429', 'Office of the Ombuds|734-763-3545']
    ```

## 3.0 Problem 03 (20 Points)

1. Use the appropriate list method to reverse the order of `health` elements.

2. Use the appropriate list method to sort the order of `academic` elements in ascending alphabetical order.

3. Use the appropriate list method to sort the order of `marginalized_comm` elements in descending alphabetical order. Be sure to also specify the parameter `reverse` in the relevant list method as `True` `(reverse=True)`.

4. Using the appropriate list method, find the index value of `UMSI Embedded CAPS Psychologist|Ashley Evearitt` in `health`. Assign this index value to the variable `umsi_caps`.

5. Slice `health` by using the `umsi_caps` variable created in the previous problem. Slice `UMSI Embedded CAPS Psychologist|Ashley Evearitt` and `Wolverine Wellness|734-763-1320` from `health`. Assign this new list to a variable named `student_focused_health_resources`.

    :exclamation: In order to pass the autograder, you must use the `umsi_caps` variable in your slicing statement.

## 4.0 Problem 04 (10 Points)

1. Retrieve the first element from `health` and convert it into a tuple with the name as the first element and the phone number as the second. Assign this tuple to a variable named `uhs`.

    :bulb: Your output must match the following:
    ```python
    ('University Health Service (UHS)', '734-764-8320')
    ```

2. Retrieve the last element from `health` using *negative index values* and convert it into a tuple with the name as the first element and the phone number as the second. Assign this tuple to a variable named `caps`.

    :bulb: Your output must match the following:
    ```python
    ('Counseling and Psychological Services (CAPS)', '734-764-8312')
    ```

3. Working with `marginalized_comm`, call the appropriate string method that accepts an iterable (e.g., a list) as an argument and return a new string composed of the `marginalized_comm` elements, each of which is separated by a comma. Assign this new string to a variable named `marginalized_comm_str`.

    :bulb: Your output must match the following:
    ```python
    'Trotter Multicultural Center|734-763-3670,Spectrum Center|734-763-4186,Sexual Assault Prevention and Awareness Center (SAPAC)|734-764-7771,Multi-ethnic Student Affairs (MESA)|734-763-9044'
    ```