# SI 506 Lecture 22

import json


def categorize_economy(country):
    """Combines The World Bank's Lower and Upper middle income categories into a
    single "Middle income" category. Returns a two-item tuple comprising the
    country name and the income group category ("High income", "Middle income',
    "Low income").

    Parameters:
        country (dict): representation of a country's economy

    Returns
       tuple: two-item tuple comprising the country name and income group
    """

    if country['income_group'].lower() == 'high income':
        return (country['country_name'], 'High income')
    elif country['income_group'].lower() in ('lower middle income', 'upper middle income'):
        return (country['country_name'], 'Middle income')
    else:
        return (country['country_name'], 'Low income')


def add_group(country, group):
    """Combines < country > and < group > data in a new dictionary if and only
    if the < country > country_code equals the < group > country_code. Otherwise
    returns None.

    If a match is obtained a selection of key-value pairs from the < country >
    and < group > dictionaries are inserted into the new dictionary in the
    following order: country_name, country_code, group_name, group_code, and
    income_group.

    Parameters:
        country (dict): represents a country
        group (dict): represents a World Bank group

    Returns:
        dict: combines country and group information in a select list of
              key-value pairs drawn from < country > and < group >
    """

    pass # TODO Implement


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


def main():
    """Entry point for program. Orchestrates workflow.

    Parameters:
        None

    Returns:
        None
    """

    # Get Country data
    countries = read_json('./wb-economies-2021_2022.json')


    # 1.0 EXAMPLE: COUNTRY NAMES

    # for loop
    country_codes = []
    for country in countries:
        country_codes.append(country['country_code'])

    # Print slice (first 5 codes)
    # print(f"\n1.2.1: for loop: country codes (n={len(country_codes)})\n = {country_codes[:5]}")

    # Clear list
    country_codes.clear() # redundant

    # print(f"\n1.2.2: country codes cleared (n={len(country_codes)})")

    # List comprehension
    country_codes = None # TODO list comp

    # Print slice (last 5 codes)
    # print(f"\n1.2.3: list comp: country codes (n={len(country_codes)})\n = {country_codes[-5:]}")


    # 2.0 TRANSFORM VALUES

    # Print slice
    # print(f"\n2.0.1: country codes: (n={len(country_codes)}) = {country_codes[:12]}")

    country_codes = None # TODO list comp

    # Print slice
    # print(f"\n2.0.2: country codes converted: (n={len(country_codes)}) = {country_codes[:12]}")

    # Mutate existing values
    for country in countries:
        if country['country_code'].islower():
            country['country_code'] = country['country_code'].upper()


    # 3.0 CONDITIONAL STATEMENTS

    # for loop
    east_asia = []
    for country in countries:
        if country['region'] == 'East Asia & Pacific':
            east_asia.append(country)

    # Print slice
    # print(f"\n3.0.1 for loop: East Asia & Pacific (n={len(east_asia)})\n = {east_asia[:2]}")

    # List comprehension (default sort = country_code)
    east_asia = None # TODO list comp

    # print(f"\n3.0.2: list comp: East Asia & Pacific (n={len(east_asia)})")

    # Write to file
    # TODO Uncomment
    # write_json('./stu-east_asia_pacific.json', east_asia)


    # 3.1 CHALLENGE 01

    # TODO Implement list comprehension

    # print(f"\n3.1 Americas: lower middle income economies (n={len(americas_low_middle)})")

    # Write to file
    # TODO Uncomment
    # write_json('./stu-americas-low_middle.json', americas_low_middle)


    # 3.2 IF-ELSE STATEMENTS

    two_categories = [
        (country['country_name'], 'High income')
        if country['income_group'].lower() == 'high income'
        else (country['country_name'], 'Middle/low income')
        for country in countries
    ]

    # Print slice
    # print(f"\n3.2 if-else two income categories (n={len(two_categories)}) = {two_categories[:12]}")


    # 3.3 IF-ELIF-ELSE (IF-ELSE-ELSE)

    three_categories = [
        (country['country_name'], 'High income')
        if country['income_group'].lower() == 'high income'
        else (country['country_name'], 'Middle income')
        if country['income_group'].lower() in ('lower middle income', 'upper middle income')
        else (country['country_name'], 'Low income')
        for country in countries
    ]

    # Print slice
    # print(f"\n3.3.1 list comp: three income categories (n={len(three_categories)}) = {three_categories[:12]}")

    three_categories = []
    for country in countries:
        if country['income_group'].lower() == 'high income':
            three_categories.append((country['country_name'], 'High income'))
        elif country['income_group'].lower() in ('lower middle income', 'upper middle income'):
            three_categories.append((country['country_name'], 'Middle income'))
        else:
            three_categories.append((country['country_name'], 'Low income'))

    # Print slice
    # print(f"\n3.3.2 for loop: three income categories (n={len(three_categories)}) = {three_categories[:12]}")

    three_categories = None # TODO list comp

    # Print slice
    # print(f"\n3.3.3 for loop: three income categories (n={len(three_categories)}) = {three_categories[:12]}")


    ## 4.0 NESTED LOOPS

    groups = read_json('./wb-groups-2021_2022.json')

    # Print slice
    # print(f"\n4.0.1 Groups (n={len(groups)})")

    arab_world = []
    for group in groups:
        if group['group_name'] == "Arab World":
            for country in countries:
                if group['country_code'] == country['country_code']:
                    arab_world.append(country)
                    break

    # Print slice
    # print(f"\n4.0.2 Arab World (n={len(arab_world)})")

    # Write to file
    # TODO Uncomment
    # write_json('./stu-arab_world-for_loop.json', arab_world)

    arab_world = [
        country
        for group in groups
        for country in countries
        if group['group_code'] == "ARB"
        and group['country_code'] == country['country_code']
        ]

    # Write to file (comment out call to write_json above)
    # TODO Uncomment
    # write_json('./stu-arab_world.json-list_comp', arab_world)


    ## CHALLENGE 02

    # TODO Write list comprehension

    # Print slice
    # print(f"\n4.1 Sub-Saharan Africa (n={len(sub_saharan_africa)})")

    # Write to file
    # TODO Uncomment
    # write_json('./stu-sub_saharan_africa.json', sub_saharan_africa)


if __name__ == '__main__':
    main()
