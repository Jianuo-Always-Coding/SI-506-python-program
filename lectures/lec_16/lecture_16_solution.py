# SI 506 Lecture 16

import csv
import pprint


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
            data.append(line) # OrderedDict()
            # data.append(dict(line)) # convert OrderedDict() to dict

        return data


def write_dicts_to_csv(filepath, data, fieldnames, encoding='utf-8', newline=''):
    """
    Writes dictionary data to a target CSV file as row data using the csv.DictWriter().
    The passed in fieldnames list is used by the DictWriter() to determine the order
    in which each dictionary's key-value pairs are written to the row.

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list): dictionary content to be written to the target file
        fieldnames (seq): sequence specifing order in which key-value pairs are written to each row
        encoding (str): name of encoding used to encode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences

    Returns:
        None
    """

    with open(filepath, 'w', encoding=encoding, newline=newline) as file_obj:
        writer = csv.DictWriter(file_obj, fieldnames=fieldnames)

        writer.writeheader() # first row
        writer.writerows(data)
        # for row in data:
        #     writer.writerow(row)


def main():
    """Program entry point.  Orchestrates program's flow of execution.

    Parameters:
        None

    Returns:
        None
    """

    # Configure pretty printer
    pp = pprint.PrettyPrinter(indent=2, sort_dicts=False, width=100)


    # 1.0 DICTIONARY

    # A list
    site = [
        527,
        'Cultural',
        'Kyiv: Saint-Sophia Cathedral and Related Monastic Buildings, Kyiv-Pechersk Lavra',
        'Designed to rival Hagia Sophia in Constantinople . . . .',
        1990,
        0,
        30.51686,
        50.45258,
        28.52,
        'Europe and North America',
        'Ukraine',
        'UKR'
    ]

    print(f"\n1.0 UNESCO heritage site (list)")
    pp.pprint(site)

    # A dictionary
    site = {
        'id_no': 527,
        'category': 'Cultural',
        'name_en': 'Kyiv: Saint-Sophia Cathedral and Related Monastic Buildings, Kyiv-Pechersk Lavra',
        'short_description_en': 'Designed to rival Hagia Sophia in Constantinople . . . .',
        'date_inscribed': 1990,
        'endangered': 0,
        'longitude': 30.51686,
        'latitude': 50.45258,
        'area_hectares': 28.52,
        'region_en': 'Europe and North America',
        'states_name_en': 'Ukraine',
        'undp_code': 'UKR'
        }

    print(f"\n1.0 UNESCO heritage site (dict)")
    pp.pprint(site)

    # Type
    site_type = type(site) # <class 'dict'>

    print(f"\n1.0 site obj type = {site_type}")


    # 2.0 CREATING A DICTIONARY

    # 2.1 EMPTY DICTIONARY

    site = {}
    site['id_no'] = 1330
    site['category'] = 'Cultural'
    site['name_en'] = 'Residence of Bukovinian and Dalmatian Metropolitans'
    site['short_description_en'] = '[R]epresents a masterful synergy of architectural styles built by Czech architect Josef Hlavka from 1864 to 1882. . . .'
    site['date_inscribed'] = 2011
    site['endangered'] = 0
    site['geo_coordinates'] = {} # nested dict
    site['geo_coordinates']['longitude'] = 25.9247222222
    site['geo_coordinates']['latitude'] = 48.2966666667
    site['area_hectares'] = 8.0
    site['region_en'] = 'Europe and North America'
    site['states_name_en'] = 'Ukraine'
    site['undp_code'] = 'UKR'

    print(f"\n2.1 Key/value pair assignment\n")
    pp.pprint(site)


    # 2.2 DICTIONARY LITERAL

    site = {
        'id_no': 865,
        'category': 'Cultural',
        'name_en': "L'viv – the Ensemble of the Historic Centre",
        'short_description_en': "The city of L'viv, founded in the late Middle Ages, was a flourishing administrative, religious and commercial centre for several centuries. The medieval urban topography has been preserved virtually intact . . . .",
        'date_inscribed': 1998,
        'endangered': 0,
        'geo_coordinates': {
            'longitude': 24.03198,
            'latitude': 49.84163
            },
        'area_hectares': 120.0,
        'region_en': 'Europe and North America',
        'states_name_en': 'Ukraine',
        'undp_code': 'UKR',
        }

    print(f"\n2.2 Dict literal\n")
    pp.pprint(site)


    # 2.3 BUILT-IN DICT() FUNCTION

    # Pass in keyword arguments (note use of nested dict())
    site = dict(
        id_no=1411,
        category='Cultural',
        name_en='Ancient City of Tauric Chersonese and its Chora',
        short_description_en='The site features the remains of a city founded by Dorian Greeks in the 5th century BC on the northern shores of the Black Sea. . . .',
        date_inscribed=2013,
        endangered=0,
        geo_coordinates=dict(longitude=33.4913888889, latitude=44.6108333333),
        area_hectares=259.3752,
        region_en='Europe and North America',
        states_name_en='Ukraine',
        undp_code='UKR'
        )

    print(f"\n2.3.1 Built-in dict() keyword args\n")
    pp.pprint(site)

    # Pass in list of tuples (note used of nested dict())
    site = dict(
        [
            ('id_no', 1411),
            ('category', 'Cultural'),
            ('name_en', 'Ancient City of Tauric Chersonese and its Chora'),
            ('short_description_en', 'The site features the remains of a city founded by Dorian Greeks in the 5th century BC on the northern shores of the Black Sea. . . .'),
            ('date_inscribed', 2013),
            ('endangered', 0),
            ('geo_coordinates', dict([('longitude', 33.4913888889), ('latitude', 44.6108333333)])),
            ('area_hectares', 259.3752),
            ('region_en', 'Europe and North America'),
            ('states_name_en', 'Ukraine'),
            ('undp_code', 'UKR')
        ]
    )

    print(f"\n2.3.2 Built-in dict() list of tuples\n")
    pp.pprint(site)


    # 3.0 WORKING WITH DICTIONARIES

    # 3.1 ACCESSING A VALUE

    site = {
        'id_no': 527,
        'category': 'Cultural',
        'name_en': 'Kyiv: Saint-Sophia Cathedral and Related Monastic Buildings, Kyiv-Pechersk Lavra',
        'short_description_en': 'Designed to rival Hagia Sophia in Constantinople . . . .',
        'date_inscribed': 1990,
        'endangered': 0,
        'geo_coordinates': {
            'longitude': 24.03198,
            'latitude': 49.84163
            },
        'area_hectares': 28.52,
        'region_en': 'Europe and North America',
        'states_name_en': 'Ukraine',
        'undp_code': 'UKR'
        }

    # Accessing a value
    site_name = site['name_en']

    # TODO Uncomment (KeyError)
    # site_name = site['name'] # raises KeyError: 'name'

    print(f"\n3.1 Site name = {site_name}")


    ## 3.2 ACCESSING A NESTED VALUE

    # Accessing a nested dictionary value
    site_latitude = site['geo_coordinates']['latitude']

    print(f"\n3.2 Site latitude = {site_latitude}")


    # 3.3 ADD KEY-VALUE PAIR

    site['subregion_en'] = 'Eastern Europe'

    print(f"\n3.3.1 New key-value pair\n")
    pp.pprint(site)

    # Add nested key-value pairs
    site['street_address'] = {}
    site['street_address']['Saint-Sophia Cathedral'] = 'Volodymyrska St, 24, Kyiv, Ukraine, 01001'
    site['street_address']['Kyiv Pechersk Lavra'] = 'Lavrska St, 15, Kyiv, Ukraine, 01015'

    print(f"\n3.3.2 Street addresses\n")
    pp.pprint(site)

    # https://en.wikipedia.org/wiki/Saint_Sophia_Cathedral,_Kyiv
    # cathedral_dimensions = {
    #     'length_m': 29.5,
    #     'width_m': 29.3,
    #     'dome_height_outer_m': 28.6
    # }


    # 3.4 MODIFY AN EXISTING VALUE

    site['endangered'] = 1

    print(f"\n3.4 Modified key-value pair\n")
    pp.pprint(site)


    # 3.5 DELETE KEY-VALUE PAIR

    # Delete key-value pair
    del(site['undp_code'])

    print(f"\n3.5 Remove UNDP code\n")
    pp.pprint(site)


    # 4.0 DICTIONARY METHODS

    # 4.1 DICT.GET()

    site_type = site.get('category') # returns str

    # TODO Uncomment
    # site_type = site['type'] # triggers KeyError
    # site_type = site.get('type') # returns None
    # site_type = site.get('type', 'Undefined') # returns default value

    print(f"\n4.1 Heritage site category = {site_type}")


    # 4.2 DICT.KEYS()

    # https://data.un.org/en/iso/ua.html

    country = {
        'name': 'Ukraine',
        'region': 'Eastern Europe',
        'population': '43467000',
        'urban_population_pct': '69.5',
        'surface_area_km2': '603500',
        'capital_city': 'Kyiv',
        'un_membership_date': '1945-10-24'
    }

    print(f"\n4.2.1 dict_keys object = {type(country.keys())}") # dict_keys object

    # Loop over dict_keys object
    print(f"\n4.2.2 Country keys")
    for key in country.keys():
        print(key)

    # Convert dict_keys to a list
    country_keys = list(country.keys())

    print(f"\n4.2.3 Country keys list\n{country_keys}")

    # Loop over list of keys; print associated values
    print(f"\n4.2.4 Country values")
    for key in country_keys:
        print(country[key])


    # 4.3 DICT.VALUES()

    print(f"\n4.3.1 dict_values object = {type(country.values())}") # dict_values object

    # Loop over dict_values object
    print(f"\n4.3.1 Country values")
    for value in country.values():
        print(value)

    # Convert to a list
    country_values = list(country.values()) # convert to a list

    print(f"\n4.3.2 Country values list\n{country_values}")

    # Print value types
    print(f"\n4.3.3 Country value types")
    for value in country.values():
        print(type(value))

    # Unpacking
    site_longitude, site_latitude = site['geo_coordinates'].values()

    print(f"\n4.3.4 Site Geo coordinates = {site_longitude}, {site_latitude}")


    # 4.4 DICT.ITEMS()

    print(f"\n4.4 dict_items object = {type(country.items())}")

    # Looping over a dictionary's items
    for key, val in country.items():
        print(f"key: {key}, val: {val}")


    # 5.1 CHALLENGE 01

    # Convert value types
    for key, val in country.items():
        if key == 'population' or key == 'surface_area_km2':
            country[key] = int(val)
        elif key == 'urban_population_pct':
            country[key] = float(val)
        else:
            continue # else condition optional

    print(f"\n5.1 Country values converted\n")
    pp.pprint(country)

    # Alternative
    # int_keys = ('population', 'surface_area_km2')
    # float_keys = ('urban_population_pct',) # single item tuple

    # for key, val in country.items():
    #     if key in int_keys:
    #         country[key] = int(val)
    #     elif key in float_keys:
    #         country[key] = float(val)
    #     else:
    #         continue # else condition optional

    # print(f"\n5.1 Country values converted\n")
    # pp.pprint(country)


    # 5.2 CHALLENGE 02

    # csv.DictReader and csv.DictWriter utility functions (next lecture)

    # Get UNESCO World heritage sites
    sites = read_csv_to_dicts('./whc-sites-2022.csv')

    print(f"\nSites list length = {len(sites)}")

    # Get Ukranian sites by undp_code 'ukr'
    ukrainian_sites = []
    for site in sites:
        if site['undp_code'] == 'ukr':
            ukrainian_sites.append(site)

    # Get fieldnames (retrieve keys from selected site)
    fieldnames = ukrainian_sites[0].keys()

    # Write to file
    write_dicts_to_csv('whc-sites-ukraine-2022.csv', ukrainian_sites, fieldnames)


if __name__ == '__main__':
    main()
