# Problem Set 08

## Exploring New York Times Bestselling Books

<br />

## Background

The New York Times publishes several "bestselling books" lists that list America's most sold books in various categories. It is a great honor for an author to have a book on a New York Times Bestselling List.

Learn more: https://www.nytimes.com/books/best-sellers/

Your data this week comes from two NYT bestseller lists that are published weekly. Note that it is very common for a book to remain on the bestselling list for multiple weeks.

- __young_adult_bestsellers.json__ contains the data from the "Young Adult Hardcover Bestsellers" lists from the last 8 weeks. These lists report the top 10 bestselling young adult hardcover books each week.

- __fiction_bestsellers.json__ contains the data from the "Hardcover Fiction Bestsellers" lists from the last 8 weeks. These lists report the top 15 bestselling hardcover fiction books each week.

:exclamation: We will be handling both bestselling _lists_ and Python _list_ objects this week. __Be careful! In each JSON file, you'll see that the bestselling _list_ for a single week is represented by a _dictionary_!__ Spend plenty of time acquainting yourself with the data and keeping your objects straight.

<br />

## Data

When read in, each JSON file comprises a __list of dictionaries__. Each dictionary represents the bestselling books list published for a specific week. __Keys__ of note within this "bestsellers list" dictionary include `"list_name"`, `"published_date"`, `"normal_list_ends_at"`, and `"books"`. You will be working primarily with the value of the `"books"` key, which is itself a __dictionary__. Review this data structure carefully.

:bulb: Although these are large files, they are repetitive and fairly clean. We are confident you can handle them!

Note: The books' prices were randomly generated. In the real data, each price was listed as '0.00'.

<br />

## Problems

The problems can generally be split into problems that work with `"young_adult_bestsellers.json"` (Problems 1-4) and problems that work with `"fiction_bestsellers.json"` (Problems 5-9).

Your goals for `"young_adult_bestsellers.json"` are to read in the file, clean the book data within it, and write the cleaned data out to a new JSON file. Finally, you will find the average price for books in the No. 1 position on the list and the No. 10 position spot on the list.

Your goal for `"fiction_bestsellers.json"` is to score each publisher based on where and how often its books appear on the bestsellers list. You will create a "scoreboard" dictionary with all the publishers and their scores. You will write this scoreboard out to a new JSON file.

The program features a number of functions including a `main()` function that serves as the entry point to the program and orchestrator of the program's work flow.

<br />

## Problem 1

__Task__: Implement a function that can read a JSON file and convert it into a Python list or dictionary.

1. Implement the function named `read_json`. The function defines two parameters:

   * `filepath`, a path to a source JSON file.
   * `encoding`, a string representing a character encoding (default value = `'utf-8'`).

   Review the function's docstring for more information about the function's expected behavior.

2. After implementing `read_json`, navigate to the `main` function. Call the `read_json` function passing it the
`'young_adult_bestsellers.json'` filepath. Assign the return value to a variable named `young_adult_bestsellers`.

3. `young_adult_bestsellers` is a very large list. Use slicing to assign the first element of the list that represents the first week's bestsellers list to the variable `young_adult_bestsellers_week_1`

   `young_adult_bestsellers_week_1` _must_ start with:

   ```python
   {
      'list_name': 'Young Adult Hardcover',
      'list_name_encoded': 'young-adult-hardcover',
      'bestsellers_date': '2022-09-03',
      'published_date': '2022-09-18',
      'published_date_description': '',
      'next_published_date': '2022-09-25',
      'previous_published_date': '2022-09-11',
      'display_name': 'Young Adult Hardcover',
      'normal_list_ends_at': 10,
      'updated': 'WEEKLY',
      'books': [
         {
            'rank': 1,
            'rank_last_week': 2,
            'asterisk': 0,
            'dagger': 0,
            'primary_isbn10': '1368069606',
            'primary_isbn13': '9781368069601',
            'publisher': 'Disney',
            'description': 'Sally, the new Queen of Halloween Town, must save her town from a sleeping curse.',
            'price': '24.99',
            'title': 'LONG LIVE THE PUMPKIN QUEEN'
            ...
   ```

<br />

## Problem 2

__Task__: Implement the functions `convert_to_float()` and `clean_book()` to ensure that the book prices can be manipulated as floats (since we want to find  average prices in Problem 3) and to edit down the book dictionaries so that they are easier to read and work with. Use these functions to clean the books within `young_adult_bestsellers`.

1. Implement the function named `convert_to_float`. Review the function's docstring regarding its expected
behavior, parameters, and return value.

   __Function requirements and hints__

   1. Wrap your code in `try` and `except` statements to handle errors.

   2. Use a conditional statement to determine if the value is of the type `int`. If the value is an `int`, do not convert it.

   3. If the value is not an integer, reassign the `value` variable to a `float` version of the value, if possible.

   4. Return `value`.

2. After implementing `convert_to_float()` return to the `main()` function

3. Test `convert_to_float()` by passing to it three different types of arguments: an `int`, a `str` that cannot be converted to a `float`, and a `str` that can be converted to a `float`. To test `convert_to_float()`, make the following function calls:

   - Call `convert_to_float()` and pass to it `integer_to_test`. Assign the return value to a variable named `integer_return`.
   - Call `convert_to_float()` and pass to it `string_to_test`. Assign the return value to a variable named `string_return`.
   - Call `convert_to_float()` and pass to it `float_to_test`. Assign the return value to a variable named `float_return`.

   Confirm that `convert_to_float()` performs as expected and does not throw any errors.

4. Implement the function named `clean_book`. Review the function's docstring regarding its expected
behavior, parameters, and return value.

   __Function requirements and hints__

   1. Create an empty dictionary that will become the new book dictionary that you must return.

   2. Loop through the keys and values of the `book` dictionary using the appropriate dictionary method.

   3. If a `desired_keys` list was passed in, ensure that only keys that are in `desired_keys` are added to the new dictionary. Pass the values paired with these keys to `convert_to_float()` and assign the return value as the value in the new dictionary.

   3. If there are no `desired_keys`, add all the keys and values to the new dictionary, _at the same time_ calling `convert_to_float()` to convert the values.

   4. Return the new dictionary that was created.

5. After implementing `clean_book()` return to the `main()` function.

6. Use `clean_book()` to clean all the books in each of the 8 "bestsellers list" dictionaries in `young_adult_bestsellers`.

   __Requirements and hints__

   1. Loop through `young_adult_bestsellers` to access the "bestsellers list" dictionaries one week at a time.

   2. You may want to access just the books from each week and assign the list of books to a variable that you can use going forward.

   3. Use `for i in range()` to call `clean_book()` on each book and assign the cleaned book back to the book list in its place.

   4. When you call `clean_book()` you _must_ pass `keep_keys` as the second argument using a _keyword argument_.

   Your cleaned `young_adult_bestsellers_week_1` list _must_ now start with:

   ```python
   {
      'list_name': 'Young Adult Hardcover',
      'list_name_encoded': 'young-adult-hardcover',
      'bestsellers_date': '2022-09-03',
      'published_date': '2022-09-18',
      'published_date_description': '',
      'next_published_date': '2022-09-25',
      'previous_published_date': '2022-09-11',
      'display_name': 'Young Adult Hardcover',
      'normal_list_ends_at': 10,
      'updated': 'WEEKLY',
      'books': [
         {
            'rank': 1,
            'rank_last_week': 2,
            'publisher': 'Disney',
            'description': 'Sally, the new Queen of Halloween Town, must save her town from a sleeping curse.',
            'price': 24.99,
            'title': 'LONG LIVE THE PUMPKIN QUEEN',
            'author': 'Shea Ernshaw',
            'isbns': [
               {
                  'isbn10': '1368069606',
                  'isbn13': '9781368069601'
               }
            ]
         }
         ...
   ```

<br />

## Problem 3

__Task__: As mentioned earlier, `young_adult_bestsellers` is a very large list that we do not necessarily want to print out in our terminal. But, we want to confirm that `clean_book()` applied to all the weeks in the `young_adult_bestsellers` list, so we want to write the cleaned data out to a new JSON file to inspect it. In this problem, you will implement a function that can write a list of dictionaries to a JSON file.

1. Implement the function named `write_json`. The function defines four parameters:

   * `filepath`, a path to target file.
   * `data`, a list of dictionaries that needs to be written
   into a JSON file;
   * `encoding`, name of encoding used to encode the file (default value = `utf-8`).
   * `indent`: an integer number of "pretty printed" indention spaces applied to encoded JSON
     (Default value = `2`).

   Review the function's docstring for more information about the function's expected behavior.

2. After implementing `write_json`, return to the main function.

3. Call the function `write_json` and pass to it as arguments `filepath` ('clean_young_adult_bestsellers.json') and `young_adult_bestsellers`. Compare your output file to the test fixture file `fxt-clean_young_adult_bestsellers.json`. Both files _must_ match, line for line, and character for character.

## Problem 4

__Task__: Our last task with the `young_adult_bestsellers` list is to implement a function that finds the average price of the books of a given rank and then test your implementation by returning the average price of books ranked No. 1 and books ranked No. 10.

1. Implement the function named `get_average_price_by_rank`. Review the function's docstring regarding its expected behavior, parameters, and return value.

   __Function requirements and hints__

   1. Begin by assigning the variable `total_price` to `0`.

   2. Each time you need to access a value from a dictionary in this function, you _must_ use the `dict.get()` method.

   3. Use nested `for` loops to loop through all the books in the eight "bestsellers list" dictionaries.

   4. If the book's `'rank'` is equivalent to the passed-in `rank`, add the price of that book to the `total_price` using the addition assignment.

   5. Once the `total_price` has fully accumulated (the looping has ended), return the average price of the books of the given rank, rounded to the nearest cent.

   :exclamation: Remember that there are 8 weeks of bestsellers lists, so there will be 8 books of each rank.

2. After implementing `get_average_price_by_rank()`, return to the `main()` function.

3. Call the function `get_average_price_by_rank()` and pass to it the `young_adult_bestsellers` list and the integer, 1, as arguments. Assign the return value to the variable named `rank_1_avg`.

   The average price of No. 1 young adult books is __$25.38__.

   :exclamation: You must use the positional arguments in the function call to pass the auto grader

4. Call the function `get_average_price_by_rank()` and pass to it the `young_adult_bestsellers` list and the integer, 10, as arguments. Assign the return value to the variable named `rank_10_avg`.

   The average price of No. 10 young adult books is __$22.85__.

   :exclamation: You must use the keyword arguments in reverse order in the function call to pass the auto grader

<br />

## Problem 5

__Task__: Problems 5-9 handle data from `fiction_bestsellers.json`. Implement a function that retrieves all the books for any given publisher. Call the function to find all the books published by Doubleday and print their titles and ranks.

1. Implement the function named `get_books_by_publisher`. Review the function's docstring regarding its expected behavior, parameters, and return value.

   __Function requirements and hints__

   1. Use the accumulator pattern. (An empty list to which objects are appended.)

   2. Use nested `for` loops to access all the books in the "bestsellers list" dictionaries.

   3. Your function must work regardless of the case of the `publisher` string that is passed in.

   4. The list that this function returns _must_ include dictionaries for the same book that come from different weeks' lists. For example, it might include `{'rank': 1, 'title': 'Where the Wild Things Are'}` from week 1, `{'rank': 1, 'title': 'Where the Wild Things Are'}` from week 3, and `{'rank': 8, 'title': 'Where the Wild Things Are'}` from week 4.

2. After implementing `get_books_by_publisher()`, return to the `main()` function.

3. Now get the data from `fiction_bestsellers.json`. Call `read_json()` passing it the
`'fiction_bestsellers.json'` filepath. Assign the return value to a variable named `fiction_bestsellers`.

4. `fiction_bestsellers` is a very large list. Use slicing to assign the dictionary that represents the __last__ week's bestsellers list to the variable `fiction_bestsellers_week_8`

   `fiction_bestsellers_week_8` _must_ start with:

   ```python
   {
      'list_name': 'Hardcover Fiction',
      'list_name_encoded': 'hardcover-fiction',
      'bestsellers_date': '2022-10-22',
      'published_date': '2022-11-06',
      'published_date_description': 'latest',
      'next_published_date': '',
      'previous_published_date': '2022-10-30',
      'display_name': 'Hardcover Fiction',
      'normal_list_ends_at': 15,
      'updated': 'WEEKLY',
      'books': [
         {
            'rank': 1,
            'rank_last_week': 0,
            'asterisk': 0,
            'dagger': 0,
            'primary_isbn10': '0385548923',
            'primary_isbn13': '9780385548922',
            'publisher': 'Doubleday',
            'description': 'Two childhood friends follow in their fathers’ footsteps, which puts them on opposite sides of the law.',
            'price': '0.00',
            'title': 'THE BOYS FROM BILOXI'
            ...
   ```

5. Now, call the function `get_books_by_publisher()` and pass to it the `fiction_bestsellers` list and the publisher, `"Doubleday"`. Assign the return value to the variable named `doubleday_books`.

6. Let's make this data a little more readable. Your goal is to print the title and rank for each of the books in the `doubleday_books` list. Uncomment the `for` loop and replace the question marks (?) with expressions that will resolve into the `'title'` and the `'rank'` for each book.

   __Requirements__

   1. You _must_ access the `'title'` from the book dictionary using _subscript notation_.

   2. You _must_ access the `'rank'` from the book dictionary using a _dictionary method_.

<br />

## Problem 6

__Task__: Implement a function that returns a score for a given book depending on its rank (in one week's list). Call the function to score the first and penultimate books from `doubleday_books`.

:bulb: "Penultimate" is another word for second-to-last.

1. Implement the function named `score_book`. Review the function's docstring regarding its expected behavior, parameters, and return value.

   __Function requirements and hints__

   1. Use `if - elif - else` statements to sort the book according to its rank, then return the appropriate score.

2. After implementing `score_book()` return to the `main()` function.

3. Call `score_book()` passing it the
first book from the `doubleday_books` list. Assign the return value to a variable named `first_book_score`.

   Replace the "?first book title?" substring in the f-string with an expression that will resolve to the title of the first book from the `doubleday_books` list. You _must_ use _subscript notation_.

   The first Doubleday book _must_ be __LESSONS IN CHEMISTRY__ and its score is __10__.

4. Call `score_book()` passing it the
penultimate book from the `doubleday_books` list. Assign the return value to a variable named `penultimate_book_score`.

   Replace the "?penultimate book title?" substring in the f-string with an expression that will resolve to the title of the penultimate book from the `doubleday_books` list. You _must_ use _subscript notation_.

   The penultimate Doubleday book _must_ be __THE BOYS FROM BILOXI__ and its score is __15__.

## Problem 7

__Task__: Implement a function that returns a score for a given publisher which is the total of the scores of all its books over the whole eight week period. Call the function to determine the score for Doubleday.

1. Implement the function named `score_publisher`. Review the function's docstring regarding its expected behavior, parameters, and return value.

   __Function requirements and hints__

   1. Use the accumulator pattern. (A variable that starts at 0 and is added to with addition assignment.)

   2. Call `get_books_by_publisher()` to access all the books published by the given publisher.

   3. Call `score_book()` on each book returned in the `get_books_by_publisher()` list, so that it might be added to the total publisher score.

2. After implementing `score_publisher()` return to the `main()` function.

3. Call `score_publisher()` passing it the
`fiction_bestsellers` list and publisher `"Doubleday"`, _using keyword arguments in reverse order_. Assign the return value to a variable named `doubleday_score`.

   The Doubleday publisher score _must_ be __70__.

## Problem 8

__Task__: Implement a function that returns a list of each of the publishers that appears in any of the eight "bestsellers list" dictionaries. Call the function to find which publishers have had a book on the NYT fiction bestsellers list in the past 8 weeks.

1. Implement the function named `find_publishers`. Review the function's docstring regarding its expected behavior, parameters, and return value.

   __Function requirements and hints__

   1. Use the accumulator pattern. (An empty list to which objects are appended.)

   2. Use nested `for` loops to access all the books in the "bestsellers list" dictionaries.

   3. Append each publisher name to the list, but be sure to use a conditional statement to avoid adding repeats of names that are already in the list.

2. After implementing `find_publishers()` return to the `main()` function.

3. Call `find_publishers()` passing it the
`fiction_bestsellers` list. Assign the return value to a variable named `fiction_publishers`.

   The `fiction_publishers` list _must_ be:

   ```python
      ['Ballantine', 'Mulholland', "St. Martin's", 'Bantam', 'Flatiron', 'Grand Central', 'Little, Brown', 'Doubleday', 'Harper Voyager', 'Viking', 'Morrow', 'Delacorte', 'Knopf', 'Scribner', 'Putnam', 'Berkley', 'Simon & Schuster', 'Minotaur', 'Zando', 'Atria/Emily Bestler', 'Tordotcom', 'Random House', 'Pamela Dorman', 'Del Rey', 'Atria', 'Penguin Press', "St. Martin's Griffin", 'Harper']
   ```

## Problem 9

__Task__: Implement a function that returns a dictionary "scoreboard" in which each key is a publisher and each value is that publisher's score, based on their books' rankings. Call the function to create a "publisher scoreboard" based on the NYT fiction bestsellers lists from the past 8 weeks.

1. Implement the function named `create_scoreboard`. Review the function's docstring regarding its expected behavior, parameters, and return value.

   __Function requirements and hints__

   1. Use the accumulator pattern with a dictionary, as explained below.

   2. Create an empty dictionary and assign it to a variable such as `scoreboard`.

   3. Call `find_publishers()` and pass to it `bestseller_lists`.

   4. Loop through the list returned by `find_publishers()` to access each `publisher`.

   5. Within the loop, add a new key-value pair to the `scoreboard` dictionary. The key must be the `publisher` and the value must be the value that returns when you pass `bestseller_lists` and `publisher` to `score_publisher()`.

   6. Return the `scoreboard` dictionary.

2. After implementing `create_scoreboard()` return to the `main()` function.

3. Call `create_scoreboard()` passing it the
`fiction_bestsellers` list. Assign the return value to a variable named `fiction_publishers_scoreboard`.

   The `fiction_publishers_scoreboard` list _must_ be:

   ```python
      {
         'Ballantine': 100,
         'Mulholland': 25,
         "St. Martin's": 45,
         'Bantam': 65,
         'Flatiron': 15,
         'Grand Central': 125,
         'Little, Brown': 85,
         'Doubleday': 70,
         'Harper Voyager': 10,
         'Viking': 35,
         'Morrow': 10,
         'Delacorte': 15,
         'Knopf': 45,
         'Scribner': 130,
         'Putnam': 50,
         'Berkley': 10,
         'Simon & Schuster': 15,
         'Minotaur': 25,
         'Zando': 40,
         'Atria/Emily Bestler': 40,
         'Tordotcom': 15,
         'Random House': 105,
         'Pamela Dorman': 15,
         'Del Rey': 15,
         'Atria': 35,
         'Penguin Press': 35,
         "St. Martin's Griffin": 10,
         'Harper': 15
         }
   ```

4. Call the function `write_json` and pass to it as arguments `filepath` ('fiction_publishers_scoreboard.json') and `fiction_publishers_scoreboard`. Compare your output file to the test fixture file `fxt-fiction_publishers_scoreboard.json`. Both files _must_ match, line for line, and character for character.

<br />

## End of Problem Set 08
