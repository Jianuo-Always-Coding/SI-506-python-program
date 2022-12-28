# Problem Set 09

                                 ___| |_ __ _ _ __  __      ____ _ _ __ ___
                                 / __| __/ _` | '__| \ \ /\ / / _` | '__/ __|
                                 \__ \ || (_| | |     \ V  V / (_| | |  \__ \
                                 |___/\__\__,_|_|      \_/\_/ \__,_|_|  |___/
(ASCII Art sourced from https://www.asciiart.eu/movies/star-wars)
<div align="center">

##### "_May the Force be with you._"
##### _Obi-Wan Kenobi_

</div>

## Background

This week's problem set focuses on the [Star Wars API (SWAPI)](https://swapi.py4e.com/about), the requests module, and JSON objects.

In the film [Star Wars: The Empire Strikes Back](https://starwars.fandom.com/wiki/Star_Wars:_Episode_V_The_Empire_Strikes_Back) the events of which are set three years after the destruction of the Death Star, the Imperial Fleet led by Darth Vader dispatches Probe Droids across the galaxy to find Princess Leia's Rebel Alliance. The rebel alliance is located on the ice planet Hoth. Luke Skywalker (a pivotal figure within the Rebel Alliance) is instructed on this planet by the Force Spirit of Obi-Wan Kenobi to go to the swamp planet Dagobah to train as a Jedi Knight under the Jedi Master Yoda.

In this problem set you will help the rebel alliance in their fight against the Empire, help Luke Skywalker get to the planet Dagobah and finally assist the Rebels in their battle against the Empire.

## API overview

You can learn more about the API by going through its [documentation](https://swapi.py4e.com/documentation) and taking it for a [test run](https://swapi.py4e.com/). Here are a few things you should know about the API to successfully complete this problem set.

1. The base URL for the API is https://swapi.py4e.com/api
2. To get information about a particular entity you need to append a querystring to the base URL.

_For example:_

To retrieve planet resources, construct a URL that combines the SWAPI base URL with the resource path `/planets`. You may also need to add a planet identifier to the path or provide a querystring if searching for a particular planet or planets.

Similarly to retrieve people resources, construct a URL that combines the SWAPI base URL with the resource path `/people`. You may also need to add a person identifier to the path or provide a querystring if searching for a particular person or persons.

Read the [API documentation](https://swapi.py4e.com/documentation#root) to learn more about the information you can fetch from SWAPI.

## Problem 01 (25 points): Introducing SWAPI

__Task__: Implement a function that can initiate an HTTP GET request to the SWAPI API to return a
representation of a resource.

1. Implement a function called `get_swapi_resource` that accepts two parameters:

   1. `url`: a URL that
   provides information about entities in the Star Wars universe, and
   2. `params`: An optional dictionary
   of querystring arguments (default value is `None`).

   Review the docstring to better understand the
   function's expected behavior.

    :bulb: You need to utilize the `.get()` method from the `requests` library to access data with
    the `url` and `params` given, if any.

2. After implementing `get_swapi_resource`, return to the main function:
   1. Create a variable called `base_url`. Assign the string `'https://swapi.py4e.com/api'` to this variable. You will build on this root URL to fetch data from SWAPI. To try this function out you will fetch data about films in the Star Wars universe. Using string concatenation, add the necessary string to the `base_url` to build the complete API URL. Assign this complete API URL to the variable `films_url`.

   :bulb: Read the documentation to discover the correct string to add to `base_url` that will enable you to fetch films in the Star Wars universe.

   2. In `main()`, create a variable called `film_params`. Assign the dictionary `{'search': 'empire strikes back'}` to this variable.
   3. Call the `get_swapi_resource()` function and pass to it `films_url` and `film_params` in order using positional arguments in order to fetch information about *Star Wars: The Empire Strikes Back*. Assign the return value of the function to a variable called `response`. Create a variable named `film_details` and assign to it the first element of the `results` key in the `response` dictionary.`film_details` will be a dictionary.

   <br />

    Your `film_details` dictionary __must__ include the following key-value pairs:

    ```python
    {
            "title": "The Empire Strikes Back",
            "episode_id": 5,
            "opening_crawl": # Text for the opening crawl,
            "director": "Irvin Kershner",
            "producer": "Gary Kurtz, Rick McCallum",
            "release_date": "1980-05-17",
            "characters": [
               # List of character URLs
            ],
            "planets": [
               # List of planet URLs
            ],
            "starships": [
               # List of starship URLs
            ],
            "vehicles": [
               # List of vehicles URLs
            ],
            "species": [
               # List of species URLs
            ],
            "created": "2014-12-12T11:26:24.656000Z",
            "edited": "2014-12-15T13:07:53.386000Z",
            "url": "https://swapi.py4e.com/api/films/2/"
        }

    ```

## Problem 02 (40 points): Hoth and Dagoba

__Task__: Luke Skywalker along with the other members of the rebel alliance are on the ice planet Hoth. The Jedi Master Yoda is on the swamp planet Dagobah. In this problem you will gather details about the two planets.

1. First, you will implement a generalized function called `request_resource_details()`. Review the function's docstring regarding its expected behavior, parameters, and return value. This function will issue an HTTP GET request to SWAPI. Within the function here is what you have to implement:
   1. Create a variable `complete_url` and assign to it the variable `base_url`. The `complete_url` variable will later contain the `base_url` along with a string concatenated to it which together will represent a resource-specific URL that can be invoked to fetch details of a particular resource from the SWAPI.

   2. Create a variable named `categories` and assign to it a list literal containing all possible values for the `category` parameter as denoted in the docstring. If the `category` parameter is in the `categories` list, using an f-string concatenate `category` value to `complete_url` that will represent a resource specific URL which can be invoked to fetch information about a particular resource.

         _Example_: If `category` is `planets` then `complete_url` will be assigned the value `https://swapi.py4e.com/api/planets`.

   3. After the correct string has been concatenated to `complete_url` if needed, call `get_swapi_resource()` and pass to it `complete_url` and the `params` dictionary. Assign the return value of the function to a variable called `resource_info`.

   4. Return `resource_info`.

2. Navigate to the `main()` function. Create a list called `planets_name` and assign to it the list value `['Hoth', 'Dagobah']`.

3. Create an empty dictionary called `planet_details`.
4. Loop over `planets_name` and for each planet encountered call the `request_resource_details()` method passing to it the necessary arguments. Note that you are working with planets.When calling `request_resource_details()`, the API will return more data than just the result, so make sure to extract the first value of `results` in the JSON you get back from the API. Assign the data fetched for each planet to the `planet_details` dictionary with the name of the planet as the key and the data as the corresponding value. **What is inside the loop must be done in one line.**

## Problem 03 (30 points): Luke and Yoda

__Task__: Luke Skywalker is currently on the ice planet Hoth while the Jedi Master Yoda is on the swamp planet Dagobah. Make updates to the respective data structures for the planets to reflect their presence.

1. In the `main()` function: Create a list called `people_names` and assign to it the list value `['Luke', 'Yoda']` Also, create an empty dictionary called `people_details`.
2. Loop over `people_names` and, using the `request_resource_details()` function, fetch data for each person listed in `people_names`. Note that you are working with people. When calling `request_resource_details()`, the API will return more data than just the result, so make sure to extract the first value of `results` in the JSON you get back from the API. Assign the data fetched for each person to a variable called `person`.  **This must be done in one line.**

3. Within the loop, utilize the helper function `get_character_info` we provided and pass to it the variables `person` and `characteristics`. Assign the function's return value to the `people_details` dictionary with the name of the person as the key and the data as the corresponding value. Your dictionary **must** be structured in the following way:

```python
{ 'Luke': { 'name': 'Luke Skywalker',
            'height': '172',
            'mass': '77',
            'birth_year': '19BBY',
            'homeworld': 'https://swapi.py4e.com/api/planets/1/',
            'species': ['https://swapi.py4e.com/api/species/1/']},
  'Yoda': { 'name': 'Yoda',
            'height': '66',
            'mass': '17',
            'birth_year': '896BBY',
            'homeworld': 'https://swapi.py4e.com/api/planets/28/',
            'species': ['https://swapi.py4e.com/api/species/6/']}
}
```
4. In the `planet_details` dictionary, access the value corresponding to the planet Hoth using list indexing with the list `planets_name`, and within it add a key called `'current_residents'`. To this key assign a list. The list will contain a single element comprising the `Luke` dictionary. It will be the dictionary containing data about Luke that you stored in the `people_details` dictionary. When accessing the `Luke` key you must use list indexing with the `people_names` list.
5. Again, in the `planet_details` dictionary, access the value corresponding to the planet Dagobah using list indexing with the list `planets_name`, and within it add a key called `'current_residents'`. To this key assign a list. The list will contain a single element comprising the `Yoda` dictionary. It will be the dictionary containing data about Yoda that you stored in the `people_details` dictionary. When accessing the `Yoda` key you must use list indexing with the `people_names` list.

## Problem 04 (40 points): The Rebels escape

__Task__: On the planet Hoth, Luke is attacked by a wampa but manages to escape by using his lightsaber. He is alive but wounded and is rescued by [blockade runner](https://starwars.fandom.com/wiki/Blockade_runner) Han Solo. The Empire is alerted to the rebels' location and launches a large scale attack on the rebels. The rebels escape the planet Hoth with Luke and R2-D2 escaping in one ship and Han, Leia, C3-PO and Chewbacca escaping in another.

In this task you will fetch information about all of the characters mentioned above and order them by species.

1. For this task you will reuse some of the data structures you created in the previous problems. First, from the `people_names` list use an appropriate list method and remove `Luke` and `Yoda` on one line for each element.

2. Then, extend the `people_names` using an appropriate list method to add the following list of names: `['Han', 'Leia', 'C-3PO', 'R2-D2', 'Chewbacca']`. Please accomplish this in a single line of code.

   :exclamation: The `people_names` list should be of type list of strings.

3. Fetch information about each of the people listed in `people_names`. Start by looping over `people_names`.
   1. Within the loop, call `request_resource_details()` passing to it the appropriate arguments that would enable you to fetch information about a person. When calling `request_resource_details()`, the API will return more data than just the result, so make sure to extract the first value of results in the JSON you get back from the API. Assign the data fetched for each person to a variable called `person`. **This must be done in one line.**

   2. Within the loop, utilize the helper function `get_character_info` we provided and pass to it the variables `person` and `characteristics`. Assign the function's return value to the `people_details` dictionary with the name of the person as the key and the return value of `get_character_info` as the corresponding value.

   <br />

   #### _At this point, before you move to the next subtask, step back from the code and take a look at any one entry within the `people_details` dictionary. The entry for Han should be as given below:_
   ```python
   'Han': { 'name': 'Han Solo',
           'height': '180',
           'mass': '80',
           'birth_year': '29BBY',
           'homeworld': 'https://swapi.py4e.com/api/planets/22/',
           'species': ['https://swapi.py4e.com/api/species/1/']}
   ```

For your next subtask you will order all the people within `people_details` by their species. However, before you can do that you will have to resolve the URL contained within the `species` key and fetch the actual information corresponding to their species. So let's accomplish that first.

4. Implement a function called `resolve_dict_url()`. This function will accept a dictionary and the name of the key which has a URL associated with it. It will replace the URL with the dictionary fetched from the URL.
5. Within `resolve_dict_url`:
    1. Create a variable called `result` and assign it a value of `None`.
    2. Fetch the value associated with `key_name` from the `resource` dictionary and assign it to a variable `resolve_url`
    3. Notice how some of the URLs were stored in a list while others were stored as a singular value. You have to handle this case. So check if the type of `resolve_url` is a `list`.
    4. If the type of `resolve_url` is `list`, then:
        1. Assign an empty list to a variable named `result`.
        2. Loop over all URLs in `resolve_url`.
        3. For each URL call `get_swapi_resource()` and append its return value to `result`.
    5. Else, if the type of `resolve_url` is not a list, then:
        1. Call `get_swapi_resource()` and pass to it `resolve_url`. Assign the return value to `result`.
        2. __Outside__ the `if-else` block assign `result` to the `resource` dictionary with the `key_name` parameter as the key.
        3. You do not need to specify an explicit `return` statement.
6. Navigate to `main()`. Create a variable called `species_order` and assign to it an empty dictionary.
7. Create a variable called `species_count` and assign to it an empty list.
8. Loop over all entries in the `people_details` dictionary. Use the `.items()` method in your loop. The iterating variable you specify in the loop which will contain the __value__ for each item tuple _(remember that items() returns a list of item tuples)_ should be called `people_info`. Within the loop:

    1. For each dictionary contained within `people_details`, call `resolve_dict_url` passing to it the `people_info` loop variable as the first argument and `'species'` as the second _(because you need to replace the URL in the `species` key with a dictionary containing information about that species)_.
    2. Now that you have useful information within the `species` key in `people_info`, access the value stored in the `species` key and fetch the name of the species. Assign this value to a variable called `species_name`.

    :exclamation: Remember that the value corresponding to the `species` key will be a list. Access the first element in the list to get the actual dictionary corresponding to that species.

    3. To the `species_order` dictionary, add the name of the species as a key and a list of people belonging to that species as its value.

        :exclamation: You will need to utilize conditional statements to check if `species_name` is already a key in `species_order`. If not, then create a new list with the necessary values else simply append to the existing list.
9. Loop over the `species_order` dictionary using the `.keys()` method. In the loop, to the `species_count` list append to it a list of tuples where each tuple contains the name of the species as its first element and the count of people belonging to that species as its second element. There is a built-in list method you can use to get this count. The value in `species_count` should be as given below:

    ```python
    [('Human', 3), ("Yoda's species", 1), ('Droid', 2), ('Wookiee', 1)]
    ```

## Problem 05 (35 points): Traveling through space

__Task__: Luke, Han, Leia, C3-PO, Chewbacca and R2D2 have escaped from Hoth. Luke and R2-D2 are flying in an X-Wing starfighter while the others are aboard a light freighter called the Millennium Falcon. Retrieve representations of these ships and update their data structures to reflect the passengers traveling within them.


1. Assign an empty dictionary to the variable `starship_info`.
2. Create a variable called `starship_names` and assign to it a list literal containing the strings `'X-Wing', 'Millennium Falcon'`
3. Create a variable called `rebels` and assign to it a list literal containing the strings `'Luke', 'R2-D2', 'Han', 'Chewbacca', 'Leia', 'C-3PO'`.
4. Now, fetch information about each starship in `starship_names`. Loop over `starship_names` and for each starship:
    1. Within the loop, call `request_resource_details()` with the starship name as the querystring. When calling `request_resource_details()`, the API will return more data than just the result, so make sure to extract the first value of results in the JSON you get back from the API. Assign the return value to a variable named `starship_details`. **This must be done in one line.** Assign `starship_details` to the `starship_info` dictionary with the starship name as the key.
5. Now, add `Luke` and `R2-D2` to the X-Wing.
    1. Fetch the dictionary corresponding to the `X-Wing` from `starship_info` and assign it to the variable `x_wing`.
    2. To the `'crew_members'` key in `x_wing` assign a dictionary literal. The dictionary contains two keys, `pilot` and `astromech_droid`. To the `pilot` key assign the dictionary representation of `Luke` fetched from the `people_details` dictionary. To the `astromech_droid` key, assign the dictionary representation of `R2-D2` fetched again from the `people_details` dictionary. You must use list indexing with the `rebels` list to get the relevant key.
6. With Luke and R2-D2 flying out in their X-Wing, add the remaining members of the Rebel Alliance to the Millennium Falcon.
    1. Fetch the dictionary corresponding to `Millennium Falcon` from `starship_info` and assign it to the variable `millennium_falcon`. Use list indexing using the `starship_names` list to get the relevant key.
    2. Set the value of `'passengers_on_board'` key in `millennium_falcon` to an empty list.
    3. To the `'crew_members'` key in `millennium_falcon` assign a dictionary. This dictionary contains two keys, `pilot` and `copilot`. To the `pilot` key assign the dictionary representation of `Han` fetched from the `people_details` dictionary. To the `copilot` key assign the dictionary representation of `Chewbacca` fetched from the `people_details` dictionary. You must use list indexing with the `rebels` list to get the relevant key.
    4. Then use a `range` based for loop to loop over the `rebels` list starting from Leia _(since Luke, R2-D2, Han and Chewbacca have already been assigned to their respective starships)_. Remember to specify the correct start index to `range()` such that the loop starts from the entry for `'Leia'`.
         1. Append the details of each passenger fetched from `people_details` to the `'passengers_on_board'` key of `millenium_falcon`. You must use list indexing with the `rebels` list to get the relevant key.
7. Using `write_json()`, write the contents of `starship_info` to a file called `starship_info.json`.

## Problem 06 (35 points): Dagobah

__Task__: Luke and R2-D2 in the X-Wing have travelled to the planet Dagobah. Let's change our data structures to reflect this.


1. In the `main()` function, assign an empty list to `residents_count`.
2. In the dictionary `planet_details`, assign an empty list to the value corresponding to the key `current_residents` for the planet Hoth.
3. Now add information about Luke and R2-D2 to Dagobah.
   1. Access the value corresponding to `'Dagobah'` in the `planet_details` dictionary. This value will be a dictionary. In this dictionary access the key called `'current_residents'` which will be of type `list`. To this list append information about Luke fetched from the `people_details` dictionary. Please accomplish this in a single line of code. List indexing is not required to access the appropriate key for `people_details`.
   2. Repeat the same process as above for R2-D2. Again, please accomplish this in a single line of code.
4. Let's also add information about the X-Wing Luke and R2-D2 travelled in to the planet Dagobah.
   1. Access the dictionary corresponding to the planet Dagobah in `planet_details`. Within this dictionary to the key `'starships'` assign a list containing information about X-Wing fetched from `starship_info`. Please accomplish this in a single line of code.
5. Loop through the `planet_details` dictionary to append tuples to `residents_count`. Each tuple should have the name of the planet as its first element and the count of current residents in it as its second value.
    1. Loop over __only__ the keys in the `planet_details` dictionary using an appropriate dictionary method.
    2. To `residents_count` append a tuple with the following structure (please accomplish this in a single line of code):
        1. First element must be the name of the planet.
        2. Second element must be the length of the list of `current_residents` present in the `planet_details` dictionary for that planet name. Make sure to use an appropriate built-in function to find the length.

## Problem 07 (40 points): Luke's training

__Task__: Luke trains with the Jedi Master Yoda on Dagobah. [Here's a clip from the movie](https://www.youtube.com/watch?v=E3-CpzZJl8w&t=17s&ab_channel=JonMercano) showing a scene from Luke's training, a scene where the quote "Do or do not, there is no try" is said by Yoda. Meanwhile, in another part of the galaxy the remaining members of the Rebel Alliance have been captured by Darth Vader in the floating Cloud City on the planet Bespin. Luke decides to travel to the Cloud City, confront the Empire led by Vader and save his friends. In this task you will detail out all information about Darth Vader which will help Luke be better prepared.

1. Implement the function `get_darth_vader_info()`. Within the function:
   1. Assign an empty list to `vader_ships_info`.
   2. Assign an empty dictionary to `all_vader_info`.
   3. Create a variable called `vader_ships` with the value being a list listeral `['Executor', 'TIE']`.
   4. Call the function `request_resource_details()` with `'Darth Vader'` as value for `search` in the querystring argument and pass the other arguments with the necessary values as you have done in the previous questions. Assign the return value to `vader_info`.
   5. Request information about a few ships commanded by Vader. So loop over `vader_ships`.
        1. For each ship in `vader_ships`, call `request_resource_details` passing the ship name as the value for `search` in the querystring argument and the other arguments should be set to the necessary values. Append the return value to `vader_ships_info`.
   6. Outside of the loop, request information about the planet Bespin. For this, call `request_resource_details()` passing `'Bespin'` as the value for `search` in the querystring argument. Assign its return value to `bespin_info`.
   7. Assign `vader_info` to the key `'leader'` in `all_vader_info`.
   8. Assign `vader_ships_info` to the key `'ships'` in `all_vader_info`.
   9. Assign `bespin_info` to the key `'planet'` in `all_vader_info`.
   10. Return `all_vader_info`.

2. Navigate to `main()` and call `get_darth_vader_info()` passing to it the `base_url` variable. Assign its return value to `all_vader_info`. This is a dictionary containing all data about Darth Vader.

3. With this information, Luke and R2-D2 begin their travel to the planet Bespin where they confront the Empire. Let's change the data structures to reflect this.

4. Since Luke and R2-D2 are no longer in Dagobah, use an appropriate list method to clear all entries corresponding to the `current_residents` key in the entry for Dagobah in `planet_details`. Repeat the same for the `starships` key.

5. In the `all_vader_info` dictionary, access the `planet` key and within it assign to the `current_residents` key a list. This list must contain the dictionaries for Luke as the first element and R2-D2 as the second element fetched from `people_details`.

6. Access the `planet` key within `all_vader_info` again and within it to the `starships` key assign the dictionary containing information about the X-Wing retrieved from `starship_info`.

7. Call `write_json()` and write the `all_vader_info` to a file called `all_vader_info.json`.

## Problem 08 (30 points): The battle at Bespin

__Task__: The Rebels and the Empire are battling each other. Luke and Darth Vader are in Cloud City's central air shaft engaged in a lightsaber [battle](https://www.youtube.com/watch?v=_lOT2p_FCvA&ab_channel=StarWarsMalaysia). It is time to evacuate residents from the areas near the war zone. Your task is to sort a given list of passengers according to their boarding order that will facilitate easy evacuation.

1. Using the `read_json()` method read the file `passengers_list.json` and assign it to a variable called `boarding_order`.

2. Implement `fetch_boarding_order()` so that it returns the key based on which the `sorted()` function will sort its list of dictionaries. Review the docstring to better understand the function's expected behavior. You can implement this function in a single line.

3. Implement a function called `sort_boarding_order()`. This function will be responsible for sorting `boarding_order` based on the value of the `boarding_order` key.

    :exclamation: To sort the list of dictionaries you must make use of the `sorted` method.

    1. Within `sort_boarding_order`: Call the `sorted()` function and pass to it the dictionary that has to be sorted and the function `fetch_boarding_order` as the value for the `key` parameter.
    2. Return the sorted list of dictionaries.

4. Return to `main()` and call `sort_boarding_order()` and pass to it `boarding_order` as the argument. Assign its return value to a variable called `sorted_boarding_order`.
5. Using `write_json()` write the `sorted_boarding_order` data to a file called `sorted_boarding_order.json`.
