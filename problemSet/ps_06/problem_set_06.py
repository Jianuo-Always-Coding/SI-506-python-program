import csv
from curses.ascii import NUL
from unittest import result
# WARN: Ensure that "import csv" is at the top of the file.
# No other import statements are required for this assignment.

print('PROBLEM SET 6\n')

# PROBLEM 1

# PROBLEM 1.1

# TODO uncomment and repair the read_csv() function
def read_csv(filepath, encoding='utf-8'):
    """
    Reads a CSV file, parsing row values per the provided delimiter. Returns a
    list of lists, wherein each nested list represents a single row from the
    input file.

    Parameters:
        filepath (str): The location of the file to read
        encoding (str): name of encoding used to decode the file

    Returns:
        data (list): list of nested "row" lists
    """

    with open(filepath, 'r', encoding=encoding) as file_obj:
        data = []
        reader = csv.reader(file_obj, delimiter=',')
        for row in reader:
            data.append(row)

        return data


# PROBLEM 2

# PROBLEM 2.1
# list_object is a list of string -- an element in data
def strip_string(list_object, character=None):
    """
    This function receives a list object containing strings with election
    information. It loops through the list and strips the strings of extra
    characters. The function checks if the optional argument character has been
    passed. If the default parameter is kept (character=None), then extra spaces
    on either side of the string are stripped. If a different character is
    passed as an argument, that character is stripped from the strings
    instead.

    Parameters:
        list_object (list): a list of strings that describe election data.
        character (str): Default=None; a string to be passed to .strip().
                         Indicates which character(s) should be stripped from
                         the strings in unit_data.
    Returns:
        None
    """
    for i in range(len(list_object)):
        list_object[i] = list_object[i].strip(character) # strip leading/trailing whitespace including '\n'





# PROBLEM 2.2

def convert_to_int(list_object):
    """
    This function receives a list object containing strings with election
    information. It loops through the list and checks if each item in the list
    can be converted to an integer. If possible, the value is converted and
    assigned to the same index position in the list

    Parameter:
        list_object (list): a list of strings that describe election data.
                            Some strings represent numbers of precincts, voters,
                            votes, or ID numbers.
    Returns:
        None
    """
    for i in range(len(list_object)):
        try:
            # print(list_object[i])
            # print(type(list_object[i]))
            list_object[i] = int(list_object[i])
        except ValueError:
            pass
            

# PROBLEM 2.3

def clean_data(data, strip=False, character=None):
    """
    Cleans data read in from a .csv file. This function receives a list of lists
    and cleans it. If strip=False, clean_data() only converts the relevant
    strings in the list into integers. If strip=True, clean_data() strips
    unnecessary characters from the strings before converting to int.

    Parameters:
        data (list): A list of lists that contain string data about
                     election results.
        strip (Bool): Default False. If True, the function strips the strings
                      before attempting to convert them to integers.
        character (str): Default None. When None, the strip_string() function
                         will strip spaces from the strings. Otherwise,
                         strip_string() will strip the passed in string.
    Returns:
        None
    """
    if strip:
        for i in range(len(data)):
            strip_string(data[i], character)
            convert_to_int(data[i])
    else:
        for i in range(len(data)):
            convert_to_int(data[i])

# PROBLEM 3

# PROBLEM 3.1

def find_fewest(column, headers, data):
    """
    Within a list of lists, this function finds the list (or multiple lists in
    case of a tie) with the smallest value for the specified column.
    For example, given the registered_voters data, it could find the city with
    the fewest active voters.

    Parameters:
        column (str): The string from the headers list that names the column of
                      interest.
        headers (list): A list of strings that name the columns for the data.
        data (list): A list of lists that contain string data about election
                     results.
    Returns:
        smallest_unit (list): A list that contains the list or lists that have
                              the smallest value for the column of interest.
    """
    smallest_value = float('inf')
    smallest_unit = []
    # print(data)
    idx = headers.index(column)
    # print(idx)

    for list in data:
        if(list[idx] == smallest_value):
            smallest_unit.append(list)
        elif(list[idx] < smallest_value):
            smallest_unit = []
            smallest_unit.append(list)
            smallest_value = list[idx]

    return smallest_unit
    # pass

# PROBLEM 4

# PROBLEM 4.1

# TODO define function
def get_active_percentage(unit_data):
    # return float
    return float(unit_data[5] / unit_data[4] * 100)

# PROBLEM 4.2

# TODO define function
def find_most_active_unit(data):
    highest_percent = 0
    most_active_unit = []
    for element in data:
        percent_active = round(get_active_percentage(element))
        if percent_active == highest_percent:   
            most_active_unit.append(([element[1]],highest_percent))
        elif percent_active > highest_percent:
            highest_percent = percent_active
            most_active_unit.clear()
            most_active_unit.append(([element[1]],highest_percent))
    return most_active_unit[0]

# PROBLEM 5

# PROBLEM 5.1

# TODO define function
def get_dem_and_rep_votes(results, headers, office_code):
    democratic_votes = 0
    republican_votes = 0
    office_idx = headers.index("OfficeCode(Text)")
    party_idx = headers.index("PartyName")
    vote_number_idx = headers.index("CandidateVotes")
    for element in results:
        if element[office_idx] == office_code and element[party_idx] == 'DEM':
            democratic_votes = democratic_votes + element[vote_number_idx]
        elif element[office_idx] == office_code and element[party_idx] == 'REP':
            republican_votes = republican_votes + element[vote_number_idx]
    return (democratic_votes, republican_votes)
# PROBLEM 6

# PROBLEM 6.1

# TODO uncomment and repair the write_csv() function
def write_csv(filepath, data, headers=None, encoding='utf-8', newline=''):
    """
    Writes data to a target CSV file. Column headers are written as the first
    row of the CSV file if optional headers are specified.

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
    """
    Serves as the main point of entry point of the program.
    """
    print('\nProblem 1\n')

    # PROBLEM 1.2

    # TODO call function
    filepath = './washtenaw_registered_voters.csv'
    registered_voters = read_csv(filepath)

    # TODO uncomment
    # print(f'1.2: Registered Voters in Washtenaw County: {registered_voters}')

    # PROBLEM 1.3
    # TODO call function
    filepath = './washtenaw_2022_primary_results.csv'
    primary_results = read_csv(filepath)

    # TODO uncomment
    # print(f'\n1.3: 2022 Primary Results for Washtenaw County: {primary_results}')

    # PROBLEM 1.4

    # TODO Create headers and data lists
    registered_headers = []
    registered_headers = registered_voters[0]
    # print(registered_headers)
    # print("\n")
    registered_voters = registered_voters[1:]

    primary_headers = primary_results[0]
    primary_results = primary_results[1:]
    # print(primary_results)



    # print(registered_voters)

    print('\nProblem 2\n')

    # PROBLEM 2.4

    # TODO call function
    
    clean_data(registered_voters)
    # TODO uncomment
    # print(f'2.4: Clean Registered Voters Data: {registered_voters}')

    # PROBLEM 2.5

    # TODO call function
    
    clean_data(data=primary_results,character='-')
    # TODO uncomment
    # print(f'\n2.5: Clean Primary Results Data: {primary_results}')

    print('\nProblem 3\n')

    # PROBLEM 3.2

    # TODO call function
    fewest_precincts = find_fewest('precincts', registered_headers, registered_voters)

    # TODO uncomment
    # print(f'The gov unit(s) with the fewests precincts: {fewest_precincts}')

    # PROBLEM 3.3

    # TODO call function
    
    fewest_votes = find_fewest('CandidateVotes', primary_headers, primary_results)


    # TODO uncomment
    # print(f'\nThe candidate(s) with the fewest votes: {fewest_votes}')

    print('\nProblem 4\n')

    # PROBLEM 4.3

    # TODO call function
    # print(find_most_active_unit(registered_voters))
    most_active_unit, percent = find_most_active_unit(registered_voters)

    # print(find_most_active_unit(registered_voters)[0])
    # TODO uncomment
    # print(f'4.3: The unit(s) with the highest percentage of active voters: {most_active_unit}.')
    # print(f'{percent}% of registered voters there are active.')

    print('\nProblem 5\n')

    # PROBLEM 5.2

    vote_totals_headers = ['Office Name', 'Office Code', 'Votes for Democrats', 'Votes for Republicans']
    vote_totals = [
        ['Governor', 2],
        ['Representative in Congress', 6],
        ['State Senator', 7],
        ['District Representative in State Legislature', 8]
        ]
    # print(primary_results)
    for element in vote_totals:
        democratic_votes, republican_votes = get_dem_and_rep_votes(primary_results, primary_headers, element[1])
        element.append(democratic_votes)
        element.append(republican_votes)


    # TODO create for loop

    # TODO uncomment
    # print(f'5.2: The vote totals by party and office: {vote_totals}')

    # PROBLEM 6.2

    # TODO call function
    filepath = './primary_votes_by_party.csv'
    write_csv(filepath, vote_totals, headers=vote_totals_headers)

    test = None
    if test == None:
        print('I am None')

# WARN: do not modify or remove the following if statement.

if __name__ == '__main__':
    main()