# SI 506 Lecture 21

import csv
import json
import pprint
import requests


def drop_data(entity, keys):
    """Deletes < entity > dictionary key-values pairs if a key matches a key in the
    passed in < keys > tuple. Checks each key in < keys > before attempting to delete
    the associated < entity > key-value pair in order to avoid runtime KeyError
    exceptions.

    Parameters:
        entity (dict): dictionary with key-value pairs to drop (i.e., delete)
        keys (tuple): key-value pairs to remove from < entity >

    Returns:
        dict: dictionary with matching key-value pairs removed
    """

    for key in keys:
        if key in entity.keys():
            del(entity[key])
    return entity


def get_swapi_resource(url, params=None, timeout=10):
    """Returns a response object decoded into a dictionary. If query string < params > are
    provided the response object body is returned in the form on an "envelope" with the data
    payload of one or more SWAPI entities to be found in ['results'] list; otherwise, response
    object body is returned as a single dictionary representation of the SWAPI entity.

    Parameters:
        url (str): a url that specifies the resource.
        params (dict): optional dictionary of querystring arguments.
        timeout (int): timeout value in seconds

    Returns:
        dict: dictionary representation of the decoded JSON.
    """

    if params:
        return requests.get(url, params, timeout=timeout).json()
    else:
        return requests.get(url, timeout=timeout).json()


def read_csv_to_dicts(filepath, encoding='utf-8', newline='', delimiter=','):
    """Accepts a file path, creates a file object, and returns a list of
    dictionaries that represent the row values using the cvs.DictReader().

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences
        delimiter (str): delimiter that separates the row values

    Returns:
        list: nested dictionaries representing the file contents
     """

    with open(filepath, 'r', newline=newline, encoding=encoding) as file_obj:
        data = []
        reader = csv.DictReader(file_obj, delimiter=delimiter)
        for line in reader:
            data.append(line) # OrderedDict
            # data.append(dict(line)) # convert OrderedDict to dict
        return data


def read_json(filepath, encoding='utf-8'):
    """Reads a JSON document, decodes the file content, and returns a list or
    dictionary if provided with a valid filepath.

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file

    Returns:
        dict/list: dict or list representations of the decoded JSON document
    """

    with open(filepath, 'r', encoding=encoding) as file_obj:
        return json.load(file_obj)


def sort_by_population(entity):
    """Tries to return an < entity > dictionary's population value converted to
    an integer.

    WARN: If the < entity > population value cannot be converted to an integer the
    function returns zero (0) to the caller.

    Parameters:
        entity (dict): dictionary to parse

    Returns:
        int: returns an integer if the original value can be cast to a string;
             otherwise, returns zero (0).
    """

    try:
        return int(entity['population'])
    except:
        return 0


def write_json(filepath, data, encoding='utf-8', ensure_ascii=False, indent=2):
    """Serializes object as JSON. Writes content to the provided filepath.

    Parameters:
        filepath (str): the path to the file
        data (dict)/(list): the data to be encoded as JSON and written to the file
        encoding (str): name of encoding used to encode the file
        ensure_ascii (str): if False non-ASCII characters are printed as is; otherwise
                            non-ASCII characters are escaped.
        indent (int): number of "pretty printed" indention spaces applied to encoded JSON

    Returns:
        None
    """

    with open(filepath, 'w', encoding=encoding) as file_obj:
        json.dump(data, file_obj, ensure_ascii=ensure_ascii, indent=indent)


def main():
    """Program entry point."""

    # Configure pretty printer
    pp = pprint.PrettyPrinter(indent=2, sort_dicts=False, width=100)


    # 2.0 SORTING

    # https://www.si.umich.edu/programs/courses
    courses = [618, 506, 579, 602, 544, 630, 561, 507, 539, 564, 664, 504]
    courses_sorted = sorted(courses)

    print(f"2.0.1 courses_sorted = {courses_sorted}")

    courses_sorted = sorted(courses, reverse=True)

    print(f"2.0.2 courses_sorted reversed = {courses_sorted}")

    # In-place sort
    courses.sort() # ascending

    print(f"2.0.3 courses ascending = {courses}")

    courses.sort(reverse=True) # descending

    print(f"2.0.3 courses descending = {courses}")

    # WARN: cannot sort non-compatible types
    mix = [1, 2, 'One', 'one', 'ONE', 1.1, '1', '01', 506]
    # mix_sorted = sorted(mix) # Triggers TypeError
    # mix.sort() # Triggers TypeError


    # 2.1 Controlling the sort order with a user-defined function

    planets = read_json('./swapi_planets.json')

    # Example planet
    print('\n2.0 Tatooine')
    pp.pprint(planets[0])

    # WARN: Triggers TypeError: '<' not supported between instances of 'dict' and 'dict'
    # planets_sorted = sorted(planets)

    # Sort by population size (ascending order, smallest to largest)
    planets_sorted = sorted(planets, key=sort_by_population) # name of function only

    # Write to file
    write_json('stu-planets_sorted.json', planets_sorted)

    # Sort by population size (descending order, largest to smallest)
    planets_sorted = sorted(planets, key=sort_by_population, reverse=True)

    # Write to file
    write_json('stu-planets_sorted_reversed.json', planets_sorted)

    # Sort in-place: list.sort() method
    planets.sort(key=sort_by_population, reverse=True)

    # Example planet
    print('\n2.0 Coruscant')
    pp.pprint(planets[0])

    # Write to file
    write_json('stu-planets_sorted_inplace.json', planets)


    # 3.0 CHALLENGES

    endpoint = 'https://swapi.py4e.com/api'


    # 3.1 CHALLENGE 01

    response = get_swapi_resource(f"{endpoint}/people/", {'search': 'chewbacca'})

    print(f"\n3.1.1 Response\n{response}") # envelope

    chewie = response['results'][0] # first element

    # Alternative
    # chewie = get_swapi_resource(f"{endpoint}/people/", {'search': 'chewbacca'})['results'][0]

    print(f"\n3.1.2 Chewbacca\n{chewie}")

    # Write to file
    write_json('stu-chewie.json', chewie)


    # 3.2 CHALLENGE 02

    # Add homeworld
    chewie['homeworld'] = get_swapi_resource(chewie['homeworld'])

    # Add species
    if chewie['species']:
        chewie['species'] = get_swapi_resource(chewie['species'][0]) # list element

    print(f"\n3.2 Chewbacca enriched\n{chewie}")

    # Write to file
    write_json('stu-chewie_enriched.json', chewie)


    # 2.3 CHALLENGE 03

    swapi_x_wing = get_swapi_resource(f"{endpoint}/starships/", {'search': 't-65 x-wing'})['results'][0]

    print(f"\n3.3.1 T-65 X-wing\n{swapi_x_wing}")

    wookiee_starships = read_csv_to_dicts('wookieepedia_starships.csv')

    wookiee_x_wing = None
    for starship in wookiee_starships:
        if 'T-65 X-wing' in starship['model']:
            wookiee_x_wing = starship
            break

    # Cheat
    # wookiee_x_wing = wookiee_starships[-2] # T-65 X-wing

    # Combine
    if wookiee_x_wing:
        swapi_x_wing.update(wookiee_x_wing) # if keys match update value, else add new key-value pair

    print(f"\n3.3.2: T-65 X-wing enhanced\n{swapi_x_wing}")

    # Write to file
    write_json('stu-x_wing_enriched.json', swapi_x_wing)


    # 3.4 CHALLENGE 04

    drop_keys = ('films', 'created', 'edited', 'people', 'residents', 'species', 'starships', 'vehicles')
    x_wing = drop_data(swapi_x_wing, drop_keys) # delete key-value pairs

    print(f"\n3.4 cleaned T-65 X-wing\n{x_wing}")

    # Write to file
    write_json('stu-x_wing_cleaned.json', x_wing)


    # 3.5 CHALLENGE 05

    for i in range(len(x_wing['pilots'])):
        # Get URL
        pilot = get_swapi_resource(x_wing['pilots'][i])
        pilot = drop_data(pilot, drop_keys)

        # Get pilot's home planet
        homeworld = get_swapi_resource(pilot['homeworld'])
        pilot['homeworld'] = drop_data(homeworld, drop_keys)

        # Replace URLs
        x_wing['pilots'][i] = pilot

    # WARN: elements are not updated using a simple for loop
    # for element in x_wing['pilots']:
    #     pilot = get_swapi_resource(element)
    #     element = drop_data(pilot, drop_keys) # does not update value

    # Write to file
    write_json('stu-x_wing_pilots.json', x_wing)


    # 3.6 CHALLENGE 06

    # Access Luke and then remove the pilots key-value pair
    luke = x_wing['pilots'][0] # first element
    x_wing = drop_data(x_wing, ('pilots',)) # one-item tuple

    # Get R2-D2 (Astromech droid)
    r2 = get_swapi_resource(f"{endpoint}/people", {'search': 'r2-d2'})['results'][0]
    r2 = drop_data(r2, drop_keys)

    # Get R2-D2's home planet
    homeworld = get_swapi_resource(r2['homeworld'])
    r2['homeworld'] = drop_data(homeworld, drop_keys)

    # Add crew members
    x_wing['crew_members'] = {'pilot': luke, 'astromech_droid': r2}

    # Write to file
    write_json('stu-x_wing_crew.json', x_wing)


if __name__ == '__main__':
    main()
