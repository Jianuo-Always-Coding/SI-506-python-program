
# SI 506: Lab Exercise 01

## This Week's Lab Exercise

This week's lab exercise includes eight (8) problems that focus on comments, using built-in functions, basic arithmetic operations, and using built-in string methods.

:bulb: In order to check your work, try using the built-in function `print()` to print out the results.


## 1.0 Problem 01 (1 Point)

You've been provided with twelve (12) variables that represent locations on campus. These variables have been assigned string values that contain the names of those locations. Some of these variables have been formatted incorrectly and will produce run-time errors. Comment out the lines with incorrect variable assignments and create a list called `locations` that contains the remaining uncommented variables.

:bulb: You must use **exactly the same** list name provided in the instructions in order to pass the auto grader.

## 2.0 Problem 02 (1 Point)

Use the built-in function `len()` to return the number of elements in the list `locations`. Assign the return value to a new variable named `num_locations`.


## 3.0 Problem 03 (1 Point)

The variables listed below all have the number of study areas assigned to them as an integer.

* `north_quad_study_areas`
* `mason_hall_study_areas`
* `palmer_study_areas`
* `modern_lang_study_areas`
* `kinesiology_study_areas`
* `education_study_areas`
* `cccb_study_areas`
* `hatcher_study_areas`
* `shapiro_study_areas`

Calculate the total number of study areas among these nine buildings by adding up the variables and assigning the computed value to a new variable called `total_study_areas`

:bulb: You can add multiple variables together in one assignment statement. Also these numbers represent approximate numbers of study areas, counting entire floors or bookable rooms designated for studying. Visit [studyspaces.umich.edu](https://studyspaces.umich.edu/) or [the library website](https://www.lib.umich.edu/visit-and-study/study-spaces/building) for additional details on study spaces across campus.

## 4.0 Problem 04 (1 Point)

Calculate the average number of study areas per building among North Quad, Mason Hall, Palmer Commons, the Modern Languages Buiding, the Schools of Kinesiology and Education, CCCB, and the Hatcher and Shapiro Libraries by using the `total_study_areas` variable computed in Problem 03 and dividing it by the number of locations you computed earlier in Problem 02.

:bulb: Consider using **floor division** here.

## 5.0 Problem 05 (2 Points)

The variable `study_areas` is a string with the same data provided earlier about buildings and study rooms. Replace each semi-colon with a colon using a built-in string method and assign the new string object to a variable named `fixed_locations`.

:warning: Avoid editing the string assigned to the variable `study_areas` as any changes made could impact the autograder.

:bulb: Each building name should be followed by a colon, then the count of study areas in that building.

## 6.0 Problem 06 (2 points)

Use the appropriate string method to return the number of times the word `"Building"` occurs in the string assigned to the variable `fixed_locations`. Assign the return value to a new variable named `count_building`.

Utilize the same string method a second time in order to return the number of times `"Library"` occurs in the string assigned to the variable `fixed_locations`. Assign the return value to a new variable named `count_library`.

:bulb: Case-sensitivity matters. Do not assume that the strings "Diag" and "diag" are equivalent.

## 7.0 Problem 07 (1 point)

Build a formatted string literal (f-string) using the variables `count_building` and `count_library` from the previous problem. Create a variable named `statement` and assign the string to it.

The f-string is formatted as follows:

``` "There are 4 locations with 'Building' in their name and 2 locations with 'Library' in their name." ```

:bulb: Copy the example output above and paste it into your template file. Reformat the string into an f-string, utilizing the variables `count_building` and `count_library`.

## 8.0 Problem 08 (1 point)

The variable `hail` is assigned to a string with a portion of the lyrics to the [Michigan Fight Song](https://mgoblue.com/news/2009/6/29/Michigan_Fight_Song.aspx). Using the built-in string methods `.lower()` and `.upper()`, return a string where all of the characters are lowercase and a string where all of the characters are uppercase. Assign each of the return values to new variables `hail_lower` and `hail_upper`, respectively.

:warning: Do not edit the string assigned to the variable `hail` as any changes made could impact the autograder.
