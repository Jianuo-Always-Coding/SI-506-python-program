# LAB EXERCISE 09
import json
import requests
import pprint

print(f'\nLab Exercise 09')
print(f'\n20th Century Fox')
print(f'\nA LUCASFILM LIMITED Production')
print(f'\nA long time ago in a galaxy far, far away....')
print(f'\nSWAPI: The Star Wars API')

# SETUP CODE
ENDPOINT = 'https://swapi.py4e.com/api'

dialogue = {
            "C-3PO":
                [
                "Did you hear that?",
                "They've shut down the main reactor.",
                "We'll be destroyed for sure. This is madness!",
                "We're doomed!",
                "There'll be no escape for the Princess this time.",
                "What's that?"
                ],
            "R2-D2":
                [
                "beep, beep, boop.",
                "boop, beep, beep.",
                "boop, beeeep!"
                ],
            "Darth Vader":
                [
                "sound of evil mechanical breathing"
                ]
            }
# END SETUP

# PROBLEM 01

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


# PROBLEM 02

def get_attribute(dict_, key):
    """Returns the value corresponding to a passed in 'key' parameter
    by leveraging a dictionary method.

    Parameters:
        dict_ (dict): a dictionary representation of the decoded JSON.
        key (str): a string representing the desired key to access.

    Returns:
        str | list | None: a str or list value corresponding to the passed in key.
    """

    return  dict_.get(key)

# PROBLEM 03

def create_starship(starship):
    """Returns a dictionary literal with the following keys:
        name
        model
        passengers
        max_atmosphering_speed
        length
    Leverages the get_attribute() function to access the corresponding value
    for certain keys (indicated above) present in the passed in starship dictionary,
    except for the 'passengers' key. Assign an empty list to the 'passengers' key instead 
    of utilizing the get_attribute() function.

    Parameters:
        starship (dict): a dictionary representation of the decoded JSON that contains starship attributes.

    Returns:
        dict: a dictionary of key-value pairs representing a starship.
    """

    return {
        'name': get_attribute(starship, 'name'),
        'model': get_attribute(starship, 'model'),
        'passengers': [],
        'max_atmosphering_speed': get_attribute(starship, 'max_atmosphering_speed'),
        'length': get_attribute(starship, 'length')
    }

# PROBLEM 04

def create_person(person):
    """Returns a dictionary literal with the following keys:
        name
        height
        mass
        birth_year
        eye_color
        dialogue
    Leverages the get_attribute() function to access the corresponding value
    for certain keys (indicated above) present in the passed in person dictionary,
    except for the 'dialogue' key. Assign an empty list to the 'dialogue' key instead
    of utilizing the get_attribute() function.

    Parameters:
        person (dict): a dictionary representation of the decoded JSON that contains people attributes.

    Returns:
        dict: a dictionary of key-value pairs representing a person.
    """

    return {
        'name': get_attribute(person, 'name'),
        'height': get_attribute(person, 'height'),
        'mass': get_attribute(person, 'mass'),
        'birth_year': get_attribute(person, 'birth_year'),
        'eye_color': get_attribute(person, 'eye_color'),
        'dialogue': []
    }

# PROBLEM 05

def board_starship(starship, people):
    """Loops over the passed in people list, which is a list of tuples each representing people/passengers
        on the starship.
    Each tuple contains a variable assigned to a decoded JSON representing a person (in the 0th index) and
        a boolean indicating their intruder status (True, if intruder; False, if just a passenger) (in the 1st index).
        ex. [(< person_variable > , < intruder_bool > ), (< person_variable > , < intruder_bool > )]
    Utilizes sequence unpacking to access the 'person' element and the 'intruder' status element from
        the passed in list of tuples.
    Utilizes an if-elif-else statement and compound conditionals to evaluate the truth value of the 'intruder'
    status and check the following conditions:
        (1) If the 'intruder' status element evaluates to True and 'intruder' is already a key in the starship dictionary,
            then it simply appends the 'person' to the 'intruder' key-value pair.
        (2) If the 'intruder' status element evaluates to True and 'intruder' is not yet a key in the starship dictionary,
            then it assigns a list literal containing the 'person' to the new 'intruder' key.
        (3) Otherwise, it appends the 'person' to the 'passengers' key.

    Parameters:
        starship (dict): a dictionary representation of the decoded JSON that contains starship attributes.
        people (list): a list of tuples where, for each tuple, a variable assigned to the decoded JSON representing
        a person is at the 0th index and a bool value indicating whether they are an intruder is at the 1st index.

    Returns:
        dict: an updated dictionary of key-value pairs representing a starship.
    """

    # for person in people:
    #     if person[1] == True and 'intruder' in starship.keys():
    #         starship['intruder'].append(person[0])
    #     elif person[1] == True and 'intruder' not in starship.keys():
    #         starship['intruder'] = [person[0]]
    #     else:
    #         starship['passengers'].append(person[0])

    for passenger in people:
        person, instruder = passenger
        if instruder and 'instruder' in starship:
            starship['instruder'].append(person)
        elif instruder and 'instruder' not in starship:
            starship['instruder'] = [person]
        else:
            starship['passengers'].append(person)
    return starship


# Problem 06

def capture_starship(starship_attacker, starship_captured):
    """Utilizes a conditional statement to check if the key 'primary_docking_bay'
    is not already present in the decoded JSON representing an attacking starship.

    If the conditional statement evaluates to 'True', it assigns the new key
    'primary_docking_bay' with a dictionary literal as its value. The dictionary
    literal has a key of 'docked' and a list literal containing the < starship_captured >
    as its value. Otherwise, it gets access to the value of the key 'primary_docking_bay'
    and appends the < starship_captured > to the 'docked' key.

    Parameters:
        starship_attacker (dict): a dictionary representation of the decoded JSON
        that contains attributes of an attacking starship.
        starship_captured (dict): a dictionary representation of the decoded JSON
        that contains attributes of a starship that is being captured.

    Returns:
        dict: an updated dictionary representation of the decoded JSON
        representing the attacking starship.
    """

    if 'primary_docking_bay' not in starship_attacker.keys():
        starship_attacker['primary_docking_bay'] = {'docked': [starship_captured]}
    else:
        starship_attacker['primary_docking_bay']['docked'].append(starship_captured)
    return starship_attacker
# Problem 07

def insert_dialogue(person, dialogue):
    """Loops over the < dialogue > dictionary key-value pairs accessing the dictionary's items
    leveraging the dictionary method `dict.items()`. Utilizes a conditional statement
    to check if the value corresponding to the 'name' key in the < person > dictionary
    matches a key in the < dialogue > dictionary.

    If the conditional statement evaluates to 'True', a list method that adds the
    elements of a list to the end of the current list is leveraged to update the
    'dialogue' key-value pair in the < person > dictionary.

    Parameters:
        person (dict): a dictionary representation of the decoded JSON that contains people attributes.
        dialogue (dict): a dictionary whose key-value pairs each represent a person and their dialogue.

    Returns:
        person (dict): a dictionary representation of the decoded JSON that contains people attributes.
    """

    for key, value in dialogue.items():
        if person['name'] == key:
            person['dialogue'].extend(value)
    return person


def write_json(filepath, data, encoding='utf-8', indent=2):
    """Serializes object as JSON. Writes content to the provided filepath.

    Parameters:
        filepath (str): the path to the file

        data (dict)/(list): the data to be encoded as JSON and written to
        the file

        encoding (str): name of encoding used to encode the file

        indent (int): number of "pretty printed" indention spaces applied to
        encoded JSON

    Returns:
        None
    """

    with open(filepath, 'w', encoding=encoding) as file_obj:
        json.dump(data, file_obj, indent=indent)

# Call functions below
def main():
    """
    This function serves as the point of entry and controls the flow of this Python script

    Parameters:
        None

    Returns:
        None
    """
    # Configure pretty printer, if helpful
    pp = None


    # Problem 01
    print("\nProblem 01:")

    swapi_new_hope = get_swapi_resource(ENDPOINT+'/films', {'search':'new hope'})['results'][0]
    # print(swapi_new_hope)

    # Problem 02
    print("\nProblem 02:")

    opening_crawl = get_attribute(swapi_new_hope, 'opening_crawl')
    # print(opening_crawl)


    # Problem 03
    print("\nProblem 03:")

    swapi_rebel_blockade = get_swapi_resource(ENDPOINT+'/starships', {'search': 'CR90 corvette'})['results'][0]

    rebel_blockade = create_starship(swapi_rebel_blockade)
    # print(rebel_blockade)
    swapi_stardestroyer = get_swapi_resource(ENDPOINT+'/starships', {'search': 'destroyer'})['results'][0]

    stardestroyer = create_starship(swapi_stardestroyer)


    # Problem 04
    print("\nProblem 04:")

    swapi_r2d2 = get_swapi_resource(ENDPOINT+'/people', {'search': 'R2-D2'})['results'][0]

    r2d2 = create_person(swapi_r2d2)

    swapi_c3po = get_swapi_resource(ENDPOINT+'/people', {'search': 'C-3PO'})['results'][0]

    c3po = create_person(swapi_c3po)


    # Problem 05
    print("\nProblem 05:")

    people = [(r2d2, False), (c3po, False)]
    board_starship(rebel_blockade, people)
    # print(rebel_blockade)


    #Problem 06
    print("\nProblem 06:")
    capture_starship(stardestroyer, rebel_blockade)


    #Problem 07
    print("\nProblem 07:")
    insert_dialogue(r2d2, dialogue)
    insert_dialogue(c3po, dialogue)

    #Problem 08
    print("\nProblem 08:")

    swapi_vader = get_swapi_resource(ENDPOINT+'/people', {'search': 'vader'})['results'][0]

    vader = create_person(swapi_vader)

    people = [(vader, True)]
    board_starship(rebel_blockade, people)
    insert_dialogue(vader, dialogue)
    write_json('stu_stardestroyer.json', stardestroyer)
if __name__ == "__main__":
    main()
