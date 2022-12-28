# SI 506 Lecture 11

## Topics

1. Function basics
   1. Defining and calling a function
   2. Specifying a parameter and a return value
   3. Multiple parameters
   4. Positional arguments (order matters)
   5. Challenge 01
2. Keyword arguments and optional parameters
   1. Keyword arguments
   2. Optional parameters
   3. Skipping optional parameters
   4. Challenge 02
3. Variable scope

<br />

## Vocabulary

* __Argument__. A value passed to a function or method that corresponds to a parameter defined for
  the function or method.
* __Caller__. The initiator of a function call.
* __Function__. A defined block of code that performs (ideally) a single task. Functions only run
  when they are explicitly called. A function can be defined with one or more _parameters_ that
  allow it to accept _arguments_ from the caller in order to perform a computation. A function can
  also be designed to return a computed value. Functions are considered "first-class" objects in the
  Python ecosystem.
* __Parameter__. A named entity in a function or method definition that specifies an argument that
  the function or method accepts.
* __Scope__. The part of a script or program in which a variable and the object to which it is
  assigned is visible and accessible.

<br />

## 1.0 Function basics

Writing a function in order to perform a particular task is a form of code modularization designed
to simplify otherwise complex processes. Functions also encourage code re-use and adherance to the
_Don’t Repeat Yourself_ (DRY) principle of software development.

<br />

## 1.1 Defining and calling a function

A function is defined using the keyword `def` and given a name that ends with an
open/close parentheses `()`.

:bulb: Per [PEP 8](https://pep8.org/#function-names):

> Function names should be lowercase, with words separated by underscores as necessary to improve
> readability.

In addition consider names employing a `< verb >_< noun >` format, such as `convert_to_int`,
`read_csv`, or `get_resource`.

In the example below a function named `print_slogan` is called by name and responds by calling the
built-in `print()` function and passing it a hard-coded string to print to the screen.

```python
def print_slogan():
    print('\n1.1 Snap, Crackle, Pop') # Kellogg's Rice Crispies slogan

print_slogan() # call function
```

:exclamation: A function's indented code block is executed if and only if the function is
called explicitly; otherwise, the code is ignored by the Python Interpreter.

<br />

## 1.2 Specifying a parameter and a return value

Functions are typically defined with one or more _parameters_ for accepting input along with a
return statement that signals the end of the computation and the "return" of a value to the caller.

:exclamation: A function call is an _expression_ (i.e., the call resolves to a value).

:exclamation: Functions that do not include a `return` statement return `None` to the caller.

In the example below the function named `print_slogan` is defined with a single parameter named
`slogan`. The function accepts input and returns a formatted string.

```python
def print_slogan(slogan):
    print(f"\n1.2 {slogan}")

slogan = 'They’rrrre GR-R-REAT'
print_slogan(slogan)
```

<br />

## 1.3 Multiple parameters

A function definition can specify multiple parameters. The caller _must_ pass to the function the
required number of _arguments_ or a runtime error will occur.

In the example below, the function `format_slogan` is called with the required arguments passed
_by position_. The function's return value is then assigned to a variable.

```python
def format_slogan(name, slogan):
    return f"{name} slogan: {slogan}"

cereal = 'Wheaties',
slogan = 'The Breakfast of Champions.'
wheaties_slogan = format_slogan(cereal, slogan) # positional arguments
```

<br />

## 1.4 Positional arguments (order matters)

If positional arguments are passed to a function, the caller must pass them in the correct order to
ensure that the function can process the values as expected.

In the example below, the function `format_slogan` is called but the arguments are passed to it in
the wrong order. The resulting computation returns an unexpected and incorrect value.

```python
cereal = 'Lucky Charms'
slogan = 'They’re always after me lucky charms' # General Mills Lucky Charms leprechaun
lucky_charms = format_slogan(slogan, cereal) # Oops! string reversed
```

<br />

## 1.5 Challenge 01

__Task__. Write a function that returns a list of cereal brands associated with a given manufacturer.

1. Implement a function named `get_cereals_by_company` that defines two parameters:

   * `cereal_brands` (`list`): a list of cereal brands
   * `company` (`str`): the name of a cereal producer

   The function returns a list of zero, one, or more cereal brands (__name only__) manufactured by
   the passed in company name.

2. Implement the accumulator pattern _inside_ the function block in order to accomplish the
   following sub-tasks:

   1. Create an empty list to accumulate cereal brand names that match the search criteria. Assign
      it to a variable named `brands`.

   1. Iterate over the passed in `cereal_brands` argument.

   2. Write an `if` statement that filters on the passed in `company` argument.

      :exclamation: The string comparison that you write _must_ allow the caller to pass in a string
      that __matches part or all__ of a company name (i.e., "Kellogg" or "kellogg" matches "Kellogg
      Company"); in other words a _case insensitive_ "near match" string comparison.

   3. After the loop terminates add a `return` statement that returns to the caller the new list of
      cereal brand names filtered on the company name.

3. After implementing `get_cereals_by_company` call the function and retrieve all cereal brands in
   `cereals` produced by Post Consumer Brands. Assign the function's return value to a variable
   named `post_cereals`.

4. Call the function __a second time__ and retrieve all cereal brands in `cereals` produced by the
   Kellogg Company. Assign the function's return value to the variable named `kellogg_cereals`.

5. Uncomment `print()` and check your work.

<br />

## 2.0 Keyword arguments and optional parameters

<br />

## 2.1 Keyword arguments

The caller of a function can pass _keyword arguments_, specifying both a key and value in the form
`key=value`. The argument is denoted by its keyword rather than by its position in the argument list.

Keyword arguments free you from having to worry about correctly ordering your arguments in the
function call, and they clarify the name of each value in the function call by binding the value
directly to the name.

:exclamation: note that by convention keyword arguments do not include spaces on either side of the
assignment operator

```python
general_mills_cereals = get_cereals_by_company(company='general mills', cereal_brands=cereals)
```

:exclamation: By convention keyword arguments do not include spaces on either side of the
assignment operator. The auto grader will check your keyword argument styling occasionally so style
your keyword arguments per [PEP 08](https://pep8.org/#other-recommendations):

```python
# Do this
some_var = some_func(arg_01=val_01, arg_02=val_02)

# Not this
some_var = some_func(arg_01 = val_01, arg_02 = val_02)
```

<br />

## 2.2 Optional parameters

As noted above, a function definition can specify one or more parameter values. Each parameter can
specify a default value. In such cases, the caller is not required to pass in a corresponding
argument unless a need exists to override the default value.

In the example below, the function `calculate_sugar_content` defines a parameter named `precision`
that determines the number of decimal places to round the return value. A default value of two (`2`)
is specified. The function can be called in one of two ways:

1. Pass one argument: the required cereal brand (a `list`). The function will then compute a value
   and round it the the second decimal place (the default `precision` value).
2. Pass two arguments: the required cereal brand (a `list`) and an integer that overrides the
   default `precision` value.

:exclamation: Optional parameters should be listed _after_ required parameters in order to allow
required arguments to be passed solely by position.

```python
def calculate_sugar_content(cereal_brand, precision=2):
    return round(cereal_brand[-1] / cereal_brand[-2], precision)
```

To simplify accessing individual cereal brands from the `cereals` list so that we can pass the
cereal to `calculate_sugar_content` as an argument, let's write a "helper" function named
`get_cereal`. This function will retrieve a a list representation of a cereal brand by its name.

```python
def get_cereal(cereal_brands, cereal_name):
    for cereal in cereal_brands[1:]:
        if cereal_name.lower() in cereal[1].lower():
            return cereal # match, exit loop immediately
```

:bulb: Note the placement of the `return` statement _inside_ the `if` statement block. If the
condition resolves to `True` the matching cereal (a `list`) is returned immediately to the caller,
the loop is terminated, and the function is exited. If no match is obtained the function returns
`None` (implicitly) to the caller. This is an efficient design as it eliminates unnecessary looping
that implementation of the accumulator pattern would induce.

The caller can now easily retrieve a cereal from the `cereals` list, calculate its sugar content,
and round the value to be returned to any number of decimal places.

```python
# Retrieve cereal
cocoa_puffs = get_cereal(cereals, 'Cocoa Puffs')

# Accept precision default value
cocoa_puffs_sugar = calculate_sugar_content(cocoa_puffs)

# Override precision default value
cocoa_puffs_sugar = calculate_sugar_content(cocoa_puffs, 4) # override

# Pass get_cereal() as an argument
cocoa_puffs_sugar = calculate_sugar_content(get_cereal(cereals, 'Cocoa Puffs'), 3)
```

<br />

## 2.3 Skipping optional parameters

If a function definition includes _multiple_ optional parameters, keyword arguments
_must_ be employed whenever a preceeding optional argument is skipped when calling the function.

In the example below the function returns either a percentage value formatted as string or float
value. If the caller passes to the function an optional `precision` value (say `3`), a keyword
argument must be passed to ensure the correct parameter binding if the optional `format_pct` value
is not specified explicitly by the caller.

```python
def calculate_sugar_content_v2(cereal_brand, format_pct=False, precision=2):
    if format_pct:
        return f"{cereal_brand[-1] / cereal_brand[-2] * 100:.{precision}f}%" # note trailing percent (%) sign
    else:
        return round(cereal_brand[-1] / cereal_brand[-2], precision)

raisin_bran = get_cereal(cereals, 'raisin bran')

# 3 binds to wrong parameter, string returned
raisin_bran_sugar = calculate_sugar_content_v2(raisin_bran, 3)

# Keyword argument binds 3 correctly, returns float
raisin_bran_sugar = calculate_sugar_content_v2(raisin_bran, precision=3) # use keyword argument

# Returns formatted string
raisin_bran_sugar = calculate_sugar_content_v2(raisin_bran, format_pct=True, precision=3)

# Returns formatted string
raisin_bran_sugar = calculate_sugar_content_v2(raisin_bran, True, 3)
```

<br />

# 2.4 Challenge 02

__Task__: Retrieve cereal(s) with the highest sugar content.

1. Setup: The following variable assignments have been pre-positioned for your use:

   ```python
   headers = cereals[0]
   cereals_max_sugar = []
   max_sugar_content = 0
   ```

2. Implement the function named `get_cereal_attribute`. The function defines three parameters:
   1. cereal (`list`): list representation of a cereal brand
   2. headers (`list`): list representing data column headers
   3. header (`str`): header value to filter on

   The function utilizes the cereal `headers` and the `header` column name to look up a cereal
   attribute (i.e., element) by its index and then returns it to the caller.

   :bulb: Replace the placeholder `pass` statement in the function block with your code. The
   function block requires only a single line of code.

3. Re-implement (i.e., refactor) the original `calculate_sugar_content` function and name it `calculate_sugar_content_v3`. The function defines three parameters:

    1. serving_size_gm (`int`): serving size in grams
    2. sugar_gm (`float`): sugar in grams
    3. precision (`int`): Number of decimal places to retain (default = 2)

    The function divides the `sugar_gm` by `serving_size_gm`, rounds the result per the `precision`
    value, and returns the rounded value to the caller.

    :bulb: Replace the placeholder `pass` statement in the function block with your code. The
    function block requires only a single line of code.

4. Loop over the cereals in the `cereals` list. Inside the loop block, call the function
   `get_cereal_attribute` __three times__ in order to retrieve the following values that you _must_
   assign to the specified variables:

   1. `brand`: cereal name
   2. `serving_size_gm`: cereal's listed serving size (grams)
   3. `sugar_gm`: cereal's sugar ingredient (grams)

   :exclamation: For each call you _must_ pass the required and optional arguments not by position
   but __in reverse order__ employing __keyword arguments__.

5. After retrieving the current cereal's serving size and sugar values, call the function
   `calculate_sugar_content_v3` passing it the required two arguments. Assign the return value to a
   variable named `sugar_content`.

6. Implement `if-elif` or `if-elif-else` logic to check if the current cereal possesses the highest
   sugar content. If the cereal's `sugar_content` is higher than the previous `max_sugar_content`,
   do the following:

   1. Update `max_sugar_content`.
   2. Remove all elements from the `cereals_max_sugar` list.
   3. Append the cereal name to `cereals_max_sugar`.

   If the cereal's `sugar_content` is equal to the previous `max_sugar_content` add the cereal name
   to the `cereals_max_sugar`.

7. After the loop terminates uncomment `print()` and check your work.

< br />
## 3.0 Variable scope

Now that you have begun to write functions it's time to discuss Python's rules for resolving name
references (i.e., variables). Accessing a variable and the object to which it is assigned depends in
large part on _where_ the variable is defined in your program. An object's duration or lifetime also
depends in part on _where_ in your program it is assigned. A variable's _scope_ is limited to those
parts of a program in which the variable is visible and can be accessed.

A variable defined _inside_ a function is considered _local_ to that function. In other words, a
local variable can only be accessed from inside the function's code block. On the other hand, a
variable defined outside a function in the main part of a program file or module possesses top level
or _global_ scope. Such a variable is visible throughout the program from the point in which it was
first defined. Treat _global_ variables carefully. Referencing _global_ variables inside functions
can have unintended effects.

Python keywords and built-in functions possess a special _built-in_ scope and are also
available whenever you execute a script or run your program.

Recall the Challenge 01 function named `get_cereals_by_company`.

```python
def get_cereals_by_company(cereal_brands, company):
    brands = []
    for cereal in cereal_brands:
        if cereal[0].lower().startswith(company.lower()):
            brands.append(cereal[1])
    return brands
```

Note the accumulator variable named `brands`. The variable possesses "local" scope and is only
available within the function block.

You can test this by attempting to access the variable from outside the function. For example, if
you attempt to pass `brands` to the built-in `print()` function outside the function block you will
trigger a `NameError` runtime exception:

```commandline
NameError: name 'brands' is not defined
```
