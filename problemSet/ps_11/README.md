# SI 506: Problem Set 11

## This week's Problem Set
This week, we focus on modules and caching.
You will work on two Python files: `problem_set_11.py` and `five_oh_six.py`, where the `problem_set_11.py` file is the main workspace that imports functions from `five_oh_six.py`.

## Data
The data used in this
assignment is sourced from the [Star Wars API](https://swapi.py4e.com/) (SWAPI) and
[Wookieepedia](https://starwars.fandom.com/wiki/Main_Page)

__Caching__: This assignment utilizes a local "cache" dictionary located in the utilities module
that eliminates redundant HTTP GET requests made to SWAPI by storing the SWAPI responses locally.
The caching workflow is implemented _fully_ and all you need do is call the function
`get_swapi_resource` whenever you need to retrieve a SWAPI representation of a person/droid,
planet, species, or starship.

:exclamation: _Do not_ call `utl.get_resource` directly. Doing so sidesteps the
cache and undercuts the built-in caching optimization strategy.

The cache dictionary is written to a JSON file every time you run `problem_set_11.py`:

```python
# PERSIST CACHE (DO NOT COMMENT OUT)
utl.write_json(utl.CACHE_FILEPATH, utl.cache)
```

The cache JSON document will remain empty until you start working on the problem set. Thereafter the
cache file will record resources retrieved from SWAPI.

# PROBLEM 01

## 1.1 Refactor `utl.read_csv_to_dicts`

__Task__ In `five_oh_six.py`, examine the commented out code in the `read_csv_to_dicts` function (__do not__ uncomment).
Reimplement the function by writing code in the `with` block that retrieves an instance of
`csv.DictReader` and employs a list comprehension to traverse the lines in the reader object and
return a new list of line elements to the caller.

### Requirements

1. You are limited to writing two (2) lines of code.

   1. Line 01 assigns an instance of `csv.DictReader` to a variable named `reader`.
   2. Line 02 returns a new list of `reader` "line" elements to the caller using
      __a list comprehension__.

2. You _must_ employ existing variable names that appear in the commented out code when writing
   your list comprehension (i.e., `reader`, `line`).

:exclamation: Review lecture notes and code solution files if you have forgotten how to write a list
comprehension. If you are unsuccessful in your endeavors uncomment the code in `utl.read_csv_to_dicts`
and get the function working so that you can continue with the assignment.

## 1.2 Call `utl.read_csv_to_dicts`

After refactoring `utl.read_csv_to_dicts`, navigate to `main` in `problem_set_11.py`. Call the `read_csv_to_dicts` function, accessed from the imported `five_oh_six.py` module, and retrieve the
data contained in the file `mandalorian_people.csv`. Assign the return value to a variable named
`mandalorian_people`.

## 1.3 Call `utl.read_json`

Call the `read_json` function, accessed from the imported `five_oh_six.py` module, and retrieve the data contained in the file `mandalorian_starships.json`. Assign the return value to a variable named
`mandalorian_starships`.

Call the `read_json` function, accessed from the imported `five_oh_six.py` module, and retrieve the data contained in the file `mandalorian_planets.json`. Assign the return value to a variable named
`mandalorian_planets`.

Call the `read_json` function, accessed from the imported `five_oh_six.py` module, and retrieve the data contained in the file `mandalorian_droids.json`. Assign the return value to a variable named
`mandalorian_droids`.

Call the `read_json` function, accessed from the imported `five_oh_six.py` module, and retrieve the data contained in the file `mandalorian_vehicles.json`. Assign the return value to a variable named
`mandalorian_vehicles`.

# PROBLEM 02

__Task__: Implement the functions `utl.convert_to_none`, `utl.convert_to_int`,
`utl.convert_to_float`, and `utl.convert_to_list`. Each function attempts to convert a passed in
`value` to a more appropriate type.

## 2.1 Implement `value` Conversion Functions

For each `convert_to_...` function you will replace `pass` with a code block that attempts to convert the passed in `value` to the requested value type.

Review each function's docstring to better understand the task it is to perform, the parameters it defines,
and the return value it computes.

The functions carry out the tasks of converting strings to
   either `int`, `float`, or `list` per the conversion chart below.

   | Conversion | value(s) | Delegate to | Notes |
   | :--------- | :------- | :---------- | :---- |
   | `str` to `int` | 'series_season_num', 'series_episode_num', 'season_episode_num' | `utl.convert_to_int()` | Blank values are converted to `None` if `utl.convert_to_none` is called by `utl.convert_to_int`. |
   | `str` to `float` | 'episode_prod_code', 'episode_us_viewers_mm' | `utl.convert_to_float()` | Blank values are converted to `None` if `utl.convert_to_none` is called by `utl.convert_to_float`. |
   | `str` to `list` | 'episode_writers' | `utl.convert_to_list()` | |

### 2.1.1 `utl.convert_to_none` function

### Requirements

In `five_oh_six.py`, navigate to the `convert_to_none` function definition. Replace `pass` with a code block that attempts to convert the passed in `value` to `None`. Review
the function's docstring to better understand the task it is to perform, the parameters it defines,
and the return value it computes.

1. The function _must_ employ `try` and `except` statements in order to handle runtime exceptions
   whenever an invalid type conversion is attempted. __Do not__ place code outside the `try`/`except`
   code blocks.

2. The function _must_ perform a __case-insensitive__ comparison between the passed in `value` and
   the items in the `utl.NONE_VALUES` tuple constant:

   ```python
   NONE_VALUES = ('', 'n/a', 'none', 'unknown')
   ```

   If a match is obtained inside the `try` block the function will return `None` to the caller,
   otherwise, the value will be returned unchanged.

   :exclamation: Don't assume that `value` is "clean"; program defensively and remove
   leading/trailing spaces before checking if the "cleaned" version of the string matches a
   `utl.NONE_VALUES` item.

3. If a runtime exception is encountered the `except` block will "catch" the exception and the
   `value` will be returned to the caller _unchanged_.

   :bulb: You do not need to specify a specific exception in the `except` statement.

### 2.1.2 `utl.convert_to_int` function

In `five_oh_six.py`, navigate to the `convert_to_int` function definition. Replace `pass` with a code block that attempts to convert the passed in `value` to an `int`. Review the function's docstring to better understand the task it is to perform, the parameters it defines,
and the return value it computes.

### Requirements

1. The function _must_ employ `try` and `except` statements in order to handle runtime exceptions
   whenever an invalid type conversion is attempted. __Do not__ place code outside the `try`/`except`
   code blocks.

2. The function _must_ convert numbers masquerading as strings, including those with commas that
   represent a thousand separator:

   * "5" -> 5
   * "50,000" -> 50000
   * "5,000,000" -> 5000000

3. If a runtime exception is encountered the `except` block will "catch" the exception, pass the
   `value` to the function `convert_to_none`, and then return the value returned by `convert_to_none` to
   the caller.

   :bulb: You do not need to specify a specific exception in the `except` statement.

### 2.1.3 `utl.convert_to_float` function

In `five_oh_six.py`, navigate to the `convert_to_float` function definition. Replace `pass` with a code block that attempts to convert the passed in `value` to a `float`. Review the function's docstring to better understand the task it is to perform, the parameters it defines, and the return value it computes.

### Requirements

1. The function _must_ employ `try` and `except` statements in order to handle runtime exceptions
   whenever an invalid type conversion is attempted. __Do not__ place code outside the `try`/`except`
   code blocks.

2. If a runtime exception is encountered the `except` block will "catch" the exception, pass the
   `value` to the function `convert_to_none`, and then return the value returned by
   `convert_to_none` to the caller.

   :bulb: You do not need to specify a specific exception in the `except` statement.

### 2.1.4 `utl.convert_to_list` function

In `five_oh_six.py`, navigate to the `convert_to_list` function definition. Replace `pass` with a code block that attempts to convert the passed in `value` to a `list` using a
`delimiter` if one is provided. Review the function's docstring to better understand the task it is
to perform, the parameters it defines, and the return value it computes.

:bulb: Model `convert_to_list` on the other type conversion functions. This challenge involves
adjusting your implementation per the hints below so that the function can handle converting
strings to lists or return the passed in value _unchanged_ if a runtime exception is encountered.

### Requirements

1. The function _must_ employ `try` and `except` statements in order to handle runtime exceptions
   whenever an invalid type conversion is attempted. __Do not__ place code outside the `try`/`except`
   code blocks.

2. If the passed in `value` matches an item in the `utl.NONE_VALUES` tuple
   (__case-insensitive comparison__), the function _must_ return `None`.

3. If a delimiter value is provided the function will use it to split the `value`; otherwise, the
   string will be split without specifying a delimiter value.

   :bulb: Note that the function's `delimiter` parameter defaults to `None`. You _must_ check the
   truth value of `delimiter` in the function block. If `True` pass the delimiter value to the
   appropriate `str` method; otherwise rely on the `str` method's default behavior.

   :exclamation: Don't assume that `value` is "clean"; program defensively and remove
   leading/trailing spaces before attempting to convert the "cleaned" version of the string to a list.

4. If a runtime exception is encountered the `except` block will "catch" the exception and the
   `value` will be returned to the caller _unchanged_.

   :bulb: You do not need to specify a specific exception in the `except` statement.

### 2.1.5 Call the functions

After implementing the four `value` conversion functions, return to `problem_set_11.py`. In `main` test the functions by uncommenting the print statements provided. These statements call each of the conversion functions and check if the return value is equivalent to the expected value.

For example the code below should produce the following output.

Python code:

```python
print(f"\n2.1.1 convert_to_none -> None = {utl.convert_to_none(' N/A ')}")
```

Expected output:

```terminal
2.1.1 convert_to_none -> None = None
```

## 2.2 Implement `convert_gravity_value`

In `problem_set_11.py`, navigate to the `convert_gravity_value` function definition. Replace `pass` with a code block that attempts to convert a planet's `"gravity"` value to a float by
first removing the "standard" unit of measure substring (if it exists) before converting the
remaining number to a float.

Review the function's docstring to better understand the task it is to perform, the parameters it defines, and the return value it computes.

:bulb: Note that `"gravity"` values vary from planet to planet. The following examples illustrate
the challenge:

```python
{
    'name': Tatooine,
    ...
    'gravity': '1 standard',
    ...
}
```

```python
{
   'name': Dagobah,
    ...,
    'gravity': 'N/A',
    ...
}
```

```python
{
    'name': Haruun Kal,
    ...
    'gravity': '0.98',
    ...
}
```

### Requirements

1. The function _must_ employ `try` and `except` statements in order to handle runtime exceptions
   whenever an invalid type conversion is attempted. __Do not__ place code outside the `try`/`except`
   code blocks.

2. The function _must_ __remove__ the substring `"standard"` if it exists anywhere in the passed in
   `value` _irrespective of case_. In other words lowercase, mixed case, and uppercase versions of
   the substring must be removed.

3. If the substring `"standard"` exists in `value`, remove it and return a version of `value` that contains only
   the numeric portion of the string.

   :bulb: a handy `str` method exists for locating substrings in a string.

   :exclamation: Don't assume that `value` is "clean"; program defensively and remove
   leading/trailing spaces before attempting to convert the "cleaned" version of the string to a
   float.

4. The function _must_ delegate to the function `utl.convert_to_float` the task of converting the
   "numeric" version of `value` to a float. The return value of `utl.convert_to_float` is then
   returned to the caller.

5. If a runtime exception is encountered the `except` block will "catch" the exception, pass the
   `value` to the function `utl.convert_to_none`, and then return the value returned by
   `utl.convert_to_none` to the caller.

### 2.2.1 Call `convert_gravity_value`

After implementing `convert_gravity_value` test the function in `main` by uncommenting the print statements provided. These statements call the `convert_gravity_value` functions and check if the value is equivalent to the expected value.

For example the code below should produce the following output.

Python code:

```python
print(f"\n2.2.1 convert_gravity_value -> float = {convert_gravity_value('1 standard')}")
```

Expected output:

```terminal
2.2.1 convert_gravity_value -> float = 1.0
```


# PROBLEM 03 

## 3.1 `get_mandalorian_data` function

In `problem_set_11.py`, navigate to the `get_mandalorian_data` function definition. Replace `pass` with a code block that utilizes a `filter` string to return a nested dictionary from
the passed in `mandalorian_data` list if the dictionary's `"name"` value matches the `filter` value.
Review the function's docstring to better understand the task it is to perform, the parameters it
defines, and the return value it computes.

The function can be employed to traverse lists of nested dictionaries sourced from the
following files in search of a particular dictionary representation of a Star Wars droid,
person, planet, or starship:

* `mandalorian_droids.json`
* `mandalorian_people.csv`
* `mandalorian_planets.json`
* `mandalorian_starships.json`
* `mandalorian_vehicles.json`

### Requirements

1. The function must perform a __case insenstitive__ comparison between the passed in `filter`
   value and each nested dictionary's `"name"` value. If a match is obtained it returns the nested
   dictionary to the caller.

2. If no match is obtained the function returns `None` to the caller.

### 3.1.1 Call `get_mandalorian_data`

After implementing `get_madalorian_data`, return to the `main` function:

* Call `get_madalorian_data` and pass to it as arguments `mandalorian_planets` as the data and `'nevarro'` as the filter term. Assign the return value to the variable name `mandalorian_nevarro`
* Call `get_madalorian_data` and pass to it as arguments `mandalorian_planets` as the data and `'ARVALA-7'` as the filter term. Assign the return value to the variable name `mandalorian_arvala_7`

### 3.1.2 Write to file

Check your work. Call the function `write_json`, accessed from the imported `five_oh_six.py` module, to write `mandalorian_nevarro` to the file
`stu-mandalorian_nevarro.json` and write `mandalorian_arvala_7` to the file `stu-mandalorian_arvala_7.json`. Compare your files to the test fixture files `fxt-mandalorian_nevarro.json` and `fxt-mandalorian_arvala_7.json`.

Both files _must_ match line-for-line, character-for-character, and indent-for-indent.

## 3.2 `create_planet` function

In `problem_set_11.py`, navigate to the `create_planet` function definition. Replace `pass` with a code block that returns a new planet dictionary based on the passed in `data`
dictionary. Review the function's docstring to better understand the task it is to perform, the
parameters it defines, and the return value it computes.

### Requirements

Certain `data` values require special handling and are subject to the following type conversion
rules:

1. Convert all `data` values to `None` that match any of the `utl.NONE_VALUES` items
   (case-insensitive match of strings stripped of leading/trailing spaces). This can be accomplished
   by judicious use of the `utl.convert_to_*` functions.

2. Convert other `data` values to `int`, `float` or `list` as specified in the table below.

   :exclamation: The new dictionary may contain keys that differ from the passed in `data`
   dictionary keys.

   | `data` | Convert to | Notes |
   | :----- | :------ | :------ |
   | suns (`str`) | suns (`int`) | |
   | moons (`str`) | moons (`int`) | |
   | orbital_period (`str`) | orbital_period_days (`float`) | |
   | diameter (`str`) | diameter_km (`int`) | |
   | gravity (`str`) | gravity_std (`float`) | |
   | climate (`str`) | climate (`list`) | |
   | terrain (`str`) | terrain (`list`) | |
   | population (`str`) | population (`int`) | |

### 3.2.1 Create the planet Tatooine

After implementing `create_planet` return to `main`. Call the function `get_swapi_resource` and retrieve
a SWAPI representation of the planet [Tatooine](https://starwars.fandom.com/wiki/Tatooine). Access
the "Tatooine" dictionary which is stored in the response object and assign the value to
`swapi_tatooine`.

:bulb: The `five_oh_six` module includes a SWAPI "planets" URL constant that you can pass as the
`url` argument. If you need help constructing the `params` argument review the lecture notes and
code.

Call the function `create_planet()` and pass the updated `swapi_tatooine` as the argument. Assign
the return value to a variable named `tatooine`.

### 3.2.2 Write to file

Check your work. Call the function `write_json`, accessed from the imported `five_oh_six.py` module, and write `tatooine` to the file
`stu-tatooine.json`. Compare your file to the test fixture file `fxt-tatooine.json`. Both files
_must_ match line-for-line, character-for-character, and indent-for-indent.

# PROBLEM 04
## 4.1 `create_droid` function

In `problem_set_11.py`, navigate to the `create_droid` function definition. Replace `pass` with a code block that returns a new droid dictionary based on the passed in `data`
dictionary. Review the function's docstring to better understand the task it is to perform, the
parameters it defines, and the return value it computes.

### Requirements

Certain `data` values require special handling and are subject to the following type conversion
rules:

1. Convert all `data` values to `None` that match any of the `utl.NONE_VALUES` items
   (case-insensitive match of strings stripped of leading/trailing spaces). This can be accomplished
   by judicious use of the `utl.convert_to_*` functions.

2. Convert other `data` values to `int`, `float` or `list` as specified in the table below.

   | `data` | `Droid` | Notes |
   | :----- | :------ | :---- |
   | height (`str`) | height_cm (`float`) | |
   | mass (`str`) | mass_kg (`float`) | |
   | equipment (`str`) | equipment (`list`) | Check delimiter in `wookieepedia_droids.json`. |

### 4.1.1 Create the droid IG-11

After implementing `create_droid` return to `main`. Call the `get_mandalorian_data` function and retrieve a dictionary representation of the droid IG-11 pass `mandalorian_droids` and `ig-11` as arguments. Assign the return
value to `mandalorian_ig_11`.

Call the function `create_droid()` and pass `mandalorian_ig_11` dictionary as the argument. Assign the
return value to a variable named `ig_11`.

### 4.1.2 Write to file

Check your work. Call the function `write_json`, accessed from the imported `five_oh_six.py` module, and write `ig_11` to the file
`stu-ig_11.json`. Compare your file to the test fixture file `fxt-ig_11json`. Both files
_must_ match line-for-line, character-for-character, and indent-for-indent.

## 4.2 `create_species` function

In `problem_set_11.py`, navigate to the `create_species` function definition. Replace `pass` with a code block that returns a new species dictionary based on the passed in
`data` dictionary. Review the function's docstring to better understand the task it is to perform,
the parameters it defines, and the return value it computes.

### Requirements

Certain `data` values require special handling and are subject to the following type conversion
rules:

1. Convert all `data` values to `None` that match any of the `utl.NONE_VALUES` items
   (case-insensitive match of strings stripped of leading/trailing spaces). This can be accomplished
   by judicious use of the `utl.convert_to_*` functions.

2. Convert other `data` values to `int`, `float` or `list` as specified in the table below.

   | `data` | `Droid` | Notes |
   | :----- | :------ | :---- |
   | average_lifespan (`str`) | average_lifespan (`int`) | |
   | average_height(`str`) | average_height_cm (`float`) | |

### 4.2.1 Create the species human

After implementing `create_species` return to `main`. Call the function `get_swapi_resource` and retrieve
a SWAPI representation of the human species. Assign the return value to `swapi_human_species`.

:bulb: The `problem_set_11` includes a SWAPI "species" URL constant that you can pass as the
`url` argument. If you need help constructing the `params` argument review the lecture notes and
code.

Call the function `create_species()` and pass `swapi_human_species` as the
argument. Assign the return value to a variable named `human_species`.

### 4.2.2 Write to file

Check your work. Call the function `write_json`, accessed from the imported `five_oh_six.py` module, and write `human_species` to the file
`stu-human_species.json`. Compare your file to the test fixture file `fxt-human_species.json`. Both
files _must_ match line-for-line, character-for-character, and indent-for-indent.

## 4.3 `create_person` function

In `problem_set_11.py`, navigate to the `create_person` function definition. Replace `pass` with a code block that returns a new person dictionary based on the passed in `data`
dictionary. Review the function's docstring to better understand the task it is to perform, the
parameters it defines, and the return value it computes.

### Requirements

Certain `data` values require special handling and are subject to the following type conversion
rules:

1. Convert all `data` values to `None` that match any of the `utl.NONE_VALUES` items
   (case-insensitive match of strings stripped of leading/trailing spaces). This can be accomplished
   by judicious use of the `utl.convert_to_*` functions.

2. Convert other `data` values to `int`, `float`, `dict`, or `list` as specified in the table below.

   | `data` | `Person` | Notes |
   | :----- | :------ | :---- |
   | height (`str`) | height_cm (`float`) | |
   | mass (`str`) | mass_kg (`float`) | |
   | homeworld (`str`) | homeworld (`dict`) | Retrieve from the cache or from SWAPI if the data is not available locally; update values with the passed in `planets` data if not `None`. |
   | species (`str`) | species (`dict`) | Retrieve from the cache or from SWAPI if the data is not available locally. |

3. :exclamation: The person's "homeworld" value _must_ be converted to a dictionary representation
   of the home planet. Implement the following steps in your code to produce the required
   "homeworld" key-value pairs:

   1. Check if an optional Wookieepedia-sourced `planets` list is provided. Call `get_mandalorian_data`
      and attempt to retrieve data that can be used to update the homeworld
      dictionary.
   2. Retrieve the planet dictionary from the cache or from SWAPI if the data is not available
      locally.
   3. Call `create_planet` and pass it the (updated) homeworld dictionary.
   4. Assign the return value to the person's `homeworld` key.

4. :exclamation: The person's "species" value _must_ also be converted to a dictionary
   representation of the species. Retrieve the species dictionary from the cache or from SWAPI if
   the data is not available locally. Once retrieved call `create_species` and pass the SWAPI
   species dictionary to it and assign the return value to the person's "species" key.

    :bulb: The value stored in homeworld and species may differ depending on the person. Implement a `try`/`except` block when retrieving information from SWAPI using `get_swapi_resource`. The following examples illustrate the challenge:

    ```python
    {
    "name": "Carasynthia Dune",
    ...
    "homeworld": "https://swapi.py4e.com/api/planets/2/",
    "species": "https://swapi.py4e.com/api/species/1/",
    ...
    },
    {
    "name": "Boba Fett",
    ...
    "homeworld": "Kamino",
    "species": "Human",
    ...
    }
    ```
## 4.3.1 Create Din Djarin
#### Background
Since the fall of the Mandalorians, one of the few surviving Mandalorians, Din Djarin, works as a bounty hunter for the Bounty Hunter Guild. 

After implementing `create_person` return to `main`. Call the `get_mandalorian_data` function pass to it `mandalorian_people` and `'Din Djarin'`.
Assign the return value to `mandalorian_din_djarin`.

Call the function `create_person()` and pass `mandalorian_din_djarin` _and_ `mandalorian_planets` as
the arguments. Assign the return value to a variable named `mando`.

## 4.3.2 Write to file

Check your work. Call the function `write_json`, accessed from the imported `five_oh_six.py` module, and write `mando` to the file
`stu-mando.json`. Compare your file to the test fixture file `fxt-mando.json`.
Both files _must_ match line-for-line, character-for-character, and indent-for-indent.

# PROBLEM 05

## 5.1 `create_starship` function

In `problem_set_11.py`, navigate to the `create_starship` function definition. Replace `pass` with a code block that returns a new starship dictionary based on the passed in
`data` dictionary. Review the function's docstring to better understand the task it is to perform,
the parameters it defines, and the return value it computes.

### Requirements

Certain `data` values require special handling and are subject to the following type conversion
rules:

1. Convert all `data` values to `None` that match any of the `utl.NONE_VALUES` items
   (case-insensitive match of strings stripped of leading/trailing spaces). This can be accomplished
   by judicious use of the `utl.convert_to_*` functions.

2. Convert other `data` values to `int`, `float` or `list` as specified in the table below.

   | `data` | `Starship` | Notes |
   | :----- | :------ | :---- |
   | length (`str`) | length_m (`float`) | |
   | max_atmosphering_speed (`str`) | max_atmosphering_speed (`int`) | |
   | hyperdrive_rating (`str`) | hyperdrive_rating (`float`) | |
   | armament (`str`) | armament (`list`) | Check delimiter in `mandalorian_starships.json`. |
   | cargo_capacity (`str`) | cargo_capacity_kg (`int`) | |

   <br />

### 5.1.1 Create the Mandalorian's starship _Razor Crest_

Call `get_mandalorian_data` passing the appropriate arguments and retrieve the starship
named [_Razor Crest_](https://starwars.fandom.com/wiki/Razor_Crest) in `mandalorian_starships`. 
Pass the return value to `create_starship`. Assign the final
return value to a variable named `razor_crest`.

### 5.1.2 Write to file

Check your work. Call the function `write_json`, accessed from the imported `five_oh_six.py` module, and write `razor_crest` to the file
`stu-razor_crest.json`. Compare your file to the test fixture file `fxt-razor_crest.json`.
Both files _must_ match line-for-line, character-for-character, and indent-for-indent.

## 5.2 `create_vehicle` function

In `problem_set_11.py`, navigate to the `create_vehicle` function definition. Replace `pass` with a code block that returns a new vehicle dictionary based on the passed in
`data` dictionary. Review the function's docstring to better understand the task it is to perform,
the parameters it defines, and the return value it computes.

### Requirements

Certain `data` values require special handling and are subject to the following type conversion
rules:

1. Convert all `data` values to `None` that match any of the `utl.NONE_VALUES` items
   (case-insensitive match of strings stripped of leading/trailing spaces). This can be accomplished
   by judicious use of the `utl.convert_to_*` functions.

2. Convert other `data` values to `int`, `float` or `list` as specified in the table below.

   | `data` | `Vehicle` | Notes |
   | :----- | :------ | :---- |
   | length (`str`) | length_m (`float`) | |
   | max_atmosphering_speed (`str`) | max_atmosphering_speed (`int`) | |
   | hyperdrive_rating (`str`) | hyperdrive_rating (`float`) | |
   | MGLT (`str`) | top_speed_mglt (`int`) | A megalight, the standard unit of distance in space.|
   | armament (`str`) | armament (`list`) | Check delimiter in `mandalorian_starships.json`. |
   | cargo_capacity (`str`) | cargo_capacity_kg (`int`) | |

   <br />

### 5.2.1 Create the Sand Crawler vehicle

After implementing `create_vehicle` return to `main`. Call the function `get_swapi_resource` and retrieve
a SWAPI representation of the sand crawler vehicle. Assign the return value to `swapi_sand_crawler`.

:bulb: The `problem_set_11` includes a SWAPI "vehicles" URL constant that you can pass as the
`url` argument. If you need help constructing the `params` argument review the lecture notes and
code.

Call the function `create_vehicles()` and pass `swapi_sand_crawler` as the
argument. Assign the return value to a variable named `sand_crawler`.

### 5.2.2 Write to file
Check your work. Call the function `write_json`, accessed from the imported `five_oh_six.py` module, and write `sand_crawler` to the file
`stu-sand_crawler.json`. Compare your file to the test fixture file `fxt-sand_crawler.json`. Both
files _must_ match line-for-line, character-for-character, and indent-for-indent.

## 5.3 `board_passengers` function

In `problem_set_11.py`, navigate to the `board_passengers` function definition. Replace `pass` with a code block that assigns passengers to a starship. Review the function's
docstring to better understand the task it is to perform, the parameters it defines, and the return
value it computes.

### Requirements

1. The passengers _must_ be passed in a list to the `board_passengers` function.

2. The number of passengers permitted to board a starship is limited by the starship's
   `"max_passengers"` value. If the number of passengers attempting to board exceeds the starship's
   `"max_passengers"` value only the first `n` passengers (where `n` = "max_passengers") are permitted
   to board the vessel. This limitation _must_ be imposed by the `board_passengers` function and
   will be subject to auto grader testing.

   For example, if a starship's `"max_passengers"` value equals `10` and `20` passengers attempt to
   board the starship, only the first `10` passengers are permitted to board the vessel.

3. After boarding the passengers return the starship to the caller.

### 5.3.1 Get the Mandalorian Din Djarin aboard the _Razor Crest_

After implementing `board_passengers` return to `main`. Call the function `board_passengers` and pass the following arguments to it:

* `razor_crest`
* a list of passengers comprising only of the variable `mando`

Assign the return value to the variable `razor_crest`.

# PROBLEM 06
#### Background

The Mandalorian's story begins on the planet Nevarro. The function `update_planets_visited` will keep track of the planets the Mandalorian visits. Greef Karga is an inhabitant of the planet Nevarro and leader of the Bounty Hunter's Guild. Greef Karga provides intel on bounty hunter assignments. 

## 6.1 `update_planets_visited` function

In `problem_set_11.py`, navigate to the `update_planets_visited` function definition. Replace `pass` with a code block that adds a starship's name to the `'planets_visited'` key. Review the function's
docstring to better understand the task it is to perform, the parameters it defines, and the return
value it computes.

### 6.1.1 Call `update_planets_visited`

After implementing `update_planets_visited`, return to the `main` function. Call `update_planets_visited`  pass `razor_crest` and the planet name stored in the `mandalorian_nevarro` dictionary as arguments. Assign the return value to `razor_crest`.

Check your work by uncommenting the print statement provided for you.

Expected output:

```terminal
6.1.1 razor crest visited planets = ['Nevarro']
```

## 6.2 Create Greef Karga

In the `main` function, call the `get_mandalorian_data` function pass to it `mandalorian_people` and `'greef karga'` dictionary as arguments. Pass the return value to `create_person`
Assign the final return value to `greef_karga`.

## 6.2.1 Write to file

Check your work. Call the function `write_json`, accessed from the imported `five_oh_six.py` module, and write `greef_karga` to the file
`stu-greef_karga.json`. Compare your file to the test fixture file `fxt-greef_karga.json`.
Both files _must_ match line-for-line, character-for-character, and indent-for-indent.

## 6.3 Call `update_planets_visited`
Greef Karga informs the Mandalorian Din of a bounty on the planet of Arvala-7. The bounty is a 50-year-old sentient being with a large reward for their capture. The Mandalorian accepts the mission and leaves for Arvala-7.

Call `update_planets_visited` and pass `razor_crest` and the name `'Arvala-7'` as the arguments.  

Check your work by uncommenting the print statement provided for you.

Expected output:

```terminal
6.3 razor crest visited planets = ['Nevarro', 'Arvala-7']
```

# PROBLEM 07

## 7.1 Create Kuiil

### Background 
On planet Arvala-7, the Mandalorian runs into an inhabitant named Kuiil who helps him locate the bounty.

In the `main` function, call the `get_mandalorian_data` function pass to it `mandalorian_people` and `'kuiil'`. Pass the return value, `mandalorian_planets` and the `ugnaught_species` to `create_person`
Assign the final return value to `kuiil`.


## 7.1.1 Write to file

Check your work. Call the function `write_json`, accessed from the imported `five_oh_six.py` module, and write `kuiil` to the file
`stu-kuiil.json`. Compare your file to the test fixture file `fxt-kuiil.json`.
Both files _must_ match line-for-line, character-for-character, and indent-for-indent.

## 7.2 Create Grogu

### Background

The Mandalorian encounters the droid IG-11 that serves as a programmed bounty hunter. With the same bounty as their target, they decide to work together. Once they reach their target, they dicover the bounty is a green, child-like creature with big ears ensconced in a floating ball transport.

In the `main` function, call the `get_mandalorian_data` function pass to it `mandalorian_people` and `'grogu'` as arguments. Pass the return value to `create_person`
Assign the final return value to `grogu`.

## 7.2.1 Write to file

Check your work. Call the function `write_json`, accessed from the imported `five_oh_six.py` module, and write `grogu` to the file
`stu-grogu.json`. Compare your file to the test fixture file `fxt-grogu.json`.
Both files _must_ match line-for-line, character-for-character and indent-for-indent.

## 7.2.2 Get Grogu aboard his floating ball transport _Hovering Pram_

1. Call `get_mandalorian_data` passing the appropriate arguments and retrieve the vehicle
named [_Hovering Pram_](https://starwars.fandom.com/wiki/Hovering_Pram) in `mandalorian_vehicles`. 
Pass the return value to `create_vehicle`. Assign the final
return value to a variable named `hovering_pram`.

2. Call `board_passengers` and pass `hovering_pram` and `grogu` as the arguments. Assign the return value to `hovering_pram`.

3. Check your work. Call the function `write_json`, accessed from the imported `five_oh_six.py` module, and write `hovering_pram` to the file
`stu-grogu_hovering_pram.json`. Compare your file to the test fixture file `fxt-grogu_hovering_pram.json`.
Both files _must_ match line-for-line, character-for-character, and indent-for-indent.

## 7.3 Reprogram IG-11

### Background

Once Grogu is with the Mandalorian and IG-11, IG-11 attempts to harm Grogu due to his programming. With the help of Kuiil, the Mandalorian is able to stop IG-11 and Kuiil reprograms IG-11 to protect baby Grogu instead.

1. Update the `'instructions'` key in the `ig_11` dictionary replacing its value with `new_instructions`
2. Check your work. Call the function `write_json`, accessed from the imported `five_oh_six.py` module, and write `ig_11` to the file
`stu-ig_11_reprogrammed.json`. Compare your file to the test fixture file `fxt-ig_11_reprogrammed.json`.
Both files _must_ match line-for-line, character-for-character, and indent-for-indent.

# PROBLEM 08

### Background
The Mandalorian, Grogu, and IG-11 head back to Nevarro in the Razor Crest to turn Grogu in to the client who requested him. The Mandalorian notes the client who wants Grogu is part of the Galactic Empire with malintent. The Mandalorian decides to betray the Empire by fleeing to the planet Sorgan with Grogu and IG-11. 

## 8.1 Update Razor Crest 

In the `main` function call `update_planets_visited` and pass to it `razor_crest` and the planet name `'Sorgan'` as arguments. Assign the return value to `razor_crest`.

Check your work by uncommenting the print statement provided for you.

Expected output:

```terminal
8.1 razor crest visited planets = ['Nevarro', 'Arvala-7', 'Sorgan']
```
## 8.2 Create Cara Dune

#### Background 
On planet Sorgan, the Mandalorian meets Carasynthia "Cara" Dune. Cara has previous experience in the Alliance military and now serves as a mercenary on Sorgan. 

1. In the `main` function, call the `get_mandalorian_data` function pass to it `mandalorian_people` and `'Carasynthia Dune'`. Pass the return value  to `create_person`.
Assign the final return value to `cara_dune`.

2. Check your work. Call the function `write_json`, accessed from the imported `five_oh_six.py` module, and write `cara_dune` to the file
`stu-cara_dune.json`. Compare your file to the test fixture file `fxt-cara_dune.json`.
Both files _must_ match line-for-line, character-for-character, and indent-for-indent.

## 8.3 Create Gideon
#### Background

While on planet Sorgan, the Mandalorian receives word from Greef Karga informing him that his actions with Grogu has led to the Empire warlord, Gideon, wreaking havoc on Nevarro. Gideon's Imperial transport is stationed on Nevarro and Gideon will not leave until he has Grogu.

### 8.3.1 Create Gideon and the Imperial transport

1. In the `main` function, call the `get_mandalorian_data` function pass to it `mandalorian_people` and `'gideon'`. Pass the return value  to `create_person`.
Assign the final return value to `gideon`.

2. Call the `get_mandalorian_data` function pass to it `mandalorian_starships` and `'imperial transport'`. Pass the return value  to `create_starship`.
Assign the final return value to `imperial_transport`.

3. Call `board_passengers` passing to it `imperial_transport` and `gideon`. Assign the return value to `imperial_transport`.

4. Check your work. Call the function `write_json`, accessed from the imported `five_oh_six.py` module, and write `imperial_transport` to the file
`stu-gideon_imperial_transport.json`. Compare your file to the test fixture file `fxt-gideon_imperial_transport.json`.

Both files _must_ match line-for-line, character-for-character, and indent-for-indent.

## 8.4 Update Razor Crest
#### Background 
The Mandalorian decides to go back to Nevarro to face Gideon. Cara Dune offers her support and is willing to fight alongside the Mandalorian against Gideon. The Mandalorian, Cara, Grogu, and IG-11 board the Razor Crest and head back to Nevarro

In the `main` function call `board_passengers` and pass `razor_crest` and the passengers `mando`, `grogu`, `cara_dune`, and `ig_11` (in that order) as arguments.

# PROBLEM 09
#### Background

On planet Nevarro, the Mandalorian and his allies defeat Gideon forcing him to leave Nevarro. Cara decides to stay and help defend the planet. The Mandalorian decides to depart Nevarro with Grogu to reunite Grogu with his people. Their first destination is Tatooine. 

1. In the `main` function call `board_passengers` and pass `razor_crest` and the passengers `mando`, `grogu` (in that order) as arguments.
   
2. Call `update_planets_visited` pass `razor_crest` and the planet name `'Tatooine'` as the arguments. Assign the return value to `razor_crest`.

Check your work by uncommenting the print statement provided for you.

Expected output:

```terminal
9.2 razor crest visited planets = ['Arvala-7', 'Nevarro', 'Sorgan', 'Tatooine']
```

3. Using the `sort` method and lambda expression, sort the `'planets_visited'` key in the `razor_crest` dictionary in ascending order.

4. Check your work.  Call the function `write_json`, accessed from the imported `five_oh_six.py` module, and write `razor_crest` to the file
`stu-razor_crest_departs.json`. Compare your file to the test fixture file `fxt-razor_crest_departs.json`.

