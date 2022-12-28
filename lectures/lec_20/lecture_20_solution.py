# SI 506 Lecture 20

import json
import requests


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

    # 1.0 TEST PIP INSTALL OF REQUESTS PACKAGE
    # Run swapi_request_solution.py

    # 2.0 SWAPI ENDPOINT (REMOTE SERVICE)
    # Only accepts GET requests (no PUT, POST, DELETE requests accepted)

    endpoint = 'https://swapi.py4e.com/api'


    # 2.1 SWAPI: RETURN DICT OF AVAILABLE RESOURCES (n=6)
    # /api/
    response = requests.get(endpoint + '/') # note trailing slash
    resources = response.json() # convert message payload to dict

    print(f"\n2.1 SWAPI Resources (n={len(resources)})")
    for key, val in resources.items():
        print(f"{key.capitalize()}: {val}")

    # Write to file
    output_path = 'swapi_resources.json'
    write_json(output_path, resources)


    # 2.2 SWAPI: REQUEST RESOURCES BY CATEGORY (PAGED RESPONSE n=10 records)
    # /api/:category/

    url = f"{endpoint}/people/"
    response = requests.get(url)

    payload = response.json() # decode
    payload_count = payload['count'] # get resource count
    people_returned = len(payload['results']) # SWAPI only returns max 10 records per request
    people = payload['results']

    print(f"\n2.2.1: Payload count = {payload_count}; People returned = {people_returned}\n")

    print(f"\n2.2.2: People returned (names only)")
    for person in people:
        print(person['name'])

    # Write to file
    output_path = 'swapi_people_page_01.json'
    write_json(output_path, people)


    # 2.3 SWAPI: REQUEST SINGLE RESOURCE BY ID
    # /api/:category/:id/

    url = f"{endpoint}/people/1/" # Luke Skywalker
    response = requests.get(url) # JSON representation of person returned
    person = response.json() # decode to dict

    print(f"\n2.3: Request person by id = {person}")

    # Write to file
    output_path = 'swapi_luke_skywalker.json'
    write_json(output_path, person)


    # 2.4 SWAPI: SEARCH CATEGORY FOR RESOURCE(S)
    # /api/:category/?search=<search term>

    url = f"{endpoint}/starships/"
    params = {'search': 'wing'} # dict
    response = requests.get(url, params)

    payload = response.json() # decode
    starships = payload['results']

    print(f"\n2.4: Search Starships ('wing') = {starships[0]}") # first element only

    # Write to file
    output_path = 'swapi_starships_wing.json'
    write_json(output_path, starships)


    # 3.0 SWAPI: REQUEST FUNCTION/METHOD CHAINING

    # Get the Empire Strikes Back (1980)
    url = f"{endpoint}/films/"
    params = {'search': 'empire strikes back'}
    payload = requests.get(url, params).json() # .get() function, response.json() method chaining
    film = payload['results'][0]

    print(f"\n3.0.1: Film = {film['title']} ({film['release_date']})")

    # Write to file
    output_path = 'swapi_film_empire.json'
    write_json(output_path, film)

    # Get Yoda
    url = f"{endpoint}/people/"
    params = {'search': 'yoda'}
    yoda = requests.get(url, params).json()['results'][0] # whoa

    print(f"\n3.0.2: Yoda = {yoda}")

    # Write to file
    output_path = 'swapi_yoda.json'
    write_json(output_path, yoda)


    # 3.2 UTILITY FUNCTION

    # Search and retrieve the astromech droid R2-D2
    url = f"{endpoint}/people"
    params = {'search': 'r2'}

    # Call function, pass args
    r2_d2 = get_swapi_resource(url, params)['results'][0]

    print(f"\n3.2 R2-D2 = {r2_d2}\n")

    # Write to file
    output_path = 'swapi_r2d_d2.json'
    write_json(output_path, r2_d2)


    # 3.3 ADDITIONAL RESPONSE ATTRIBUTES

    url = f"{endpoint}/people/"
    params = {'search': 'chewbacca'}
    response = requests.get(url, params)

    # Status code
    print(f"\n3.3.1 Response status code = {response.status_code}")

    # Response headers
    print(f"\n3.3.2 Response headers = {response.headers}")

    # Encoding
    print(f"\n3.3.3 Response encoding = {response.encoding}")

    # Check for bad request
    if response.raise_for_status():
        print(f"\n3.3.4 Bad request")
    else:
        print(f"\n3.3.4 Valid request")

    # Decode response
    name = response.json()['results'][0]['name']
    print(f"\n3.3.5 Resource name = {name}")


if __name__ == '__main__':
    main()
