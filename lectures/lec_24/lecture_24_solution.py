# SI 506 Lecture 24

import copy
import pprint

from datetime import datetime
from pathlib import Path

# import lecture_24_utils_solution
import lecture_24_utils_solution as utl

# from lecture_24_utils_solution import (
#     cache, convert_to_int, create_cache_key, get_resources, CACHE_FILEPATH,
#     SWAPI_ENDPOINT, SWAPI_CATEGORES, SWAPI_FILMS, SWAPI_PEOPLE, SWAPI_PLANETS,
#     SWAPI_SPECIES, SWAPI_STARSHIPS, SWAPI_VEHICLES, read_json, write_json
#     ) # (...) permits statement to be expressed accross multiple lines

# from lecture_24_utils_solution import *


def create_person(data):
    """Returns a new dictionary representation of a person from the passed in
    < data >. Calls < utl.get_swapi_resource() > to retrieve species data if
    cached data is not available.

    Type conversions:
        species -> species (str to dict)

    Key order:
        url
        name
        birth_year
        species

    Parameters:
        data (dict): source data

    Returns:
        dict: new person dictionary
    """

    if data.get('species'):
        species_data = get_swapi_resource(data['species'][0]) # checks cache
        species = create_species(species_data) # trim
    else:
        species = None

    return {
        'url': data.get('url'),
        'name': data.get('name'),
        'birth_year': data.get('birth_year'),
        'species': species
        }


def create_species(data):
    """Returns a new dictionary representation of a species from the passed in
    < data >, converting string values to the appropriate type whenever possible.

    Type conversions:
        average_lifespan -> average_lifespan (str to int)

    Key order:
        url
        name
        classification
        designation
        average_lifespan
        language

    Parameters:
        data (dict): source data

    Returns:
        dict: new dictionary
    """

    return {
        'url': data.get('url'),
        'name': data.get('name'),
        'classification': data.get('classification'),
        'designation': data.get('designation'),
        'average_lifespan': utl.convert_to_int(data.get('average_lifespan')),
        'language': data.get('language')
    }


def get_swapi_resource(url, params=None, timeout=10):
    """Retrieves deep copies of SWAPI resources from either the local < cache > dictionary
    or from a remote API if no local copy exists. Deep copies of resources retrieved remotely
    are added to the local < cache > before the resource is returned to the caller. Deep
    copying is required to guard against possible mutatation of the cache objects when
    dictionaries representing SWAPI entities (e.g., films, people, planets, species,
    starships, and vehicles) are modified by other processes.

    Deep copying: Constructs a new compound object from a given mutable object
    (e.g., list, dict), recursively copying into it objects found in the original.

    Parameters:
        url (str): a uniform resource locator that specifies the resource.
        params (dict): optional dictionary of querystring arguments.
        timeout (int): timeout value in seconds

    Returns:
        dict|list: requested resource sourced from either the local cache or a remote API
      """

    # WARN: deep copying required to guard against mutating cache objects
    key = utl.create_cache_key(url, params)
    if key in utl.cache.keys():
        return copy.deepcopy(utl.cache[key]) # recursive copy of objects
    else:
        resource = utl.get_resource(url, params, timeout)
        utl.cache[key] = copy.deepcopy(resource) # recursive copy of objects
        return resource


def main():
    """Entry point for the script.

    Paramters:
        None

    Returns:
        None
    """

    # Configure pretty printer
    pp = pprint.PrettyPrinter(indent=2, sort_dicts=False, width=100)


    # 1.0 MODULES

    # 1.3 GET MODULE NAME

    # module_name = utl.__name__

    # print(f"\n1.1: utl module name = {module_name}")


    # 1.2 IMPORTING MODULES ACCESS MODULE DEFINITIONS AND STATEMENTS

    # Get the SWAPI representation of the ice planet Hoth

    # Unaliased module
    # import lecture_24_utils_solution
    # response = lecture_24_utils_solution.get_resource(lecture_24_utils_solution.SWAPI_PLANETS, {'search': 'hoth'})
    # swapi_hoth = response['results'][0]

    # TODO Uncomment
    # print(f"\n1.2.1: SWAPI Planet Hoth={swapi_hoth}")

    # Aliased module
    # import lecture_24_utils_solution as utl
    # response = utl.get_resource(utl.SWAPI_PLANETS, {'search': 'hoth'})
    # swapi_hoth = response['results'][0]

    # TODO Uncomment
    # print(f"\n1.2.2: SWAPI Planet Hoth={swapi_hoth}")

    # Import module names directly using the < from > keyword
    # from lecture_24_utils_solution import get_resource, SWAPI_PLANETS
    # response = get_resource(SWAPI_PLANETS, {'search': 'hoth'})
    # swapi_hoth = response['results'][0]

    # TODO Uncomment
    # print(f"\n1.2.3: SWAPI Planet Hoth={swapi_hoth}")

    # Assign aliases to imported names
    # from lecture_24_utils_solution import get_resource as get, SWAPI_PLANETS as url
    # response = get(url, {'search': 'hoth'})
    # swapi_hoth = response['results'][0]

    # TODO Uncomment
    # print(f"\n1.2.4: SWAPI Planet Hoth={swapi_hoth}")


    # 1.3 BUILT-IN DIR() FUNCTION

    utl_names = dir(utl)

    print(f"\n1.3 utl module's names = {utl_names}")


    # 1.4 DEMO: MODULE/CACHING

    # Get Luke
    response = get_swapi_resource(f"{utl.SWAPI_PEOPLE}", params={'search': 'Luke Skywalker'})
    luke = create_person(response['results'][0]) # retrieves species from SWAPI

    # Get Leia
    response = get_swapi_resource(f"{utl.SWAPI_PEOPLE}", params={'search': 'Leia Organa'})
    leia = create_person(response['results'][0]) # retrieves species from cache

    # Write to file
    utl.write_json('./stu-luke_leia.json', [luke, leia])

    # Write cache to file
    utl.write_json('./stu-cache.json', utl.cache)


    # 2.2 SORTING A LIST OF STRINGS

    people = [
        'Obi-Wan Kenobi',
        'Luke Skywalker',
        'Chewbacca',
        'Leia Organa',
        'Han Solo',
        'Rey',
        'Lando Calrissian',
        'Poe Dameron',
        'Yoda'
    ]

    # Alphanumeric sort
    people_sorted = sorted(people, key=lambda x: x)

    print('\n2.0.1 Alphanumeric sort')
    pp.pprint(people_sorted)

    # Alphanumeric sort reversed
    people_sorted = sorted(people, key=lambda x: x, reverse=True)

    print('\n2.0.2 Alphanumeric sort reversed')
    pp.pprint(people_sorted)

    # Alphanumeric sort on last name
    people_sorted = sorted(people, key=lambda x: x.split()[-1])

    print('\n2.0.3 Alphanumeric sort on last name')
    pp.pprint(people_sorted)

    # Alphanumeric in-place sort
    people.sort(key=lambda x: x.split()[-1])

    print('\n2.0.3 Alphanumeric sort on last name')
    pp.pprint(people)


    # 2.2 SORTING A LIST OF DICTIONARIES

    people = [
        {'name': 'Obi-Wan Kenobi', 'force_sensitive': True},
        {'name': 'Rey', 'force_sensitive': True},
        {'name': 'Luke Skywalker', 'force_sensitive': True},
        {'name': 'Leia Organa', 'force_sensitive': True},
        {'name': 'Han Solo', 'force_sensitive': False},
        {'name': 'Yoda', 'force_sensitive': True},
        {'name': 'Chewbacca', 'force_sensitive': False},
        {'name': 'Lando Calrissian', 'force_sensitive': False},
        {'name': 'Poe Dameron', 'force_sensitive': False},
        {'name': 'Finn', 'force_sensitive': False}
    ]

    # Sort by name
    people_sorted = sorted(people, key=lambda x: x['name'])

    print('\n2.0.3 people_sorted by name')
    pp.pprint(people_sorted)

    # Sort by force_sensitive (False = 0; True = 1), name
    people_sorted = sorted(people, key=lambda x: (x['force_sensitive'], x['name']))

    print('\n2.0.4 Alphanumeric sort by force sensitivity (False, True), name')
    pp.pprint(people_sorted)

    # Sort by force_sensitive, name
    people_sorted = sorted(people, key=lambda x: (x['force_sensitive'], x['name']), reverse=True)

    print('\n2.0.5 Reverse sort by force sensitivity, name')
    pp.pprint(people_sorted)

    # Bidirectional sort by force_sensitive (True (1) then False (0)), name
    people_sorted = sorted(people, key=lambda x: (-x['force_sensitive'], x['name']))

    print('\n2.0.6 Bidirectional sort by force sensitivity (True, False), name')
    pp.pprint(people_sorted)


    # 2.4 LAMBDAS AND CONDITIONAL LOGIC

    # Note: planet https://swapi.py4e.com/api/planets/28/ named 'unknown' removed from the data set
    planet_data = utl.read_json('./planets.json')

    # Sort by population
    # WARN triggers exception
    # planets = sorted(planet_data, key=lambda x: x['population']) # Fails NoneType encountered

    # Ternary operator
    planets = sorted(planet_data, key=lambda x: x['population'] if x['population'] else 0)

    # Write to file
    utl.write_json('./stu_planets-v1p0.json', planets)

    # Sort population in reverse order: bidirectional alternatives
    planets = sorted(planet_data, key=lambda x: x['population'] if x['population'] else 0, reverse=True)
    # planets = sorted(planet_data, key=lambda x: -x['population'] if x['population'] else 0)
    # planets = sorted(planet_data, key=lambda x: -x['population'] if x['population'] else False)

    # Write to file
    utl.write_json('./stu_planets-v1p1.json', planets)

    # Sort by population (descending), then name (ascending)
    planets = sorted(planet_data, key=lambda x: (-x['population'] if x['population'] else 0, x['name']))

    # Write to file
    utl.write_json('./stu_planets-v1p2.json', planets)

    # TODO Compare v1p2 against v1p1 to demonstrate impact of multiple conditions


    # CHALLENGES

    film_data = utl.read_json('./films.json')


    # CHALLENGE 01

    # Sort by episode (descending)

    films = sorted(film_data, key=lambda x: x['episode'], reverse=True)
    # films = sorted(film_data, key=lambda x: -x['episode']) # alternative

    # Write to file
    utl.write_json('./stu_films-v1p0.json', films)


    # CHALLENGE 02

    # Sort by release_date year (ascending)
    films = sorted(film_data, key=lambda x: int(x['release_date'].split('-')[0]))
    # Alternative datetime strptime() "str parse time"
    # films = sorted(film_data, key=lambda x: datetime.strptime(x['release_date'], '%Y-%m-%d').year)

    # Write to file
    utl.write_json('./stu_films-v1p1.json', films)


    # CHALLENGE 03

    # Sort by director's last name (ascending), then by episode (ascending)
    films = sorted(film_data, key=lambda x: (x['director'].split()[-1], x['episode']))

    # Write to file
    utl.write_json('./stu_films-v1p2.json', films)


    # CHALLENGE 04

    # Sort by director's last name (ascending), then by release date year (descending)
    # Bidirectional
    films = sorted(film_data, key=lambda x: (
        x['director'].split()[-1],
        -datetime.strptime(x['release_date'], '%Y-%m-%d').year)
        )

    # Write to file
    utl.write_json('./stu_films-v1p3.json', films)


    # CHALLENGE 05

    # Sort by the number of producers (descending), episode (descending)
    films = sorted(film_data, key=lambda x: (-len(x['producers']), -x['episode']))

    # Write to file
    utl.write_json('./stu_films-v1p4.json', films)


    # CHALLENGE 06

    # In-place sort of films_data by year of release descending
    film_data.sort(key=lambda x: int(x['release_date'].split('-')[0]), reverse=True)
    # film_data.sort(key=lambda x: -int(x['release_date'].split('-')[0])) # Alternative
    # film_data.sort(key=lambda x: -datetime.strptime(x['release_date'], '%Y-%m-%d').year) # Alternative

    # Write to file
    utl.write_json('./stu_films-v1p5.json', film_data)


if __name__ == '__main__':
    main()
