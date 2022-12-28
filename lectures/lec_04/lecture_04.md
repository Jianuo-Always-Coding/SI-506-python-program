# SI 506 Lecture 04

## Topics

1. Statements and expressions
2. string formatting: f-string; `\n` newline escape sequence
3. Object behaviors (a gentle intro)
4. Basic arithmetic
5. In-class coding challenges

<br />

## Vocabulary

* __Boolean__. A type (`bool`) or an expression that evaluates to either `True` or `False`.
* __Built-in Function__. A [function](https://docs.python.org/3/library/functions.html) defined by
  the Standard Library that is always available for use.
* __Concatenation__. Joining one object to another in order to create a new object. Joining two
  strings together (e.g., `greeting = 'Hello ' + 'SI 506'`) is an example of string concatenation.
* __Expression__. An accumulation of values, operators, and/or function calls that return a value.
  `len(< some_list >)` is considered an expression.
* __f-string__. Formatted string literal prefixed with `f` or `F`.
* __Method__. A function defined by and bound to an object. For example the `str` type is
  provisioned with a number of methods including `str.lower()` and `str.strip()`.
* __Operator__. A [symbol](https://www.w3schools.com/python/python_operators.asp) for performing
  operations on values and variables. The assignment operator (`=`) and arithmetic operators
  (`+`, `-`, `*`, `/`, `**`, `%`, `//`).
* __Statement__. An instruction that the Python Interpreter can execute. For example, assigning a
  variable to a value such as `name = 'arwhyte'` is considered a statement.

<br />

## Book censorship

The American Library Association's Office for Intellectual Freedom (OIF) maintains a list of the
"Top 10 Most Challenged Books" in order to highlight censorship in US libraries and schools. For the
year 2021 the ALA recorded 729 censorship challenges, the highest number of annual challenges
reported by the ALA in a single year since it began tracking challenges twenty years ago. Over
1,597 books were targeted for removal from library collections in 2021. The ALA states that the
majority of challenges involved works by or about Black or LBGTQIA+ persons. Today's lecture features challenged works drawn from the ALA "Most Challenged" list as well as census and voter data related to a failed library millage which occurred recently in West Michigan.


<br />

## 1.0 Statements and expressions

A Python _statement_ is an instruction that performs some action. For example, a variable assignment
is considered a statement. Actions that evaluate one or more conditions (`if-else-if`) or involve
iteration over a sequence or a dictionary (`for`, `while`) are also considered statements.

A Python _expression_ is a combination of values, pointers (i.e., variables), operators, and/or
function or method calls that return a value.

:bulb: A statement can include one or more expressions (the reverse is not true).

```python
ala = "American Library Association" # statement

challenges_2019_to_2021 = 377 + 156 + 729 # arithmetical expression

print(challenges_2019_to_2021) # expression
```

<br />

## 1.1 Challenge 01

__Task__. Assign string values to specified variables. Confirm variable assignments by passing
variables to the built-in `print()` function.

Maia Kobabe's graphic memoir _Gender Queer_ (2019) leads the 2021 list of most challenged books
according to the ALA.

1. Assign the string "Gender Queer: A Memoir" to a variable named `banned_title`.
2. Assign the string "Maia Kobabe" to a variable named `banned_author`.
3. Assign the string "(Lion Forge Comics, 2019)" to a variable named `banned_publisher`.

<br />

## 1.2 Challenge 02

__Task__. Confirm the Challenge 01 variable assignments by passing the "banned" variables as
multiple arguments to the built-in `print()` function.

:bulb: The built-in `print()` function can accept multiple arguments. See Bartosz Zaczyński,
["Your Guide to the Python print() Function"](https://realpython.com/python-print/)
(Real Python, Aug 2019) for an extended discussion of the function's capabilities.

1. Call the built-in `print()` function and pass the three variables to it as arguments in the
   following order:

   1. `banned_author`
   2. `banned_title`
   3. `banned_publisher`

2. Separate each argument by a comma and a space (`, `) inside the function's trailing parentheses
   (`(< var_01 >, < var_02 >, < var_03 >)`).

3. The terminal output _must_ match the following string:

   ```commandline
   Maia Kobabe Gender Queer: A Memoir (Lion Forge Comics, 2019)
   ```

<br />

## 1.3 Challenge 03

__Task__. Use string concatenation to return a _new_ string assembled from the three "banned"
variables.

:bulb: You can use the plus (`+`) operator to construct a new string by joining two or more strings.
This is known as string _concatenation_.

1. Concatenate the "banned" strings by creating an expression that places the plus (`+`) operator
   between the three variables.

   :exclamation: Employ the same variable order as Challenge 02.

2. Add a comma and a space (`', '`) between `banned_author` and `banned_title`. This will require
   the insertion of another plus (`+`) operator in the expression.

3. Add a space (`' '`) between `banned_title` and `banned_publisher`. This will require
   the insertion of yet another plus (`+`) operator in the expression.

4. Assign the new string returned by the expression to a variable named `banned_book`.

5. Call the built-in `print()` function (an expression) and pass it `banned_book` as the argument.
   The terminal output _must_ match the following string:

   ```commandline
   Maia Kobabe, Gender Queer: A Memoir (Lion Forge Comics, 2019)
   ```

<br />

## 2.0 String formatting

The lectures, lab exercises, and problem sets will often include a number of pre-positioned
`print()` functions (an expression) in which a _formatted string literal_ (a.k.a f-string) is
passed in as an argument.

The f-string syntax `f"some_string {some_variable_inside_curly_braces}"` is less verbose and easier
to construct than earlier string formatting approaches. You will learn how to write f-strings as
well as format strings using the older approaches in the very near future.

```python
author = 'George M. Johnson'

print(f"Author = {author}\n") # note use of curly braces
```

:bulb: The `\n` characters represents an escape sequence, specifically an ASCII linefeed (LF).
Think of `\n` as "newline". Passing `\n` in a string will insert a new line at the position of the
escape sequence.

<br />

## 2.1 Challenge 04

__Task__. Pass a formatted string literal (f-string) to the built-in `print()` function.

1. Call the built-in `print()` function and pass it an f-string that produces the following
   terminal output:

   ```commandline
   Maia Kobabe, Gender Queer: A Memoir (Lion Forge Comics, 2019)
   < newline >
   ```

   The expression you create is constructed as follows:

   ```python
   print(f"< variable >< newline >")
   ```

2. Pass the f-string as an argument directly to the built-in `print()` function as
   follows:

   1.  Inside the built-in `print()` function's parentheses `()`, start the f-string expression
       using a leading `f` followed by two double quotation marks (`""`).

   2.  Insert the variable `banned_book` into the f-string surrounding it with the appropriate
       characters.

   3.  Add a trailing newline sequence (`\n`) to the end of the f-string.


<br />

## 2.2 Challenge 05

__Task__. Return the length of a string and then pass a formatted string literal (f-string)
containing the character count to the built-in `print()` function.

Nobel Prize winner Toni Morrison's first novel _The Bluest Eye_ (1970) has appeared on the ALA's
[Top 10 Most Challenged Books list](https://www.ala.org/advocacy/bbooks/frequentlychallengedbooks/top10)
five times since 2006.

1. Use the appropriate [built-in function](https://docs.python.org/3/library/functions.html) to
   return the length of the string that represent's Morrison's novel _The Bluest Eye_.

2. Assign the return value to a variable named `bluest_eye_len`.

3. Call the built-in `print()` function and pass it an f-string formatted as follows:

```python
f"bluest_eye char count = < variable >< newline >"
```

<br />

## 3.0 Object behaviors (a gentle intro)

The string (`str`) type or object can be said to exhibit behaviors that are expressed in the form of
_methods_ that you can call. For example, you can call `str.upper()` in order to return a version
of the string converted to all upper case characters:

```python
event = 'banned books week (18-24 September 2022)'
event_upper = event.upper()
```

Over the course of the semester you will learn to use a number of `str` methods. For a complete
listing see w3schools'
["Python String Methods"](https://www.w3schools.com/python/python_ref_string.asp).

:bulb: Other data types such as lists, tuples, and dictionaries also include methods you can call.
We will explore those types and their methods in the coming weeks.

Below are a few examples of `str` methods that you can call.

<br />

## 3.0.1 str.lower() / str.upper()

Return a version of the string in which its characters have been converted to either upper case or
lower case.

```python
title = 'Beyond Magenta'
lower_case = title.lower() # Returns 'beyond magenta'
upper_case = title.upper() # Returns 'BEYOND MAGENTA'
```

<br />

## 3.0.2 str.startswidth() / str.endswith()

Calling `str.startswidth()` returns `True` if the string commences with the specified value. Calling
`str.endswith()` returns `True` if the string ends with the specified value. In either case, if the
condition is not satisfied the method returns `False`.

```python
title = 'Out of Darkness'
starts_with_O = title.startswith('O') # Returns True
ends_with_S = title.endswith('S') # Returns False
```

<br />

## 3.0.3 str.count()

Return the number of times a specified value occurs in a string.

New York Times, The Learning Network, ['What Students Are Saying About Banning Books From School Libraries'](https://www.nytimes.com/2022/02/18/learning/students-book-bans.html) (New York Times, 18 Feb 2022)

```python
source = 'The Learning Network, "What Students Are Saying About Banning Books From School Libraries" (New York Times, 18 Feb 2022).'
char_a_count = source.count('a') # Returns 6
char_ban_count source.count('Ban') # Returns 1
```

<br />

## 3.0.4 str.replace()

Returns a new string by replacing the specified substring with a new value.

```python
ala_statement = 'The American Library Association condemns censorship and works to ensure free access to information.'
ala_statement = ala_statement.replace('American Library Association', 'ALA') # Returns 'The ALA condemns censorship and works to ensure free access to information.'
```

<br />

## 3.1 Challenge 06

__Task__. Fix a typo in a challenged book title using the appropriate string method that can return a corrected version of the string.

Angie Thomas's debut novel _The Hate U Give_ (2017) has been targeted for removal from library
collections nearly every year since its publication five years ago.

1. The string value assigned to the variable `hate_u_give` contains a typographical error in the
   book's title. Review w3schools'
   ["Python String Methods"](https://www.w3schools.com/python/python_ref_string.asp)
   list and select the appropriate string method that can be used to return a corrected version of the string.

2. Assign the return value to the (existing) variable `hate_u_give`.

   :bulb: Note the object identifier values returned by calling the built-in `id()` function in the
   accompany `print()` output. The id change demonstrates that the `hate_u_give` variable has
   been reassigned to a new string object.

<br />

## 3.2 Challenge 07

__Task__. Employ the appropriate string method that returns a count of the number of times a specified character occurs in the string object.

In 2020 the historian Ibram X. Kendi published _Stamped: Racism, Antiracism,
and You_, a young adult "remix" of his book _Stamped from the Beginning: The
Definitive History of Racist Ideas in America_ (2016). The book quickly emerged
as one of the most challenged books of 2020, ranking second on the ALA's
annual list.

1. Review w3schools'
   ["Python String Methods"](https://www.w3schools.com/python/python_ref_string.asp)
   list and select the appropriate string method that returns an integer value representing the
   number of times the character `i` occurs in the string `stamped`.

2. Assign the return value to the variable named `stamped_i_count`.

<br />

## 4.0 Basic Arithmetic

Python supports mathematical operations. The order of operations is expressed conveniently by the acronym
__PEMDAS__: Parentheses, Exponentation, Multiplication \| Division (same precedence), Addition \|
Subtraction.

1. Parentheses have the highest precedence and can be used to force an expression to evaluate in the
   order you want. Since expressions in parentheses are evaluated first, `2 * (3-1)` is 4, and
   `(1+1)**(5-2)` is 8. You can also use parentheses to make an expression easier to read, as in
   `(minute * 100) / 60`, even though it doesn’t change the result.

2. Exponentiation has the next highest precedence, so `2 ** 1 + 1` is 3 and not 4, and `3 * 1 ** 3`
   is 3 and not 27.

3. Multiplication and both division operators have the same precedence, which is higher than
   addition and subtraction, which also have the same precedence. So `2*3-1` yields 5 rather than 4,
   and `5-2*2` is 1, not 6.

4. Operators with the same precedence (except for **) are evaluated from left-to-right. In algebra
   we say they are left-associative. So in the expression `6-3+2`, the subtraction happens first,
   yielding 3. We then add 2 to get the result 5. If the operations had been evaluated from right
   to left, the result would have been `6-(3+2)`, which is 1.

<br />

## 4.0.1 Arithmetic operators

| Operator | Name | Description |
| :------- | :--- | :---------- |
| + | Addition | |
| - | Subtraction | |
| * | Multiplication | |
| / | (Floating Point) Division | Returns a floating-point value (a `float`) that contains a fractional component (`5 / 2` returns `2.5`).|
| // | Floor Division | Returns an integer (i.e., a whole number) ignoring any fractional component (`5 // 2` returns `2`). |
| % | Modulus | Returns the remainder of a division operation (e.g., `5 % 2` returns `1`).  |
| ** | Exponentiation | Returns the product of a number (the base) multiplied `n` times specified exponent (`2.5 ** 2` returns `6.25`). |

## 4.1 Challenge 08

__Task__. Determine the percentage of votes cast in favor of and against a proposed public library
millage held in Jamestown Charter Township, Ottawa County, Michigan on 2 August 2022.

On 2 August 2022 residents of
[Jamestown Charter Township](https://twp.jamestown.mi.us/) voted against a
proposed millage increase sought by the community-supported
[Patmos Library](http://www.patmoslibrary.org/). Without an approved millage
(a tax assessed on real property) to fund its operations the library is
likely to close in 2023. Jamestown Charter Township is located in Ottawa County, Michigan
(southwest of Grand Rapids, MI).

Press reports ascribe the millage defeat to the Patmos Library Board's refusal
to remove books featuring LGBTQIA+ themes from the library's collection. On
16 August 2022 the Library Board submitted a proposal to the Ottawa County
Clerk's Office to place the millage proposal on the upcoming November ballot.
Taxable property would be assessed $0.60 on each $1000.00 of taxable value
annually for a period of ten years.

1. Calculate the percentage of votes cast _both for and against_ the proposed
   library millage. Voting tallies are recorded below.

   ```python
   votes_cast = 3045
   votes_yes = 1141
   votes_no = 1904
   ```

2. Assign the computed percentage values to the variables: `votes_yes_pct` and
   `votes_no_percent`.

   :bulb: note the use of the format specifier `:.2f` in the f-strings. The
   specifier restricts the output of the float value to two decimal points.

<br />

## 4.2 Challenge 09

__Task__. Provide an estimate of Jamestown Charter Township voter turnout for the 2 August 2022
election.

The [US Census Bureau](https://www.census.gov/quickfacts/jamestownchartertownshipottawacountymichigan)
estimates that Jamestown Charter Township contains 9923 residents as of 1 July 2021. Residents under
the age of 18&mdash;who are ineligible to vote&mdash; are estimated to comprise 31.6% of the
population.

1. Determine the number of eligible voters who live in Jamestown Charter Township by constructing
   an arithmetic expression based on the following values:

   ```python
   pop_est_2021 = 9923
   pop_under_18 = .316
   ```

   :exclamation: Bear in mind that the number of eligible voters is likely to exceed the number of
   registered voters so the estimate of voter turnout that you will compute below is at best an
   approximation.

2. Assign the return value to a variable named `eligible_voters`.

3. Call the built-in `int()` function and convert the float value assigned to `eligible_voters` to
   an integer (whole number) value.

4. Assign the integer to `eligible_voters`.

5. Finally, determine the estimated voter turnout percentage by constructing an arithmetic
   expression based on values assigned to the following variables:

   * `votes_cast`
   * `eligible_voters`

6. Assign the return value to a variable named `turnout_est_pct`.

<br />

## Sources

* https://www.ala.org/advocacy/bbooks/frequentlychallengedbooks/top10
* https://www.ala.org/news/press-releases/2022/04/national-library-week-kicks-state-america-s-libraries-report-annual-top-10
* https://www.ala.org/news/state-americas-libraries-report-2022
* https://bannedbooksweek.org/
* https://en.wikipedia.org/wiki/Gender_Queer
* https://en.wikipedia.org/wiki/Lawn_Boy_(Evison_novel)
* https://en.wikipedia.org/wiki/All_Boys_Aren%27t_Blue
* https://en.wikipedia.org/wiki/Out_of_Darkness_(novel)
* https://en.wikipedia.org/wiki/The_Hate_U_Give
* https://en.wikipedia.org/wiki/The_Absolutely_True_Diary_of_a_Part-Time_Indian
* https://en.wikipedia.org/wiki/Me_and_Earl_and_the_Dying_Girl
* https://en.wikipedia.org/wiki/The_Bluest_Eye
* https://en.wikipedia.org/wiki/Beyond_Magenta
* https://www.census.gov/quickfacts/jamestownchartertownshipottawacountymichigan
* https://miottawavotes.gov/ElectionResults/Election/Summary/AUG0222
* https://www.bridgemi.com/michigan-government/upset-over-lgbtq-books-michigan-town-defunds-its-library-tax-vote
* https://www.bridgemi.com/michigan-government/donations-pour-after-michigan-town-defunded-library-over-lgbtq-books
* https://www.bridgemi.com/talent-education/romance-author-nora-roberts-helps-save-mi-library-defunded-over-lgbtq-books
* https://www.theguardian.com/books/2022/aug/05/michigan-library-book-bans-lgbtq-authors
* https://www.mlive.com/news/grand-rapids/2022/08/library-puts-millage-on-nov-8-ballot-after-voters-reject-first-request-amid-lgbtq-book-dispute.html
* https://www.nytimes.com/2022/02/18/learning/students-book-bans.html
