# SI 506 Last assignment

## 1.0 Dates

* Available: Thursday, 08 December 2022, 4:00 PM Eastern
* Due: on or before Monday, 19 December 2022, 11:59 PM Eastern

:exclamation: No late submissions will be accepted for scoring.

<br />

## 2.0 Overview

The last assignment is open network, open readings, and open notes. You may refer to
code in previous lecture exercises, lab exercises, and problem sets for inspiration. See the
`last_assignment_overview.pdf` document for more details regarding this assignment.

<br />

## 3.0 Points

The last assignment is worth __1800__ points and you accumulate points by passing a series of
autograder tests. In addition, the assignment includes a __bonus__ sub-task worth an additional
__90__ points.

<br />

## 4.0 Solo effort

Please abide by the following rules:

1. The last assignment that you submit __must constitute your own work__. You are
   __prohibited from soliciting assistance or accepting assistance__ from any person while
   working to complete the programming assignment. This includes but is not limited to individual
   classmates, study group members, and tutors.

   * :exclamation: If you have formed or participated in an SI 506 study group please
     __suspend all study group activities__ for the duration of the midterm assignment.

   * :exclamation: If you work with a tutor please __suspend contact__ with the tutor for the
     duration of the assignment.

2. Likewise, you are __prohibited from assisting any other student__ who is required to complete
   this assignment. This includes students attempting the assignment during the regular exam period,
   as well as those who may attempt the assignment at another time and/or place due to scheduling
   conflicts or other issues.

3. Direct all __questions__ regarding the assignment to the Slack SI 506 workspace `# last_assignment`
   channel. Do not post code snippets. If you encounter an issue with your code you may request a
   code review by members of Team 506 via a private direct message (DM).

<br />

## 5.0 Files

In line with the weekly lab exercises and problem sets you will be provided with a number of
files:

1. `README.md`: assignment instructions
2. `last_assignment.py`: script including a `main()` function and other definitions and statements
3. `five_oh_six.py`: module containing utility functions and constants
4. `data-clone_wars_episodes.csv`: data file
5. `data-nyt_star_wars_articles.json`: data file
6. `data-wookieepedia_droids.json`: data file
7. `data-wookieepedia_people.json`: data file
8. `data-wookieepedia_planets.csv`: data file
9. `data-wookieepedia_starships.csv`: data file
10. One or more `fxt_*.json` test fixture files that you must match with the files you produce

Please download the assignment files from Canvas Files as soon as they are released. This is a timed
event and delays in acquiring the assignment files will shorten the time available to engage with
the challenges. The clock is not your friend.

:exclamation: _DO NOT_ modify or remove the scaffolded code that we provide in the Python script or
module files unless instructed to do so.

<br />

## 5.1 Module imports

The template file `last_assignment.py` includes a single `import` statement:

```python
import copy
import five_oh_six as utl
```

The utilities module `five_oh_six.py` includes the following `import` statements:

```python
import csv
import json
import requests

from urllib.parse import quote, urlencode, urljoin
```

:exclamation: __Do not__ comment out or remove these `import` statements. That said, check your
`import` statements periodically. If you discover that other `import` statements have been added to
your Python files remove them. In such cases, VS Code is attempting to assist you by inserting
additional `import` statements based on your keystrokes. Their presence can trigger
`ModuleNotFoundError` runtime exceptions when you submit your code to Gradescope.

<br />

## 5.2 Caching

As discussed in class, this assignment utilizes a caching workflow that eliminates
redundant HTTP GET requests made to SWAPI by storing the SWAPI responses locally. Caching is
implemented _fully_ and all you need do is call the function `get_swapi_resource()` whenever you
need to retrieve a SWAPI representation of a person/droid, planet, species, or starship, either
locally from the cache or remotely from SWAPI. The cache dictionary is serialized as JSON and
written to `CACHE.json` every time you run `last_assignment.py`.

:exclamation: _Do not_ call the function named `utl.get_resource` directly. Doing so sidesteps the
cache and undercuts the caching optimization strategy.

<br />

## 6.0 Data

The Star Wars saga has spawned films, animated series, books, music, artwork, toys, games, fandom
websites, cosplayers, scientific names for new organisms (e.g.,
[_Trigonopterus yoda_](https://en.wikipedia.org/wiki/Trigonopterus_yoda)), and even a Darth Vader
_grotesque_ attached to the
[northwest tower](https://en.wikipedia.org/wiki/Darth_Vader_grotesque#/media/File:Darth_vader_grotesque.jpg)
of the Washington National Cathedral. Leading US news sources such as the
[New York Times](https://www.nytimes.com/) cover the Star Wars phenomenon on a regular basis.

The last assignment adds yet another Star Wars-inspired artifact to the list. The data used in this
assignment is sourced from the [Star Wars API](https://swapi.py4e.com/) (SWAPI),
[Wookieepedia](https://starwars.fandom.com/wiki/Main_Page),
[Wikipedia](https://www.wikipedia.org/), and the [New York Times](https://www.nytimes.com/spotlight/star-wars).

<br />

## 7.0 Debugging

As you write your code take advantage of the built-in `print` function, VS code's debugger, and VS
Codes file comparison feature to check your work and debug your code. See the
`last_assignment_overview.pdf` for additional details and instructions.

<br />

## 8.0 Gradescope submissions

You may submit your solution to Gradescope as many times as needed before the expiration of
the exam time. Your __final__ submission will constitute your exam submission.

:exclamation: You _must_ submit your solution file to _Gradescope_ before the expiration of exam
time. Solution files submitted to the teaching team after the expiration of exam time will receive
a score of zero (0).

If you are unable to earn full points on the assignment the teaching team will grade your submission
__manually__. Partial credit __may__ be awarded for submissions that fail one or more autograder
tests if the teaching team (at their sole discretion) deem a score adjustment warranted.

If you submit a partial solution, feel free to include comments (if you have time) that explain
what you were attempting to accomplish in the area(s) of the program that are not working properly.
We will review your comments when determining partial credit.

<br />

## 9.0 Challenges

A long time ago in a galaxy far, far away, there occured the Clone Wars (22-19 BBY), a major
conflict that pitted the [Galatic Republic](https://starwars.fandom.com/wiki/Galactic_Republic)
against the breakaway
[Separatist Alliance](https://starwars.fandom.com/wiki/Confederacy_of_Independent_Systems). The
Republic fielded genetically modified human clone troopers commanded by members of the Jedi order
against Separatist battle droids. The struggle was waged across the galaxy and, in time, inspired an
animated television series entitled
[_Star Wars: The Clone Wars_](https://starwars.fandom.com/wiki/Star_Wars:_The_Clone_Wars) which
debuted in October 2008 and ran for seven seasons (2008-2014, 2020).

__Challenge 01__ implement a number of `utl.convert_to_*` functions employing `try` and `except`
blocks that will be employed in later challenges.

__Challenges 02-05__ utilize a _Clone Wars_ data set that provides summary data about the
first two seasons of the animated series. You will implement a number of functions that will
simplify interacting with the data in order to surface basic information about the episodes and
their directors, writers, and viewership.

__Challenges 06-08__ work with New York Times article data (1977-2022) that charts the creative,
cultural, and economic impact of the _Star Wars_ saga both within the US and elsewhere over the past
forty-five years.

__Challenges 09-20__ recreates the escape of the light freighter
[_Twilight_](https://starwars.fandom.com/wiki/Twilight) from the sabotaged and doomed Separatist
heavy cruiser [_Malevolence_](https://starwars.fandom.com/wiki/Malevolence) which took place
during the first year of the conflict (22 BBY). Your task is to reassemble the crew of the
_Twilight_ and take on passengers before disengaging from the _Malevolence_ and heading into deep
space. The Jedi generals [Anakin Skywalker](https://starwars.fandom.com/wiki/Anakin_Skywalker) and
[Obi-Wan Kenobi](https://starwars.fandom.com/wiki/Obi-Wan_Kenobi) together with the astromech droid
(robot) [R2-D2](https://starwars.fandom.com/wiki/R2-D2) had earlier boarded the _Malevolence_
after maneuvering the much smaller _Twilight_ up against the heavy cruiser and
docking via an emergency air lock. Their mission was twofold:

   1. Retrieve the Republican Senator
      [Padmé Amidala](https://starwars.fandom.com/wiki/Padm%C3%A9_Amidala) and the protocol
      (communications) droid [C-3PO](https://starwars.fandom.com/wiki/C-3PO) whose ship had been
      seized after being caught in the _Malevolence's_ tractor beam, and
   2. Sabotage the warship.

In these challenges you will implement functions and follow a workflow that generates a JSON
document that recreates the _Twilight's_ escape from the _Malevolence_.

:bulb: The workflow outlined below illustrates the general creational pattern applied to each droid,
person, planet, species, and starship encountered in the challenges.

__Workflow__

1. Retrieve SWAPI representation of the entity if one exists.
2. Update SWAPI entity with Wookieepedia data if provided.
3. Return a new dictionary with values found in `util.NONE_VALUES` converted to `None`.
4. Return a "thinned" version of the new dictionary that retains a subset of the original
   SWAPI/Wookieepedia key-value pairs, substituting in new keys and converting certain values to
   more appropriate types.
5. Write to file (i.e., check your work)

:exclamation: The SWAPI entity will serve as the default representation of the entities that feature
in the assignment. The Wookieepedia data will be used to enrich the SWAPI data with new and updated
key-value pairs.

__May the Force be with You.__

<br />

## 9.1 Challenge 01 (180 points)

__Task__: Implement the functions `utl.convert_to_none()`, `utl.convert_to_int()`,
`utl.convert_to_float()`, and `utl.convert_to_list()`. Each function attempts to convert a passed
in `value` to a more appropriate type.

<br />

## 9.1.1 Implement `utl.convert_to_none()`

Replace `pass` with a code block that attempts to convert the passed in `value` to `None`. Review
the function's docstring to better understand the task it is to perform, the parameters it defines,
and the return value it computes.

### Requirements

1. Employ `try` and `except` statements in order to handle runtime exceptions whenever an invalid
   conversion is attempted. __Do not__ place code outside the `try` and `except` code blocks.

2. In the `try` block check if the passed in `value` can be found in `utl.NONE_VALUES`
   (perform a __case insensitive__ membership check). If a match is obtained return `None` to the
   caller; otherwise, return the `value` unchanged.

   :exclamation: Don't assume that `value` is "clean"; program defensively and remove
   leading/trailing spaces before checking if the "cleaned" version of the string matches a
   `utl.NONE_VALUES` item.

3. If a runtime exception is encountered "catch" the exception in the `except` block and return the
   `value` to the caller __unchanged__.

   :bulb: You do not need to specify specific exceptions in the `except` statement.

<br />

## 9.1.2 Test `utl.convert_to_none()`

After implementing the function return to `main()`.

1. Uncomment the relevant `assert` statements and test the function.

2. If an `AssertionError` is raised, debug your code, and then retest. Repeat as necessary.

<br />

## 9.1.3 Implement `utl.convert_to_float()`

Replace `pass` with a code block that attempts to convert the passed in `value` to a `float`.
Review the function's docstring to better understand the task it is to perform, the parameters it
defines, and the return value it computes.

### Requirements

1. Employ `try` and `except` statements in order to handle runtime exceptions whenever an invalid
   conversion is attempted. __Do not__ place code outside the `try` and `except` code blocks.

2. If a runtime exception is encountered "catch" the exception in the `except` block and return the
   `value` to the caller __unchanged__.

   :bulb: You do not need to specify specific exceptions in the `except` statement.


## 9.1.4 Test `utl.convert_to_float()`

After implementing the function return to `main()`.

1. Uncomment the relevant `assert` statements and test the function.

2. If an `AssertionError` is raised, debug your code, and then retest. Repeat as necessary.

<br />

## 9.1.5 Implement `utl.convert_to_int()`

Replace `pass` with a code block that attempts to convert the passed in `value` to an `int`. Review
the function's docstring to better understand the task it is to perform, the parameters it defines,
and the return value it computes.

### Requirements

1. Employ `try` and `except` statements in order to handle runtime exceptions whenever an invalid
   conversion is attempted. __Do not__ place code outside the `try` and `except` code blocks.

2. The function _must_ convert numbers masquerading as strings, incuding those with commas that
   represent a thousand separator (e.g., '500,000,000') and those with a period that designates a
   fractional component (e.g., '500,000,000.9999').

3. If a runtime exception is encountered "catch" the exception in the `except` block and return the
   `value` to the caller __unchanged__.

   :bulb: You do not need to specify specific exceptions in the `except` statement.

<br />

## 9.1.6 Test `utl.convert_to_int()`

After implementing the function return to `main()`.

1. Uncomment the relevant `assert` statements and test the function.

2. If an `AssertionError` is raised, debug your code, and then retest. Repeat as necessary.

<br />

## 9.1.7 Implement `utl.convert_to_list()`

Replace `pass` with a code block that attempts to convert the passed in `value` to a `list` using a
`delimiter` if one is provided. Review the function's docstring to better understand the task it is
to perform, the parameters it defines, and the return value it computes.

### Requirements

1. Employ `try` and `except` statements in order to handle runtime exceptions whenever an invalid
   conversion is attempted. __Do not__ place code outside the `try` and `except` code blocks.

2. If the caller provides a `delimiter` value the function _must_ use it to split the `value`;
   otherwise, split the string without specifying a delimiter value.

   :bulb: Let the truth value of `delimiter` determine how you choose to split the string.

   :exclamation: Don't assume that `value` is "clean"; program defensively and remove
   leading/trailing spaces before attempting to convert the string to a list.

3. If a runtime exception is encountered "catch" the exception in the `except` block and return the
   `value` to the caller __unchanged__.

   :bulb: You do not need to specify specific exceptions in the `except` statement.

<br />

## 9.1.8 Test `utl.convert_to_list()`

After implementing the function return to `main()`.

1. Uncomment the relevant `assert` statements and test the function.

2. If an `AssertionError` is raised, debug your code, and then retest. Repeat as necessary.

<br />

## 9.2 Challenge 02 (80 points)

__Task__: Refactor (e.g., modify) the function `utl.read_csv_to_dicts()` to use a
__list comprehension__ and then call the function to read a CSV file that contains information about
the first two seasons of _Clone Wars_ episodes. Then implement the function `has_viewer_data()` that
checks whether or not an episode possesses viewership information.

:bulb: This challenge involves a list of nested dictionaries. Use the built-in function `print()` to
explore one of nested dictionaries or call the function `utl.write_json()` in `main()`, encode the
data as JSON, and write it to a "test" JSON file so that you can view the list of dictionaries more
easily.

<br />

## 9.2.1 Refactor `utl.read_csv_to_dicts()`

Examine the commented out code in `utl.read_csv_to_dicts()` function (__do not__ uncomment).
Reimplement the function by writing code in the `with` block that retrieves an instance of
`csv.DictReader` and then employs a list comprehension to traverse the lines in the reader object
and return a new list of line elements to the caller.

:exclamation: Review lecture notes and code solution files if you have forgotten how to write a list
comprehension. If you are unsuccessful in your endeavors uncomment the code in
`utl.read_csv_to_dicts()` and get the function working so that you can continue with the assignment.

### Requirements

1. You are limited to writing two (2) lines of code.

   1. Line 01 assigns an instance of `csv.DictReader` to a variable named `reader`.
   2. Line 02 returns a new list of `reader` "line" elements to the caller using
      __a list comprehension__.

2. You _must_ employ existing variable names that appear in the commented out code when writing
   your list comprehension.

<br />

## 9.2.2 Test `utl.read_csv_to_dicts()`

After refactoring `utl.read_csv_to_dicts()` return to `main()`.

1. Call the function and retrieve the data contained in the file `data-clone_wars_episodes.csv`.

2. Assign the return value to a variable named `clone_wars_episodes`.

<br />

## 9.2.3 Implement `has_viewer_data()`

Replace `pass` with a code block that checks whether or not an individual _Clone Wars_ episode
possesses viewership information. Review the function's docstring to better understand the task it
is to perform, the parameters it defines, and the return value it computes.

### Requirements

1. The function _must_ compute the truth value of the passed in episode's "episode_us_viewers_mm"
   key-value pair, returning either `True` or `False` to the caller.

   :bulb: Recall that a function can include more than one `return` statement. That said, you can
   also employ Python's ternary operator to solve this challenge with a single line of code.

<br />

## 9.2.4 Call `has_viewer_data()`

After implementing the function return to `main()`.

1. Test your implementation of `has_viewer_data()` by counting the number of episodes in the
   `clone_wars_episodes` list that possess a "episode_us_viewers_mm" numeric value. Whenever the
   return value of `has_viewer_data()` equals `True` increment your episode count by 1.

   :bulb: Recall that a function call is considered an expression and `if` statements are composed
   of one or more expressions.

2. The number of episodes that possess an "episode_us_viewers_mm" viewership value equals
   twenty-five (`25`). If your loop does not accumulate this total, recheck both your implementation
   of `has_viewer_data()` and your `for` loop and loop block `if` statement.

<br />

## 9.3 Challenge 03 (100 points)

__Task__: Implement a function that converts _Clone Wars_ episode string values to more appropriate
types.

<br />

## 9.3.1 Implement `convert_episode_values()`

Replace `pass` with a code block that converts specifed string values to more appropriate types.
Review the function's docstring to better understand the task it is to perform, the parameters it
defines, and the return value it computes.

### Requirements

1. The function accepts a list of nested "episode" dictionaries and you _must_ implement a nested
   loop to perform the value type conversions.

   * Outer loop: passed in `episodes` list of nested dictionaries
   * Inner loop: individual "episode" dictionary items

2. You will need to employ multiple conditional statements to convert the values encountered to more
   appropriate types.

3. The function _must_ also check the truth value of each nested episode dictionary value. Do this
   first. Negate the expression in the `if` statement to handle a value whose truth value evaluates
   to `False`. This will allow you to map (i.e., assign) `None` to the associated key in an
   efficient manner.

4. Otherwise, add additional conditional statements that allow you to target particular key-value
   pairs for value conversion. Use the appropriate `utl.convert_to_*()` function to convert values
   that satisfy a particular condition.

5. After the outer loop terminates return the list of mutated dictionaries to the caller.

<br />

## 9.3.2 Call `convert_episode_values()`

After implementing the function, return to `main()`.

1. Call the function passing the `clone_wars_episodes` list as the argument.

2. Assign the return value to `clone_wars_episodes`.

3. Call the function `utl.write_json()` and write `clone_wars_episodes` to the file
   `stu-clone_wars-episodes_converted.json`. Compare your file to the test fixture file
   `fxt-clone_wars-episodes_converted.json`. Both files _must_ match, line-for-line, and
   character-for-character.

<br />

## 9.4 Challenge 04 (85 points)

__Task__: Implement a function that retrieves the most viewed episode(s) of the first two seasons of _The Clone Wars_.

<br />

## 9.4.1 Implement `get_most_viewed_episode()`

Replace `pass` with a code block that finds the most viewed _Clone Wars_ episode(s) in the data
set. Review the function's docstring to better understand the task it is to perform, the parameters
it defines, and the return value it computes.

### Requirements

1. The function _must_ return a list of one or more episodes from the passed in `episodes` list
   with the highest recorded viewership. Include in the list only those episodes that tie for
   the highest recorded viewership. If no ties exist only one episode will be returned in the
   list. Ignores episodes with no viewership value.

2. Delegate to `has_viewer_data()` the task of checking whether an episode contains a _truthy_
   "episode_us_viewers_mm" value. You need to check the truth value of "episode_us_viewers_mm"
   before you attempt to compare the current "episode_us_viewers_mm" value to the previous value.

   :bulb: Assign two local "accumulator" variables to the viewer count and the top episode(s).

<br />

## 9.4.2 Call `get_most_viewed_episode()`

After implementing the function return to `main()`.

1. Call the function and pass `clone_wars_episodes` to it as the argument.

2. Assign the return value to `most_viewed_episode`. If the list contains the following elements
   proceed to the next challenge; if not, recheck your code.

   ```python
   [
      {
         'series_title': 'Star Wars: The Clone Wars',
         'series_season_num': 1,
         'series_episode_num': 2,
         'season_episode_num': 2,
         'episode_title': 'Rising Malevolence',
         'episode_director': 'Dave Filoni',
         'episode_writers': ['Steven Melching'],
         'episode_release_date': 'October 3, 2008',
         'episode_prod_code': 1.07,
         'episode_us_viewers_mm': 4.92
         },
      {
         'series_title': 'Star Wars: The Clone Wars',
         'series_season_num': 2, 'series_episode_num': 45,
         'season_episode_num': 23,
         'episode_title': 'Test Record',
         'episode_director': 'Anthony Whyte',
         'episode_writers': ['Anthony Whyte', 'Chris Teplovs'],
         'episode_release_date': 'May 7, 2010',
         'episode_prod_code': 2.22,
         'episode_us_viewers_mm': 4.92
      }
   ]
   ```

<br />

## 9.5 Challenge 05 (90 points)

__Task__: Construct a dictionary of directors and a count of the number of episodes each directed
during the first two seasons of _The Clone Wars_ sorted by episode count (descending) and the director name (ascending).

<br />

## 9.5.1 Implement `count_episodes_by_director()`

Replace `pass` with a code block that returns a dictionary of key-value pairs that associate each
director in the `episodes` list of nested dictionaries with a count of the episodes that they are
credited with directing. Review the function's docstring to better understand the task it is to
perform, the parameters it defines, and the return value it computes.

### Requirements

1. The function _must_ accumulates episode counts for each director listed in the `eposides` list.

2. The director's name comprises the key and the associated value a count of the number of episodes
   they directed. Implement conditional logic to ensure that each director is assigned a key and the
   episode counts are properly tabulated and assigned as the value.

   ```python
   {
      < director_name_01 >: < episode_count >,
      < director_name_02 >: < episode_count >,
      ...
   }
   ```

<br />

## 9.5.2 Call `count_episodes_by_director()`

After implementing function return to `main()`.

1. Call the function and pass `clone_wars_episodes` to it as the argument.

2. Assign the return value to `director_episode_counts`.

3. __Uncomment__ the dictionary comprehension that employs the built-in function `sorted()`
   and a `lambda` function to sort the episode counts by the count (descending) and the director's
   last name.

   ```python
   # BONUS: Sort by count (descending), last name (ascending)
    director_episode_counts = {
        director: count
        for director, count
        in sorted(director_episode_counts.items(), key=lambda x: (-x[1], x[0].split()[-1]))
        }
   ```

4. Call the function `utl.write_json()` and write the _sorted_ `director_episode_counts` to the file
   `stu-clone_wars-director_episode_counts.json`. Compare your file to the test fixture file
   `fxt-clone_wars-director_episode_counts.json`. Both files _must_ match, line-for-line, and
   character-for-character.

<br />

## 9.6 Challenge 06 (85 points)

__Task__: Implement the function `get_nyt_news_desks()`.

<br />

## 9.6.1 Implement `get_nyt_news_desks()`

Replace `pass` with a code block that returns a list of New York Times "news desks" sourced from the
passed in `articles` list. Review the function's docstring to better understand the task it is to
perform, the parameters it defines, and the return value it computes.

:bulb: Each article dictionary contains a "news_desk" key-value pair.

### Requirements

1. The list of news desk names returned by the function _must not_ contain any duplicate elements.
   Accumulate the values carefully.

2. The function must delegate to the function `utl.convert_to_none` the task of converting
   "news_desk" values that equal "None" (a string) to `None`. Only news_desk values that are
   "truthy" (i.e., not None) are to be returned in the list.

   :bulb: There are eight (8) articles with a "news_desk" value of "None". Exclude this
   value from the list by passing each "news_desk" value to `utl.convert_to_none` and assigning
   the return value to a local variable. You can filter out the `None` values with a truth value
   test.

<br />

## 9.6.2 Call `get_nyt_news_desks()`

After implementing the function return to `main()`.

1. Call the function `utl.read_json()` and retrieve the New York Times article data in the file
   `./data-nyt_star_wars_articles.json`.

2. Assign the return value to `articles`.

3. Test your implementation of `get_nyt_news_desks()` by calling the function and passing to it the
   argument `articles`. Assign the return value to the variable `news_desks`.

4. Call the function `utl.write_json()` and write `news_desks` to the file `stu-nyt_news_desks.json`.
   Compare your file to the test fixture file`fxt-nyt_news_desks.json`. The files _must_ match line
   for line, indent for indent, and character for character.

<br />

## 9.7 Challenge 07 (100 points)

__Task__: Implement the function `group_nyt_articles_by_news_desk()`.

<br />

## 9.7.1 Implement `group_nyt_articles_by_news_desk()`

Replace `pass` with a code block that returns a dictionary of "news desk" key-value pairs that
group the passed in `articles` by their parent news desk drawn from the `news_desks` list. Review
the function's docstring to better understand the task it is to perform, the parameters it defines,
and the return value it computes.

### Requirements

1. Implement a nested loop. Review the `data-nyt_star_wars_articles.json` and `stu-nyt_news_desks.json`
   files and decide which list should be traversed by the outer loop and which list should be
   traversed by the inner loop.

   :bulb: The news desk name provides the link between the two lists.

2. Assign an empty list to a local variable. You will accumulate article dictionaries in this list
   and then assign the list to its "parent" news desk key. There are three locations in the function
   block where this initial variable assignment could be placed: outside the loops, inside the outer
   loop, or inside the inner loop. Choose wisely.

3. Each article dictionary added to its parent news desk list represents a "thinned" version of the
   original. The keys to employ and their order is illustrated by the example below:

   ```python
   {
      "web_url": "https://www.nytimes.com/2016/10/20/business/media/lucasfilm-sues-jedi-classes.html",
      "headline_main": "Classes for Jedis Run Afoul of the Lucasfilm Empire",
      "news_desk": "Business",
      "byline_original": "By Erin McCann",
      "document_type": "article",
      "material_type": "News",
      "abstract": "A man whose businesses offers private lessons and certifications for fine-tuning lightsaber skills is operating without the permission of the “Star Wars” owner.",
      "word_count": 865,
      "pub_date": "2016-10-19T13:26:21+0000"
   }
   ```

   :exclamation: Certain keys such as "headline_main", "byline_original", and "material_type" are
   not found in the original New York Times dictionaries. Hopefully, the names provide a sufficient
   hint about which values to map (i.e., assign) to each.

<br />

## 9.7.2 Call `group_nyt_articles_by_news_desk()`

After implementing the function return to `main()`.

1. Call the function and pass it `news_desks` and `articles` as arguments. Assign the return value
   to the variable `news_desk_articles`.

2. Call the function `utl.write_json()` and write `news_desk_articles` to the file
   `stu-nyt_news_desk_articles.json`. Compare your file to the test fixture file
   `fxt-nyt_news_desk_articles.json`. The files _must_ match line for line, indent for indent, and character for character.

<br />

## 9.8 Challenge 08 (90 points)

__Task__ Implement the function `calculate_articles_mean_word_count()`.

<br />

## 9.8.1 `calculate_articles_mean_word_count()` function

Replace `pass` with a code block that returns the mean (e.g., average) word count of the passed in
list of `articles` less any articles with a word count of zero (0). Review the function's docstring
to better understand the task it is to perform, the parameters it defines, and the return value it
computes.

__mean__: central value of a set of values that is determined by calculating
_the sum of the values divided by the number of values_.

__Requirements__

1. The function _must_ calculate the mean word count of the passed in articles __excluding__ from
   the calculation all articles with a "word_count" value of zero (`0`) or `None`.

2. The function _must_ maintain a count of the number of articles evaluated and a count of the
   total words accumulated from each article's "word_count" value. Assign the running counts to
   two local "accumulator" variables.

3. The function _must_ check the truth value of each article's "word_count" before attempting to
    increment the article count and total words count. If the truth vallue of the "word_count" is
    `False` the article is excluded from the count.

4. You _must_ __round__ the mean value to the second (2nd) decimal place before returning the value
   to the caller.

<br />

## 9.8.2 Call `calculate_articles_mean_word_count()`

After implementing the function return to `main()`.

1. Create an empty dictionary named `mean_word_counts`. You will use it to accumulate mean words
   counts.

2. Loop over the `news_desk_articles` key-value pairs. Write a conditional statement inside the loop
   block that checks if the current key is a member of the `ignore` news desks tuple. If the key is
   __not__ a member call the function `calculate_articles_mean_word_count()` and pass it the list of
   articles mapped (i.e., assigned) to the key.

3. Inside the loop add a new key-value pair to `mean_word_counts` consisting of the current key and
   the return value of the call to `calculate_articles_mean_word_count()`. Below is one of the
   key-value pairs added to `mean_word_counts` that your code _must_ produce:

   ```python
   {
      "Obits": 823.14,
      ...
   }
   ```

4. Call the function `utl.write_json()` and write `mean_word_counts` to the file
   `stu-nyt_news_desk_mean_word_counts.json`. Compare your file to the test fixture file
   `fxt-nyt_news_desk_mean_word_counts.json`. The files _must_ match line-for-line and
   character-for-character.

<br />

## 9.9 Challenge 09 (45 points)

__Task__: Implement the function `get_wookieepedia_data()`.

<br />

## 9.9.1 Implement `get_wookieepedia_data()`

Replace `pass` with a code block that utilizes a `filter` string to return a nested dictionary from
the passed in `wookiee_data` list if the dictionary's "name" value matches the `filter` value.
Review the function's docstring to better understand the task it is to perform, the parameters it
defines, and the return value it computes.

The function can be employed to traverse lists of nested dictionaries sourced from the
following files in search of a particular dictionary representation of a Star Wars droid,
person, planet, or starship:

* `data-wookieepedia_droids.json`
* `data-wookieepedia_people.json`
* `data-wookieepedia_planets.csv`
* `data-wookieepedia_starships.csv`

:bulb: Familiarize yourself with the Wookieepedia-sourced data files before commencing the remaining
challenges.

### Requirements

1. The function must perform a __case insenstitive__ comparison between the passed in `filter`
   value and each nested dictionary's "name" value. If a match is obtained it returns the nested
   dictionary to the caller.

2. If no match is obtained the function returns `None` to the caller.

<br />

## 9.9.2 Call `get_wookieepedia_data()`

After implementing the function return to `main()`.

1. Call the function `utl.read_csv_to_dicts()` and retrieve the supplementary Wookieepedia planet
   data in the file `data-wookieepedia_planets.csv`.

2. Assign the return value to `wookiee_planets`.

3. Call the function `get_wookieepedia_data()` and pass it `wookiee_planets` and the _lowercase_
   string "dagobah" as the arguments.

4. Assign the return value to the variable `wookiee_dagobah`.

5. Call the function `utl.write_json()` and write `wookiee_dagobah` to the file
   `stu-wookiee_dagobah.json`. Compare your file to the test fixture file `fxt-wookiee_dagobah.json`
   The files _must_ match line forline, indent for indent, and character for character.

6. Call `get_wookieepedia_data()` a second time and pass it `wookiee_planets` and the _uppercase_
   string "HARUUN KAL" as the arguments.

7. Assign the return value to the variable `wookiee_haruun_kal`.

8. Call the function `utl.write_json()` and write `wookiee_haruun_kal` to the file
   `stu-wookiee_haruun_kal.json`. Compare your file to the test fixture file
   `fxt-wookiee_haruun_kal.json`. The files _must_ match line forline, indent for indent, and
   character for character.

<br />

## 9.10 Challenge 10 (85 points)

__Task__: Implement the function `convert_none_values()`.

## 9.10.1 Implement `utl.convert_none_values()`

Replace `pass` with a code block that returns a new dictionary comprised of key-value pairs sourced
from `data` that includes values converted to `None` if they are found in `utl.NONE_VALUES`. Review
the function's docstring to better understand the task it is to perform, the parameters it defines,
and the return value it computes.

### Requirements

1. A dictionary comprehension _must_ be employed to create the new dictionary.

   :bulb: If you are unsure how to craft the comprehension write a "standard" `for` loop first,
   confirm that it returns the expected value, then comment it out and build your comprehension
   based on the commented out code and lecture and problem set examples.

2. Loop over the `data` items and call the function `convert_to_none()` from inside the dictionary
   comprehension, passing to it the appropriate arguments.

3. Utilize the `data` dictionary's keys for the new dictionary's keys.

<br />

## 9.10.2 Test `utl.convert_none_values()`

After implementing `convert_none_values()` return to `main()`.

1. Uncomment the relevant `assert` statements and test the function.

2. If an `AssertionError` is raised, debug your code, and then retest. Repeat as necessary.

<br />

## 9.11 Challenge 11 (105 points)

__Task__: Implement the functions `utl.convert_gravity_value()` and `create_planet()`.

## 9.11.1 Implement `utl.convert_gravity_value()`

Replace `pass` with a code block that attempts to convert a planet's "gravity" value to a float by
first removing the "standard" unit of measure substring (if it exists) before converting the
remaining number to a float. Review the function's docstring to better understand the task it is to
perform, the parameters it defines, and the return value it computes.

:bulb: Note that "gravity" values vary from planet to planet. The following examples illustrate
the challenge:

```python
{
    'name': Tatooine,
    ...
    'gravity': '1 standard',
    ...
}

{
   'name': Dagobah,
    ...,
    'gravity': 'N/A',
    ...
}

{
    'name': Haruun Kal,
    ...
    'gravity': '0.98',
    ...
}
```

<br />

### Requirements

1. Employ `try` and `except` statements in order to handle runtime exceptions whenever an invalid
   conversion is attempted. __Do not__ place code outside the `try` and `except` code blocks.

2. In the `try` block evaluate whether or not the substring "standard" is part of `value` (perform a
   _case insensitive_ check). If found, remove the substring and pass the new (truncated) string
   to the function `utl.convert_to_float()` in order to convert the numeric part of the `value` to
   a float. If not found pass `value` directly to `utl.convert_to_float()`.

   :exclamation: Don't assume that `value` is "clean"; program defensively and remove
   leading/trailing spaces before attempting to convert the "cleaned" version of the string to a
   float.

3. If a runtime exception is encountered "catch" the exception in the `except` block and return the
   `value` to the caller __unchanged__.

   :bulb: You do not need to specify specific exceptions in the `except` statement.

<br />

## 9.11.2 Test `utl.convert_gravity_value()`

After implementing the function return to `main()`.

1. Uncomment the relevant `assert` statements and test the function.

2. If an `AssertionError` is raised, debug your code, and then retest. Repeat as necessary.

<br />

## 9.11.3 Implement `create_planet()`

Replace `pass` with a code block that returns a dictionary representation of a planet based on the
passed in `data` dictionary. Review the function's docstring to better understand the task it is to
perform, the parameters it defines, and the return value it computes.

### Requirements

Certain `data` values require special handling and are subject to the following type conversion
rules:

1. Call the appropriate utility function that returns a _new_ dictionary containing `data`
   values converted to `None` if found in `utl.NONE_VALUES`. Assign the return value to a local
   variable of your choice (choose a name that can be understood by a code reviewer&mdash;avoid
   opaque names).

2. Employ a dictionary literal&mdash;that you return directly to the caller&mdash;to transform the
   key-value pairs sourced from the new dictionary. You _may_ need to perform the following tasks
   as prescribed in the docstring:

   1. Filter out certain key-value pairs.

   2. Convert values found in the new dictionary to `int`, `float`, `list`, etc. by judicious
      use of the appropriate `utl.convert_to_*` functions.

   3. Map certain values to keys that differ from the original `data` dictionary keys.

   4. Reorder the key-value pairs.

<br />

## 9.11.4 Test `create_planet()`

After implementing `create_planet()` return to `main()`.

1. Call the function `get_swapi_resource()` and retrieve a SWAPI representation of the planet
   [Tatooine](https://starwars.fandom.com/wiki/Tatooine). Access the "Tatooine" dictionary which is
   stored in the response object and assign the value to `swapi_tatooine`.

   :bulb: The `five_oh_six` module includes a SWAPI "planets" URL constant that you can pass as the
   `url` argument. If you need help constructing the `params` argument review the lecture notes and
   code.

2. Call the function `get_wookieepedia_data()` passing it the appropriate arguments and retrieve the
   "Tatooine" dictionary in `wookiee_planets`.

3. Assign the return value to `wookiee_tatooine`.

4. Check the truth value of `wookiee_tatooine`. If "truthy" update `swapi_tatooine` with
   `wookiee_tatooine`.

5. Call the function `create_planet()` and pass the updated `swapi_tatooine` as the argument.

6. Assign the return value to a variable named `tatooine`.

7. Call the function `utl.write_json()` and write `tatooine` to the file `stu-tatooine.json`.
   Compare your file to the test fixture file `fxt-tatooine.json`. Both files _must_ match line for
   line, indent for indent, and character for character.

<br />

## 9.12 Challenge 12 (130 points)

__Task__: Implement the functions `utl.convert_to_year_era()` and  `create_droid()`.

<br />

## 9.12.1 Implement `utl.convert_to_year_era()`

Replace `pass` with a code block that attempts to separate the Galactic standard calendar year and
era (e.g., 896BBY, 24ABY) that comprise the passed in `value` in order to store the separated values
in a two-item dictionary.

### Requirements

1. Employ `try` and `except` statements in order to handle runtime exceptions whenever an invalid
   conversion is attempted. __Do not__ place code outside the `try` and `except` code blocks.

2. In the `try` block use slicing to access the year and era segments of the string.

   :bulb: Note that while the year segment's length varies (e.g., 896, 19, 0) the era segment of
   the Galactic calender date string comprises three characters: "BBY" or "ABY". Keep this in mind
   as you design your slicing expressions.

3. Before mapping the sliced segments to a dictionary, you _must_ first check if the "year" segment
   of the `value` is a number by employing the appropriate string method. If the substring is
   numeric, return a dictionary literal that maps the necessary slicing expressions to "year"
   and "era" keys as values. Structure the dictionary as follows:

   ```python
   {'year': < year > (int), 'era': < era > (str)}
   ```

4. Otherwise, if the "year" segment is not considered numeric return the `value` to the caller
   __unchanged__.

5. If the year segment is numeric, convert the "year" segment to an integer by passing it as the
   argument to the function `convert_to_int()`. Call the function from within the dictionary
   literal.

6. If a runtime exception is encountered "catch" the exception in the `except` block and return the
   `value` to the caller __unchanged__.

   :bulb: You do not need to specify specific exceptions in the `except` statement.

<br />

## 9.12.2 Test `utl.convert_to_year_era()`

After implementing the function return to `main()`.

1. Uncomment the relevant `assert` statements and test the function.

2. If an `AssertionError` is raised, debug your code, and then retest. Repeat as necessary.

<br />

## 9.12.3 Implement `create_droid()`

Replace `pass` with a code block that returns a dictionary representation of a driod (e.g., a
sentient robot) based on the passed in `data` dictionary. Review the function's docstring to better
understand the task it is to perform, the parameters it defines, and the return value it computes.

### Requirements

Certain `data` values require special handling and are subject to the following type conversion
rules:

1. Call the appropriate utility function that returns a _new_ dictionary containing `data`
   values converted to `None` if found in `utl.NONE_VALUES`. Assign the return value to a local
   variable of your choice (choose a name that can be understood by a code reviewer&mdash;avoid
   opaque names).

2. Employ a dictionary literal&mdash;that you return directly to the caller&mdash;to transform the
   key-value pairs sourced from the new dictionary. You _may_ need to perform the following tasks
   as prescribed in the docstring:

   1. Filter out certain key-value pairs.

   2. Convert values found in the new dictionary to `int`, `float`, `list`, etc. by judicious
      use of the appropriate `utl.convert_to_*` functions.

   3. Map certain values to keys that differ from the original `data` dictionary keys.

   4. Reorder the key-value pairs.

<br />

## 9.12.4 Test `create_droid()`

After implementing `create_droid()` return to `main()`.

1. Call the `utl.read_json()` function and retrieve the supplementary Wookieepedia droid data in the
   file `data-wookieepedia_droids.json`.

2. Assign the return value to `wookiee_droids`.

3. Call the function `get_swapi_resource()` and retrieve a SWAPI representation of the astromech
   droid [R2-D2](https://starwars.fandom.com/wiki/R2-D2). Make use of the appropriate constant to
   simplify construction of the URL.

4. Access the "R2-D2" dictionary which is stored in the response object and assign the value to
   `swapi_r2_d2`.

5. Call `get_wookieepedia_data()` passing it the appropriate arguments and retrieve the "R2-D2"
   dictionary in `wookiee_droids`.

6. Assign the return value to `wookiee_r2_d2`.

7. Check the truth value of `wookiee_r2_d2`. If "truthy" update `swapi_r2_d2` with `wookiee_r2_d2`.

8. Call the function `create_droid()` and pass the updated `swapi_r2_d2` as the argument. Assign
   the return value to a variable named `r2_d2`.

9. Call the function `utl.write_json()` and write `r2_d2` to the file `stu-r2_d2.json`. Compare your
   file to the test fixture file `fxt-r2_d2.json`. Both files _must_ match line for line, indent for
   indent, and character for character.

<br />

## 9.13 Challenge 13 (50 points)

__Task__: Implement the function `create_species()`.

<br />

## 9.13.1 Implement `create_species()`

Replace `pass` with a code block that returns a dictionary representation of a species based on the
passed in `data` dictionary. Review the function's docstring to better understand the task it is to
perform, the parameters it defines, and the return value it computes.

### Requirements

Certain `data` values require special handling and are subject to the following type conversion
rules:

1. Call the appropriate utility function that returns a _new_ dictionary containing `data`
   values converted to `None` if found in `utl.NONE_VALUES`. Assign the return value to a local
   variable of your choice (choose a name that can be understood by a code reviewer&mdash;avoid
   opaque names).

2. Employ a dictionary literal&mdash;that you return directly to the caller&mdash;to transform the
   key-value pairs sourced from the new dictionary. You _may_ need to perform the following tasks
   as prescribed in the docstring:

   1. Filter out certain key-value pairs.

   2. Convert values found in the new dictionary to `int`, `float`, `list`, etc. by judicious
      use of the appropriate `utl.convert_to_*` functions.

   3. Map certain values to keys that differ from the original `data` dictionary keys.

   4. Reorder the key-value pairs.

<br />

## 9.13.2 Call `create_species()`

After implementing `create_species()` return to `main()`.

1. Call the function `get_swapi_resource()` and retrieve a SWAPI representation of the human
   species. Make use of the appropriate constant to simplify construction of the URL.

2. Assign the return value to `swapi_human_species`.

3. Call the function `create_species()` and pass `swapi_human_species` as the argument.

4. Assign the return value to a variable named `human_species`.

5. Call the function `utl.write_json()` and write `human_species` to the file
   `stu-human_species.json`. Compare your file to the test fixture file `fxt-human_species.json`.
   Both files _must_ match line for line, indent for indent, and character for character.

<br />


## 9.14 Challenge 14 (75 points)

__Task__: Implement the function `get_homeworld()` The function will be utilized by the function
`create_person()` to enrich a person's home planet information.

<br />

## 9.14.1 Implement `get_homeworld()`

Replace `pass` with a code block that attempts to return a dictionary representation of a person's
home planet using the provided `identifier` and optional `planets` arguments. Review the function's
docstring to better understand the task it is to perform, the parameters it defines, and the return
value it computes.

### Requirements

1. Take heed: the `identifier` is assumed to be either a __planet name__ (e.g., Dagobah) OR a
   __SWAPI planet URL__ (e.g., https://swapi.py4e.com/api/planets/5/).

2. If the `identifier` commences with the substring "https://" the `identifier` is considered a URL
   and is passed to the function `get_swapi_resource()` as the `url` argument. Otherwise the
   `identifier` is assumed to be a planet name and is passed to `get_swapi_resource()` as a `params`
   value along with the appropriate constant URL.

3. If an optional Wookieepedia-sourced `planets` list is provided by the caller, the task of
   retrieving the appropriate nested dictionary is delegated to the function
   `get_wookieepedia_data()`.

   :exclamation: Processing `planets` only occurs if the passed in `identifier` is a __planet name__
   since `get_wookieepedia_data()` filters on planet names only.

4. If a match is obtained the SWAPI homeworld dictionary is updated with the Wookieepedia planet
   data. The updated dictionary is then passed to the function `create_planet()` for further
   processing before a "thinned" dictionary representation of the planet is returned to the caller.

## 9.14.2 Test `get_homeworld()`

After implementing the function return to `main()`.

1. Call the function `get_swapi_resource()` and retrieve a SWAPI representation of the Jedi knight
   [Anakin Skywalker](https://starwars.fandom.com/wiki/Anakin_Skywalker). Pass the Jedi knight's
   name as a `params` value. Make use of the appropriate constant to simplify construction of the
   URL.

2. Access the "Anakin" dictionary from the response object and assign the value to `swapi_anakin`.

3. Call the function `get_homeworld()` and pass to it the `swapi_anakin` dictionary's "homeworld"
   value as the argument.

   :bulb: consider using the built-in function `print()` or the debugger to check the "homeworld"
   value.

4. Assign the return value to the variable named `anakin_swapi_homeworld`.

   :bulb: If you trigger a runtime `KeyError` exception review how you are accessing dictionary
   values in the function `create_planet()`. You may need to assign some or all values using an
   expression that returns `None` instead of triggering a `KeyError` if the associated key is not
   located in the passed in dictionary. A dictionary method exists for accomplishing such a task.

5. Call the function `utl.write_json()` and write `anakin_swapi_homeworld` to the file
   `stu-anakin_swapi_homeworld.json`. Compare your file to the test fixture file
   `fxt-anakin_swapi_homeworld.json`. Both files _must_ match line for line, indent for indent, and
   character for character.

6. Next, call the `utl.read_json()` function and retrieve the supplementary Wookieepedia person data
   in the file `data-wookieepedia_people.json`.

7. Assign the return value to `wookiee_people`.

8. Call `get_wookieepedia_data()` passing it the appropriate arguments and retrieve the "Anakin
   Skywalker" dictionary in `wookiee_people`.

9.  Assign the return value to the `wookiee_anakin`.

10. Check the truth value of `wookiee_anakin`. If "truthy" update `swapi_anakin` with
   `wookiee_anakin`.

11. Call the function `get_homeworld()` and pass to it as arguments the `swapi_anakin` "homeworld"
    value and `wookiee_planets`.

12. Assign the return value to the variable named `anakin_swapi_wookiee_homeworld`.

13. Call the function `utl.write_json()` and write `anakin_swapi_wookiee_homeworld` to the file
   `stu-anakin_swapi_wookiee_homeworld.json`. Compare your file to the test fixture file
   `fxt-anakin_swapi_wookiee_homeworld.json`. Both files _must_ match line for line, indent for
   indent, and character for character.

<br />


## 9.15 Challenge 15 (55 points)

__Task__: Implement the function `get_species()` The function will be utilized by the function
`create_person()` to enrich a person's species information.

<br />

## 9.15.1 Implement `get_species()`

Replace `pass` with a code block that attempts to return a dictionary representation of a person's
species dictionary using the provided `identifier` argument. Review the function's docstring to
better understand the task it is to perform, the parameters it defines, and the return value it
computes.

### Requirements

1. Take heed: the `identifier` is assumed to be either a __species name__ (e.g., Wookiee) OR a
   __SWAPI species URL__ (e.g., https://swapi.py4e.com/api/species/3/), OR __a list__ that holds the
   SWAPI species URL.

2. The function _must_ first check the `identifer` type. If the `identifier` is a `list` rather than
   a `str` access the first list element and assign it to `identifier`.

   :bulb: If `identifier` is a not a `list` you can assume that it is a string.

3. If the `identifier` commences with the substring "https://" the `identifier` is considered a URL
   and is passed to the function `get_swapi_resource()` as the `url` argument. Otherwise the
   `identifier` is assumed to be a planet name and is passed to `get_swapi_resource()` as a `params`
   value along with the appropriate constant URL.

4. The SWAPI species dictionary is then passed to the function `create_species()` for further
   processing. This results in a "thinned" dictionary representation of the species which is then
   returned to the caller.

## 9.15.2 Test `get_species()`

After implementing the function return to `main()`.

1. Call the function `get_species()` and pass to it the `swapi_anakin` dictionary's "species" value
   as the argument.

2. Assign the return value to the variable named `anakin_swapi_species`.

3. Call the function `utl.write_json()` and write `anakin_swapi_species` to the file
   `stu-anakin_swapi_species.json`. Compare your file to the test fixture file
   `fxt-anakin_swapi_species.json`. Both files _must_ match line for line, indent for indent, and
   character for character.

<br />

## 9.16 Challenge 16 (90 points)

__Task__: Implement the function `create_person()`.

<br />

## 9.16.1 Implement `create_person()`

Replace `pass` with a code block that returns a new person dictionary based on the passed in `data`
dictionary. Review the function's docstring to better understand the task it is to perform, the
parameters it defines, and the return value it computes.

### Requirements

Certain `data` values require special handling and are subject to the following type conversion
rules:

1. Call the appropriate utility function that returns a _new_ dictionary containing `data`
   values converted to `None` if found in `utl.NONE_VALUES`. Assign the return value to a local
   variable of your choice (choose a name that can be understood by a code reviewer&mdash;avoid
   opaque names).

2. Employ a dictionary literal&mdash;that you return directly to the caller&mdash;to transform the
   key-value pairs sourced from the new dictionary. You _may_ need to perform the following tasks as
   prescribed in the docstring:

   1. Filter out certain key-value pairs.

   2. Convert values found in the new dictionary to `int`, `float`, `list`, `dict`, etc. by
      judicious use of the appropriate `utl.convert_to_*` functions.

   3. Map certain values to keys that differ from the original `data` dictionary keys.

   4. Reorder the key-value pairs.

   5. :exclamation: Utilize the "homeworld" and "species" values to retrieve "thinned" dictionary
    representations of a planet and species. Retrieving a person's home planet is delegated
    to the function `get_homeworld()` while retrieving the species is delegated to the function
    `get_species()`. If an optional Wookieepedia-sourced `planets` list is provided, the
    argument is passed on to `get_homeworld()` for processing but __only__ if the "homeworld" value
    is a planet name. Map (i.e., assign) the thinned dictionaries to their respective keys in the
    dictionary literal.

<br />

## 9.16.2 Call create_person()

After implementing `create_person()` return to `main()`.

1. Call the function and pass to it the Wookieepedia-enhanced `swapi_anakin` _and_ `wookiee_planets`
   as the arguments.

2. Assign the return value to a variable named `anakin`.

3. Call the function `utl.write_json()` and write `anakin` to the file
   `stu-anakin_skywalker.json`. Compare your file to the test fixture file
   `fxt-anakin_skywalker.json`. Both files _must_ match line for line, indent for indent, and
   character for character.

4. Next, create an "enriched" dictionary representation of the
   [Jedi](https://en.wikipedia.org/wiki/Jedi) master and general
   [Obi-Wan Kenobi](https://starwars.fandom.com/wiki/Obi-Wan_Kenobi). Pass the Jedi general's name
   as a `params` value. Make use of the appropriate constant to simplify construction of the URL.

   Utilize the same "creational" workflow employed to create Anakin Skywalker:

   1. Retrieve a dictionary representation of Obi-Wan Kenobi from SWAPI. We recommend assigning the
      return value to a variable named `swapi_obi_wan`.

   2. Call `get_wookieepedia_data()` and access the Wookieepedia dictionary representation of
      Obi-Wan Kenobi in `wookiee_people`. We recommend assigning the return value to a variable named
      `wookiee_obi_wan`.

   3. Check the truth value of `wookiee_obi_wan` and, if "truthy", update `swapi_obi_wan` with
      `wookiee_obi_wan`.

   4. Call `create_person()` and pass the updated `swapi_obi_wan` _and_ `wookiee_planets` as the
      arguments. Assign the return value to a variable named `obi_wan`.

5. Call the function `utl.write_json()` and write `obi_wan` to the file `stu-obi_wan_kenobi.json`.
   Compare your file to the test fixture file `fxt-obi_wan_kenobi.json`. Both files _must_ match
   line for line, indent for indent, and character for character.

<br />

## 9.17 Challenge 17 (80 points)

__Task__: Implement the function `create_starship()`.

<br />

## 9.17.1 Implement `create_starship()`

Replace `pass` with a code block that returns a new starship dictionary based on the passed in
`data` dictionary. Review the function's docstring to better understand the task it is to perform,
the parameters it defines, and the return value it computes.

### Requirements

Certain `data` values require special handling and are subject to the following type conversion
rules:

1. Call the appropriate utility function that returns a _new_ dictionary containing `data`
   values converted to `None` if found in `utl.NONE_VALUES`. Assign the return value to a local
   variable of your choice (choose a name that can be understood by a code reviewer&mdash;avoid
   opaque names).

2. Employ a dictionary literal&mdash;that you return directly to the caller&mdash;to transform the
   key-value pairs sourced from the new dictionary. You _may_ need to perform the following tasks
   as prescribed in the docstring:

   1. Filter out certain key-value pairs.

   2. Convert values found in the new dictionary to `int`, `float`, `list`, etc. by judicious
      use of the appropriate `utl.convert_to_*` functions.

   3. Map certain values to keys that differ from the original `data` dictionary keys.

   4. Reorder the key-value pairs.

      :exclamation: Be aware that the semantics (i.e., meaning) of the SWAPI/Wookieepedia
      "passengers" and "crew" key-value pairs evolve as the representation of a starship is
      transformed by the code you write:

      ### SWAPI/Wookieepedia

      ```python
      'crew': '2',
      'passengers': '6',
      ```
      ### `create_starship()`

      ```python
      'crew': {
         'crew_size': 2,
         'crew_members': {...}
      },
      'passengers': {
         'max_passengers': 6,
         'on_board': [...]
      }
      ```

<br />

## 9.17.2 Call `create_starship()`

:exclamation: The starship _Twilight_ is sourced from Wookieepedia only. No SWAPI representation of
the light freighter exists.

After implementing `create_starship()` return to `main()`.

1. Call the `utl.read_csv_to_dicts()` function and retrieve the supplementary Wookieepedia starship
   data in the file `data-wookieepedia_starships.csv`.

2. Assign the return value to `wookiee_starships`.

3. Call `get_wookieepedia_data()` passing the appropriate arguments and retrieve the light freigter
named [_Twilight_](https://starwars.fandom.com/wiki/Twilight) in `wookiee_starships`.

4. Assign the return value to a variable named `wookiee_twilight`.

5. Call the function `create_starship()` and pass `wookiee_twilight` to it as the argument. Assign
   the return value to a variable named `twilight`.

6. Call the function `utl.write_json()` and write `twilight` to the file `stu-twilight.json`.
   Compare your file to the test fixture file `fxt-twilight.json`. Both files _must_ match line for
   line, indent for indent, and character for character.

<br />

## 9.18 Challenge 18 (65 points)

__Task__: Implement the function `board_passengers()`. Get Senator Padmé Amidala, the protocol
droid C-3PO, and the astromech droid R2-D2 aboard the _Twilight_ as passengers.

<br />

## 9.18.1 Implement `board_passengers()`

Replace `pass` with a code block that assigns a limited number of passengers to a list. Review the
function's docstring to better understand the task it is to perform, the parameters it defines, and
the return value it computes.

### Requirements

1. The passengers _must_ be passed in a `list` to the `board_passengers()` function.

2. The number of passengers permitted to board a starship or other vehicle is limited by the
    provided `max_passengers` value. If the number of passengers attempting to board exceeds
    `max_passengers` only the first `n` passengers (where `n` = `max_passengers`) are permitted
    to board the vessel.

   For example, if a starship's `max_passengers` value equals `10` and `20` passengers attempt to
   board the starship, only the first `10` passengers are permitted aboard the vessel.

<br />

## 9.18.2 Call `board_passengers()`

> R2 are you quite certain that the ship is in this direction? This way looks potentially dangerous. _C-3PO_

After implementing `board_passengers()` return to `main()`.

1. Create a dictionary representation of the Galactic senator
   [Padmé Amidala](https://starwars.fandom.com/wiki/Padm%C3%A9_Amidala). Pass the senator's name
   as a `params` value. Utilize the same "creational" workflow employed to create the dictionary
   representations of `anakin` and `obi_wan`. Use the following variable names to represent
   Padmé Amidala.

   * `swapi_padme` (assigned to the SWAPI dictionary)
   * `wookiee_padme` (assigned to the Wookieepedia dictionary)
   * `padme` (assigned to the `create_person()` return value)

2. Call the function `utl.write_json()` and write `padme` to the file `stu-padme_amidala.json`.
   Compare your file to the test fixture file `fxt-padme_amidala.json`. Both files _must_ match
   line for line, indent for indent, and character for character.

3. Create a dictionary representation of the protocol droid named
   [C-3PO](https://starwars.fandom.com/wiki/C-3PO). Pass the droid's name as a `params` value.
   Utilize the same "creational" workflow employed to create `r2_d2`. Consider using the following
   variable names to represent C-3PO.

   * `swapi_c_3po` (assigned to the SWAPI dictionary)
   * `wookiee_c_3po` (assigned to the Wookieepedia dictionary)
   * `c_3po` (assigned to the `create_droid()` return value)

4. Call the function `utl.write_json()` and write `c_3po` to the file `stu-c_3po.json`. Compare your
   file to the test fixture file `fxt-c_3po.json`. Both files _must_ match line for line, indent for
   indent, and character for character.

5. Next, call the function `board_passengers()` and pass the `twilight` starship's "max_passengers"
   value and a list of passengers comprising `padme`, `c_3po`, and `r2_d2` (in that order) as
   arguments.

6. Map (i.e., assign) the return value to the `twilight` dictionary's "on_board" key.

   :bulb: Consider testing your function by passing additional passengers to it in excess of the
   permitted "max_passengers" value. Consider creating dictionary representations of the following
   Jedi masters:

   * [Mace Windo](https://starwars.fandom.com/wiki/Mace_Windu) (https://swapi.py4e.com/api/people/51/)
   * [Plo Koon](https://starwars.fandom.com/wiki/Plo_Koon) (https://swapi.py4e.com/api/people/58/)
   * [Shaak Ti](https://starwars.fandom.com/wiki/Shaak_Ti) (https://swapi.py4e.com/api/people/78/)
   * [Yoda](https://starwars.fandom.com/wiki/Yoda) (https://swapi.py4e.com/api/people/20/)

   If the function `board_passengers()` is implemented correctly only `padme`, `c_3po`, `r2_d2`, and
   three of the Jedi masters should be able to board the `twilight`. You can retrieve both SWAPI and
   Wookieepedia dictionary representations of each to use for testing. Do this on separate lines and
   remember to comment it out before submitting your solution to Gradescope. JSON fixture files
   of these Jedi have also been included in the file dump.

<br />

## 9.19 Challenge 19 (100 points)

> Let's get back to the ship. Power up the engines R2. _Anakin Skywalker_

__Task__: Implement the function `assign_crew_members()`. Assign Anakin Skywalker and
Obi-Wan Kenobi to the _Twilight_ as crew members.

<br />

## 9.19.1 Implement `assign_crew_members()`

Replace `pass` with a code block that assigns personnel by position (e.g., pilot, copilot) to a
starship using a dictionary comprehension. Review the function's docstring to better understand the
task it is to perform, the parameters it defines, and the return value it computes.

### Requirements

1. To earn full credit you _must_ create the "crew_members" dictionary by writing a
   __dictionary comprehension__ on a __single line__.

   :exclamation: If necessary write a `for` loop that adds the
   position/crew member key-value pairs to an accumulation dictionary named `crew_members`. Get it
   working first and then convert it to a dictionary comprehension.

   :bulb: Avoid looping over the passed in lists. Instead __loop over a sequence of numbers__ and
   think carefully about the appropriate stop value to employ in order to limit the number of loop
   iterations. Utilize the sequence of numbers to pair `crew_position` and `personnel` elements by
   their matching index position.

2. The crew positions (e.g., 'pilot', 'copilot') and personnel (e.g., Anakin Skywalker, Obi-Wan
   Kenobie) must be passed in separate `crew_positions` and `personnel` lists to the function
   `assign_crew_members()`.

3. Assume that each ship requires a full compliment of personnel to crew the vessel. In other words,
   if a starship's "crew_size" equals three (`3`) you _must_ pass to `assign_crew_members()`
   three crew positions and three personnel.

   Assume too that the maximum number of crew members that can be assigned to a starship is limited
   by the starship's "crew_size" value. No additional crew members are permitted to be assigned to
   the starship even if included in the `crew_positions` and `personnel` lists. This limitation
   _must_ be imposed from within the dictionary comprehension.

   For example, if a starship's "crew_size" value equals `3` but `4` crew positions/personnel are
   passed to the function only the first `3` crew positions/personnel are permitted to be added
   as key-value pairs to the crew members dictionary.

4. The passed in `crew_positions` and `personnel` lists _must_ contain the same number of elements.
   The individual `crew_positions` and `personnel` elements are then paired by index
   position and stored in a dictionary structured as follows:

   ```python
   {< crew_position[0] >: < personnel[0] >, < crew_position[1] >: < personnel[1] >, ...}
   ```

<br />

## 9.19.2 Call `assign_crew_members()`

After implementing `assign_crew_members()` return to `main()`.

1. Call the function `assign_crew_members()` and pass the Twilight's "crew_size" value, a crew
   positions list comprising the following string elements: "pilot" and "copilot", and a personnel
   list comprising `anakin` and `obi_wan`.

2. Map (i.e., assign) the return value to the `twilight` dictionary's "crew_members" key.

   :bulb: Consider testing your function by passing an additional crew position (e.g., navigator)
   and crew member (e.g, [Mace Windo](https://starwars.fandom.com/wiki/Mace_Windu) to it in excess
   of the permitted "crew_size". Do this on a separate line and remember to comment it out before
   submitting your solution to Gradescope.

## 9.19.3 Issue instructions to R2-D2

Create a list containing Anakin's "Power up the engines" order (a string) and map (i.e., assign) the
list to the droid `r2_d2's` "instructions" key.

<br />

## 9.20 Challenge 20 (110 points + 90 Bonus points)

__Task__: Sort `wookiee_planets` and then issue commands to R2-D2 to chart a course to the planet
Naboo before instructing the droid to release the docking clamp and detach the _Twilight_ from the
_Malevolence_.

## 9.20.1 Sort `wookiee_planets`

1. Write a __single-line list comprehension__ that transforms each Wookieepedia-sourced planet
   dictionary in the `wookiee_planets` list by passing each planet referenced in the comprehension
   to the function `create_planet()`.

2. Assign the new list to a variable named `planets`.

   :exclamation: if your list comprehension triggers a `KeyError` exception, check your
   implementation `create_planet()`. The function is likely attempting to access a key in the planet
   dictionary that does not exist. Recall that there is a friendly `dict` method for dealing with
   such issues; refactor (i.e., revise) your function block accordingly.

3. Perform an __in_place__ sort of the `planets` list passing to it as the `key` function a `lambda`
   function that sorts the planets __by name__. __Reverse__ the sort so that the planets are sorted
   by name in __descending order__.

4. Call the function `utl.write_json()` and write `planets` to the file
   `stu-planets_sorted_name.json`. Compare your file to the test fixture file
   `fxt-planets_sorted_name.json`. Both files _must_ match line for line, indent for indent, and
   character for character.

<br />

## 9.20.3 Issue instructions to R2-D2

1. Access the sixth (6th) planet in `planets` by its index (__no looping__) and add its "region" and
   "sector" values to a formatted string literal (f-string) structured as follows:

   ```python
   "Plot course for Naboo, < region >, < sector >"
   ```

2. Add the f-string to `r2_d2's` "instructions" list so that _Twilight_ can chart a course to the
   planet Naboo, Padmé Amidala's home world.

<br />

## 9.20.4 BONUS: Sort planets by diameter and name (90 points)

:gift: Complete this __BONUS__ sub-task and earn extra credit points.

:bulb: If you get stuck on sorting `planets` by "diameter_km" and "name", pause your sorting work
and proceed to the final task ("Escape from the Malevolvence") and complete it. Then return and
restart this bonus task.

1. Employ the built-in function `sorted()` and a `lambda` function to sort `planets` by the
   following attributes:

   | Key | Value | Order |
   | :-- | :---- | :---- |
   | diameter_km | `int` \| `None` | descending |
   | name | ascending | `str` |

2. You _must_ craft your `lambda` expression using the __ternary operator__ when sorting on
   "diameter_km" because several planets lack a known diameter and in consequence `None` has been
   mapped (i.e., assigned) to their "diameter_km" key.

3. Assign the return value of `sorted()` to a variable named `planets_diameter_km`.

   :exclamation: Write the entire statement on a single line to facilitate auto grader testing:

   ```python
   planets_diameter_km = sorted(...)
   ```

4. Call the function `utl.write_json()` and write `planets_diameter_km` to the file
   `stu-planets_sorted_diameter.json`. Compare your file to the test fixture file
   `fxt-planets_sorted_diameter.json`. Both files _must_ match line for line, indent for indent, and
   character for character.

<br />

## 9.20.5 Escape from the Malevolence

> R2 release the docking clamp. _Anakin Skywalker_

With our heroes on board the _Twilight_ and the engines fired, the light freighter detaches
itself from the stricken heavy cruiser _Malevolence_ and departs to rejoin the Republican fleet
before heading to Naboo.

1. Add Anakin's order "Release the docking clamp" to `r2_d2's` "instructions" key-value pair.

2. Call the function `utl.write_json()` and write `twilight` to the file
   `stu-twilight_departs.json`. Compare your file to the test fixture file
   `fxt-twilight_departs.json`. Both files _must_ match line for line, indent for indent, and
   character for character.

If the files match your job is done. Never mind that Separatist starfighters are in hot pursuit of
the _Twilight_&mdash;declare victory!

Congratulations on completing SI 506.

<br />

## FINIS
