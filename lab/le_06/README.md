# SI 506: Lab Exercise 06

## Background

This week's lab exercise focuses on reading from and writing to a text file. The source file provided is Amanda Gorman's poem "The Hill We Climb".  Amanda Gorman, National Youth Poet Laureate and the youngest inaugural poet in U.S. history delivered the poem at President Joe Biden and Vice President Kamala Harris's inaugural ceremony.

Gorman finished the poem the night after pro-Trump rioters sieged the Capitol building. “In my poem, I’m not going to in any way gloss over what we’ve seen over the past few weeks and, dare I say, the past few years. But what I really aspire to do in the poem is to be able to use my words to envision a way in which our country can still come together and can still heal,” she said. “It’s doing that in a way that is not erasing or neglecting the harsh truths I think America needs to reconcile with”. She drew inspiration from the speeches of American leaders during other historic times of division, including Abraham Lincoln and the Rev. Martin Luther King Jr.


## 1.0 Problem 01 (4 Points)

Modify the `read_file()` function. The function accepts a filepath string and encoding as arguments and returns a list of strings with each line in the text file as a list element. You are given incorrect implementation of the `read_file()` function. Correct the mistakes for the function to work.

   1. Modify the function definition. The function defines two parameters:
      * filepath (str): The path of the file to be read
      * encoding (str): name of encoding used to decode the file (default = utf-8)
   2. Modify the built-in `open()` method by fixing any typos.
   3. Modify the method called on `file_obj` with the appropriate method to read the line from the `file_obj`.
   4. Modify the string method called on `line` to remove any leading or trailing space characters.

To test this function, navigate to the `main()` function and using the provided `filepath`, call `read_file()` and assign its return value to `poem`.


## 2.0 Problem 02 (4 Points)

Implement the `has_phrase()` function. The function accepts two arguments: a list of lines from the poem and a phrase (it can be a single word or a full phrase) that you are trying to check for in the poem. It returns a `bool` value based on the presence or absence of the phrase in the poem. This function will be used in later problems. Do the following to implement the function:

   1. Loop over the `poem` list and use an `if` statement inside the loop. 
   2. Check if the phrase can be found in the line of the poem.
   3. If the phrase is present in the line of the poem, return `True`, otherwise return `False`.

:exclamation: Python is a case-sensitive programming language. Do not assume that each string or substring that you may be asked to access is consistent in terms of uppercase / lowercase usage.

## 3.0 Problem 03 (4 Points)

Implement the `file_lines_with_phrase()` function which finds lines of the poem containing a given phrase. The function accepts two arguments: a list of lines from the poem and a phrase (it can be a single word or a full phrase). It returns a list of lines from the poem that contain the phrase as a substring. This function will be used in later problems. Do the following to implement the function: 

   1. Create an empty list called `lines`.
   2. Loop over the `poem`  list and use an `if` statement inside the loop. 
   3. Check if the phrase can be found in the line of the poem. 
   4. In the `if` block, append the line to the `lines` list.
   5. Return `lines` after the loop ends.

:exclamation: Python is a case-sensitive programming language. Do not assume that each string or substring that you may be asked to access is consistent in terms of uppercase / lowercase usage.

## 4.0 Problem 04 (6 Points)

Implement the `find_phrases()` function. The function accepts two arguments: a list of lines from the poem and a list of phrases you are trying to check for in the poem. This function returns a list where each list element is a tuple consisting of 2 elements - a phrase that exists in the poem and list of lines of the poem having that phrase as a substring. Do the following to implement this function:

   1. Create an empty list `data`.
   2. Write a `for` loop to iterate over the list `phrases`.
   3. Inside the loop, use an `if` statement employing the `has_phrase()` function as the condition to check for the presence of the phrase.
   4. Inside the `if` block, use the `file_lines_with_phrase()` function to make a tuple. The phrase must be the first element and a list of poem lines containing the phrase must be the second element.
   5. Append the tuple to the list `data`.
   6. Return `data` at the end of the loop.

To test this function, go to the `main()` function and using the provided `phrases` list, call `find_phrases()` with `poem` and `phrases` as arguments and assign its return value to the object `phrases_in_poem`.


:exclamation: The list to be returned does not contain phrases that are not present in the poem.

## 5.0 Problem 05 (3 Points)

Implement the `write_file` function. The function accepts two arguments: a filepath string and a sequence (e.g., `list`). The function _must_ write each list element to its own line in the created file.

## 6.0 Problem 06 (4 points)

This problem focuses on tuple unpacking. Find the phrases from the provided list `phrases` that occur 3 or more times in the poem. Store the lines from the poem, that contain these phrases, as a substring in the list `frequent_phrases`.

   1. Loop over the `phrases_in_poem` list to get the phrase and lines of the poem using tuple unpacking.
   2.  Employ an `if` statement to check the count of occurrences of a phrase and store the lines from the poem in the list `frequent_phrases` if the phrase occurs 3 or more times.

:exclamation: The list `frequent_phrases` is a list of lines from the poem.

Call the function `write_file()` and pass to it the filepath string `'stu_frequent_phrases_results.txt'` and the list `frequent_phrases` that was created in the previous step.