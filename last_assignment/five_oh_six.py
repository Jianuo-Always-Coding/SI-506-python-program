import csv
import json
import requests

from urllib.parse import quote, urlencode, urljoin


# Constants
CACHE_FILEPATH = './CACHE.json'
NONE_VALUES = ('', 'n/a', 'none', 'unknown')
SWAPI_ENDPOINT = 'https://swapi.py4e.com/api'
SWAPI_CATEGORES = f"{SWAPI_ENDPOINT}/"
SWAPI_PEOPLE = f"{SWAPI_ENDPOINT}/people/"
SWAPI_PLANETS = f"{SWAPI_ENDPOINT}/planets/"
SWAPI_SPECIES = f"{SWAPI_ENDPOINT}/species/"
SWAPI_STARSHIPS = f"{SWAPI_ENDPOINT}/starships/"


def convert_gravity_value(value):
    """Convert a planet's "gravity" value in the < try > block to a float. Removes the "standard"
    unit of measure if it exists in the string (case insensitive comparison). Delegates to the
    function < convert_to_float() > the task of casting the < value > to a float.

    If a runtime exception is encountered the < value > is returned unchanged in the except block.

    Parameters:
        value (obj): string to be converted

    Returns:
        float: if value successfully converted; otherwise returns value unchanged
    """

    try:
        if 'standard' in value.lower():
            a = value.lower().strip().strip('standard')
        else:
            a = value
        return convert_to_float(a)
    except:
        return convert_to_none(value, NONE_VALUES)




def convert_to_float(value):
    """Attempts to convert a string, number, or boolean < value > in the < try > block to a float.
    Can also convert numbers masquerading as strings that include one or more thousand separator
    commas (e.g., "5,000,000").

    If a runtime exception is encountered the < value > is returned unchanged in the except block.

    Parameters:
        value (obj): string or number to be converted

    Returns:
        float|any: float if value successfully converted; otherwise returns value unchanged
    """

    try:
        if type(value) == str:
            return float(value.strip().replace(',', ''))
        if type(value) == int:
            return float(value)
        return value
    except:
        return value



def convert_to_int(value):
    """Attempts to convert a string, number boolean < value > in the < try > block to an integer.
    Can also convert numbers masquerading as strings that include one or more thousand separator
    commas (e.g., "5,000,000") or a period that designates a fractional component
    (e.g., "5,000,000.9999").

    If a runtime exception is encountered the < value > is returned unchanged in the except block.

    Parameters:
        value (str|int): string or number to be converted

    Returns:
        int|any: integer if value successfully converted else returns value unchanged
    """

    try:
        if type(value) == str:
            value = value.split('.')[0]
            value = value.strip().replace(',', '')
            # print(type(int(value)))
            return int(value)
        else:
            return int(value)
    except:
        return value


def convert_to_list(value, delimiter=None):
    """Attempts to convert a string < value > to a list in the < try > block using the provided
    < delimiter >. Removes leading/trailing spaces before converting < value > to a list.

    If a runtime exception is encountered the < value > is returned unchanged in the except block.

    Parameters:
        value (str): string to be split.
        delimiter (str): optional delimiter provided for splitting the string

    Returns:
         list|any: list if value successfully converted else returns value unchanged
    """

    try:
        # value = value.replace(',', '')
        if value.strip().replace(',', '').lower() in NONE_VALUES:
            return None
        if delimiter:
            return value.strip().split(delimiter)
        else:
            return value.strip().replace(',', '').split()
    except:
        return value


def convert_none_values(data, convert):
    """Attempts to convert certain < data > values to < None > by passing each value in < data >
    along with < convert > to the function < convert_to_none >.

    Loops over the < data > items and calls < convert_to_none > to transform values found in
    < convert > from within a dictionary comprehension. Existing < data > keys are used in the new
    dictionary produced by the comprehension.

    Parameters:
        data (dict): source data
        convert (tuple): strings to convert to None

    Returns:
        dict: new dictionary in which values found in < convert > have been replaced by
              < None >
    """
    
    return {key: convert_to_none(val, convert) for key, val in data.items()}
    # for key, val in data.items():
    #     if val.strip().lower() in convert:
    #         dic[key] = convert_to_none(val, NONE_VALUES)
    #     else:
    #         dic[key] = val
    # return dic

def convert_to_none(value, convert):
    """Attempts to convert the passed in < value > to < None > in the < try > block if the < value >
    matches any of the strings in the passed in tuple < to_convert >.

    Leading/trailing spaces are removed from the < value > before a case insensitive comparison is
    performed between the < value > and the < to_convert > items. If a match is obtained < None > is
    returned; otherwise the < value > is returned unchanged.

    If a runtime exception is encountered the < value > is returned unchanged in the except block.

    Parameters:
        value (obj): string or number to be converted
        convert (tuple): strings to convert to None

    Returns:
        None|any: if value successfully converted; otherwise returns value unchanged
    """

    try:
        if value.strip().lower() in convert:
            return None
        else:
            return value
    except:
        return value


def convert_to_year_era(value):
    """Attempts to separate the Galactic standard calendar "year" and "era" (e.g., 896BBY, 24ABY)
    segments in < value > in the < try > block for storage in a dictionary.

    In the < try > block the function first checks if the "year" segment of < value > is a number by
    employing the appropriate string method. If the substring is numeric, the function returns a
    dictionary literal that maps the necessary slicing expressions to "year" and "era" keys as
    values. The dictionary is structured as follows:

    {'year': < year > (int), 'era': < era > (str)}

    {'year': 896, 'era': BBY}

    Otherwise, if the "year" segment is not considered numeric return the `value` to the caller
    unchanged.

    If the year segment is numeric, delegates to the function < convert_to_int() > the task of
    converting the segment representing the year to an integer. The function is called from within
    the dictionary literal.

    If a runtime exception is encountered the < value > is returned unchanged in the except block.

    Parameters:
        value (str): Galactic YearEra string to be converted

    Returns:
        dict: comprising year and era key-value pairs
     """

    try:
        if len(value) > 3 and value[-3:] in ('BBY', 'ABY'):
            if type(int(value[:-3])) == int:
                return {'year': int(value[:-3]), 'era': value[-3:]}
        else:
            return value
    except:
        return value


def create_cache(filepath):
    """Attempts to retrieve cache contents written to the file system. If successful the
    cache contents from the previous script run are returned to the caller as the new
    cache. If unsuccessful an empty cache is returned to the caller.

    Parameters:
        filepath (str): path to the cache file

    Returns:
        dict: cache either empty or populated with resources from the previous script run
    """

    try:
        return read_json(filepath)
    except FileNotFoundError:
        return {}


def create_cache_key(url, params=None):
    """Returns a lowercase string key comprising the passed in < url >, and, if < params >
    is not None, the "?" separator, and any URL encoded querystring fields and values.
    Passes to the function < urllib.parse.urljoin > the optional < quote_via=quote >
    argument to override the default behavior and encode spaces with '%20' rather
    than "+".

    Example:
       url = https://swapi.py4e.com/api/people/
       params = {'search': 'Anakin Skywalker'}
       returns 'https://swapi.py4e.com/api/people/?search=anakin%20skywalker'

    Parameters:
        url (str): string representing a Uniform Resource Locator (URL)
        params (dict): one or more key-value pairs representing querystring fields and values

    Returns:
        str: Lowercase "key" comprising the URL and accompanying querystring fields and values
    """

    if params:
        return urljoin(url, f"?{urlencode(params, quote_via=quote)}").lower() # space replaced with '%20'
    else:
        return url.lower()


def get_resource(url, params=None, timeout=10):
    """Returns a response object decoded into a dictionary. If query string < params > are
    provided the response object body is returned in the form on an "envelope" with the data
    payload of one or more entities to be found in ['results'] list; otherwise, response
    object body is returned as a single dictionary representation of the entity.

    Parameters:
        url (str): a uniform resource locator that specifies the resource.
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
        return [line for line in reader]
        # for line in reader:
        #     data.append(line) # OrderedDict() | alternative: data.append(dict(line))

       


def read_json(filepath, encoding='utf-8'):
    """Reads a JSON document, decodes the file content, and returns a list or dictionary if
    provided with a valid filepath.

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
