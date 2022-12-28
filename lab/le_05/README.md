# SI 506: Lab Exercise 05

## This week's Lab Exercise

This week's lab exercise includes five (5) problems focused on creating and calling functions.

## Data description

At University of Michigan, there are more than 1,700 student organizations with opportunities to get involved based on your interests, skills, or identity. This week's dataset is sourced from an official campus directory of student organizations, called [Maize Pages](https://maizepages.umich.edu/organizations), which is managed by the [Center for Campus Involvement](https://campusinvolvement.umich.edu/). Through the Maize Pages website and the Center for Campus Involvement's calendar of [Programs & Events](https://events.umich.edu/day), you can find tons of opportunities to get involved around campus.

For this lab, you are provided with a list of strings assigned to the variable `student_orgs` that includes some basic information about several of the student organizations on campus. Each string element represents an organization and includes the organization's name, email, category, a brief description of the organization, and a binary number that indicates whether the organization is currently active (1=Active; 0=Inactive).


## 1.0 Problem 01 (4 Points)

Define a function named `split_strings()` that:

1. Defines a single parameter named `orgs` (a `list`)
2. Loops over the string elements of the list using a range-based for loop.
3. Splits the string elements on the correct delimiter
4. Returns the list of organizations as a list of lists

After implementing the function, call `split_strings()` and pass to it, as an argument, the list of `student_orgs`. Assign the return value to a variable named `student_orgs_split`.

Using list indexing, access the first element in `student_orgs_split` and assign it to the variable `student_org_headers`. Using list slicing, access the rest of the elements in `student_orgs_split` and assign them to the variable `student_org_data`.


## 2.0 Problem 02 (3 Points)

Define a function named `convert_to_int()` that:

1. Defines a single parameter named `org` (a `list`)
2. Accesses the last element in the list - representing the organization's 'Active' status (1 = Active; 0 = Inactive) - and casts it to an integer
3. Returns the updated list

After implementing the function, loop over the `student_org_data` and call `convert_to_int()`, passing to it as an argument each organization in `student_org_data`.


## 3.0 Problem 03 (5 Points)

Define a function named `get_org_email_by_active_status()` that defines one required parameter and one optional parameter with a default value:

* `orgs` (list): list of nested organization lists; required
* `active` (int): integer (1 or 0) that indicates an organization's status with a default of 1; optional

In the function block, create an empty list and assign it to the variable `emails`. Looping over the passed in organizations list, access the element representing the 'Active' status using list indexing and check if it matches the value passed in the argument `active`. If it does, append _only_ the element representing the organization's email to the `emails` list. Return the `emails` list.

After implementing the function, call `get_org_email_by_active_status()` twice:
1. Assign the first call to the variable `active_emails`. Remember that active status is 1.
2. Assign the second call to the variable `inactive_emails`. Remember that inactive status is 0.

Pass to each function call, as an argument, the list of `student_org_data` and the corresponding integer value.


## 4.0 Problem 04 (6 points)

Define a function named `get_organization_by_category()` that defines two parameters:

* `orgs` (list): list of nested organization lists
* `category` (str): organization category or group

In the function, create an empty list and assign it to the variable `org_names`. Looping over the list of organizations, access the element that represents the organization's category and use the appropriate string method to check if the element starts with the passed in `category` argument.

:exclamation: Python is a case-sensitive programming language. Do not assume that each string or substring that you may be asked to access is consistent in terms of uppercase / lowercase usage.

:bulb: You _must_ employ a particular string method to check if the category element starts with a passed in `str` literal.

Append _only_ the organization's name to the list `org_names` if the category is a match. Return the list `org_names`.

Call the `get_organization_by_category()` function four (4) times:
1. Assign the first return value to the variable `sports_orgs` and pass to the function the variable `student_org_data` and the `str` 'Sports'.
2. Assign the second return value to the variable `academic_orgs` and pass to the function the variable `student_org_data` and the `str` 'Academic'.
3. Assign the third return value to the variable `creative_orgs` and pass to the function the variable `student_org_data` and the `str` 'Creative'.
4. Assign the last return value to the variable `service_orgs` and pass to the function the variable `student_org_data` and the `str` 'Service'.


## 5.0 Problem 05 (7 points)

The variable `search_terms` is assigned to a tuple with three (3) `str` elements. Using sequence unpacking, access each element in the tuple and assign each element to the variables `chess`, `coding`, and `community`, respectively.

Define a function named `search_org_descriptions()` that defines two parameters:

* `orgs` (list): list of nested organization lists
* `search_term` (str): search filter string

In the function block, create an empty list and assign it to the variable `org_names`. Loop over the list of organizations and access the string element that represents that organization's description, in order to check if the passed in argument `search_term` is contained in the organization's description. Append _only_ the name of each organization, with a matching word in the description, to the list `org_names`. Return the list `org_names`.

:exclamation: Python is a case-sensitive programming language. Do not assume that each string or substring that you may be asked to access is consistent in terms of uppercase / lowercase usage.

Call the `search_org_descriptions()` function three (3) times:
1. Assign the first return value to the variable `chess_orgs` and employ keyword arguments passed to the function in _reverse order_ using the variable `chess`.
2. Assign the second return value to the variable `coding_orgs` and employ keyword arguments passed to the function in _reverse order_ using the variable `coding`.
3. Assign the third return value to the variable `community_orgs` and employ keyword arguments passed to the function in _reverse order_ using the variable `community`.

:exclamation: You _must_ employ keyword arguments passed to the function in _reverse order_ in order to pass the auto grader. You must also style the keyword argument assignment correctly (e.g., `keyword_arg=value`, not `keyword_arg = value`).
