# SI 506: Problem Set 05

## This week's Problem Set

This week's problem set includes seven (7) problems that focus on functions,
loops and conditional statements.

## Background

For this week's Problem Set, you will analyze data from the
[University of Michigan Maize Pages]("https://maizepages.umich.edu/organizations")
on activities organized by the student clubs in various categories.

You are provided with a list of strings called `club_events`. The list
contains the information specified by the header.

- Host Organization: Name of the student club
- Event Name: Name of the activity
- Date: The event start date is formatted as year/month/day.
- Start Time: Event start time
- Duration: Total number of hours of activity
- Location: Location of the event
- Theme: Type of activity


## Problem 01 (20 Points)

### Part 1

Define a function called `convert_str_to_list` provisioned with two parameters in order:
`element` (a string element of `club_list`) and `separator` (a string delimiter).
Using an appropriate string method, convert the string element to a list and
return the converted list to the caller.

### Part 2
Using a `for` loop with `range()` type, iterate over the elements in the
`club_events` list. In the loop code block, call the `convert_str_to_list`
function on each element in `club_events`. You *must* pass
**keyword arguments in reverse order** when calling the function.

:exclamation: Be mindful of spacing when using keyword arguments.

After mutating the list, the `club_events` list *must* be structured in the same
manner as the list below:

```python
    [
        ['Host Organization', 'Event Name', 'Date', 'Start Time', 'Duration', 'Location', 'Theme'],
        ['Zouk Dance Club', 'Zouk Dance Club Lesson', '2022/9/29', '6 PM', '3 hours', 'Mason Hall', 'Arts & Music'],
        ['Student Astronomical Society', 'SAS Open House', '2022/9/30', '9 PM', '2 hours', 'Angell Hall', 'Learning'],
        ...
    ]
```

## Problem 02 (20 Points)

1. Define a function called `get_duration` provisioned with a single parameter `event_info`
(a list element of `club_events`). This function returns a float representing
the event duration to the caller.

2. Define a function called `get_event_month` provisioned with a single parameter `event_info` (a list element of `club_events`). This function returns an integer number representation of event month to the caller.

    :bulb: You should utilize an appropriate string method to split the date information, then extract the month.

To check if you have implemented the functions correctly, try calling `get_duration(club_events[1])` and `get_event_month(club_event[1])`. The correct answers should be 3.0 and 9, respectively.

## Problem 03 (30 Points)

### Part 1
Define a function called `event_with_longest_duration` that returns a tuple containing the name of the longest event and its duration. Using a `for` loop and a conditional statement with the newly defined function, find the longest
event from the `club_events` list.

1. Define a function called `event_with_longest_duration` provisioned with a single parameter `club_events` (a list of events).

2. In the function code block, assign zero (0) to a variable named `longest_duration`.

3. Using a `for` loop and skipping the headers list, iterate over `club_events`.

4. In the loop, call the `get_duration` function to find the event duration and then use an `if` statement to check whether the event duration is greater than the value of `longest_duration`. If the `if` statement evaluates to `True`, update the value of `longest_duration` and assign the event name to a variable `longest_event`.

    :bulb: For this problem, you can safely assume there is only one event that has the longest duration. Hence you do not need to handle the tie.

5. The function `event_with_longest_duration` *must* return a tuple of two elements. The first element should be `longest_event`, and the second element should be `longest_duration`

### Part 2
Call the `event_with_longest_duration` function, unpacking the return value into two variables: `event_name` and `event_duration`.

## Problem 04 (30 Points)

### Part 1
Define a function called `categorize_events_by_month` that returns a list of required event names. Using a `for` loop and a conditional statement with the newly defined function, find the required events from the `club_events` list.

1. Define a function called `categorize_events_by_month` provisioned with two parameters in order: `club_events` (a list of events) and `month` (an integer represents the month).

2. In the function code block, initialize an empty list called `events_by_month`.

3. Using a `for` loop and skipping the headers
list, iterate over the information in `club_events`.

4. In the loop, call the function `get_event_month` to get an integer representation of the event month.

5. In the loop, using an `if` statement, check whether the event month is the same as the value of `month` we pass to the function `categorize_events_by_month`. If the `if` statement evaluates to `True`, append the event name to the `events_by_month` list.

6. After the loop terminates, return the `events_by_month` to the caller.

### Part 2
Call the function, passing the `club_events` list and the integer ten (10) as arguments. Assign the return value to the variable named `oct_events`.

The `oct_events` list you create will contain the following elements:
```python
['Apple Orchard Trip 2022',
'September Zouk Social',
'Bachata Class',
'A2ML Weekly Social',
'Bujinkan Budo Training Session',
'Technique Class',
'Spartan Grand Classic',
'Cary Price 2022',
'Boo Bash 2022',
'General Meeting',
'NIRCA Cross Country Great Lakes Regional'
]
```


## Problem 05 (25 Points)

### Part 1
Define a function called `categorize_events_by_theme` that returns a list of categorized event names. Using a `for` loop and a conditional statement with the newly defined function, find the required events from the `club_events` list.

1. Define a function called `categorize_events_by_theme` that provisioned with two parameters in order: `club_events` (a list of events) and `theme` (a string representing the event category).

2. In the function code block, initialize an empty list called `events_by_theme`.

3. Using a `for` loop and skipping the headers
list, iterate over the information in `club_events`.

4. In the loop, using an `if` statement, check whether the value of `theme` pass to the function is a substring of the string representing the event theme in each iteration. If the `if` statement evaluates to `True`, append the event name to the `events_by_theme` list.

    :bulb: Since you need to check if a substring exists in a string, you should use a membership operator in your conditional statement.

5. After the loop terminates, return the `events_by_theme` to the caller.

### Part 2
Given the `themes` list we provided, using a `for` loop and the function `categorize_events_by_theme`， find all the event names that match any theme in the `themes` list.

1. Initialize an empty list called `specified_theme_events`.

2. Using a `for` loop, iterate over the `themes` list. Call the `categorize_events_by_theme` function on each element
in the `themes` list. Append the return value from the function to the `specified_theme_events`.

The `specified_theme_events` list you create will contain the following elements:

```python
    [
        ['Zouk Dance Club Lesson', 'Bachata Class'],
        ['Apple Orchard Trip 2022', 'September Zouk Social', 'A2ML Weekly Social'],
        ['SAS Open House']
    ]
```

## Problem 06 (25 Points)

### Part 1
Define a function called `categorize_events_by_time` that returns a list of event names. Using a `for` loop and a conditional statement with the newly defined function, find the required events from the `club_events` list.

1. Define a function called `categorize_events_by_time` provisioned with three parameters in order: `club_events` (a list of events), an optional argument `time` (a string representing the event start time) with default value `'7 pm'` and another optional argument `duration` (an integer representing the event duration) with default value `1`.

2. In the function code block, initialize an empty list called `events_by_time`.

3. Using a `for` loop and skipping the headers
list, iterate over the information in `club_events`.

4. In the loop, using a compound `if` statement, check whether the event start time is the same as the value of `time` and whether the event duration is **greater than or equal to** the value of `duration`. If the `if` statement evaluates to `True`, append the event name to the `events_by_time` list.

5. After the loop terminates, return the `events_by_time` to the caller.


### Part 2
Call the function, passing the `club_events` list as its required argument. Assign the return value to the variable named `evening_events`.

The `evening_events` list you create will contain the following elements:
```python
['September Zouk Social', 'Bujinkan Budo Training Session']
```

## Problem 07 (25 Points)
Define a function called `calculate_num_events` that returns an integer representation of the number of events hosted by the specified student organization.

### Part 1
Define a function called `calculate_num_events` provisioned with two parameters in order: `club_events` (a list of events), `host_org` (a string representing the student organization's name).

1. Assign zero (0) to a variable named `num_events`.

2. Using a `for` loop, iterate over the information in `club_events`.

3. In the loop, if the student organization's name is the same as the value of `host_org`, increment the value of `num_events` by one (1).

4. After the loop terminates, return the `num_events` to the caller.

### Part 2
Call the function, passing the `club_events` list and the string `'Zouk Dance Club'` as arguments. Assign the return value to the variable named `num_events_for_zouk`.