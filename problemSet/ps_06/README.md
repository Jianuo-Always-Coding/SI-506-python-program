# SI 506: Problem Set 6

## This week's Problem Set

````This week's problem set will focus on reading and writing CSV files, creating and using functions,
and using the `main()` function.

## Background

You will be working with election data! Midterm elections will be held in the United States on
November 8, 2022. Though the US President is not on the ballot, midterms are important elections
since many state and local officials and proposals are on the ballot.

In Michigan, three important proposals are on the ballot, allowing citizens to directly affect the
future of Michigan's state laws.
These are:

- Prop 1 - Voters for Transparency and Term Limits
- Prop 2 - Promote the Vote 2022
- Prop 3 - Reproductive Freedom for All

Learn more [here](https://www.bridgemi.com/michigan-government/2022-michigan-ballot-issues-tracker-what-know-about-election-proposals)

The deadline to register to vote in Michigan is **October 24, 2022.**

:bulb: If you're eligible to vote in Michigan, you can register and vote early at the
[University of Michigan Museum of Art](https://umma.umich.edu/exhibitions/2020/vote-2020-ann-arbor-city-clerk-satellite-office-at-umma)

:bulb: [Learn how to absentee vote in a different state](https://www.usa.gov/absentee-voting)

## Data

You have been provided two (2) files that contain different information about elections in Washtenaw
county (where Ann Arbor is located).

- `washtenaw_registered_voters.csv`: Each row contains the county, city or township name (both
  referred to simply as 'city' or 'unit'), voting equipment, number of precincts (smaller divisions
  within the city), registered voters, and active voters for a city in Washtenaw county in August
  2022.

- `washtenaw_2022_primary_results.csv`: The 2022 Michigan primary occured in August. A primary
  election narrows the candidates down to one for each political party, so voters vote for which
  person they want to represent their party. Each row contains a lot of information, but important
  for us is the election date, office code, county name, office description, party name, party
  description, candidate last name, candidate first name, and candidate votes. These results come
  from each of the districts that the University of Michigan campus is in.
````
## Problem 1 (24 Points)

The function `read_csv()` is defined for you. However, it's broken and you need to fix it.

1. Uncomment the function definition.

2. Assign the correct value to the variable `data`.

3. Replace the `pass` statement with working code.

4. After fixing `read_csv` proceed to the `main` function. Under "Problem 1.2", call `read_csv()`
   and pass to it as an argument the relative path `washtenaw_registered_voters.csv`. Assign the
   return value to a variable called `registered_voters`.

   :exclamation: Do **not** conduct any data cleaning in the `read_csv()` function.

The `registered_voters` nested list _must_ be structured as follows:

    ```python
        [
            ['county', 'city_township', 'voting_equipment', 'precincts', 'registered_voters', 'active_voters'],
            ['Washtenaw', 'Ann Arbor', 'Hart Verity Scan/Touch Writer', '53', '110056', '76266'],
            ['Washtenaw', 'Ann Arbor Township', 'Hart Verity Scan/Touch Writer', '2', '4162', '3605'],
            ['Washtenaw', 'Augusta Township', 'Hart Verity Scan/Touch Writer', '3', '6135', '5587'],
            ...
        ]
    ```

1. In `main()` under "Problem 1.3" call `read_csv()` to read the 
   `washtenaw_2022_primary_results.csv` file. Assign the return value to a variable called
   `primary_results`.

   :exclamation: Do **not** conduct any data cleaning in the `read_csv()` function.

The `primary_results` nested list _must_ be structured as follows:

    ```python
        [
            ['ElectionDate', 'OfficeCode(Text)', 'DistrictCode(Text)', 'StatusCode', 'CountyCode', 'CountyName', 'OfficeDescription', 'PartyOrder', 'PartyName', 'PartyDescription', 'CandidateID', 'CandidateLastName', 'CandidateFirstName', 'CandidateMiddleName', 'CandidateFormerName', 'CandidateVotes', 'WriteIn(W)/Uncommitted(Z)', 'Recount(*)', 'Nominated(N)/Elected(E)'],
            ['8/2/2022', '2', '0', '0', '81', 'WASHTENAW', 'Governor 4 Year Term (1) Position', '1', 'DEM', 'Democratic', '518014', 'Whitmer', 'Gretchen', '', '', '61144', '', '', 'N'],
            ['8/2/2022', '2', '0', '0', '81', 'WASHTENAW', 'Governor 4 Year Term (1) Position', '2', 'REP', 'Republican', '520065', 'Dixon', 'Tudor', 'M.', '', '10691', '', '', 'N'],
            ['8/2/2022', '2', '0', '0', '81', 'WASHTENAW', 'Governor 4 Year Term (1) Position', '2', 'REP', 'Republican', '519976', 'Kelley', 'Ryan', 'D.', '', '3031', '', '', ''],
            ...
        ]
    ```

1. In `main()` under Problem 1.4 assign the "headers" from `registered_voters` to a variable named `registered_headers` and reassign `registered_voters` to a list slice that excludes the headers.

2. Do the same for `primary_results`, creating `primary_headers` and `primary_results`.

   :exclamation: `registered_headers` and `registered_voters` _must_ have no lists in common. Same
   for the primary lists.

## Problem 2 (60 Points)

You will define a function called `clean_data()` to change the values within the data that you have
read in from both csvs. `clean_data()` will call two other functions (`strip_string()` and
`convert_to_int()`) inside it, so you will define those functions first.

:bulb: All the functions defined in Problem 2 must work with both `registered_voters` and
`primary_results`.

1. Navigate to "Problem 2" by scrolling up your template file away from the `main` function.

2. Implement a function called `strip_string()` that defines two parameters:

   - `list_object` (list): a list of strings that describe election data.

   - `character` (str): default: None; a string to be passed to `str.strip()` method. Indicates which
     character(s) should be stripped from the strings in unit_data.

   :exclamation: `list_object` is **one** of the "rows" from the CSV data.

   :bulb: Review the `strip_string` docstring to better understand the function's expected behavior and defined parameters.

   __Requirements__

   In the function block implement the following:

   1. Use a `for` loop and the `range` type to access each string within the `list_object`.

   2. Check if a `character` argument was passed to the function by the caller. If a `character`
      was passed, use a string method to strip that `character` from either side of each string in
      the `list_object`. Assign the stripped string back to the original string at the original
      index position.

   3. If no `character` was passed, use a string method to strip any spaces (`' '`) from either
      side of each string in the `list_object`. Assign the stripped string back to the original
      string at the original index position.

    :exclamation: This function does not include a return statement (it implicitly returns `None`).

3. Implement a function called `convert_to_int()` that defines one parameter:

   - `list_object` (list): a list of strings that describe election data.

    :exclamation: `list_object` is **one** of the "rows" from the CSV data.

   __Requirements__

   In the function block implement the following:

   1. Use a `for` loop and the `range` type to access each string within the `list_object`.

   2. Use `try` and `except` statements to attempt to cast each string to an integer. Assign the
      integer back to the `list_object`.

   3. If the string cannot be converted to an integer leave the value unchanged.

    :exclamation: This function does not include a return statement (it implicitly returns `None`).

4. Implement a function called `clean_data()` that defines three parameters. Review the function's
   docstring to better understand the function's expected behavior and defined parameters.

   __Requirements__

   This function _must_ do the following:

   1. Determine if string stripping is requested by the caller.

   2. If stripping is required, loop over `data` and call `strip_string()` and `convert_to_int()`
      on each object.

      :exclamation: Call `strip_string()` **before** `convert_to_int()`.

   3. If stripping is not required, loop over `data` and call `convert_to_int()` on each object.

5. After implementing the three functions, return to `main`. Under "Problem 2.4", call `clean_data()`
   on the `registered_voters` list.

6. In `main` under "Problem 2.5" call `clean_data()` on the `primary_results` list, passing the
   appropriate arguments so that you do not end up with any negative integers as `CandidateIDs`.

  :exclamation: Use the correct *keyword arguments* when passing in arguments to the optional
  parameters.

If Problem 2 has been implemented correctly, `primary_results` will be structured as follows:

```python
    [['8/2/2022', 2, 0, 0, 81, 'WASHTENAW', 'Governor 4 Year Term (1) Position', 1, 'DEM', 'Democratic', 518014, 'Whitmer', 'Gretchen', '', '', 61144, '', '', 'N'],
    ['8/2/2022', 2, 0, 0, 81, 'WASHTENAW', 'Governor 4 Year Term (1) Position', 2, 'REP', 'Republican', 520065, 'Dixon', 'Tudor', 'M.', '', 10691, '', '', 'N'],
    ...
    ['8/2/2022', 2, 0, 0, 81, 'WASHTENAW', 'Governor 4 Year Term (1) Position', 2, 'REP', 'Republican', 520093, 'Craig', 'James', 'Elmer', '', 865, 'W', '', ''],
    ['8/2/2022', 6, 600, 0, 58, 'MONROE', '6th District Representative in Congress 2 Year Term (1) Position', 1, 'DEM', 'Democratic', 1432, 'Dingell', 'Debbie', '', '', 171, '', '', 'N']
    ...
    ]
```

## Problem 3 (30 Points)

1. Implement the function called `find_fewest()` provisioned with three parameters. Review the
   function's docstring to better understand its expected behavior.

   __Requirements__

    :bulb: You have performed similar tasks finding maximum and minimum values before.

    1. Create a variable named `smallest_value` and assign the Pythonic expression for infinity to
       it.

    1. Create an empty list and assign it to the variable `smallest_unit`.

    2. Use the `list.index()` method on `headers` to determine the index values throughout.

    3. Use `if-elif` to ensure that you have a way to handle ties.

    4. Append the **entire** "row" that consists of the `smallest_value` to `smallest_unit`.

2. In `main` under "Problem 3.2" call `find_fewest()` and pass to it the appropriate arguments to
   determine the cities/townships in the `registered_voters` list with the fewest precincts. Assign
   the return value to a variable called `fewest_precincts`.

Your `fewest_precincts` list *must* be structured as follows:

    ``` python
            [
                ['Washtenaw', 'Bridgewater Township', 'Hart Verity Scan/Touch Writer', 1, 1463, 1339],
                ['Washtenaw', 'Freedom Township', 'Hart Verity Scan/Touch Writer', 1, 1295, 1181],
                ['Washtenaw', 'Lyndon Township', 'Hart Verity Scan/Touch Writer', 1, 2269, 2160],
                ['Washtenaw', 'Milan city', 'Hart Verity Scan/Touch Writer', 1, 3140, 2877],
                ['Washtenaw', 'Saline Township', 'Hart Verity Scan/Touch Writer', 1, 1886, 1763],
                ['Washtenaw', 'Sharon Township', 'Hart Verity Scan/Touch Writer', 1, 1658, 1526],
                ['Washtenaw', 'Sylvan Township', 'Hart Verity Scan/Touch Writer', 1, 3029, 2790]
            ]
    ```

1. In `main()` under "Problem 3.3", call `find_fewest()` and pass to it the appropriate arguments to
   determine the candidate(s) in the `primary_results` list with the fewest 'CandidateVotes'. Assign
   the returned list to a variable called `fewest_votes`.

Your `fewest_votes` list *must* be structured as follows:

    ``` python
            [
                ['8/2/2022', 2, 0, 0, 81, 'WASHTENAW', 'Governor 4 Year Term (1) Position', 2, 'REP', 'Republican', 520913, 'Adkisson', 'Elizabeth', 'Ann', '', 0, 'W', '', '', ''],
                ['8/2/2022', 2, 0, 0, 81, 'WASHTENAW', 'Governor 4 Year Term (1) Position', 2, 'REP', 'Republican', 520647, 'Blackburn', 'Justin', 'Paul', '', 0, 'W', '', '', '']
            ]
    ```

## Problem 4 (40 Points)

We need to determine which city or township in Washtenaw County has the highest percentage of active
voters (based on the total registered).

1. Define a function called `get_active_percentage()` provisioned with a single parameter:

   - `unit_data` (list): a list of strings that describe voter registration data for one city or
     township.

   __Requirements__

    This function *must*:

    - Determine the active voters and registered voters for the city or township

    - **Return** the percentage of registered voters for the city or township that are active
      (a `float`).

    - :exclamation: You do not have to use `list.index()` or the headers in this function definition.

    - :exclamation: Do **not** round the percent that is returned.

2. Define a function called `find_most_active_unit()` provisioned with a single parameter:

   - `data` (list): a list of lists that describe voter registration data for the cities and
     townships in Washtenaw county.

    The function **returns** a two-item tuple ordered as follows:

    - `most_active_unit` (list): a list of the city/township name(s) of the unit(s) with the most
      active voters, as a percent of registered voters.

    - `highest_percent` (int): the percent of registered voters that are active in the most active
      unit, rounded to the nearest integer.

    __Requirements__

    :bulb: You have performed similar tasks finding maximums and minimums before.

    1. Create a variable named `highest_percent` and assign `0` to it.

    2. Create an empty list and assign it to the variable `most_active_unit`.

    3. Loop over data and call `get_active_percentage()` to determine the `percent_active` for each
       unit/city.

    4. Use `if-elif` to ensure that you have a way to handle ties.

    5. Append the `city_township` **name only** of the unit with the `highest_percent` to
 `most_active_unit`.

    6. **Return** a tuple comprising `most_active_unit` and `highest_percent`.

      :bulb: You need to use a built-in function to round up the value of the `highest_percent` to an
      integer.


3. Return to `main`. Under "Problem 4.3" call `find_most_active_unit()` on `registered_voters` and
   **unpack** the tuple that is returned into the variables `most_active_unit` and `percent`.

    If implemented correctly, your print statements for Problem 4.3 will output the following string:

    ``` python
    "4.3: The unit(s) with the highest percentage of active voters: ['York Township']. 98% of registered voters there are active."
    ```

## Problem 5 (30 Points)

Next, we need to determine how many votes were cast for Democrats and how many votes were cast for
Republicans for each office in the primary election.

1. Implement a function called `get_dem_and_rep_votes()` provisioned with three parameters:

   - `results` (list): A list of lists, each containing a candidate's information from the 2022
     primary (e.g., name, office, office code, party name, number of votes).

   - `headers` (list): A list containing the headers from the primary election results data.

   - `office_code` (int): the office code for the different offices up for election during the
     August primary such as code 2 for Governor.

   The function **returns** a two-item tuple ordered as follows:

   - `democratic_votes` (int): the number of votes cast for Democratic candidates for this position

   - `republican_votes` (int): the number of votes cast for Republican candidates for this position

   __Requirements__

   1. Assign zero (`0`) to variables named `democratic_votes` and `republican_votes`.

   2. Loop over the `results` list.

   3. Use `headers` and `list.index()` throughout to help with indexing.

   4. If the 'OfficeCode(Text)' matches the `office_code` and the 'PartyName' is 'DEM', add the
     'CandidateVotes' to the `democratic_votes`.

   5. If the 'OfficeCode(Text)' matches the `office_code` and the 'PartyName' is 'REP', add the
      'CandidateVotes' to the `republican_votes`.

   6. **Return** a tuple comprising `democratic_votes` and `republican_votes`.

2. Return to `main()`.  Under Problem 5.2 and below the provided lists, loop over `vote_totals`.
   Use `get_dem_and_rep_votes` to append the total Democratic and Republican vote counts to each
   office's list. Pass the `primary_results`, `primary_headers`, and the "Office Code" from
   each `vote_total` as arguments to the function `get_dem_and_rep_votes`.

Your `vote_totals` *must* be structured as follows:

    ``` python
        [
            ['Governor', 2, 61144, 22215],
            ['Representative in Congress', 6, 102859, 56935],
            ['State Senator', 7, 37230, 11466],
            ['District Representative in State Legislature', 8, 8207, 4614]
        ]
    ```

## Problem 06 (16 Points)
Finally, let's write some of our new data to a csv file.

1. Similar to Problem 1, a function called `write_csv` is defined for you, but is broken and you
   need to fix it. Uncomment the function definition and correct the `pass`, `None`, ?, etc. to
   make the `write_csv()` function work again. This function writes data to a csv file in filepath,
   where each list is a row in the csv file.

2. Return to `main`. Under Problem 6.2, call `write_csv()` using the `vote_totals_headers` element
   as the `headers` argument and the data in `vote_totals` to write to a new file called
   `primary_votes_by_party.csv`.

   :exclamation: Use the correct *keyword argument* when passing in the "headers" element. Do
   **not** use keyword arguments for the other two arguments while calling the function.
