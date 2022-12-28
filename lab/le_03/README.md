# SI 506: Lab Exercise 03

## This week's Lab Exercise

This week's lab exercise includes seven (7) problems that focus on slicing, loops, and conditional statements.

## Background
Netflix manages a Global Top 10 list of most-watched TV shows and films that is updated weekly ([Source](https://top10.netflix.com/tv)). For this lab, you are provided with a list of lists assigned to the variable `shows` that includes some basic information about the top streamed TV shows from the last few weeks. The variable is assigned to a list of lists. Each list element contains string elements. Each string represents the show's name, genre, latest season number, and a one word description of the show taken from user reviews, respectively. You are going to use slicing, `for` loops, and `conditional statements` to complete each problem.

```python
shows = [
    ["The Imperfects", "Science Fiction", "1", "entertaining"],
    ["Devil in Ohio", "Thriller", "1", "spooky"],
    ["The Crown", "Historical Drama", "4", "Powerful"],
    ["Narco-Saints", "Thriller", "1", "Entertaining"],
    ["In the Dark", "Crime Drama", "4", "intriguing"],
    ["Cyberpunk: Edgerunners", "Anime", "1", "amazing"],
    ["Dated & Related", "Reality", "1", "awkward"],
    ["Diary of a Gigolo", "Mystery", "1", "intriguing"],
    ["Cobra Kai", "Dramedy", "5", "nostalgic"],
    ["I Survived a Crime", "True Crime", "1", "violent"],
    ["Echoes: Limited Series", "Thriller", "1", "intriguing"],
    ["The Sandman", "Fantasy", "1", "striking"],
    ["Partner Track", "Legal Drama", "1", "Enjoyable"],
    ["Stranger Things", "Science Fiction", "4", "Spooky"],
    ["I AM A KILLER", "Crime", "3", "somber"],
    ["Manifest", "Supernatural", "4", "mysterious"],
    ["Never Have I Ever", "Dramedy", "3", "entertaining"],
    ["Selling The OC", "Reality", "1", "dramatic"],
    ["Glow Up", "Reality", "4", "entertaining"],
    ["Locke & Key", "Horror", "3", "intriguing"]
]
```
## 1.0 Problem 01 (1 point)
Employ slicing with a `stride` value to access every other tv show in reverse order and assign the variable `every_other_reversed` to the new list.

The expected output is:
```python
every_other_reversed = [
            ['Locke & Key', 'Horror', '3', 'intriguing'],
            ['Selling The OC', 'Reality', '1', 'dramatic'],
            ['Manifest', 'Supernatural', '4', 'mysterious'],
            ['Stranger Things', 'Science Fiction', '4', 'Spooky'],
            ['The Sandman', 'Fantasy', '1', 'striking'],
            ['I Survived a Crime', 'True Crime', '1', 'violent'],
            ['Diary of a Gigolo', 'Mystery', '1', 'intriguing'],
            ['Cyberpunk: Edgerunners', 'Anime', '1', 'amazing'],
            ['Narco-Saints', 'Thriller', '1', 'Entertaining'],
            ['Devil in Ohio', 'Thriller', '1', 'spooky']
        ]
```

## 2.0 Problem 02 (3 points)

Loop over the `shows` list and access each show's genre. As you loop through the list, append each genre value to the empty list named `genres`.

:bulb: Access the genre element using list indexing. Python indexes are zero-based and you must keep this in mind as you append each genre element to the new list.

## 3.0 Problem 03 (3 points)

Implement an `if` statement inside a `for` loop that identifies each show described as "entertaining".

Loop over the `shows` list; if the show is described as "entertaining", append **_only_** the show's name to the new list named `entertaining_shows`.

:warning: Python is a case-sensitive programming language. Do not assume that each string or substring that you may be asked to access is consistent in terms of uppercase / lowercase usage. You might need to use a built-in `str` method to convert the uppercase letters to lowercase when performing string matching in your conditional statement. The show name elements that you will append to the new list must be left in their original case.

:bulb: Recall that you can utilize the built-in function `print()` to check on the values being appended to the new and established genres lists. When satisfied with your conditional statements, you can comment out `print()` or remove the expression from your code. This practice will come in handy as you move through the rest of the lab exercise.

## 4.0 Problem 04 (3 points)

Implement an `if` statement inside a `for` loop that evaluates whether or not the name of the show comprises more than three words.

Loop over the `shows` list; if the show has more than three words in its name, increment the variable `count` by one (1).

Build a formatted string literal (f-string) using the `count` variable. The f-string is formatted as follows:

```"There are a total of 4 shows with more than three words in their title."```

## 5.0 Problem 05 (3 points)

Loop over the `shows` list and convert the number of seasons from type `string` to type `int`. Take the converted number and assign it back to the original position in `shows`.

:bulb: Convert each season number encountered to an integer and access the list element using list indexing chaining to update the season number.

:warning: You must utilize a `for i in range():` loop and subscript notation chaining to accomplish this task. Refer to the lecture notes for guidance.

## 6.0 Problem 06 (3 points)

Implement an `if` statement inside a `for` loop that evaluates whether or not a show's run is less than two (2) seasons.

Loop over the `shows` list and if the number of seasons in the show is less than 2 (exclusive), then append the show's name to a list named `new_shows`.

## 7.0 Problem 07 (4 points)

Implement an `if` statement inside a `for` loop in order to identify the longest-running show.

Loop over the `shows` list and check the number of seasons for each show. Assign the name of the show with the most seasons to the new variable named `longest_show`.
