# SI 506: Problem Set 10

## This week's Problem Set

This week's problem set focuses on list and dictionary comprehensions.

## Background

The data from this week consists of New York Times articles that reference the cultural phenomenon that is Star Wars.

Throughout this assignment we will ask you to use list and dictionary comprehensions. For each implementation, we will ask you to assign a specific name to the loop variable in each comprehension. **Please** ensure that you name your loop variables appropriately for accurate grading. **Make sure your comprehensions are on _one line_ when you submit!!**

Kindly refer to the code snippets below to notice the placement of loop variables in list and dictionary comprehensions:

```python
   # LIST COMPREHENSION
   [< expression > for < loop_variable > in < list/dict > if condition]

   # DICTIONARY COMPREHENSION
   {< key >: < value > for < loop_variable > in < list/dict > if condition}
```

## BEFORE BEGINNING

0. Note three things:
   1. In order to pass the grader, assume that all comprehensions must be written in one line
   unless otherwise specified.
   2. You must use the loop variable names that we specify in the instructions in order to pass the grader.
   3. If you are struggling to write any of the comprehensions directly, write the loop in the standard way first and try to get the function to behave in its expected manner. Once you have done that, you can build out the comprehension.

1. Inside of `main()`, call the provided `read_json()` function to read in the `'nyt-articles-star-wars.json'` file provided and assign the return value to a variable named `nyt_star_wars`.

## Problem 01 (80 points)

__Task__: Implement the function named `filter_articles()`. Review the function's docstring regarding its expected behavior, parameters, and return value (if any).

1. To implement this function, you must use the following structure:

    ```python
    [{< key >: < value > for < statement > if condition} for <statement>]
    ```

    __Function requirements and hints__
    1. In `main`, create a list named `keys_to_exclude`. Assign `['abstract', 'web_url', 'snippet', 'lead_paragraph', 'source', 'document_type', 'news_desk', 'type_of_material']` to it.

    2. Go back up to the `filter_articles` function. Write a dictionary comprehension nested within a list comprehension that keeps only the key-value pairs which are not present in the `keys_to_exclude` list. Start by having a list comprehension that loops through `data`. Your loop variable must be `article`. Add in the dictionary comprehension by using the `` method to loop through each article's key-value pair. The loop variables for this must be `k` and `v` respectively. Return this comprehension.

2. After implementing `filter_articles`, return to the `main` function.
    1. Call the function passing it the `nyt_star_wars` list and the `keys_to_exclude` list. Assign the return value back to a variable named `nyt_star_wars_filtered`.

3. Implement the function named `convert_article_value`. Review the function's docstring regarding its expected behavior, parameters, and return value (if any). This question does not involve comprehensions, only a standard nested `for` loop.
    1. Loop through `data`.
    2. Within this loop, write a nested loop that uses the `dict.items()` method to loop through
   each key-value pair.
    3. Create an `if-elif` structure within the inner loop. Check for if the key is equal to `'keywords'` first, and then `'pub_date'`. In the raw data, `'keywords'` maps to a list of dictionaries. You must change the value to be the first element of that list only. The value of `'keywords'` will now be a dictionary.
    4. If the `elif` condition (the key being equal to `'pub_date'`) is `True`, convert the string value of `'pub_date'` to be a `datetime` object using the `strptime()` function. The `datetime.strptime()` function takes the value you wish to convert to a `datetime` object as its first parameter, and you must pass in `'%Y-%m-%dT%H:%M:%S%z'` as the second parameter.
    5. Return `data` outside of the for loop and navigate back to `main`.

4. After implementing `convert_article_value`, navigate to `main` and call `convert_article_value` passing to it `nyt_star_wars_filtered`. Assign the return value back to `nyt_star_wars`.

    :bulb: The first element of your `nyt_star_wars` list __must__ match the dictionary below:

    ```python
    {'headline': {'main': 'Bakery Creates ‘Pan Solo,’ a 6-Foot Replica of ‘Star Wars’ Hero Made of Bread', 'kicker': None, 'content_kicker': None, 'print_headline': 'Crusty ‘Star Wars’ Hero  Receives Fitting Tribute', 'name': None, 'seo': None, 'sub': None}, 'keywords': {'name': 'subject', 'value': 'Bakeries and Baked Products', 'rank': 1, 'major': 'N'}, 'pub_date': datetime.datetime(2022, 10, 15, 13, 0, 7, tzinfo=datetime.timezone.utc), 'section_name': 'U.S.', 'byline': {'original': 'By Michael Levenson', 'person': [{'firstname': 'Michael', 'middlename': None, 'lastname': 'Levenson', 'qualifier': None, 'title': None, 'role': 'reported', 'organization': '', 'rank': 1}], 'organization': None}, 'word_count': 641}
    ```

## Problem 02 (45 points)

__Task__: Implement the function named `count_words_by_year()`. Review the function's docstring regarding its expected behavior, parameters, and return value (if any).

   :exclamation: This function does NOT involve a comprehension.
   :bulb: Note that to access a year from a `datetime` object, you can use `.year`.

1. Implement the function named `count_words_by_year`.

    __Function requirements and hints__

   1. Create an empty dictionary named `word_count_year`.
   2. Loop through `data` using a standard `for` loop.
   3. In the loop, assign the return value of the provided helper function `get_subject_keyword` with an article in `data` passed in as its parameter to a variable named `subject_keyword`.
   4. Check if the `subject_keyword` variable is present in the keys of `word_count_year`.
      1. If it is, check if the article's publication date year is present in the value's keys.
         1. If the year is present, use the plus-equal operator to add the word count to the value that the year maps to. You should be using subscript operator chaining for this.
         2. If the year is not present, assign the word count to the value that the year maps to. You should be using subscript operator chaining for this.
      2. If the `subject_keyword` variable is not present in the keys of `word_count_year`, create the key-value pair in `word_count_year`. The key should be the `subject_keyword` variable and the value should be a dictionary with its key being the publication date year and its value being the word count of the article.
   5. Return `word_count_year`.

2. After implementing `count_words_by_year()`, return to the `main` function. Call the function passing it the list `nyt_star_wars` as an argument. Assign the return value to a variable named `star_wars_word_count`.

Your output must be structured as follows:

```python
{'Bakeries and Baked Products': {2022: 641}, 'The Lord of the Rings (Book)': {2022: 1171}, 'Waititi, Taika': {2022: 2513}, 'Cantwell, Colin (1932-2022)': {2022: 1251}, 'Ladd, Alan Jr': {2022: 1088}, 'Disney, Walt, World (Lake Buena Vista, Fla)': {2022: 1660}, 'Crossword Puzzles': {2022: 1168, 2016: 1412}, 'Television': {2021: 3791, 2020: 1393, 2015: 1100, 2014: 1366}, 'Movies': {2021: 1490, 2020: 839, 2019: 6055, 2018: 2065, 2017: 7371, 2016: 1001, 2015: 9265, 2014: 0, 2013: 1721}, 'Star Wars (Movie)': {2021: 0, 2019: 1505, 2015: 791}, 'Bulloch, Jeremy (1945-2020)': {2020: 579}, 'Jones, James Earl': {2020: 763}, 'Cobb, Ron (1937-2020)': {2020: 885}, 'Lippincott, Charles (1939-2020)': {2020: 516}, 'Walt Disney Company': {2020: 479, 2017: 700, 2015: 1701, 2014: 737}, 'Presidential Election of 2020': {2019: 748}, 'Williams, Billy Dee': {2019: 977}, 'Lucasfilm Ltd': {2019: 432, 2015: 1228}, 'The Mandalorian (TV Program)': {2019: 1126}, 'Real Estate and Housing (Residential)': {2019: 1118}, 'Transportation Security Administration': {2019: 312}, 'AMUSEMENT AND THEME PARKS': {2019: 2264}, 'Mayhew, Peter (1944-2019)': {2019: 590}, 'White House Council of Economic Advisers': {2019: 403}, 'Mollo, John (1931-2017)': {2018: 1232, 2017: 953}, 'Kurtz, Gary (1940-2018)': {2018: 978}, 'Textbooks': {2017: 525}, 'Classical Music': {2017: 822}, 'Virtual Reality (Computers)': {2017: 336}, 'Socks': {2017: 627}, 'Religion and Belief': {2017: 743}, 'Costumes': {2016: 1332}, 'Books and Literature': {2016: 1779, 2015: 1163}, 'Celebrities': {2016: 893}, 'Actors and Actresses': {2016: 816, 2014: 218}, 'Fisher, Carrie': {2016: 1689}, 'Biersdorfer, J D': {2016: 624}, 'Women and Girls': {2016: 1672}, 'Trademarks and Trade Names': {2016: 865}, 'Mandel, David H (1970- )': {2016: 738}, 'Deaths (Obituaries)': {2016: 1475}, 'Sunstein, Cass R': {2016: 1158}, 'Social Media': {2016: 502}, 'Presidential Election of 2016': {2016: 198, 2015: 462}, 'United States Economy': {2016: 968}, 'Lucas, George': {2015: 678, 1997: 993, 1987: 1193, 1985: 256}, 'Fashion and Apparel': {2015: 462, 2014: 175}, 'Star Wars: The Force Awakens (Movie)': {2015: 1299}, 'Mobile Applications': {2015: 885}, 'Hodgman, John': {2015: 146}, 'Travel and Vacations': {2015: 1145}, 'Shopping and Retail': {2015: 892}, 'Computer and Video Games': {2015: 1328}, 'Toys': {2015: 742}, 'AIRLINES AND AIRPLANES': {2015: 552}, 'Windolf, Jim': {2015: 688}, 'London (England)': {2015: 128}, 'Marvel Comics': {2014: 328}, 'Taylor, Gilbert (1914-2013)': {2013: 477}, 'Appointments and Executive Changes': {2013: 515}, 'Blogs and Blogging (Internet)': {2013: 1232}, 'Freeborn, Stuart (1914-2013)': {2013: 839}, 'Tolkien, J R R': {2002: 2079}, 'LUCAS ARTS': {1998: 1043}, 'National Air and Space Museum': {1997: 254}, 'Galoob Toys Inc': {1997: 134}, 'Cantor, Aviva': {1997: 98}, 'Morton, David': {1997: 104}, 'Bromfield, Roger': {1997: 136}, 'Marion, Georgette': {1997: 92}, 'MOTION PICTURES': {1997: 1181, 1985: 597, 1977: 8602}, 'Twentieth Century Fox': {1997: 666}, 'RECORDINGS (AUDIO)': {1996: 223}, 'Disney, Walt, World': {1989: 1306}, 'Reagan, Ronald Wilson': {1985: 266}, 'United States': {1985: 213}, 'UNION OF SOVIET SOCIALIST REPUBLICS': {1985: 838}, 'TWENTIETH CENTURY-FOX FILM CORP.': {1977: 582}, 'ST SIMONS ISLAND (GEORGIA)': {1977: 1236}}
```

## Problem 03 (60 points)

__Task__: Implement the function named `get_avg_word_count`. Review the function's docstring regarding its expected behavior, parameters, and return value (if any).

1. Implement the function named `get_avg_word_count`

    __Function requirements and hints__

   1. Loop through `star_wars_word_count` using the `dict.items()` method. Make sure your loop variables are `k` and `v` respectively. Refer to the docstring for instructions on the rest of the problem.

2. After implementing `get_avg_word_count`, return to the `main` function. Call the function passing it the `star_wars_word_count` dictionary. Assign the return value to a variable named `avg_word_count`.

   :bulb: `avg_word_count` __must__ resemble the dictionary below:

   ```python
   {'Bakeries and Baked Products': 641.0, 'The Lord of the Rings (Book)': 1171.0, 'Waititi, Taika': 2513.0, 'Cantwell, Colin (1932-2022)': 1251.0, 'Ladd, Alan Jr': 1088.0, 'Disney, Walt, World (Lake Buena Vista, Fla)': 1660.0, 'Crossword Puzzles': 1290.0, 'Television': 1912.5, 'Movies': 3311.8888888888887, 'Star Wars (Movie)': 765.3333333333334, 'Bulloch, Jeremy (1945-2020)': 579.0, 'Jones, James Earl': 763.0, 'Cobb, Ron (1937-2020)': 885.0, 'Lippincott, Charles (1939-2020)': 516.0, 'Walt Disney Company': 904.25, 'Presidential Election of 2020': 748.0, 'Williams, Billy Dee': 977.0, 'Lucasfilm Ltd': 830.0, 'The Mandalorian (TV Program)': 1126.0, 'Real Estate and Housing (Residential)': 1118.0, 'Transportation Security Administration': 312.0, 'AMUSEMENT AND THEME PARKS': 2264.0, 'Mayhew, Peter (1944-2019)': 590.0, 'White House Council of Economic Advisers': 403.0, 'Mollo, John (1931-2017)': 1092.5, 'Kurtz, Gary (1940-2018)': 978.0, 'Textbooks': 525.0, 'Classical Music': 822.0, 'Virtual Reality (Computers)': 336.0, 'Socks': 627.0, 'Religion and Belief': 743.0, 'Costumes': 1332.0, 'Books and Literature': 1471.0, 'Celebrities': 893.0, 'Actors and Actresses': 517.0, 'Fisher, Carrie': 1689.0, 'Biersdorfer, J D': 624.0, 'Women and Girls': 1672.0, 'Trademarks and Trade Names': 865.0, 'Mandel, David H (1970- )': 738.0, 'Deaths (Obituaries)': 1475.0, 'Sunstein, Cass R': 1158.0, 'Social Media': 502.0, 'Presidential Election of 2016': 330.0, 'United States Economy': 968.0, 'Lucas, George': 780.0, 'Fashion and Apparel': 318.5, 'Star Wars: The Force Awakens (Movie)': 1299.0, 'Mobile Applications': 885.0, 'Hodgman, John': 146.0, 'Travel and Vacations': 1145.0, 'Shopping and Retail': 892.0, 'Computer and Video Games': 1328.0, 'Toys': 742.0, 'AIRLINES AND AIRPLANES': 552.0, 'Windolf, Jim': 688.0, 'London (England)': 128.0, 'Marvel Comics': 328.0, 'Taylor, Gilbert (1914-2013)': 477.0, 'Appointments and Executive Changes': 515.0, 'Blogs and Blogging (Internet)': 1232.0, 'Freeborn, Stuart (1914-2013)': 839.0, 'Tolkien, J R R': 2079.0, 'LUCAS ARTS': 1043.0, 'National Air and Space Museum': 254.0, 'Galoob Toys Inc': 134.0, 'Cantor, Aviva': 98.0, 'Morton, David': 104.0, 'Bromfield, Roger': 136.0, 'Marion, Georgette': 92.0, 'MOTION PICTURES': 3460.0, 'Twentieth Century Fox': 666.0, 'RECORDINGS (AUDIO)': 223.0, 'Disney, Walt, World': 1306.0, 'Reagan, Ronald Wilson': 266.0, 'United States': 213.0, 'UNION OF SOVIET SOCIALIST REPUBLICS': 838.0, 'TWENTIETH CENTURY-FOX FILM CORP.': 582.0, 'ST SIMONS ISLAND (GEORGIA)': 1236.0}
   ```
3. Now, still in `main`, write a dictionary comprehension that returns the key-value pair of the subject with the maximum value in this dictionary. Loop through `avg_word_count` using the `dict.items()` method. Ensure your loop variables are `k` and `v` respectively. If the value you are looping over has the same value of the maximum of the `.values()` of `avg_word_count`, then add this key-value pair to the dictionary. Assign the dictionary comprehension to a variable named `highest_avg`. `highest_avg` must have the following value:

   ```python
   {'MOTION PICTURES': 3460.0}
   ```
   :bulb: You can use the built-in function `max()` to find the maximum value of a sequence.

## Problem 04 (50 points)

__Task__: Implement two functions named `check_for_character_in_headline` and `star_wars_character_count`. Review the functions' docstrings regarding their expected behaviors, parameters, and return values (if any).

1. Implement the function named `check_for_character_in_headline`

    __Function requirements and hints__

    1. Loop through the return value of calling  `.split()` on the characters name.
    2. Within the loop, check if each part of the character's name is present in the main headline of the article and return `True` if it is, and `False` if it is not. Note that you must do a case-insensitive check.

2. Implement the function named `star_wars_character_count`.

    __Function requirements and hints__

    1. In `main`, create a list named `star_wars_characters` and assign to it the value `['Luke Skywalker', 'Darth Vader', 'Yoda', 'Leia Organa', 'Owen Lars', 'Han Solo', 'Obi Wan Kenobi']`. Create a dictionary named `character_count` and assign to it the value `{'Luke Skywalker': 0, 'Darth Vader': 0, 'Yoda': 0, 'Leia Organa': 0, 'Owen Lars': 0, 'Han Solo': 0, 'Obi Wan Kenobi': 0}`.
    2. Navigate back to the `star_wars_character_count` function. Write a dictionary comprehension to *update* `character_count` by adding 1 to the relevant value when a character's name or part of a character's name is found in the headline of the article.

        :bulb: If you are struggling to write this dictionary comprehension directly, write the nested for loop first and try building it out based on the structure you have.

        1. Loop through `data`. Your loop variable must be named `article`.
        2. Within this loop, implement a nested loop by looping over `characters`. Your loop variable must be named `character`.
        3. Within this loop, check if the `check_for_character_in_headline` function passed the relevant parameters is `True`.
         :bulb: Review the `check_for_character_in_headline` function's docstring to know what your parameters for this function in the comprehension should be.
        4. If `True`, use the correct dictionary method to *update* `character_count` by adding one to the value of the character that was found.

3. After implementing `star_wars_character_count`, return to the `main` function. Call the function passing to it the arguments `nyt_star_wars`, `star_wars_characters`, and `character_count`. Assign the return value to a variable named `characters`. `characters` must look like the following:

    ```python
        {'Luke Skywalker': 2, 'Darth Vader': 2, 'Yoda': 2, 'Leia Organa': 1, 'Owen Lars': 1, 'Han Solo': 5, 'Obi Wan Kenobi': 2}
    ```

## Problem 05 (65 points)

__Task__: Implement two functions named `get_author_name` and `section_authors`. Review the functions' docstrings regarding their expected behaviors, parameters, and return values (if any).

1. Implement the function named `get_author_name`. Refer to the docstring for instructions.

2. Implement the function named `section_authors`.

    __Function requirements and hints__
    1. To implement this function, you must use a list comprehension in order to create a list of dictionaries to return. This function is limited to a single line of code that comprises the return statement.
    2. First, loop through `data`. The loop variable of `data` must be `article`.
    3. Then check if `get_author_name` returns anything for each article.
    4. If `True`, create a dictionary literal with the `section_name` of the article as its key and the value being the return value of `get_author_name`. *Enclose this return value in a list.*

3. After implementing `section_authors`, return to `main`.

    1. Call `section_authors`, passing to it the `nyt_star_wars` list of dictionaries. Assign the return value to a variable named `authors`.
    2. Create an empty dictionary called `authors_merged`.
    3. Loop through `authors` using a loop variable `author`. Within this loop, loop through the key-value pairs of `author` using the `dict.items()` method. If the key you are currently looping over is in the keys of `authors_merged` already, *extend* the list value of this key in `authors_merged` with the value you are currently looping over. If this key is not in `authors_merged` already, create the key in `authors_merged` and assign the corresponding value to it.

    `authors_merged` _must_ match the following data structure:
    ```python
    {'U.S.': ['Michael Levenson', 'Mariel Padilla', 'Kwame Opam', 'Niraj Chokshi', 'Jim Tankersley', 'Christopher Mele', 'Matt Flegenheimer', 'Amy Chozick', 'James Clarity'], 'Movies': ['Dave Itzkoff', 'Richard Sandomir', 'Neil Genzlinger', 'Ian Philbrick', 'Michael Levenson', 'Kwame Opam', 'Alex Marshall', 'Jacey Fortin', 'Daniel Slotnik', 'Stephanie Goodman', 'Maya Salam', 'Maya Salam', 'Mariel Padilla', 'Scott Tobias', 'Jason Bailey', 'Sopan Deb', 'John Koblin', 'Sopan Deb', 'Dave Itzkoff', 'Cara Buckley', 'Justin Bank', 'Christopher Mele', 'Amanda Hess', 'Liam Stack', 'Ainara TIEFENTHÄLER', 'Dave Itzkoff', 'Christopher Mele', 'Amanda Hess', 'Neil Genzlinger', 'Cara Buckley', 'Dave Itzkoff', 'Liam Stack', 'Mary Murphy', 'Sewell Chan', 'Katie Rogers', 'Michael Wilson', 'Neil Genzlinger', 'Stephanie Goodman', 'Manohla Dargis', 'A. Scott', 'Cara BUCKLEY', 'Dave Itzkoff', 'Douglas Martin', 'A. Scott', 'Janet Maslin', 'Bernard Weinraub', 'Neil Strauss', 'Aljean Harmetz', 'Aljean Harmetz'], 'Business Day': ['Brooks Barnes', 'Derrick Taylor', 'Brooks Barnes', 'Derrick Taylor', 'Brooks Barnes', 'Brooks Barnes', 'Brooks Barnes', 'Erin McCann', 'Liam Stack', 'Brooks Barnes', 'Brooks Barnes', 'Rachel ABRAMS', 'Rachel Abrams', 'Brooks Barnes', 'Brooks Barnes', 'Brooks Barnes', 'Brooks Barnes', 'Brooks Barnes', 'Brooks Barnes', 'Brooks Barnes', 'Brooks Barnes', 'Brooks Barnes', 'Dow Jones', 'Stacy Lu'], 'Crosswords & Games': ['Caitlin Lovinger', 'Deb Amlen', 'Deb Amlen'], 'Arts': ['Mike Hale', 'Dave Itzkoff', 'Robert Ito', 'Dave Itzkoff', 'Thomas Vinciguerra', 'Daniel Victor', 'Joshua Barone', 'A. Scott', 'Daniel Slotnik', 'Neil Genzlinger', 'Brooks Barnes', 'Daniel Slotnik'], 'Opinion': ['Ben Proudfoot', 'Ben Proudfoot', 'Annalee Newitz', 'Tim Kreider', 'Lawrence Downes', 'Zachary Feinstein', 'David Brooks'], 'Real Estate': ['Ronda Kaysen'], 'Travel': ['Brooks Barnes', 'Lucinda Hahn', 'Elaine Glusac', 'Elaine Glusac', 'Katherine House'], 'Obituaries': ['Jacey Fortin', 'Daniel Slotnik', 'Daniel Slotnik'], 'World': ['Ben Hubbard', 'Liam Stack'], 'Fashion & Style': ['Vanessa Friedman', 'George Gustines', 'Katherine Rosman', 'Vanessa Friedman', 'Jim Windolf'], 'Books': ['Alexandra Alter', 'A. Scott', 'Ethan Gilsdorf', 'Dana Jennings'], 'NYT Now': ['Adeel Hassan'], 'Technology': ['Kit Eaton', 'J. Herz'], 'Magazine': ['John Hodgman'], 'T Magazine': ['Ben Barna', 'Malina Gilchrist'], 'New York': ['David Dunlap'], 'Archives': ['Russell Baker', 'Ben Bova', 'Anna Quindlen', 'Vincent Canby', 'Aljean Harmetz', 'Robert Metz', 'Aliean Harmetz', 'Wayne Special', 'Vincent Canby']}
    ```

4. Call the provided `write_json()` function and pass to it using positional arguments a filepath name of `stu_authors.json` and the `authors_merged` data you have just created.