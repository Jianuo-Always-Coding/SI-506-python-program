# SI 506: Lab Exercise 10

## This week's Lab Exercise
This week's lab exercise includes six (6) problems that focus on list comprehensions.

## Background
For this lab you are provided with a list of 20 space-related articles published by the New York
Times. The articles are represented as a list of JSON objects, with each JSON object representing
a NYT article.

## Data
The New York Times provides an [Article Search API](https://developer.nytimes.com/docs/articlesearch-product/1/overview) (Application Programming Interface) that permits keyword searching
and retrieval of JSON representations of NY Times articles.

Today's data comprises a list of 20 JSON objects that represent NY Times articles related to space
exploration, published by the Science Desk.

The JSON document named `nyt_articles_space.json` is what you will be working with in this lab
exercise. Review the file and familiarize yourself with its structure and name-value pairs. Similar data
was presented during earlier lectures, so you should be familiar with each article's data structure.

## 1.0 Problem 01 (5 points)

1. Implement a function called `get_keywords_by_name()`. Review the function's docstring regarding
   its expected behavior, parameters, and return value.

   __Function requirements and hints__

   1. You _must_ write a list comprehension that returns a list of article keyword values filtered
      on the keyword 'name'. Only keyword values associated with a 'name' that matches the passed in
      `keyword_name` argument are to be included in the list returned to the caller.

   2. If you are unsure how to structure the list comprehension, implement a standard `for` loop
      first. Get the function working correctly, then comment out the `for` loop and reconfigure it into a
      list comprehension.
         :bulb: Note the structure of the `'keywords'` key within each article dictionary.

   3. The function block is restricted to __a single line__ of uncommented out code.

2. After implementing the function, return to `main()`.

3. Assign the filepath `'nyt_articles_space.json'` to the `FILEPATH` variable. Then call the
   function `read_json()` and pass to it the argument `FILEPATH`. Assign the return value to the
   variable `nyt_api_articles`.

4. You have been provided with a list of keyword dictionaries called `TEST_KEYWORDS`. `TEST_KEYWORDS`
   mimics each NYT article's `'keywords'` list of dictionaries . You will use this to test your
   function. Call `get_keywords_by_name()` and pass to it the provided `TEST_KEYWORDS` variable and
   the string "subject" as its arguments. Assign the variable `test_keywords` to the return
   value.

   Your `test_keywords` values _must_ match the list below.

   ```Python
   ['Space', 'telescope']
   ```

## 2.0 Problem 02 (5 points)

1. Implement a function named `create_thinned_articles()`. Review the function's docstring regarding
   its expected behavior, parameters, and return value.

   __Function requirements and hints__

   1. You _must_ write a list comprehension that returns a list of "thinned" NYT article
      dictionaries. This involves embedding a dictionary literal inside the comprehension and
      mapping the required values to the appropriate keys.

   2. You _must_ delegate to the function `get_keywords_by_name()` the task of retrieving a list of
      keyword values when assigning the 'keywords' key-value pair.

   3. If you are unsure how to structure the list comprehension, implement a standard `for` loop
      first. Get the function working correctly, then comment out the `for` loop and reconfigure it into a
      list comprehension.

   4. The list comprehension can and should be expressed over multiple lines in adherance to Python's
      79-100 character line limit.

    Below is an example of a "thinned" article dictionary.

   ```Python
   [
       {
           'abstract': 'Astronomers said they might be on the verge of finding out ....',
           'snippet': 'Astronomers said they might be on the verge of finding out ....',
           'lead_paragraph': 'The dark side of the universe is whispering, but scientists ....',
           'headline_main': 'Tantalizing New Clues Into the Mysteries of Dark Matter',
           'keywords': [
                'Dark Matter (Astronomy)',
                'Space',
                'Astronomy and Astrophysics',
                'International Space Station'
                ],
           'word_count': 1071,
           'pub_date': '2013-04-03T15:06:19+0000'
       }
   ]
   ```

2. After implementing `create_thinned_articles()`, return to `main()`.

3. Call `create_thinned_articles()` passing to it `nyt_api_articles` and the string '`subject'` as
   variables. Assign the return value to the variable `articles`.

## 3.0 Problem 03 (5 points)

1. Implement a function named `filter_articles()`. Review the function's docstring regarding
   its expected behavior, parameters, and return value.

   __Function requirements and hints__

    1. You _must_ implement two list comprehensions. Employ conditional logic to determine which comprehension returns the new list to the caller. Each comprehension _must_ be expressed in a single line of code and returned immediately to the caller (e.g., do not assign the comprehension to a local variable).

    2. Evaluate the truth value of `min_word_count`. If `True`, filter the articles on both subject
       keyword and minimum word count (greater than or equal to the specified minimum) as specified
       in the docstring. If `False`, filter the articles on the subject keyword only.

   3. If you are unsure how to structure the list comprehension, implement a standard `for` loop
      first. Get the function working correctly, then comment out the `for` loop and reconfigure it into a
      list comprehension.

2. After implementing `filter_articles()`, return to `main()`.

3. Call the `filter_articles()` function three (3) times:

    1. In the first call, pass `articles`, the string `'Space'`, and the integer `1000` as arguments.
       Assign the return value to the variable `articles_min1000`.

    2. In the second call, pass the `articles` and the string `'Asteroids'` as arguments.
       Assign the return value to the variable `articles_asteroids`.

    3. In the third call, pass the `articles` variable, the string `'International Space Station'`,
       and the integer `1000`. Assign the return value to the variable `articles_space_station`.

## 4.0 Problem 04 (5 points)

1. Implement the function named `create_thinned_article_tuples()`. Review the function's docstring
   regarding its expected behavior, parameters, and return value.

   __Function requirements and hints__

    1. You _must_ write a list comprehension that returns a list of tuples that represent a
       subset of the "thinned" NYT article attributes. This involves embedding a tuple _literal_
       inside the comprehension and assigning the required values as tuple items in the order
       specified in the docstring.

    2. You will need to access the Year-Month-Day (YYYY-MM-DD) portion of the article's publication
       date. Utilize the appropriate `str` method and indexing to access the desired substring.

    3. If you are unsure how to structure the list comprehension, implement a standard `for` loop
      first. Get the function working correctly, then comment out the `for` loop and reconfigure it into a
      list comprehension.


2. After implementing `create_thinned_article_tuples()` return to `main()`.

3. Call `create_thinned_articles_tuples()` and pass to it `articles_min1000` as the argument. Assign
   the return value to the variable `article_tuples`.

## 5.0 Problem 05 (5 points)

1. Implement a function called `sum_word_counts()`. Review the function's docstring
   regarding its expected behavior, parameters, and return value.

    __Function requirements and hints__

    1. You _must_ write a list comprehension that returns a list of __word counts__ sourced from
       each article tuple in `article_tuples`. Pass the comprehension directly to the appropriate
       built-in function that can accept a list of integers in order to add the integers together to
       obtain the total amount. Return this value immmediately to the caller (i.e., do not assign it
       to a local variable).

    2. If you are unsure how to structure the list comprehension, implement a standard `for` loop
      first that implements the accumulation pattern. Get the function working correctly, then
      comment out the `for` loop and reconfigure it into a list comprehension.

    3. The function block is restricted to __a single line__ of uncommented out code.

2. After defining `sum_word_counts()`, return to `main()`.

3.  Call `sum_word_counts()` function twice.

    1. Call the function `create_thinned_article_tuples()` and pass to it the argument
       `articles_asteroids`. Pass this expression directly to the function `sum_word_counts()` as
       its argument. Assign the return value to the variable named `total_words_asteroids`. Do all
       this in one line of code.

    2. Call the function `create_thinned_article_tuples()` and pass to it the argument
       `articles_space_station`. Pass this expression directly to the function `sum_word_counts()`
       as its argument. Assign the return value to the variable named `total_words_space_station`.
       Do all this in one line of code.

## 6.0 Problem 06 (5 points)

1. Implement the function named `get_word_count()`. Review the function's docstring
   regarding its expected behavior, parameters, and return value.

   __Function requirements and hints__

    1. Implement with a single line of code. Return the passed in tuple's word count item to the
       caller.

    :bulb: This function will be used to provide the value upon which to sort the article tuples in
    `article_tuples`.

2. After implementing  `get_word_count()`, return to `main()`.

3. Call `get_word_count()` and pass to it as the argument the first tuple element in
   `article_tuples`. Assign the return value to the variable `test_word_count`.

4. Call the built-in `sorted()` function and pass to it the required arguments to sort `article_tuples`
   based on each article tuple's word count in _descending_ order. Assign the new sorted list to the
   variable named `sorted_articles`.

5. Utilize the provided `write_json()` function and write the value assigned to `sorted_articles` to
   a file named `stu_sorted_articles.json`.
