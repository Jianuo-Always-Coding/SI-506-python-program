# SI 506: Lab Exercise 07

## This week's Lab Exercise

This week's lab exercise includes five (5) problems that focus on the dictionary, reading and writing a CSV file to a dictionary, functions, and conditional statements.

## Background

For this lab, you are provided with a CSV file containing data that represents 48 of the [200 Best Horror Movies of All Time](https://editorial.rottentomatoes.com/guide/best-horror-movies-of-all-time/) and includes information sourced from The Open Movie Database's API ([OMDb API](https://www.omdbapi.com/)).

As described by the site maintainers,
> "The OMDb API is a [RESTful](https://medium.com/extend/what-is-rest-a-simple-explanation-for-beginners-part-1-introduction-b4a072f8740f) web service to obtain movie information, all content and images on the site are contributed and maintained by our users."

For a sneak preview of our week 11 topic - Web API - check out [examples of the data structures and information](https://www.omdbapi.com/#examples) that you can access 'By Title' or 'By ID' on the OMDB API website.

## Data
Once the data is read in from the CSV, each nested dictionary within the list contains 19 key-value pairs describing each movie's runtime, genre, plot, language, ratings, box office (gross ticket sales), and more.

```Python
    [
        { 'Title': 'The Mist',
        'Year': '2007',
        'Rated': 'R',
        'Released': '21-Nov-07',
        'Runtime': '126 min',
        'Genre': 'Horror, Sci-Fi, Thriller',
        'Director': 'Frank Darabont',
        'Writer': 'Frank Darabont, Stephen King',
        'Actors': 'Thomas Jane, Marcia Gay Harden, Laurie Holden',
        'Plot': 'A freak storm unleashes a species of bloodthirsty creatures on a small town, where a '
                'small band of citizens hole up in a supermarket and fight for their lives.',
        'Language': 'English',
        'Country': 'United States',
        'Awards': '6 wins & 13 nominations',
        'imdbRating': '7.1',
        'imdbVotes': '308,835',
        'imdbID': 'tt0884328',
        'Type': 'movie',
        'DVD': '25-Mar-08',
        'BoxOffice': '$25,594,957 '
        },
        ...
    ]
```

## 1.0 Problem 01 (5 points)
### Part 1
The functions `read_csv_to_dicts()` and `write_dicts_to_csv()` have been defined for you. However, in similar fashion to a previous assignment, they have been broken in various ways and require you to fix them.

1. Uncomment the function definition.
2. Replace '?' and `pass` statements with working code.

After fixing both functions, navigate to Problem 01 in the `main()` function and call `read_csv_to_dicts()`. Pass in the filepath for the horror movies CSV file and assign the variable `horror_movies` to the return value.

:bulb: Note that the `pprint` module has been imported for you. While not required to pass the autograder, you may find it helpful to construct an instance of `PrettyPrinter` to display your output in a more human-readable format.

### Part 2
Define a function named `remove_DVD()` that loops over the list of nested dictionaries and deletes the unnecessary key-value pair with the key of `DVD`. The function defines one (1) parameter:

   - `movies` (list): nested dictionaries containing movie data

:bulb: For each function to be defined in this lab exercise, the docstring has already been written for you. Refer to each function's docstring as you may find additional details and guidance to help you work through each problem.

After defining the function, navigate back to Problem 01 in the `main()` function and call `remove_DVD()`. Pass in the `horror_movies` data.

## 2.0 Problem 02 (5 points)
### Part 1
Next, you will define three (3) functions: `clean_runtime()`, `clean_boxoffice()`, and `clean_imdb_data()`. You will first define and test each function one at a time, using a sample dictionary assigned to the variable `test_movie`, before ultimately passing the full list of `horror_movies` to each of them. Each of these functions defines one (1) parameter:

   - `movie` (dict): dictionary containing key-value pairs representing data for one movie

#### Part 1.1
Define a function named `clean_runtime()` that:
   1. Accesses the key-value pair with the key 'Runtime'.
   2. Utilizes a `str` method to split the number element from the unit element.
   3. Accesses _only_ the number element to cast it to an integer.

After defining the function, navigate to Problem 02 in the `main()` function and call `clean_runtime()`. Pass in the `test_movie` data and confirm that the function has successfully cast the 'Runtime' value to an integer.

#### Part 1.2
Define a function named `clean_boxoffice()` that:
   1. Utilizes a try-except statement to attempt to cast the number value to an integer, otherwise assigns the value of 0 to the key 'BoxOffice'.
   2. Utilizes a chain of three (3) `str` methods to:
      - (1) return a trimmed version of the string
      - (2) split the string at a specified separator and access the full number value using list indexing
      - (3) return a string where a specified value is replaced with a specified value in order to cast it to an integer.

After defining the function, navigate to Problem 02 in the `main()` function and call `clean_boxoffice()`. Pass in the `test_movie` data and confirm that the function has successfully cast the 'BoxOffice' value to an integer.

#### Part 1.3
Define a function named `clean_imdb_data()` that:
   1. Accesses the key-value pair with the key 'imdbVotes', utilizes a `str` method to return a string where a specified value is replaced with a specified value, and casts the string to an integer.
   2. Accesses the key-value pair with the key 'imdbRating' and casts the value to a float.

After defining the function, navigate to Problem 02 in the `main()` function and call `clean_imdb_data()`. Pass in the `test_movie` data and confirm that the function has successfully cast the 'imdbRating' and 'imdbVotes' values to a float and an integer, respectively.

Before proceeding to Part 2, `test_movie` _must_ look like the following:
```Python
{
   'Title': 'Train to Busan',
   'Year': '2016',
   'Rated': 'Not Rated',
   'Released': '20-Jul-16',
   'Runtime': 118,
   'Genre': 'Action, Horror, Thriller',
   'Director': 'Sang-ho Yeon',
   'Writer': 'Joo-Suk Park, Sang-ho Yeon',
   'Actors': 'Gong Yoo, Jung Yu-mi, Ma Dong-seok',
   'Plot': 'While a zombie virus breaks out in South Korea, passengers struggle to survive on the '
            'train from Seoul to Busan.',
   'Language': 'Korean, Hawaiian, English',
   'Country': 'South Korea',
   'Awards': '35 wins & 39 nominations',
   'imdbRating': 7.6,
   'imdbVotes': 217609,
   'imdbID': 'tt5700672',
   'Type': 'movie',
   'BoxOffice': 2129768
}
```
### Part 2
After defining and testing the three (3) functions, navigate to Problem 02 in the `main()` function and loop over the `horror_movies` list in order to call each function on each nested dictionary in the list.

## 3.0 Problem 03 (5 points)
### Part 1
Define a function named `get_most_popular_movies()` that defines one (1) parameter:

   - `movies` (list): nested dictionaries containing movie data

The function checks whether a movie's 'BoxOffice' and 'imdbRating' are greater than a certain threshold. If the compound conditional returns `True`, it appends a dictionary _literal_ to a new list named `popular_movies`. The dictionary _literal_ is formatted with the movie's 'Title' as the key and the movie's 'BoxOffice' and 'imdbRating' - stored in a tuple - as the value.

   1. Assign an empty list to the variable `popular_movies`.
   2. Loop over the movies list.
   3. Utilize a compound conditional statement to check if the movie's 'BoxOffice' is greater than 100000000 and 'imdbRating' is greater than 7.
   4. Append a dictionary _literal_ with the movie's 'Title', 'BoxOffice', and 'imdbRating' to the `popular_movies` list.

The output should look like the following:

```Python
[
   {'The Conjuring 2': (102516140, 7.3)},
   {'The Conjuring': (137446368, 7.5)},
   {'The Ring': (129128133, 7.1)},
   {'It': (328874981, 7.3)},
   {'A Quiet Place': (188024361, 7.5)},
   {'Get Out': (176196665, 7.7)}
]
```

### Part 2
After defining the function, navigate to Problem 03 in the `main()` function and call `get_most_popular_movies()` passing in the `horror_movies` list. Assign a variable named `popular_horror_movies` to the return value.

## 4.0 Problem 04 (5 points)
### Part 1
Define a function named `count_sub_genres()` that defines one (1) parameter:

   - `movies` (list): nested dictionaries containing movie data

The function creates a new dictionary `sub_genres` with key-value pairs that have a specified set of sub-genres as their keys and a starting value of 0 as their initial values. Then, it loops over the movies list and, using an `if-elif` conditional statement, it checks for the presence of each sub-genre in each movie's 'Genre'. If the conditional returns `True`, it increments the count value for the genre by 1.

   1. Assign an empty dictionary to the variable `sub_genres`.
   2. Assign key-value pairs one at a time to the empty dictionary using the subscript operator (`[]`). Refer to the docstring for the exact names and order for the keys.
   3. Loop over the movies list.
   4. Utilize an `if-elif` statement to check if each sub-genre string is present in the movie's 'Genre'.
   5. If `True`, increment that corresponding key's value by 1.

The dictionary you produce _must_ match the following data structure:
```Python
{'Sci-Fi': 4, 'Fantasy': 10, 'Thriller': 13, 'Mystery': 9}
```

### Part 2
After defining the function, navigate to Problem 04 in the `main()` function and call `count_sub_genres()` passing in the `horror_movies` list. Assign the variable `subgenre_counts` to the return value.

## 5.0 Problem 05 (5 points)
### Part 1
Define a function named `create_new_movies_dicts()` that defines one (1) parameter:

   - `movies` (list): nested dictionaries containing movie data

The function loops over the list of movies and utilizes an `if-else` statement to check whether each movie's 'Runtime' is greater than 2 hours (120 mins). If `True`, it appends a dictionary _literal_ which includes a selection of key-value pairs accessed from the original data, a _new_ key-value pair 'Length': 'Long', and a nested dictionary assigned to a _new_ key 'imdbInfo'. Otherwise, it appends a dictionary _literal_ which includes a selection of key-value pairs accessed from the original data, a _new_ key-value pair 'Length': 'Short', and a nested dictionary assigned to a _new_ key 'imdbInfo'.

   1. Assign an empty list to the variable `movies_new`.
   2. Loop over the movies list.
   3. Utilize an `if-else` statement to check whether the movie's 'Runtime' is greater than 120.
   4. If `True`, create a **new** dictionary by defining a dictionary _literal_ with a selection of key-value pairs accessed from the original data and 2 new key-value pairs ('Length' and 'imdbInfo') and appending it to the list `movies_new`.
   5. Otherwise, create a **new** dictionary by defining a dictionary _literal_ with a selection of key-value pairs accessed from the original data and 2 new key-value pairs ('Length' and 'imdbInfo') and appending it to the list `movies_new`.

An example output for either condition is:
```Python
    [
        { 'Title': 'The Mist',
        'Genre': 'Horror, Sci-Fi, Thriller',
        'Runtime': 126,
        'Length': 'Long',
        'Rated': 'R',
        'Plot': 'A freak storm unleashes a species of bloodthirsty creatures on a small town, where a '
                'small band of citizens hole up in a supermarket and fight for their lives.',
        'imdbInfo': {
            'imdbRating': 7.1, 'imdbVotes': 308835, 'imdbID': 'tt0884328'
            },
        'BoxOffice': 25594957
        },
        { 'Title': 'Dog Soldiers',
        'Genre': 'Action, Horror, Thriller',
        'Runtime': 105,
        'Length': 'Short',
        'Rated': 'R',
        'Plot': 'A routine military exercise turns into a nightmare in the Scotland wilderness.',
        'imdbInfo': {
            'imdbRating': 6.8, 'imdbVotes': 60632, 'imdbID': 'tt0280609'
            },
        'BoxOffice': 0
        },
        ...
    ]
```

:exclamation: Pay attention to the use of a nested dictionary _literal_ to combine the original key-value pairs of 'imdbRating', 'imdbVotes', and 'imdbID' into a value with the key 'imdbInfo'. Also, pay close attention to the order of the selection of key-value pairs shown in the example output above. The dictionary _literal_ that you create must mirror the examples above for either condition.

### Part 2
After defining the function, navigate to Problem 05 in the `main()` function and call `create_new_movies_dicts()` passing in the `horror_movies` list. Assign the variable `horror_movies_new` to the return value.

Finally, call the function `write_dicts_to_csv()`. Pass in:
   1. the filepath `'stu_horror_movies_new.csv'`
   2. the new list of dictionaries you've just created
   3. a list of the dictionary's keys by accessing the keys of the first dictionary element in the list

:bulb: What dictionary method will allow you to access just the keys?
