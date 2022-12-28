import csv
import json
import requests

#Problem 01
SWAPI_ENDPOINT = "https://swapi.py4e.com/api"


#Problem 06
def convert_to_unknown(value):
    """Utilizes nested if-else statements and the built-in `isinstance()` function to first check if the
    passed in < value > is  a string, then checks if the passed in < value > is an empty string. If the < value > 
    is an empty string, the function returns the `str` 'unknown'. If the < value > is a string but is not empty,
    the function returns the < value >  unchanged. If the < value > is not a `str` instance, it returns the < value > 
    unchanged.

    Parameters:
        value: a dictionary value.

    Returns:
        str: either 'unknown' or the unchanged < value >.
    """
    if isinstance(value, str):
        if value:
            return value
        else:
            return 'unknown'
    else:
        return value

def get_attribute(dict_, key):
    """Returns the value corresponding to a passed in 'key' parameter
    by leveraging a dictionary method.

    Parameters:
        dict_ (dict): a dictionary representation of the decoded JSON.
        key (str): a string representing the desired key to access.

    Returns:
        str|list|None: a str or list value corresponding to the passed in key.
    """
    return dict_.get(key)

def get_resource(url, params=None, timeout=10):
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

#Problem 03
def read_csv_to_dicts(filepath, encoding='utf-8', newline='', delimiter=','):
    """Accepts a file path, creates a file object, and returns a list of dictionaries that
    represent the row values using the cvs.DictReader().

    WARN: This function must be implemented using a list comprehension in order to earn points.

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
        # data = []
        reader = csv.DictReader(file_obj, delimiter=delimiter)
        # for line in reader:
        #     data.append(line) # OrderedDict() | alternative: data.append(dict(line))
        return [line for line in reader]

def write_json(filepath, data, encoding='utf-8', ensure_ascii=False, indent=2):
    """Serializes object as JSON. Writes content to the provided filepath.

    Parameters:
        filepath (str): the path to the file
        data (dict)/(list): the data to be encoded as JSON and written to the file
        encoding (str): name of encoding used to encode the file
        ensure_ascii (str): if False non-ASCII characters are printed as is;
                            otherwise non-ASCII characters are escaped.
        indent (int): number of "pretty printed" indention spaces applied to
                      encoded JSON

    Returns:
        None
    """

    with open(filepath, 'w', encoding=encoding) as file_obj:
        json.dump(data, file_obj, ensure_ascii=ensure_ascii, indent=indent)