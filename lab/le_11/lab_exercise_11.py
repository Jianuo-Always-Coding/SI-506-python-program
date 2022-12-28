# LAB EXERCISE 11
import copy
import pprint
import five_oh_six as utl
# TODO import the 'five_oh_six' module

print('Lab Exercise 11\n')

# SETUP CODE

villain_names = [
                'palpatine',
                'anakin skywalker',
                'grievous',
                'wilhuff tarkin',
                'dooku'
]

# END SETUP

#Problem 02
def create_person(person):
    """Returns a dictionary literal with the keys listed below (order matters).
    Leverages the get_attribute() function to access the corresponding value
    for the first five (5) keys from the passed in person dictionary.
    The last two (2) keys listed below require special handling:
        homeworld: leverages the get_attribute() function to return the string representation
            of the URL for a person's homeworld attribute. Immediately passes the returned
            URL to get_resource() in order to assign the returned decoded JSON object, representing
            the person's homeworld, to the 'homeworld' key
        species: leverages the get_attribute() function to return the string representation
            of the URL for a person's species attribute, which is stored in a list. Employs
            list indexing to access the first URL element in the list and immediately passes the returned
            string representation of the URL to get_resource(). Utilizes the correct dictionary method
            to retrieve the value assigned to the 'name' key in the return decoded JSON object representing
            the person's species.

    Keys:
        name
        height
        hair_color
        eye_color
        birth_year
        homeworld
        species

    Parameters:
        person (dict): a dictionary representation of the decoded JSON that contains person attributes.

    Returns:
        dict: a dictionary of key-value pairs representing a person.
    """
    return {
        'name': utl.get_attribute(person, 'name'),
        'height': utl.get_attribute(person, 'height'),
        'hair_color': utl.get_attribute(person, 'hair_color'),
        'eye_color': utl.get_attribute(person, 'eye_color'),
        'birth_year': utl.get_attribute(person, 'birth_year'),
        'homeworld': utl.get_resource(utl.get_attribute(person, 'homeworld')),
        'species': utl.get_resource(utl.get_attribute(person, 'species')[0]).get('name')
    }

#Problem 04
def enrich_planet(planet, wookiee_planets, filters):
    """Loops over the passed in < wookiee_planets > data to check if the passed in < planet >
    'name' matches the 'name' in < wookiee_planets >.
    If a match is obtained, it updates the < planet > dictionary with the new key-value pairs
    from < wookiee_planets >.
    Loops over the < planet > dictionary's items to check if each key is in the passed in
    < filters > list. If the key is present in < filters >, it assigns the key-vaue pair
    to a new filtered dictionary.

    Parameters:
        planet (dict): a dictionary representation of the decoded JSON that contains planet attributes.
        wookiee_planets (list): a list of dictionaries containing planet attributes sourced from Wookieepedia.
        filters (tuple): a list containing names of planet attributes.

    Returns:
        dict: an enriched dictionary of key-value pairs representing a planet.
    """
    for wookiee_planet in wookiee_planets:
        if wookiee_planet['name'].lower() == planet['name'].lower():
            planet.update(wookiee_planet)

    new_planets = {}
    for key, val in planet.items():
        if key in filters:
            new_planets[key] = val
    return new_planets

# Call functions below
def main():
    """
    This function serves as the point of entry and controls the flow of this Python script.

    Parameters:
        None

    Returns:
        None
    """

    # Configure pretty printer, if helpful
    pp = pprint.PrettyPrinter(indent=2, sort_dicts=False, width=100)


    #Problem 01
    print("\nProblem 01:")

    villains = []
    for person in villain_names:
        swapi_villain = utl.get_resource(f"{utl.SWAPI_ENDPOINT}/people", {'search': person})['results'][0]
        villains.append(swapi_villain)
    # pp.pprint(villains[0])

    # Problem 02
    print("\nProblem 02:")

    villains_created = [create_person(villain) for villain in villains]
    pp.pprint(villains_created[0])

    # Problem 03
    print("\nProblem 03:")

    wookiee_homeworlds = utl.read_csv_to_dicts('wookieepedia_planets.csv')
    # pp.pprint(wookiee_homeworlds)

    # Problem 04
    print("\nProblem 04:")

    key_filters = (
                    'name',
                    'region',
                    'sector',
                    'system',
                    'rotation_period',
                    'orbital_period',
                    'gravity',
                    'surface_water',
                    'atmosphere',
                    'climate',
                    'terrain',
                    'population',
                    'primary_languages'
    )

    for villain in villains_created:
        villain['homeworld'] = enrich_planet(villain['homeworld'], wookiee_homeworlds, key_filters)



    # Problem 05
    print("\nProblem 05:")

    villains_sorted = sorted(villains_created, key=lambda x: x['name'])
    pp.pprint(type(villains_sorted))

    # Problem 06
    print("\nProblem 06:\n")

    villains_sorted_clean = copy.deepcopy(villains_sorted)
    for villain in villains_sorted_clean:
        for k, v in villain['homeworld'].items():
            villain['homeworld'][k] = utl.convert_to_unknown(v)
    utl.write_json('stu-villain_homeworlds.json', villains_sorted)
    utl.write_json('stu-villain_homeworlds_cleaned.json', villains_sorted_clean)

if __name__ == "__main__":
    main()
