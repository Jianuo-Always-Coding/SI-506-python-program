# SI 506: Lab Exercise 09

## This week's Lab Exercise

This week's lab exercise includes eight (8) problems that focus on using the `requests` module to load data from the [The Star Wars API](https://swapi.py4e.com/).

## Background

In this lab, you will create a Python representation of the [opening scene from _'Star Wars: Episode IV – A New Hope'_](https://youtu.be/GHsnpo8QMro?t=50). At the start of every Star Wars film is the iconic opening crawl, which provides the backstory and sets the stage for what's to come. The scene opens on the planet [Tatooine](https://starwars.fandom.com/wiki/Tatooine?so=search#Description) emerging from a total eclipse, as a [Rebel Blockade Runner](shorturl.at/bMPUV) races through space, pursued by an [Imperial Stardestroyer](https://starwars.fandom.com/wiki/Imperial_I-class_Star_Destroyer).

On board the Rebel Blockade Runner and amidst laserfire passed between Rebel troopers and Imperial Stormtroopers, we meet two robots, [R2-D2](https://starwars.fandom.com/wiki/R2-D2/Legends) and [C-3PO](https://starwars.fandom.com/wiki/C-3PO), who are struggling to avoid the chaos. After a tremendous blast, smoke fills the corridor and, once it clears, reveals a hole in the main passageway as the starship is overtaken by more Stormtroopers and the infamous Dark Lord of the Sith, [Darth Vader](https://en.wikipedia.org/wiki/Darth_Vader).

## Data

Continuing with the SWAPI data from this week's lecture, you will leverage the requests module and a utility function, called `get_swapi_resource()`, to access [JSON documents](https://realpython.com/python-json/) that represent the film, its starships, and its characters.


## 1.0 Problem 01 (3 points)

### Part 1
Write a function called `get_swapi_resource()` that defines three parameters:

   * `url` (str): a url that specifies the resource.

   * `params` (dict): optional dictionary of querystring arguments; *default value* is `None`.

   * `timeout` (int): timeout value in seconds; *default value* is `10`

This function should use the `requests` module to get the data from the SWAPI API and return the JSON interpretation of the response. Read the docstring for more information.

:bulb: Check your lecture notes if you have additional questions about how this should function.

### Part 2

After defining the function, navigate to Problem 01 in the `main()` function. Create a variable called `swapi_new_hope` and assign it the return value of `get_swapi_resource()`. When calling `get_swapi_resource()`, pass to it the provided `ENDPOINT` variable and the string `'/films'` as the url with `'new hope'` as the search parameter. The API will return more data than just the result, so make sure to extract the first value of `results` in the JSON you get back from the API. **This must be done in one line.**

:bulb: Remember, `params` is of type `dict` with a key representing the action you are taking, such as 'search', and a value representing the value you're searching for.

## 2.0 Problem 02 (3 points)

### Part 1

Next, define a function called `get_attribute()`, which defines two (2) parameters:

   * `dict_` (dict): a dictionary representation of the decoded JSON.
   * `key` (str): a string representing the desired key to access.

The function should return the dictionary value that corresponds with the passed in key. Refer to the docstring for additional details.

### Part 2

After defining the function, navigate to Problem 02 in `main()`. Call the function `get_attribute()`, passing to it the `swapi_new_hope` data and the string `'opening_crawl'`. Assign the variable `opening_crawl` to the return value.

## 3.0 Problem 03 (3 points)

### Part 1

Define a function called `create_starship()`, which defines one (1) parameter:

   * `starship` (dict): a dictionary representation of the decoded JSON that contains starship attributes.

The function should return a dictionary _literal_ that also leverages the `get_attribute()` function to access the corresponding values for each key defined in the dictionary. Refer to the docstring for additional details on the specific keys and their order.

An example return value from this function is shown below:

```Python
    {
    'name': 'CR90 corvette',
    'model': 'CR90 corvette',
    'passengers': [],
    'max_atmosphering_speed': '950',
    'length': '150'
    }
```
:exclamation: Review last week's lecture notes if you need to refresh your memory on the creation of a dictionary literal. Ensure you are leveraging the `get_attribute()` function in each of your key-value pair assignments, except for 'passengers' (which should be provisioned with an empty list).

### Part 2

After defining the function, navigate to Problem 03 in `main()`. Call the function `get_swapi_resource()` two (2) times:

   * In the first function call, pass the provided `ENDPOINT` variable and the string `'/starships'` as the url with `'CR90 corvette'` as the search parameter. Assign the variable `swapi_rebel_blockade` to the return value.
   * In the second function call, pass the provided `ENDPOINT` variable and the string `'/starships'` as the url with `'destroyer'` as the search parameter. Assign the variable `swapi_stardestroyer` to the return value.

:exclamation: When calling `get_swapi_resource()`, the API will return more data than just the result, so make sure to extract the first value of `results` in the JSON you get back from the API. **This must be done in one line.**

Then, call the function `create_starship()` two (2) times:

   * In the first function call, pass the `swapi_rebel_blockade` data. Assign the variable `rebel_blockade` to the return value.
   * In the second function call, pass the `swapi_stardestroyer` data. Assign the variable `stardestroyer` to the return value.

## 4.0 Problem 04 (3 points)

### Part 1

Define a function called `create_person()`, which defines one (1) parameter:

   * `person` (dict): a dictionary representation of the decoded JSON that contains person attributes.

The function should return a dictionary _literal_ that also leverages the `get_attribute()` function to access the corresponding values for each key defined in the dictionary. Refer to the docstring for additional details on the specific keys and their order.

An example return value from this function is shown below:

```Python
    {
      'name': 'R2-D2',
      'height': '96',
      'mass': '32',
      'birth_year': '33BBY',
      'eye_color': 'red',
      'dialogue': []
   }
```
:exclamation: Review last week's lecture notes if you need to refresh your memory on the creation of a dictionary literal. Ensure you are leveraging the `get_attribute()` function in each of your key-value pair assignments, except for 'dialogue' (which should be provisioned with an empty list).

### Part 2

After defining the function, navigate to Problem 04 in `main()`. Call the function `get_swapi_resource()` two (2) times:

   * In the first function call, pass the provided `ENDPOINT` variable and the string `'/people'` as the url with `'R2-D2'` as the search parameter. Assign the variable `swapi_r2d2` to the return value.
   * In the second function call, pass the provided `ENDPOINT` variable and the string `'/people'` as the url with `'C-3PO'` as the search parameter. Assign the variable `swapi_c3po` to the return value.

:exclamation: When calling `get_swapi_resource()`, the API will return more data than just the result, so make sure to extract the first value of `results` in the JSON you get back from the API. **This must be done in one line.**

Then, call the function `create_person()` two (2) times:

   * In the first function call, pass the `swapi_r2d2` data. Assign the variable `r2d2` to the return value.
   * In the second function call, pass the `swapi_c3po` data. Assign the variable `c3po` to the return value.

## 5.0 Problem 05 (5 points)

### Part 1

Define a function called `board_starship()`, which defines two (2) parameters:

   * `starship` (dict): a dictionary representation of the decoded JSON that contains starship attributes.
   * `people` (list): a list of tuples where, for each tuple, a variable assigned to the decoded JSON representing a person is at the 0th index and a `bool` value indicating whether they are an intruder is at the 1st index.

The function should return an updated version of the dictionary representation of the decoded JSON that contains starship attributes. Refer to the docstring for additional details on the function's implementation and which key-value pairs should be updated or created.

### Part 2

After defining the function, navigate to Problem 05 in `main()`. Assign a list of tuples to the variable `people`. The first tuple _must_ contain `r2d2` and `False`. The second tuple _must_ contain `c3po` and `False`.

Call the function `board_starship()` and pass to it the `rebel_blockade` and the list of tuples `people`.

The updated `rebel_blockade` _must_ mirror the example below:
```Python
   {
      'name': 'CR90 corvette',
      'model': 'CR90 corvette',
      'passengers': [{
                        'name': 'R2-D2',
                        'height': '96',
                        'mass': '32',
                        'birth_year': '33BBY',
                        'eye_color': 'red',
                        'dialogue': []},
                     {
                        'name': 'C-3PO',
                        'height': '167',
                        'mass': '75',
                        'birth_year': '112BBY',
                        'eye_color': 'yellow',
                        'dialogue': []
                     }],
      'max_atmosphering_speed': '950',
      'length': '150'
   }
```
:exclamation: There is no need to assign the return value from this function call to a new variable, since we simply want to update the decoded JSON object _in place_.

## 6.0 Problem 06 (3 points)

### Part 1

Define a function called `capture_starship()`, which defines two (2) parameters:

   * `starship_attacker` (dict): a dictionary representation of the decoded JSON that contains attributes of an attacking starship.
   * `starship_captured` (dict): a dictionary representation of the decoded JSON that contains attributes of a starship that is being captured.

The function should return an updated version of the dictionary representation of the decoded JSON that contains attributes of the attacking starship. Refer to the docstring for additional details on the function's implementation and which key-value pairs should be updated or created.

### Part 2

After defining the function, navigate to Problem 06 in `main()`. Call the function `capture_starship()` and pass to it the `stardestroyer` and the `rebel_blockade`, in that order.

The updated `stardestroyer` _must_ mirror the example below:
```Python
   {
      'name': 'Star Destroyer',
      'model': 'Imperial I-class Star Destroyer',
      'passengers': [],
      'max_atmosphering_speed': '975',
      'length': '1,600',
      'primary_docking_bay': {
                                 'docked': [
                                             {
                                                'name': 'CR90 corvette',
                                                'model': 'CR90 corvette',
                                                'passengers': [{ 'name': 'R2-D2',
                                                                  'height': '96',
                                                                  'mass': '32',
                                                                  'birth_year': '33BBY',
                                                                  'eye_color': 'red',
                                                                  'dialogue': []},
                                                                  { 'name': 'C-3PO',
                                                                  'height': '167',
                                                                  'mass': '75',
                                                                  'birth_year': '112BBY',
                                                                  'eye_color': 'yellow',
                                                                  'dialogue': []}],
                                                'max_atmosphering_speed': '950',
                                                'length': '150'
                                             }
                                          ]
                              }
   }
```
:exclamation: There is no need to assign the return value from this function call to a new variable, since we simply want to update the decoded JSON object _in place_.

## 7.0 Problem 07 (6 points)

### Part 1

Define a function called `insert_dialogue()`, which defines two (2) parameters:

   * `person` (dict): a dictionary representation of the decoded JSON that contains people attributes.
   * `dialogue` (dict): a dictionary whose key-value pairs each represent a person and their dialogue.

Refer to the docstring for additional details on this function's tasks, parameters, and return value.

### Part 2

After defining the function, navigate to Problem 07 in `main()`. Call the function `insert_dialogue()` two (2) times:

   * In the first function call, pass `r2d2` and the provided `dialogue` dictionary.
   * In the second function call, pass `c3po` and the provided `dialogue` dictionary.

An example return value for this function is shown below:

```Python
   {
      'name': 'R2-D2',
      'height': '96',
      'mass': '32',
      'birth_year': '33BBY',
      'eye_color': 'red',
      'dialogue': [
                     'beep, beep, boop.',
                     'boop, beep, beep.',
                     'boop, beeeep!'
                  ]
   }
```

:exclamation: There is no need to assign the return values from these function calls to a new variable, since we simply want to update the decoded JSON objects _in place_.

## 8.0 Problem 08 (4 points)

### Part 1

Navigate to Problem 08 in `main()`. Repeat the series of function calls from the previous problems to acquire the JSON object representing the Sith Lord, Darth Vader, create a representation of a person utilizing the data accessed from SWAPI, update the 'intruder' key of the `rebel_blockade` with the JSON object representing Darth Vader, and insert his dialogue into the correct key-value pair in the decoded JSON `vader`.

1. Call the function `get_swapi_resource()` and pass to it the provided `ENDPOINT` variable and the string `'/people'` as the url with `vader` as the search parameter. Assign the variable `swapi_vader` to the return value.

    :exclamation: When calling `get_swapi_resource()`, the API will return more data than just the result, so make sure to extract the first value of `results` in the JSON you get back from the API. **This must be done in one line.**

2. Call the function `create_person()` and pass to it `swapi_vader`. Assign the variable `vader` to the return value.
3. Assign a list with one tuple to the variable `people`. The tuple _must_ contain `vader` and `True`. Call the function `board_starship()` and pass to it the `rebel_blockade` and the list `people`.
4. Call the function `insert_dialogue()` and pass to it `vader` and the provided `dialogue` dictionary.

### Part 2

Finally, the function `write_json()` has been implemented for you. Call `write_json()` with the filepath of `'stu_stardestroyer.json'` using the `stardestroyer` dictionary. The JSON document you generate _must_ match the `fxt_stardestroyer.json` file provided.
