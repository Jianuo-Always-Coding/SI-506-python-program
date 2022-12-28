# SI 506 Lecture 25

import copy
import pprint
import five_oh_six_solution as utl

from datetime import datetime


# Cache
cache = utl.create_cache(utl.CACHE_FILEPATH)


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


def create_starship(data):
    """Returns a new starship dictionary from the passed in < data >, converting string
    values to the appropriate type whenever possible. Delegates to the function
    < create_film > the task of creating film dictionaries.

    Type conversions:
        hyperdrive_rating -> hyperdrive_rating (str to float)
        MGLT -> top_speed_mglt (str to int)
        crew -> crew_size (str to int)
        armament -> armament (str to list)

    Key order:
        url
        name
        model
        starship_class
        hyperdrive_rating
        top_speed_mglt
        crew_size
        armament

    Parameters:
        data (dict): source data

    Returns:
        dict: new dictionary
    """

    return {
        'url': data.get('url'),
        'name': data.get('name'),
        'model': data.get('model'),
        'starship_class': data.get('starship_class'),
        'hyperdrive_rating': utl.convert_to_float(data.get('hyperdrive_rating')),
        'top_speed_mglt': utl.convert_to_float(data.get('MGLT')),
        'crew_size': utl.convert_to_int(data.get('crew')),
        'armament': utl.convert_to_list(data.get('armament'), ',')
    }


def get_swapi_resource(url, params=None, timeout=10):
    """Retrieves a deep copy of a SWAPI resource from either the local < cache >
    dictionary or from a remote API if no local copy exists. Delegates to the function
    < utl.create_cache_key > the task of minting a key that is used to identify a cached
    resource. If the desired resource is not located in the cache, delegates to the
    function < get_resource > the task of retrieving the resource from SWAPI.
    A deep copy of the resource retrieved remotely is then added to the local < cache > by
    mapping it to a new < cache[key] >. The mutated cache is written to the file
    system before a deep copy of the resource is returned to the caller.

    WARN: Deep copying is required to guard against possible mutatation of the cached
    objects when dictionaries representing SWAPI entities (e.g., films, people, planets,
    species, starships, and vehicles) are modified by other processes.

    Parameters:
        url (str): a uniform resource locator that specifies the resource.
        params (dict): optional dictionary of querystring arguments.
        timeout (int): timeout value in seconds

    Returns:
        dict|list: requested resource sourced from either the local cache or a remote API
      """

    key = utl.create_cache_key(url, params)
    if key in cache.keys():
        return copy.deepcopy(cache[key]) # recursive copy of objects
    else:
        resource = utl.get_resource(url, params, timeout)
        cache[key] = copy.deepcopy(resource) # recursive copy of objects
        utl.write_json('./stu-cache.json', cache) # persist mutated cache

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

    # 1.1 CACHING

    # Get Anakin
    response = get_swapi_resource(f"{utl.SWAPI_PEOPLE}", params={'search': 'Anakin Skywalker'})
    anakin = create_person(response['results'][0]) # retrieves species from SWAPI

    # Get Obi-wan
    response = get_swapi_resource(f"{utl.SWAPI_PEOPLE}", params={'search': 'Obi-wan Kenobi'})
    obi_wan = create_person(response['results'][0]) # retrieves species from cache

    # Write to file
    utl.write_json('./stu-jedi.json', [anakin, obi_wan])


    # 2.0 ISINSTANCE()

    # WARN: isinstance(jedi, None) triggers a TypeError
    # WARN: isinstance(jedi, NoneType ) triggers a NameError
    # isinstance(jedi, type(None)) evaluates without triggering an exception

    # Preferred: negate the truth value of None or use the identity operator < is > since
    # < None > is the sole singleton < NoneType > object

    jedi = []
    # jedi = {}
    # jedi = ''
    # jedi = None
    if isinstance(jedi, list):
        jedi.append(obi_wan)
        jedi.append(anakin)
    elif isinstance(jedi, dict):
        jedi['obi_wan'] = obi_wan
        jedi['anakin'] = anakin
    elif isinstance(jedi, str):
        jedi = f"{anakin['name']}, {obi_wan['name']}"
    elif not jedi:
        jedi = f"{anakin['url']}, {obi_wan['url']}"
    # elif jedi is None:
    #     jedi = f"{anakin['url']}, {obi_wan['url']}"

    print('\n2.0 jedi')
    pp.pprint(jedi)


    # 4.0 CHALLENGES


    # 4.1 CHALLENGE 01

    assert utl.convert_to_float('500') == 500.0
    assert utl.convert_to_float('500.9999') == 500.9999
    assert utl.convert_to_float('500,000,000.9999') == 500000000.9999

    assert utl.convert_to_int('500') == 500
    assert utl.convert_to_int('500,000,000') == 500000000


    # 4.2 CHALLENGE 02

    assert utl.convert_to_int('500,000,000') == 500000000
    assert utl.convert_to_int('500,000,000.9999') == 500000000


    # 4.3 CHALLENGE 03

    assert utl.convert_to_list('Use the Force') == ['Use', 'the', 'Force']

    assert utl.convert_to_list(
        'tundra|ice caves|mountain ranges',
        '|') == ['tundra', 'ice caves', 'mountain ranges']

    assert utl.convert_to_list(
        'tundra, ice caves, mountain ranges',
        ', ') == ['tundra', 'ice caves', 'mountain ranges']


    # 4.4 CHALLENGE 04

    swapi_starships = utl.read_json('./episode_iv_starships.json')
    wookiee_starships = utl.read_csv_to_dicts('./wookieepedia_starships.csv')

    # Combine data (in-place update)
    for swapi_starship in swapi_starships:
        for wookiee_starship in wookiee_starships:
            if swapi_starship['model'].lower() == wookiee_starship['model'].lower():
                swapi_starship |= wookiee_starship # Union/Merge operator >= Python 3.9
                # swapi_starship.update(wookiee_starship) # < Python 3.9
                break

    # Write to file
    utl.write_json('stu-starships_v1p0.json', swapi_starships)


    # 4.5 CHALLENGE 05

    starships = [create_starship(starship) for starship in swapi_starships]

    # Write to file
    utl.write_json('stu-starships_v1p1.json', starships)


    # 4.6 CHALLENGE 06
    starships.sort(key=lambda x: x['name'], reverse=True)
    print(type(starships))
    # Write to file
    utl.write_json('stu-starships_v1p2.json', starships)


    # 4.7 CHALLENGE 07

    hyperdrive_ratings = sorted(
        starships,
        key=lambda x: (
            x['hyperdrive_rating'] if x['hyperdrive_rating'] else float('inf'),
            x['name']
            )
        )

    # Write to file
    utl.write_json('stu-starships_v1p3.json', hyperdrive_ratings)


if __name__ == '__main__':
    main()
