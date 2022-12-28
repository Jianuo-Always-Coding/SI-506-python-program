# SI 506: Problem Set 03

## This Week's Problem Set

This week's problem set will focus on conditional statements, `for` loops, and the `range()` type.
Some topics from previous sections (e.g. methods, indexing, slicing) are also included.

## Background

This week's problem set incorporates information about tv shows from various streaming platforms. You are asked to iterate over two different lists to extract information.

You are provided with a list called `tv_shows`. In order, each element of this list contains the following information:

- Show Name
- Genre
- Year of Release
- IMDB rating out of 10
- Rotten Tomatoes rating out of 100
- Streaming Platform

### Problem 01 (15 Points)

You are given another list of tv shows named `tv_shows_to_update` which contains information about some other tv shows not present in the `tv_shows` list. Replace all the Horror genre `tv_shows` after formatting the shows provided in `tv_shows_to_update`.

1. Create an empty list called `format_tv_shows`.

2. Using a `for` loop, iterate over each element in `tv_shows_to_update` and convert it to a string similar to the string elements present in `tv_shows`. Append the string literals to `format_tv_shows`.

   :bulb: Note that each element in `tv_shows_to_update` is type `list`.

3. Replace horror genre shows in `tv_shows` with shows in `format_tv_shows` by assigning a list slice to the `tv_shows` with the horror genre.


The `format_tv_shows` list you create must contain the following elements:

```python
   [
    'The Bold Type | Drama | 2017 | 7.8 | 89 | Hulu',
    'Suits | Drama | 2011 | 8.5 | 90 | Netflix',
    'Virgin River | Drama | 2019 | 7.4 | 84 | Netflix'
    ]
```

### Problem 02 (15 points)

Using the accumulator pattern with a conditional statement, add the names of drama shows to a new list called `drama`.

1. Create an empty list called `drama`.

2. Using a `for` loop, iterate over each string in `tv_shows`.

3. In the loop block, check whether each show is a drama.

   :heavy_exclamation_mark: Python is a case-sensitive programming language. For this problem ensure that your `if` statement performs a *case-insensitive* comparison of the string values.

4. Add *_only_* the names of the drama shows to the `drama` list.

   :bulb: Consider splitting each string encountered into a list and extracting the required information using indexing.

The `drama` list you create must contain the following elements:

```python
   [
   "Grey's Anatomy",
   'Fargo',
   'The Bold Type',
   'Suits',
   'Virgin River',
   'Bridgerton',
   "The Queen's Gambit",
   'The Crown',
   'On My Block',
   'Fleabag'
   ]
```

### Problem 03 (15 points)

Using the accumulator pattern, calculate the average Rotten Tomatoes rating across all television shows in `tv_shows`. Assign this average to a variable called `avg_rating_all_shows`.

1. Assign zero (0) to a variable named `total_ratings`.

2. Using a `for` loop, iterate over each string in `tv_shows`.

3. In the loop, extract the Rotten Tomatoes rating from each string and add it to `total_ratings`.

   :bulb: Python can perform arithmetic operations on both string and numbers. Carefully cast the extracted Rotten Tomatoes rating to right datatype.

4. Calculate the average rating of all shows using `total_ratings` and the length of the `tv_shows` list and assign it to the variable `avg_rating_all_shows`. Limit the fractional component of the float value to two (2) decimal places by employing the built-in round() function.

   :bulb: The built-in function `round()` accepts two arguments: (1) the value to be rounded and (2) the number of decimal points to retain. The function returns a `float`. For a working example see the w3schools ["Python round() function"](https://www.w3schools.com/python/ref_func_round.asp) page.

### Problem 04 (15 Points)

Using a `for` loop and conditional statements, compare the Rotten Tomatoes rating for each show to `avg_rating_all_shows`. Categorize the shows as below average or above average based on this comparison.

1. Create two empty lists: one called `above_avg` and another called `below_avg`.

2. Using a `for` loop, iterate over each string in `tv_shows`.

3. In the loop, compare the rating for each show to `avg_rating_all_shows`.

   :heavy_exclamation_mark: Note that the rating in `tv_shows` is not the same type as `avg_rating_all_shows` variable.

4. Add *_only_* the names of shows that possess a rating greater than average to the `above_avg` list.
   Otherwise, add the name to the `below_avg` list.

   :bulb: You will need to implement `if-else` statement here.

### Problem 05 (16 points)

Using a `for` loop, calculate a rating between 0 and 100 for each show. Attach this rating to the name of the show in the format `< show_name > - < rating >`. Add this new string to a new list called `tv_shows_new`.

1. Create an empty list called `tv_shows_new`.

2. Using a `for` loop, iterate over each element in `tv_shows`.

3. In the loop, extract the IMDB and Rotten Tomatoes ratings. Convert IMDB rating from a scale of 10 to a scale of 100. Compute the average of each new IMDB rating and Rotten Tomatoes rating. Output *must* be on a scale of 100 and an integer.

   :bulb: You will need to use floor division while calculating the average.

4. Using formatted string literal (f-string), add this newly calculated rating to the end of the name of the show. Remember to include a space-hyphen-space(" - ") separator between the name and the new rating.

```python
    "< show_name > - < rating >"
```
5. Add this string to `tv_shows_new`.

The `tv_shows_new` list you create must contain the following elements:

```python
     [
     'Only Murders in the Building - 90',
     'Reservation Dogs - 90', 'Justified - 91',
     'Better Things - 88',
     "Grey's Anatomy - 80",
     'Atlanta - 92',
     'Fargo - 93',
     'Lost - 84',
     'The Bold Type - 83',
     'Suits - 87',
     'Virgin River - 79'
     ...
     ]
```

### Problem 06 (19 Points)

Using a `for` loop, find the oldest show in `tv_shows`.

1. Create a numerical variable called `min_year`. Assign the value 2022 to this variable.

2. Using a `for` loop, iterate over each element in `tv_shows`.

3. In the loop, extract the release year for each show. Compare this year to `min_year` to find the oldest show.

4. Assign the name of the oldest show to a variable called `oldest_show`.


### Problem 07 (10 Points)

Using a `for` loop with the `range()` type, create a list that contains *every other* show on Hulu.

1. Initialize an empty list variable called `select_content`.

2. Create a `for` loop that iterates over the `range()` type. Adjust the `start`, `stop`, and `step` arguments to return *every other* string from the `tv_shows` list where shows are streamed on Hulu Platform.

3. Add these strings to the `select_content` list.

The `select_content` list you create must contain the following elements:

```python
     [
     'Only Murders in the Building | Comedy | 2021 | 8.1 | 99 | Hulu',
     'Justified | crime | 2010 | 8.6 | 97 | Hulu',
     "Grey's Anatomy | Drama | 2005 | 7.6 | 84 | hulu",
     'Fargo | Drama | 2014 | 8.9 | 97 | Hulu',
     'The Bold Type | Drama | 2017 | 7.8 | 89 | Hulu'
     ]
```

### Problem 08 (20 Points)

Using a `for` loop and conditional statements, discover the unique genre and unique streaming services present in the list `tv_shows`

1. Create two empty lists: one called `unique_genre` and another called `unique_streaming_service`.

2. Using a `for` loop with the `range()` type, iterate over each element in `tv_shows`.

3. In the loop, extract genre and streaming service from each string. Check if that genre exists in `unique_genre` or not. If it does not exist, append the genre name in `unique_genre`. Perform similar check for streaming service.

   :bulb: You will need two `if` statements here for both `unique_genre` and `unique_streaming_service`.

   :bulb:  Python is a case-sensitive programming language. For this problem ensure that your `if` statement performs a *case-insensitive* comparison to the items in the list.

   :bulb:  All the elements in lists `unique_genre` and `unique_streaming_service` are expected to be in lower case.

The `unique_genre` list must look like this:
```python
['comedy', 'crime', 'drama', 'scifi', 'thriller', 'fantasy']
```

The `unique_streaming_service` list must look like this:

```python
    [
    'hulu',
    'netflix',
    'prime',
    'appletv'
    ]
```
