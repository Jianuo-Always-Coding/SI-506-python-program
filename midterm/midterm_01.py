# Midterm

from ast import Slice
import csv


def calculate_vax_pct(target_demographic, census_demographic, precision=None):
    """Computes the < target_demographic > vaccination percentage by dividing the
    < target_demographic > by the < census_demographic > and multiplying the result by 100. The
    computed value is then rounded to the specified < precision > integer before returning the
    computed value to the caller.

    If the caller does not specify the number of decimal places, calling the built-in < round >
    function is performed without passing it the optional second argument. In such cases the value
    returned is the nearest integer value to the computed value (e.g., 506.78914 -> 507).
    Otherwise, the function returns a floating point number with the number of decimal places to
    include in the computed value determined by the passed in < precision > value.

    The < target_demographic > comprises a particular vaccinated demographic (e.g.,
    all residents, residents 12 years and older, residents 65 years and older). The
    < census_demographic > corresponds to the total population (vaccinated and unvaccinated) for the
    specified target demographic.

    Parameters:
        target_demographic (int): vaccinated residents total for the specified county population
                            group
        census_demographic (int): total census population (vaccinated and unvaccinated) for the
                                  specified county population group
        precision (int): optional number of decimal places to round the computed value. Default
                         value is None

    Returns:
        float|int: floating point number if the < precision > is specified; otherwise the
                    value returned is the nearest integer value to the computed value
    """
    if precision:
        return round(target_demographic / census_demographic * 100, precision)

    return round(target_demographic / census_demographic * 100)

    # pass # TODO Implement


def clean_data(county):
    """Mutates the passed in < county > list by converting whole numbers masquerading as
    strings to an integer. Loops over < county > and for each element encountered delegates
    to the function < convert_to_int > the task of attempting to convert the element from a
    string (str) to an integer (int). Assigns the return value to the current element. After
    the loop terminates the county list is returned to the caller.

    Parameters:
      county (list): county vaccination data

    Returns:
       list: mutated < county > list with string elements that represent whole numbers
             converted to integers
    """
    for i in range(len(county)):
        county[i] = convert_to_int(county[i])
    return county
        # print(county[i])

def convert_to_int(value):
    """Attempts to convert a string, number or boolean < value > to an int. If a runtime
    ValueError exception is encountered, the function returns the < value > unchanged.

    WARN: This function does not convert a float value masquerading as a string to an
    integer (e.g., '506.5' -> 506). This is due to presence of a non-numeric character
    (a period) in the string. That said, the function will happily convert a float to
    an integer (e.g., 506.5 -> 506)

    Parameters:
        value (str|bool|float): string, boolean, or float value to be converted

    Returns:
        int|any: returns int if value successfully converted; otherwise returns the value
                 unchanged
    """
    try:
        return int(value)
    except ValueError:
        return value
    # pass # TODO Implement


def count_vaccinated(counties, headers, header_items):
    """Provides a two-item tuple containing the statewide vaccination count for a given population
    demographic together with the corresponding census population total across all counties.

    Loops over the < counties > list. For each nested county list encountered, delegates to the
    function < get_attribute > the task of retrieving the county's vaccinated residents
    and census population totals (vaccinated and unvaccinated) for a specified demographic
    (e.g., all residents, residents between 5 and 17 years old, residents 65 years and older).
    The function < get_attribute > is called twice to retrieve the two values.

    The < header_items > tuple provides the header names required for the two < get_attribute >
    calls. < header_items > is ordered as follows:

    ( < vaccinated residents header >, < corresponding census population header >)

    The tuple returned by this function is ordered as follows:

    ( < vaccinated residents count >, < corresponding census population count >)

    Parameters:
        counties (list): list of county lists
        headers (list): column names sourced from the first row of the CSV file
        header_items (tuple): two-item tuple comprising column names sourced from < headers >
                              that are used to look up index values

    Returns:
        tuple: statewide vaccination and census counts for a given demographic

    """
    h1 = 0
    h2 = 0
    item1, item2 = header_items
    for country in counties:
        h1 += get_attribute(country, headers, item1)
        h2 += get_attribute(country, headers, item2)
    return (h1, h2)



def get_attribute(county, headers, header):
    """Returns a < county > list element by looking up its index in the corresponding < headers >
    list using the < header > name as a filter.

    Parameters:
        county (list): county vaccination data
        headers (list): column names sourced from the first row of the CSV file
        header (str): column name sourced from < headers > that is used to look
                      up an index value

    Returns:
        any: element sourced from < county >. The value returned is usually a string but
             other return types are possible if the element has been mutated.
    """
    return county[headers.index(header)]
    # pass # TODO Implement


def get_county(counties, county_name):
    """Attempts to retrieve a nested "county" list from the passed in < counties > list by
    performing a string comparison between the nested list's county name value and the passed in
    < county_name > string. A case-insensitive string comparison is performed. If a match is
    obtained a list representing the county is returned to the caller; otherwise None is returned.

    Parameters:
        counties (list): list of lists. Each nested list represents an individual county
        county_name (str): name of a county

    Returns:
        list | None: county with a name value that matches the < county_name > or None if no match
                     was obtained.
    """
    for country in counties:
        if county_name.upper() == country[1].upper():
            return country
    return None
    # pass # TODO Implement


def get_ur_scheme(ur_codes, county_name):
    """Returns the NCHS urban/rural classification scheme code and descriptors, comprising
    the < cbsa_title >, < ur_code > (converted to an int), and < ur_code_name > associated
    with the matching < county_name > value. Name matching is case-insensitive. If no match
    is obtained the function returns None.

    Delegates to the function < convert_to_int > the task of converting the < ur_code > to
    an integer.

    Parameters:
        ur_codes (list): nested lists of NCHS urban/rural codes and descriptors
        county_name (str): name of the county (e.g., 'Washtenaw County')

    Returns:
        tuple|None: three-item tuple comprising the < cbsa_title > (str), < code > (int),
                    and < code_name > (str) for a given county; otherwise None if no
                    match is obtained
    """
    for element in ur_codes:
        if element[1].lower() == county_name.lower():
            return (element[2], convert_to_int(element[-2]), element[-1])
    return None


def read_csv(filepath, encoding='utf-8', newline='', delimiter=','):
    """
    Reads a CSV file, parsing row values per the provided delimiter. Returns a list of lists,
    wherein each nested list represents a single row from the input file.

    WARN: If a byte order mark (BOM) is encountered at the beginning of the first line of decoded
    text, call < read_csv > and pass 'utf-8-sig' as the < encoding > argument.

    WARN: if newline='' is not specified, newlines '\n' or '\r\n' embedded inside quoted fields
    may not be interpreted correctly by the csv.reader.

    Parameters:
        filepath (str): The location of the file to read
        encoding (str): name of encoding used to decode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences
        delimiter (str): delimiter that separates the row values

    Returns:
        list: nested "row" lists
    """

    with open(filepath, 'r', encoding=encoding, newline=newline) as file_obj:
        data = []
        reader = csv.reader(file_obj, delimiter=delimiter)
        for row in reader:
            data.append(row)
        return data



def write_csv(filepath, data, headers=None, encoding='utf-8', newline=''):
    """
    Writes data to a target CSV file. Column headers are written as the first
    row of the CSV file if optional headers are specified.

    WARN: If newline='' is not specified, newlines '\n' or '\r\n' embedded inside quoted
    fields may not be interpreted correctly by the csv.reader. On platforms that utilize
    `\r\n` an extra `\r` will be added.

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list | tuple): sequence to be written to the target file
        headers (seq): optional header row list or tuple
        encoding (str): name of encoding used to encode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences

    Returns:
        None
    """

    with open(filepath, 'w', encoding=encoding, newline=newline) as file_obj:
        writer = csv.writer(file_obj)
        if headers:
            writer.writerow(headers)
            for row in data:
                writer.writerow(row)
        else:
            writer.writerows(data)


def main():
    """Program entry point.

    Parameters:
        None

    Returns:
        None
    """

    # 9.1 CHALLENGE 01

    washtenaw_vax_rates = [
        ['Date', 'MMWR_week', 'Recip_County', 'Series_Complete_Yes', 'Series_Complete_Pop_Pct', 'Booster_Doses', 'Booster_Doses_Vax_Pct'],
        ['10/05/2022', 40, 'Washtenaw County', 266717, 72.6, 166848, 62.6],
        ['09/07/2022', 36, 'Washtenaw County', 265129, 72.1, 165052, 62.3],
        ['08/03/2022', 31, 'Washtenaw County', 263924, 71.8, 162532, 61.6],
        ['07/06/2022', 27, 'Washtenaw County', 263351, 71.6, 161285, 61.2],
        ['06/01/2022', 22, 'Washtenaw County', 262441, 71.4, 158801, 60.5],
        ['05/01/2022', 18, 'Washtenaw County', 261414, 71.1, 156630, 59.9],
        ['04/01/2022', 13, 'Washtenaw County', 260341, 70.8, 154744, 59.4],
        ['03/01/2022', 9, 'Washtenaw County', 258342, 70.3, 145886, 56.5],
        ['02/01/2022', 5, 'Washtenaw County', 255141, 69.4, 129506, 50.8],
        ['01/01/2022', 52, 'Washtenaw County', 251138, 68.3, 110569, 44.0],
        ['12/01/2021', 48, 'Washtenaw County', 245726, 66.8, None, None],
        ['11/01/2021', 44, 'Washtenaw County', 242688, 66.0, None, None],
        ['10/01/2021', 39, 'Washtenaw County', 230849, 62.8, None, None],
        ['09/01/2021', 35, 'Washtenaw County', 214233, 58.3, None, None],
        ['08/01/2021', 31, 'Washtenaw County', 209128, 56.9, None, None],
        ['07/01/2021', 26, 'Washtenaw County', 203868, 55.5, None, None],
        ['06/01/2021', 22, 'Washtenaw County', 185032, 50.3, None, None],
        ['05/01/2021', 17, 'Washtenaw County', 140623, 38.3, None, None],
        ['04/01/2021', 13, 'Washtenaw County', 76206, 20.7, None, None],
        ['03/01/2021', 9, 'Washtenaw County', 42605, 11.6, None, None],
        ['02/01/2021', 5, 'Washtenaw County', 17592, 4.8, None, None],
        ['01/01/2021', 53, 'Washtenaw County', 0, 0.0, None, None]
        ]


    vax_2022 = washtenaw_vax_rates[1:11] 
    # print(f"\nvax_2022 = {vax_2022}")

    vax_under_200k = washtenaw_vax_rates[-6:] 
    # print(f"\nvax_under_200k = {vax_under_200k}")

    vax_even_months = washtenaw_vax_rates[1::2] 
    # print(f"\nvax_even_months = {vax_even_months}")
    
    jan_2022_booster_pct = washtenaw_vax_rates[10][-1]
    # print(f"\njan_2022_booster_pct = {jan_2022_booster_pct}")


    # 9.2 CHALLENGE 02
    # filepath = './mi_county_covid_cases-20221014.csv'
    # case_data = read_csv(filepath)
    # 9.2.1
    case_data = read_csv('./mi_county_covid_cases-20221014.csv')
    # print(case_data)
    # 9.2.2
    case_headers = case_data[0]
    # print(case_headers)
    # 9.2.3
    case_counties = case_data[1:]
    # print(case_counties)
    # 9.2.4
    for element in case_counties:
        if "Ingham" in element[1]:
            case_ingham = element
            break
    # print(case_ingham)

    region = (
        'genesee county',
        'lapeer county',
        'livingston county',
        'macomb county',
        'monroe county',
        'oakland county',
        'washtenaw county',
        'wayne county',
        'st. clair county'
        )
    # 9.2.5
    region_cases = []

    for i in range(len(case_counties)):
        if case_counties[i][1].lower() in region:
            region_cases.append(case_counties[i])
    # print(region_cases)
    # 9.2.6
    county_name = 'franklin county'
    has_county = False

    
    # print(case_counties[i])
    i = 0
    while i < len(case_counties):
        # print(case_counties[counter])
        if county_name == case_counties[i][1]:
            has_county = True
            break
        else:
            i += 1
    # print(has_county)


    # 9.3 CHALLENGE 03

    case_jackson = get_county(case_counties, 'JACKSON COUNTY') # TODO call function
    # print(case_jackson)
    # 9.4 CHALLENGE 04

    # Add Anthony
    cases_idx = case_headers.index("cases")
    case_jackson[cases_idx] = convert_to_int(case_jackson[cases_idx]) + 1
    # print(case_jackson[cases_idx])
    


    new_cases_idx = case_headers.index("new_cases")
    case_jackson[new_cases_idx] = convert_to_int(case_jackson[new_cases_idx]) + 1
    # print(case_jackson[new_cases_idx])
    # print(f"\n3.3 case_counties nested list mutated = {case_counties[37]}")


    # 9.5 CHALLENGE 05
    vax_county_data = read_csv('./mi_county_vax_levels-20221005.csv')
    # vax_county_data = None # TODO call function
    vax_headers = vax_county_data[0]
    # print("vax_headers=",vax_headers)
    vax_counties = vax_county_data[1:]
    washtenaw = get_county(vax_counties, 'washtenaw county')
    # print(washtenaw)
    washtenaw_vax_series_complete = get_attribute(washtenaw, vax_headers, "Series_Complete_Yes")  # TODO call function
    # print(type(washtenaw_vax_series_complete))
    washtenaw_vax_series_complete = convert_to_int(washtenaw_vax_series_complete) # TODO call function
    

    # 9.6 CHALLENGE 06
    
    washtenaw_pop_total = get_attribute(washtenaw, vax_headers, "Census2019") # TODO call function
    # print(type(washtenaw_pop_total))
    washtenaw_pop_total = convert_to_int(washtenaw_pop_total) # TODO call function
    # print(washtenaw_pop_total)
    washtenaw_vax_series_complete_pct = calculate_vax_pct(washtenaw_vax_series_complete, washtenaw_pop_total, 2) # TODO call function
    # print(washtenaw_vax_series_complete_pct)

    # 9.7 CHALLENGE 07

    # print(vax_counties)
    # print(vax_counties)
    for i in range(len(vax_counties)):
        vax_counties[i] = clean_data(vax_counties[i])
    # print(vax_counties)

    genesee = get_county(vax_counties, 'Genesee County') 
    # print(genesee)
    genesee_vax_series_complete_5to17 = get_attribute(genesee, vax_headers, "Series_Complete_5to17") 
    # print(genesee_vax_series_complete_5to17)
    genesee_pop_total_5to17 = get_attribute(genesee, vax_headers, "Census2019_5to17Pop")
    genesee_vax_series_complete_5to17_pct = calculate_vax_pct(genesee_vax_series_complete_5to17, genesee_pop_total_5to17) # TODO call function
    # print(genesee_vax_series_complete_5to17_pct)

    # 9.8 CHALLENGE 08

    header_items = ("Series_Complete_18Plus", "Census2019_18PlusPop")
    # print(vax_total_18plus_pct)
    vax_total_18plus, census_total_18plus = count_vaccinated(vax_counties, vax_headers, header_items)
    vax_total_18plus_pct = calculate_vax_pct(vax_total_18plus, census_total_18plus, 2)
    # print(vax_total_18plus_pct)

    # 9.9 CHALLENGE 09

    ur_data = read_csv('./mi_ur_codes.csv')
    # print(ur_data)
    ur_headers = ur_data[0]
    ur_schemes = ur_data[1:]

    # print(len(vax_counties))
    # print(len(ur_schemes))

    # print(vax_headers)
    for i in range(len(vax_counties)):
        county_name = get_attribute(vax_counties[i], vax_headers, 'Recip_County')
        # print(county_name)
        # print(get_ur_scheme(ur_schemes, county_name))
        cbsa_title, ur_code, ur_code_name = get_ur_scheme(ur_schemes, county_name)
        vax_counties[i].insert(2, cbsa_title)
        vax_counties[i].insert(3, ur_code)
        vax_counties[i].insert(4, ur_code_name)
            # print(element)






    # for county in ur_schemes:
    #     county_name = get_attribute(county, ur_headers, "county")
    #     # print(county_name)
    #     # print(get_ur_scheme(ur_schemes, county_name))
    #     cbsa_title, ur_code, ur_code_name = get_ur_scheme(ur_schemes, county_name)

    #     for i in range(len(vax_counties)):
    #         if county_name == vax_counties[i][1]:
    #             # print("flag")
    #             vax_counties[i].insert(2, cbsa_title)
    #             vax_counties[i].insert(3, ur_code)
    #             vax_counties[i].insert(4, ur_code_name)
    #             # print(element)
    vax_headers.insert(2, ur_headers[2])
    vax_headers.insert(3, ur_headers[3])
    vax_headers.insert(4, ur_headers[4])







    # print(vax_counties)

    # 9.10 CHALLENGE 10

    large_central_and_fringe_metro = 0
    medium_and_small_metro = 0
    micropolitan = 0
    non_core = 0
    # print(vax_headers)
    for element in vax_counties:
        ur_code = get_attribute(element, ur_headers, "ur_code")
        if ur_code == 1 or ur_code == 2:
            large_central_and_fringe_metro += 1
        elif ur_code == 3 or ur_code == 4:
            medium_and_small_metro  += 1
        elif ur_code == 5:
            micropolitan += 1
        else:
            non_core += 1
    # print(non_core)

    # TODO Call write_csv() (keyword args in reverse order)
    # filepath = 'stu-mi_ur_county_vax_levels.csv'
    write_csv(headers=vax_headers, data=vax_counties, filepath='./stu-mi_ur_county_vax_levels.csv')

# Do not modify or remove this if statement
if __name__ == '__main__':
    main()
