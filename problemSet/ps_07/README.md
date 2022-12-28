# SI 506: Problem Set 7

## This week's Problem Set

This week's problem set will focus on dictionaries (associative arrays).

## Background

For this lab, you are provided with a CSV file containing horror movies data sourced from The Open Movie Database's API ([OMDb API](https://www.omdbapi.com/)) and a CSV containing information about the amount of jump scares in the movie sourced from ([Where's the Jump?](https://wheresthejump.com/full-movie-list/)). The 'Where's the Jump?' site also maps out the time of each jump scare. 

- `horror_movies.csv`: Each row contains information about a horror movie. 
  
- `movie_jumpscares.csv`: Each row contains information about the movie's number of jump scares and jump scare rating.

## Problem 01 (20 points)

1. The functions `read_csv_to_dicts()` and `write_dicts_to_csv()` have been defined for you. However, in similar fashion to a previous assignment, they have been broken in various ways and require you to fix them. Review the function's docstring regarding its expected behavior, parameters, and return value (if any).

   - Uncomment the function definition.
   - Replace '?' and pass statements with working code.

2. After fixing both functions, return to the `main()` function and call `read_csv_to_dicts()`.
   - Pass in the filepath for the horror movies CSV file and assign the variable `horror_movies` to the return value. 
   - Pass in the filepath for the jump scare data CSV file and assign the variable `jumpscare_data` to the return value.

:bulb: Note that the `pprint` module has been imported for you. While not required to pass the autograder, you may find it helpful to construct an instance of `PrettyPrinter` to display your output in a more human-readable format since the output will be a list of dictionaries, where each dictionary is one row from the csv file.

The `horror_movies` list must contain the following element(s):

```python
    [
        {
        'Title': 'Would You Rather',
        'Year': '2012',
        'Rated': 'Not Rated',
        'Released': '06 Jun 2019',
        'Runtime': '93 min',
        'Genre': 'Horror, Thriller',
        'Director': 'David Guy Levy',
        'Writer': 'Steffen Schlachtenhaufen',
        'Actors': 'Brittany Snow, June Squibb, Jeffrey Combs',
        'Plot': 'Desperate to help her ailing brother, a young woman unknowingly agrees to compete in a deadly game of "Would You Rather," hosted by a sadistic aristocrat.',
        'Language': 'English',
        'Country': 'United States',
        'Awards': '1 nomination',
        'imdbRating': '5.7'
        },
        ...
    ]
```

The `jumpscare_data` list must contain the following element(s):

```python
    [
        {
        'Movie Name': '[Rec]', 
        'Director': 'Jaume Balagueró, Paco Plaza', 
        'Year': '2007', 
        'Jump Count': '11', 
        'Jump Scare Rating': '3.5', 
        'Netflix (US)': 'No'
        },
        ...
    ]
```

:bulb: Given the length of `horror_movies` and `jumpscare_data`, examples shown are the first element of each list.


## Problem 02 (30 points)

1. Implement a function called `clean_row()`. Review the function's docstring regarding its expected behavior, parameters, and return value (if any).

2. After implementing `clean_row()` and its helper functions, return to the `main()` function. Call `clean_row()` on each dictionary in `horror_movies` and `jumpscare_data`.

The `horror_movies` list must contain the following elements:

```python
    [
        {
        'Title': 'Would You Rather',
        'Year': 2012,
        'Rated': 'Not Rated',
        'Released': '06 Jun 2019',
        'Runtime': 93,
        'Genre': 'Horror, Thriller',
        'Director': 'David Guy Levy',
        'Writer': 'Steffen Schlachtenhaufen',
        'Actors': 'Brittany Snow, June Squibb, Jeffrey Combs',
        'Plot': 'Desperate to help her ailing brother, a young woman unknowingly agrees to compete in a deadly game of "Would You Rather," hosted by a sadistic aristocrat.',
        'Language': 'English',
        'Country': 'United States',
        'Awards': '1 nomination',
        'imdbRating': '5.7'
        },
        ...
    ]
```

The `jumpscare_data` list must contain the following elements:

```python
    [
        {
        'Movie Name': '[Rec]', 
        'Director': 'Jaume Balagueró, Paco Plaza', 
        'Year': '2007', 
        'Jump Count': 11, 
        'Jump Scare Rating': 3.5, 
        'Netflix (US)': 'No'
        },
        ...
    ]
```

## Problem 03 (30 points)

1. Implement a function called `filter_movie_by_genre()`. Review the function's docstring regarding its expected behavior, parameters, and return value (if any).

    After implementing `filter_movie_by_genre()`, return to the `main()` function. Test `filter_movie_by_genre()` by passing to it `horror_movies` and the genre `'action'` and assigning the return value to the variable `action_movies`.

The `action_movies` list must include the following element(s):

```python
        [
            {
            'Title': 'The Purge: Anarchy',
            'Year': 2014,
            'Rated': 'R',
            'Released': '18 Jul 2014',
            'Runtime': 103,
            'Genre': 'Action, Horror, Sci-Fi',
            'Director': 'James DeMonaco',
            'Writer': 'James DeMonaco',
            'Actors': 'Frank Grillo, Carmen Ejogo, Zach Gilford',
            'Plot': 'Three groups of people intertwine and are left stranded in the streets on Purge Night, trying to survive the chaos and violence that occurs.',
            'Language': 'English',
            'Country': 'United States, France',
            'Awards': '3 wins & 6 nominations',
            'imdbRating': '6.4'
        }, {
            'Title': 'The Mummy',
            'Year': 1999,
            'Rated': 'PG-13',
            'Released': '07 May 1999',
            'Runtime': 124,
            'Genre': 'Action, Adventure, Fantasy',
            'Director': 'Stephen Sommers',
            'Writer': 'Stephen Sommers, Lloyd Fonvielle, Kevin Jarre',
            'Actors': 'Brendan Fraser, Rachel Weisz, John Hannah',
            'Plot': 'At an archaeological dig in the ancient city of Hamunaptra, an American serving in the French Foreign Legion accidentally awakens a mummy who begins to wreak havoc as he searches for the reincarnation of his long-lost love.',
            'Language': 'English, Egyptian (Ancient), Arabic, Chinese, Hebrew, Hungarian',
            'Country': 'United States',
            'Awards': 'Nominated for 1 Oscar. 5 wins & 24 nominations total',
            'imdbRating': '7.1'
        }, 
        ...
```

2. After testing `filter_movie_by_genre()` remain in the `main()` function. Call the function `filter_movie_by_genre()` and pass the `horror_movies` list of dictionaries and the str `'horror'` as the genre to the function. Assign the return value back to the variable name `horror_movies`.

## Problem 04 (30 points)

1. Implement a function called `get_jumpscare_data()`. Review the function's docstring regarding its expected behavior, parameters, and return value (if any).

2. After implementing `get_jumpscare_data()`, return to the `main()` function. Call the function `get_jumpscare_data()` on each movie dictionary `horror_movies` and use sequence unpacking to extract the jump count and jump scare rating. Create two new keys in each movie dictionary, `Jumpscare_count` and `Jumpscare_rating`, and assign the jump count and jump scare rating return values to these keys.

## Problem 05 (30 points)

1. Implement a function called `filter_movies()`. Review the function's docstring regarding its expected behavior, parameters, and return value (if any).

2. After implementing `filter_movies()` return to the `main()` function. Call the `filter_movies()` on `horror_movies` to filter movies that have a relatively short runtime between 30 to 90 minutes (inclusive). Assign the return value to the variable `short_movies`

The `short_movies` list must contain the following element(s):

```python
    [
        {'Title': 'The Texas Chain Saw Massacre',
        'Year': 1974,
        'Rated': 'R',
        'Released': '11 Oct 1974',
        'Runtime': 83,
        'Genre': 'Horror',
        'Director': 'Tobe Hooper',
        'Writer': 'Kim Henkel, Tobe Hooper',
        'Actors': 'Marilyn Burns, Edwin Neal, Allen Danziger',
        'Plot': 'Five friends head out to rural Texas to visit the grave of a grandfather. On the way they stumble across what appears to be a deserted house, only to discover something sinister within. Something armed with a chainsaw.',
        'Language': 'English',
        'Country': 'United States',
        'Awards': '1 win & 2 nominations',
        'imdbRating': '7.4',
        'Jumpscare_count': 2,
        'Jumpscare_rating': '1.0'}
    ]
```

## Problem 06 (40 points)

1. Implement a function called `search_movie_plot()`. Review the function's docstring regarding its expected behavior, parameters, and return value (if any).

2. After implementing `search_movie_plot()` return to the `main()` function. Iterate over `horror_movies` and call the function `search_movie_plot()` on each movie dictionary. Use the list, assigned to the variable `ghost_terms`, as the `search_terms` parameter to return all movie dictionaries that include these terms in their plot. Implement a conditional to check whether `search_movie_plot()` returns `True`; if the condition is met, add the movie dictionary to the variable `ghost_movies`.

The `ghost_movies` list must include:

```python
    [{
        'Title': 'The Others',
        'Year': 2001,
        'Rated': 'PG-13',
        'Released': '10 Aug 2001',
        'Runtime': 104,
        'Genre': 'Horror, Mystery, Thriller',
        'Director': 'Alejandro Amenábar',
        'Writer': 'Alejandro Amenábar',
        'Actors': 'Nicole Kidman, Christopher Eccleston, Fionnula Flanagan',
        'Plot': 'A woman who lives in her darkened old family house with her two photosensitive children becomes convinced that the home is haunted.',
        'Language': 'English',
        'Country': 'Spain, United States, France, Italy',
        'Awards': 'Nominated for 2 BAFTA 29 wins & 55 nominations total',
        'imdbRating': '7.6',
        'Jumpscare_count': 4,
        'Jumpscare_rating': '2.0'
    }, {
        'Title': 'The Nun',
        'Year': 2018,
        'Rated': 'R',
        'Released': '07 Sep 2018',
        'Runtime': 96,
        'Genre': 'Horror, Mystery, Thriller',
        'Director': 'Corin Hardy',
        'Writer': 'Gary Dauberman, James Wan',
        'Actors': 'Demián Bichir, Taissa Farmiga, Jonas Bloquet',
        'Plot': 'A priest with a haunted past and a novice on the threshold of her final vows are sent by the Vatican to investigate the death of a young nun in Romania and confront a malevolent force in the form of a demonic nun.',
        'Language': 'English, French, Romanian, Latin',
        'Country': 'United States',
        'Awards': '2 wins & 1 nomination',
        'imdbRating': '5.3',
        'Jumpscare_count': 21,
        'Jumpscare_rating': '4.5'
    },
    ...
```

3. Call `filter_movies()` and pass to it the `ghost_movies` list and filter for movies that have a relatively high jump scare count that is anywhere from 10 to 30 jump scares (inclusively). Assign the return value to `high_jumpscare_ghost_movies`. 

## Problem 07 (45 points)

1. Implement a function called `extract_kv_pair()`. Review the function's docstring regarding its expected behavior, parameters, and return value (if any).

2. After implementing `extract_kv_pair()` return to the `main()` function.

    1. Create an empty dictionary and assign it to a variable with name `'movie_runtimes'`
    2. Iterate over `high_jumpscare_ghost_movies` and call `extract_kv_pair()`. Pass to it each movie dictionary in `high_jumpscare_ghost_movies` and the string `'Runtime''` to extract each movie's runtime.
    3. Add each returned tuple to the `movie_runtimes` dictionary by unpacking the returned tuple and assigning the first element (movie's title) as the key and second element (movie's runtime) as its value.

The `movie_runtimes` dictionary must include:

```python
    {
        'The Nun': 96,
        'The Conjuring': 112,
        'House on Haunted Hill': 93
    }
```

3. Implement a function called `total_runtime_hrs()`. Review the function's docstring regarding its expected behavior, parameters, and return value (if any).

    After implementing `total_runtime_hrs()` return to the `main()` function. Call `total_runtime_hrs()` and pass to it the `movie_runtimes` dictionary. Assign the return value to the variable `total_runtime`.

    :bulb: The value returned from `total_runtime_hrs()` is a whole number (no fractional component).

4. Lastly, call `write_dicts_to_csv()` and pass to it three arguments:
    1. the filepath `'stu_jumpscare_ghost_movies.csv'`
    2. the list created in the previous problem `high_jumpscare_ghost_movies` as its data
    3. the appropriate field names, which should be the keys of one dictionary in the `high_jumpscare_ghost_movies` list. 