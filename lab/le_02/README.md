# SI 506: Lab Exercise 02

## This week's Lab Exercise

This week's lab exercise includes eight (8) problems that focus on strings and list operations.

:bulb: Feel free to refer to w3school's [List/Array methods](https://www.w3schools.com/python/python_ref_list.asp) page.

## Background
Well-being is an important aspect (if not the most important aspect) of our lives. As is described at https://wellbeing.studentlife.umich.edu/:

***"Well-being is the journey we take, one step and one choice at a time, to care for ourselves. It’s how we appraise and feel about our lives, including success in school and all other aspects. It’s personal, family and friends, community, and beyond."***

The University of Michigan offers numerous resources that can help you and other students in their well-being journeys. Our lab exercise this week deals with a list of the most often used resources. The resources are in the following format:

> \<name of the resource>:<phone number of the resource center's office>

We hope that through this exercise, in addition to obtaining an understanding of strings and list operations, you also gain awareness of the numerous resources that U-M offers for your benefit (These are also available in the SI 506 [Syllabus](https://si506.org/syllabus/)). You can explore more about them at https://wellbeing.studentlife.umich.edu/


## 1.0 Problem 01 (3 points)

The variable `wellbeing_resources_data` is a string comprising of well-being resources at U-M. Note that each resource is delineated (i.e., separated) by a new line. Call the appropriate string method to return a list of resource elements. Assign the list to the variable `wellbeing_resources`.

## 2.0 Problem 02 (3 points)

Among the `wellbeing_resources` elements there is one resource that does not have a phone number associated with it. Using indexing retrieve the resource without a phone number and assign it to the variable `wellbeing_resource_with_no_phone`.

:bulb: Recall that Python employs zero-based indexing.

## 3.0 Problem 03 (1 point)

When working on problem 4 and 5 below you will create a new variable called `wellbeing_resources_temp`. This variable will be assigned a list representation of the `wellbeing_resources_data` string. This is similar to what you did for problem 01 above.

The goal behind the creation of this variable is to avoid modification of the contents in our original `wellbeing_resources` list which will be needed from problem 6 onwards.

## 4.0 Problem 04 (2 points)

Using the `list.remove()` method, remove the wellbeing resource that does not have a phone number associated with it (the one you identified in problem 02 above) from the `wellbeing_resources_temp` list.

## 5.0 Problem 05 (2 points)

Call the appropriate `list` method to return a version of the list that reverses the elements in `wellbeing_resources_temp`.

## 6.0 Problem 06 (2 points)

There is an additional resource that has to be added to the `wellbeing_resources` list. This resource is specified in the `additional_data` variable. Add this data into the existing `wellbeing_resources` list using the appropriate list method.

## 7.0 Problem 07 (1 point)

Fetch the index of the resource you added in problem 06 above using the appropriate list method and assign the return value to the variable `new_data_index`.

## 8.0 Problem 08 (1 point)

List all elements in the `wellbeing_resources` list between the indices 4 to 8 (both inclusive) and assign to the variable `elements_sliced` the resulting list slice.


