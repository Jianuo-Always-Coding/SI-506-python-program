# SI 506: Lab Exercise 08

## This week's Lab Exercise

This week's lab exercise includes five (5) problems that focus on using the dictionaries and json module to load data from json file and write data to json file.

## Background

For this lab, you will be using data from a json file  `nyt-books.json`. Data for this  file was fetched from the New York Times web developer API (Application Program Interface). The data provided represents New York Times best selling books for the week of October 23, 2022 for various categories. The json file contains a list of dictionaries where each dictionary corresponds to one category of books. Each dictionary element corresponding to one category of books contains many key-value pairs among which one is 'books'. The key 'books' contains a list of top 5 bestselling books. Each element of the list of top 5 bestselling books is a dictionary containing metadata for one book. Take some time to familiarize yourself with the json file provided.
## Problem 01 (3 points)

1. Make corrections in the implementation of the function called `read_json()` which reads a JSON document per the provided filepath and _decodes_ the file data as a `dict` or a `list` (of dictionaries), before returning the decoded data to the caller. It defines two parameters:

    - filepath (str): path to file

    - encoding (str): name of encoding used to decode the file

2. Inside of the `main()` function, create a variable called `books_data` and assign it the value of `read_json()` function with the filepath of `nyt-books.json` file.

    :exclamation: To check if you read the json file correctly, uncomment the print statement and it should look like the string shown below.

   ```python
    'Length of books_data list from json file is: 18'
    ```

3. The `books_data` is a list of dictionaries where each dictionary element corresponds to a category of books. The name of the category is stored in the key `list_name`. Write a `for` loop to collect all the categories of books present in the `books_data` in the list called `list_names`.

## Problem 02 (7 points)

1.  Implement a function called `illustration_books`. This function defines 1 parameter

    - data(list): a list of dictionaries each of which contains a list of books.

    This function returns a dictionary which has category name as the key and list of book titles which have illustration contributions by people other than the author as the value.

    :exclamation: Illustrations contributor can be found in the key `contributor_note` in the dictionary associated with a single book.

    1. Create an empty dictionary. This dictionary will later contain name of the category as keys and list of book titles as value.
    2. Use `for` loop to iterate over each element of the list `data`.
    3. Within the loop, use indexing to fetch the list of top 5 bestselling books corresponding to that category(stored in the key `books`).

        :exclamation: Create an empty list which will later store the title of the books that have illustration contributor inside the second `for` loop.

    4. Use another nested `for` loop to iterate over the list of top 5 bestselling books and get a list of titles of the books that have illustrations contributor(stored in the key `contributor_note`) for the book using the empty list created in the outer loop.

        :exclamation: If the value of the key `contributor_note` is not an empty string, it means the book has an illustration contributor.

        :exclamation: Use the value for the key `contributor_note` _only_ in the conditional statement. Any string character gives a truth value of `True` and any empty string gives a truth value of `False`.

    5. If a list of bestselling books has one or more books with illustration contributors, add the data to the dictionary created in Step 1 with the category name (stored in the key `list_name`) as the key and the list of book titles created in Step 4 as value.

        :bulb: The dictionary to be returned contains only those categories which have one or more books with illustrations.

2. Inside the `main()` function, create a variable called `books_with_illustrations` and assign it the value of the `illustration_books()` function with `books_data` as its argument.


## Problem 03 (6 points)

1. Implement a function called `get_publishers`. This function defines 1 parameter

   - data(list): a list of dictionaries each of which contains a list of books.

    It returns a dictionary of publishers having the name of the publisher as the key and the count of books published by the respective publisher as the value.

   1. Create an empty dictionary.
   2. Loop through the list `data` and fetch the top 5 bestselling books for each category.
   3. Using another nested `for` loop, iterate over the list of top 5 bestselling books.
   4. Add the publisher (stored in the key `publisher`) as the key and employ the `.get()` method to add the publisher count as the value to the dictionary created in Step 1.
        :exclamation: You will have to make use of the optional parameter in `.get()` in case this is the first time coming across a publisher.
   5. Outside of the two `for` loops, return the dictionary containing the name of the publisher as key and count of books published by that publisher as value.


2. Inside the `main()` function, create a variable called `publishers_data` and assign it the value of the `get_publishers()` function with `books_data` as an argument.

3. Create an empty list called `frequent_publishers`. Loop over `publishers_data` and add the name of the publishers that published more than 3 books to the `frequent_publishers` list.

    :exclamation: Employ `.items()` method when looping over `publishers_data`.

## Problem 04 (6 points)

NYT publishes a list of bestselling books every week for many categories. A book can appear multiple times in the bestselling list. For each book in the `books_data`, the `weeks_on_list` key stores the number of times the book has appeared in the bestselling list.

1. Implement the function called `bestselling_books`. This function defines 2 parameters

   - data(list): a list of dictionaries each of which contains a list of books.

   - publishers_list(list): list of names of publishers.

    It returns a list of book titles that have appeared in the bestselling list more than 200 times and have publisher among the `publishers_list`.

    1. Create an empty list which will later contain the book titles.
    2. Loop through the list `data` and fetch the top 5 bestselling books for each category.
    3. Using another nested `for` loop, iterate over the list of top 5 bestselling books.
    4. Employ a compound conditional statement to check for if the number of times the book has appeared in the bestselling list(stored in key `weeks_on_list`) is greater than 200 and if the book published by a publisher is present in the `publishers_list`.
    5. If the compound conditional statement evaluates to `True`, populate the list created in Step 1 with the book's title.
    6. Return the list of book titles.

2. Inside the `main()` function, create a variable called `max_times_best_selling` and assign it the value of  the `bestselling_books()` function with `books_data` and `frequent_publishers` as arguments.

    :exclamation: Do not provide keyword arguments in the `bestselling_books()` function call. Pass the arguments in the order of parameters in the function definition.

## Problem 05 (3 points)
1. Make corrections in the implementation of the function called `write_json()` which serializes object as JSON and writes the JSON to the provided filepath. It defines five parameters:

    - filepath (str): the path to the file
    - data (dict)/(list): the data to be encoded as JSON and written to the file
    - encoding (str): name of encoding used to encode the file
    - ensure_ascii (str): if False non-ASCII characters are printed as is; otherwise non-ASCII characters are escaped.
    - indent (int): number of "pretty printed" indention spaces applied to encoded JSON


2. Inside the `main()` function, create an empty dictionary called `books_dictionary`. This dictionary will contain data from all the functions you have worked on in the file.

   1. Add a key-value pair to this dictionary with the string `'books_with_illustrations'` as the key and the variable `books_with_illustrations` after the `illustration_books()` function as the value.
   2. Add a key-value pair to this dictionary with the string `'frequent_publishers'` as the key and the `frequent_publishers` list after the implementation of the `for` loop as the value.
   3. Add a key-value pair to this dictionary with the string `'max_times_best_selling'` as the key and the variable `max_times_best_selling` after the `bestselling_books()` function call as the value.
   4. Call the `write_json()` function and pass to it `stu_books_data.json` as the filepath and `books_dictionary` as the data.

    :exclamation: Do not provide keyword arguments in the `write_json()` function call.  Pass the arguments in the order of parameters in the function definition.
