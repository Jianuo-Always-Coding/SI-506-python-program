# SI 506: Lab Exercise 11

## This week's Lab Exercise

This week's lab exercise includes six (6) problems that focus on using modules, the `copy` module, lambda functions, and the `requests` module to access data from the SWAPI API.

## Background

In this lab, you will continue to work with data accessed from the [SWAPI API](https://swapi.py4e.com/documentation) in order to create Python representations of several, ultimately, villainous characters from [Star Wars: Episode III – Revenge of the Sith](https://en.wikipedia.org/wiki/Star_Wars:_Episode_III_%E2%80%93_Revenge_of_the_Sith). In this final installment in the Star Wars prequel trilogy, but third chapter chronologically:
> "...[t]he Republic is crumbling under attacks by the ruthless Sith Lord, Count Dooku. There are heroes on both sides. Evil is everywhere. In a stunning move, the fiendish droid leader, General Grievous, has swept into the Republic capital and kidnapped Chancellor Palpatine, leader of the Galactic Senate. As the Separatist Droid Army attempts to flee the besieged capital with their valuable hostage, two Jedi Knights lead a desperate mission to rescue the captive Chancellor...."

You have been provided with a list of villains, named `villain_names`, and are tasked with defining and leveraging various functions in order to create and enrich Python representations for each character and their respective homeworld.

```python
villain_names = [
                    'palpatine',
                    'anakin skywalker',
                    'grievous',
                    'wilhuff tarkin',
                    'dooku'
]
```

## Files

* `lab_exercise_11.py`: script including a `main()` function and other definitions and statements
* `five_oh_six.py`: module containing utility functions and constants
* `wookieepedia_planets.csv`: CSV file containing planet attributes sourced from Wookieepedia
* One or more `fxt_*.json` test fixture files that you must match with the files you produce

## 1.0 Problem 01 (5 points)

Navigate to Problem 01 in `five_oh_six.py`. Assign the correct endpoint URL to the global variable `SWAPI_ENDPOINT`.

In `lab_exercise_11.py`, import `five_oh_six` as `utl` at the top of the file. Then, navigate to Problem 01 in the `main()` function of `lab_exercise_11.py`.

:exclamation: Ensure you have saved any changes made to the `five_oh_six.py` file before importing it as a module in `lab_exercise_11.py`.

1. Create an empty list called `villains`.
2. Loop over the provided list of villain names, called `villain_names`.
3. Call the provided `get_resource()` function, accessed from the imported `five_oh_six` module, and pass to it the `SWAPI_ENDPOINT` variable and the string `'/people'` as the url with each villain's name as the search parameter. The API will return more data than just the result, so make sure to extract the first value of `results` in the JSON you get back from the API. **This must be done in one line.**
4. Append the return value for each function call to the list `villains`.

:bulb: Review the docstring and code for the `get_resource()` function in the `five_oh_six` module in order to re-familiarize yourself with its functionality, parameters, and return value.

:exclamation: As a reminder, employ dot notation (`.`) to access a module's definitions and statements or call the built-in `dir()` function to return a list containing a module's definitions and statement names.

:exclamation: Remember, `params` is of type `dict` with a key representing the action you are taking, such as 'search', and a value representing the value you're searching for.

:bulb: For additional practice with list comprehensions, see if you can reconfigure your solution for Problem 01 into a list comprehension after following the steps above.

## 2.0 Problem 02 (5 points)

### Part 01

Implement a function named `create_person()`, which _must_ return a dictionary _literal_ that also leverages the provided `get_attribute()` function, accessed from the imported `five_oh_six` module, to access the corresponding values for each key assigned to the dictionary. Review the function's docstring regarding its expected behavior, parameters, and return value, if any.

An example return value from this function is shown below:

```Python
    {
        'name': 'Palpatine',
        'height': '170',
        'hair_color': 'grey',
        'eye_color': 'yellow',
        'birth_year': '82BBY',
        'homeworld': {
                            'name': 'Naboo',
                            'rotation_period': '26',
                            'orbital_period': '312',
                            'diameter': '12120',
                            'climate': 'temperate',
                            'gravity': '1 standard',
                            'terrain': 'grassy hills, swamps, forests, mountains',
                            'surface_water': '12',
                            'population': '4500000000',
                            'residents': [ 'https://swapi.py4e.com/api/people/3/',
                                            'https://swapi.py4e.com/api/people/21/',
                                            'https://swapi.py4e.com/api/people/35/',
                                            'https://swapi.py4e.com/api/people/36/',
                                            'https://swapi.py4e.com/api/people/37/',
                                            'https://swapi.py4e.com/api/people/38/',
                                            'https://swapi.py4e.com/api/people/39/',
                                            'https://swapi.py4e.com/api/people/42/',
                                            'https://swapi.py4e.com/api/people/60/',
                                            'https://swapi.py4e.com/api/people/61/',
                                            'https://swapi.py4e.com/api/people/66/'],
                            'films': [ 'https://swapi.py4e.com/api/films/3/',
                                        'https://swapi.py4e.com/api/films/4/',
                                        'https://swapi.py4e.com/api/films/5/',
                                        'https://swapi.py4e.com/api/films/6/'],
                            'created': '2014-12-10T11:52:31.066000Z',
                            'edited': '2014-12-20T20:58:18.430000Z',
                            'url': 'https://swapi.py4e.com/api/planets/8/'
                    },
        'species': 'Human'
    }
```

### Part 02

After defining the function, navigate to Problem 02 in `main()`. Create a list comprehension that loops over each nested dictionary, representing a villain, in the list assigned to the variable `villains`. While looping over the list `villains`, pass each villain element to the function `create_person()`. Assign the list comprehension to the variable `villains_created`.

:bulb: As suggested in previous exercises, if you are unsure how to structure the list comprehension, implement a standard `for` loop first. Get the function working correctly, then comment out the `for` loop and reconfigure it into a list comprehension.

## 3.0 Problem 03 (5 points)

### Part 01

Navigate to Problem 03 in `five_oh_six.py`. Examine the commented out code in the `utl.read_csv_to_dicts()` function (__do not__ uncomment). Reimplement the function by writing code in the `with` block that retrieves a `csv` reader object and employs a __list comprehension__ to traverse the rows in the reader object and return a new list of row elements to the caller.

You are limited to writing two (2) lines of code.

   1. Line 01 assigns the "reader" object returned by calling `csv.DictReader` to a variable named `reader`.
   2. Line 02 returns a new list of `reader` "row" elements to the caller using __a list comprehension__.

You _must_ employ existing variable names that appear in the commented out code when writing your list comprehension (i.e., `reader`, `row`).

### Part 02

After defining the function, navigate to Problem 03 in the `main()` function of `lab_exercise_11.py`. Call the function `read_csv_to_dicts()`, accessed from the `five_oh_six` module, and pass to it the filepath for the provided `'wookieepedia_planets.csv'` file. Assign the return value to the variable `wookiee_homeworlds`.

## 4.0 Problem 04 (5 points)

### Part 01

Implement a function named `enrich_planet()`, which loops over the passed in list of planet attributes, sourced from Wookieepedia, and utilizes a conditional statement to match on the planet's 'name' key, in order to update the `planet` dictionary with the correct key-value pairs. The function _must_ return an enriched dictionary that contains only the keys contained in the provided `key_filters` tuple. Review the function's docstring regarding its expected behavior, parameters, and return value, if any.

An example return value from this function is shown below:

```Python
    {
        'name': 'Palpatine',
        'height': '170',
        'hair_color': 'grey',
        'eye_color': 'yellow',
        'birth_year': '82BBY',
        'homeworld': {
                        'name': 'Naboo',
                        'rotation_period': '26',
                        'orbital_period': '312',
                        'climate': 'Temperate',
                        'gravity': '1 standard',
                        'terrain': 'Swamps, Hills, Plains, Cities, Mountains',
                        'surface_water': '12',
                        'population': '4500000000',
                        'region': 'Mid Rim Territories',
                        'sector': 'Chommell sector',
                        'system': 'Naboo system',
                        'atmosphere': 'Type I (breathable)',
                        'primary_languages': 'Galactic Basic, Gunganese'
                    },
        'species': 'Human'
    }
```

### Part 02

After defining the function, navigate to Problem 04 in `main()`. Loop over the `villains_created` list to access each dictionary representation of a villain. Call the function `enrich_planet()` and pass to it (1) the dictionary representation for each villain's homeworld, by accessing each villain's 'homeworld' key-value pair within the loop, (2) the list of nested dictionaries named `wookiee_homeworlds`, and (3) the `key_filters` tuple. Assign the return value back to each villain's 'homeworld' key, in order to update the key-value pair with the newly enriched planet dictionary.

## 5.0 Problem 05 (3 points)

Navigate to Problem 05 in `main()`. Call the built-in `sorted()` function to return a sorted list of a passed in iterable object. The `sorted()` function accepts a required `iterable` parameter and optional `key` and `reverse` parameters. Pass to it the list of nested dictionaries named `villains_created`, along with a lambda function assigned to the `key`, in order to sort the list of nested dictionaries by each dictionary's 'name' attribute in _ascending_ order. Assign the return value to the variable `villains_sorted`.

:bulb: The default values for the `key` and `reverse` parameters of the built-in `sorted()` function are `None` and `False`, respectively.

## 6.0 Problem 06 (7 points)

### Part 01

Navigate to Problem 06 in `five_oh_six.py`. Implement a function named `convert_to_unknown()`, which accepts any single `value` and utilizes if-else statements and the built-in function `isinstance()` to check if the passed in `value` is an empty string. Review the function's docstring regarding its expected behavior, parameters, and return value, if any.

### Part 02

After defining the function, navigate to Problem 06 in the `main()` function. First, leverage the `copy` module to return a deep copy of the sorted list of nested dictionaries `villains_sorted`, utilizing `copy.deepcopy()`. Assign the return value to the variable `villains_sorted_clean`.

Next, loop over the copied list of nested dictionaries `villains_sorted_clean` and utilize a nested `for` loop to loop over each key-value pair stored in each villain's nested dictionary assigned to 'homeworld'. Leverage the dictionary method that accesses each of the dictionary's key-value pairs. Call the function `convert_to_unknown()`, accessed from the `five_oh_six` module, and pass to it each value in the villain's nested dictionary assigned to 'homeworld'. Assign the return value back to its corresponding `key` within the villain's nested dictionary assigned to 'homeworld'.

Finally, call the function `write_json()`, accessed from the `five_oh_six` module, two (2) times:
1. On the first function call, pass to it the filepath `'stu-villain_homeworlds.json'` and the original sorted list of nested dictionaries `villains_sorted`.
2. On the second function call, pass to it the filepath `'stu-villain_homeworlds_cleaned.json'` and the copied list of nested dictionaries `villains_sorted_clean`.

:exclamation: Compare both of your final output files to the provided `fxt_*.json` files to check your work.

:bulb: Notice, with the use of the `copy` module's `deepcopy()` method, that the original list of sorted nested dictionaries `villains_sorted` remains unchanged after the `convert_to_unknown()` function was called on the deep copy of it, which was assigned to a new variable `villains_sorted_clean`.
