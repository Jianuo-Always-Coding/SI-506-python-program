# SI 506 Lecture 14

import csv
import os
from pathlib import Path


def clean_data(publication):
    """Mutates the passed in < publication > list by converting numbers masquerading as
    strings to an integer (int).

    Checks each string element in the < publication > list. Delegates to the function
    < convert_to_int > the task of attempting to convert the target string to an integer.
    Strings that cannot be converted are returned unchanged.

    Parameters:
      publication (list): represents a publication

    Returns:
        list: mutated publication list
    """

    for i in range(len(publication)):
        publication[i] = convert_to_int(publication[i])
    return publication


def convert_to_int(value):
    """Attempts to convert a string, number or boolean value to an int. If
    a runtime ValueError exception is encountered, the function returns the
    value unchanged.

    Parameters:
        value (str|bool): string or boolean value to be converted

    Returns:
        int: if value successfully converted else returns value unchanged
    """

    try:
        return int(value)
    except ValueError:
        return value


def convert_to_float(value):
    """Attempts to convert a string, number or boolean value to a float. If
    a runtime ValueError exception is encountered, the function returns the
    value unchanged.

    Parameters:
        value (str|bool): string or boolean value to be converted

    Returns:
        float: if value successfully converted else returns value unchanged
    """

    try:
        return float(value)
    except ValueError:
        return value


def get_attribute(publication, headers, column_name):
    """Returns a < publication > list element by looking up its index value in
    the accompanying < headers > list using the < column_name > as the target
    header value.

    Parameters:
        publication (list): represents a publication
        headers (list): column names sourced from the first row of the CSV file
        column_name (str): provides header value used to look up the index value
                           of the target element

    Returns:
        str: element sourced from passed in publication list
    """

    pass # TODO Implement


def get_citation_count_by_year(publications, headers, year):
    """Returns the annual citation count across all < publications > per
    the provided < year >. Delegates the task of accessing each publication's
    yearly citation count to the function < get_attribute >.

    Parameters:
        publications (list): nested list of publications
        headers (list): column names sourced from the CSV
        year (str): column name (e.g., '1995')

    Returns:
        int: citation count across all publications for a given year
    """

    pass # TODO Implement


def has_umsi_faculty_author(umsi_faculty, coauthors, ignore='Resnick, Paul'):
    """Identifies whether or not a publication's < coauthors > includes at least
    one member of the UMSI faculty other than the faculty member flagged to
    < ignore >. If a match is obtained the function returns True; other False
    is returned.

    Comparing the names of faculty members and publication coauthors requires
    adoption of the following string format:

    `<last name>, <first name>`

    Parameters:
        umsi_faculty (list): nested list of UMSI faculty members
        coauthors (list): list of a publication's coauthors
        ignore (str): name of a UMSI faculty member to ignore. Default = None

    Returns:
        bool: True if a match is obtained; False otherwise
    """

    for faculty_member in umsi_faculty:
        name = ', '.join(faculty_member)
        # name = f"{faculty_member[0]}, {faculty_member[1]}" # alternative

        pass # TODO Implement conditional statement

    return False


def read_csv(filepath, encoding='utf-8', newline='', delimiter=','):
    """
    Reads a CSV file, parsing row values per the provided delimiter. Returns a list of lists,
    wherein each nested list represents a single row from the input file.

    WARN: If a byte order mark (BOM) is encountered at the beginning of the first line of decoded
    text, call < read_csv > and pass 'utf-8-sig' as the < encoding > argument.

    WARN: If newline='' is not specified, newlines '\n' or '\r\n' embedded inside quoted fields
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
    """Program entry point. Orchestrates execution flow.

    Parameters:
        None

    Returns:
        None
    """

    # 1.0 FILE PATHS: OS MODULE VS PATHLIB.PATH MODULE

    # 1.1 CURRENT WORKING DIRECTORY (CWD)

    cwd = Path.cwd() # method call
    # print(f"\n1.1.1 pathlib.path cwd = {cwd}")

    # Ye olde way
    os_cwd = os.getcwd() # function call
    # print(f"\n1.1.1 os cwd = {os_cwd}")


    # 1.2 ABSOLUTE PATH

    # 1.2.1 Parent directory this *.py
    parent_path = Path(__file__).resolve().parent
    # print(f"\n1.2.1 Path(__file__).resolve().parent = {parent_path}")

    # OR

    parent_path = Path().absolute()
    # print(f"\n1.2.1 Path.absolute() = {parent_path}")

    # OR

    parent_path = Path().resolve()
    # print(f"\n1.2.1 Path.resolve() = {parent_path}")


    # Ye olde way
    os_parent_path = os.path.dirname(os.path.abspath(__file__)) # ugly
    # print(f"\n1.2.1 os.path.dirname() = {os_parent_path}")


    # 1.2.2 This *.py absolute path
    abs_path = Path(__file__).absolute()
    # print(f"\n1.2.2 Path(__file__).absolute() = {abs_path}")

    # OR

    abs_path = Path(__file__).resolve()
    # print(f"\n1.2.2 Path(__file__).resolve() = {abs_path}")

    # OR

    # TODO Uncomment (after lecture)
    # abs_path = Path('lecture_14.py').resolve()
    # print(f"\n1.2.2 Path(__file__).resolve() = {abs_path}")

    # Ye olde way
    os_abs_path = os.path.abspath(__file__)
    # print(f"\n1.2.2 os.path.abspath(__file__) = {os_abs_path}")

    # OR

    # TODO Uncomment (after lecture)
    # os_abs_path = os.path.abspath('lecture_14.py')
    # print(f"\n1.2.2 os.path.abspath('lecture_14.py') = {os_abs_path}")

    # 1.2.3 Construct macOS and Windows friendly paths with Path.joinpath()
    parent_path = Path(__file__).resolve().parent # parent directory

    faculty_path = parent_path.joinpath('umsi-faculty.csv')
    # print(f"\n1.2.3 Path.joinpath() umsi-faculty.csv path = {faculty_path}")

    resnick_path = parent_path.joinpath('resnick-citations.csv')
    # print(f"\n1.2.3 Path.joinpath() resnick-citations.csv path = {resnick_path}")

    # print(f"\n1.2.3 resnick_path type = {type(resnick_path)}")

    # OR

    # TODO Uncomment (after lecture)
    # faculty_path = Path('umsi-faculty.csv').absolute()
    # print(f"\n1.2.3 Path('umsi-faculty.csv').absolute path = {faculty_path}")

    # resnick_path = Path('resnick-citations.csv').absolute()
    # print(f"\n1.2.3 Path('resnick-citations.csv').absolute() path = {resnick_path}")

    # Path segments

    # TODO Uncomment
    # print('\n1.2.5 Path parts',
    #     f"\nname = {resnick_path.name}",
    #     f"\nstem = {resnick_path.stem}",
    #     f"\nsuffix = {resnick_path.suffix}",
    #     f"\nparent dir = {resnick_path.parent}",
    #     f"\nparent.parent dir = {resnick_path.parent.parent}"
    #     )

    # Ye olde way
    os_parent_path = os.path.dirname(os.path.abspath(__file__)) # ugly
    os_faculty_path = os.path.join(os_parent_path, 'umsi-faculty.csv')
    os_resnick_path = os.path.join(os_parent_path, 'resnick-citations.csv')

    # print(f"\n1.2.3 os.path.join() umsi-faculty.csv path = {os_faculty_path}")
    # print(f"\n1.2.3 os.path.join() resnick-citations.csv path = {os_resnick_path}")


    # 2.0 TRY/EXCEPT

    # Read CSV file and retrieve data
    publication_data = read_csv(resnick_path)
    headers = publication_data[0]
    publications = publication_data[1:]

    # print(f"\n2.0.0 All strings = {publications[-7]}") # Recommender systems article

    for publication in publications:
        publication = clean_data(publication)

    # print(f"\n2.0.1 Integers converted = {publications[-7]}") # Recommender systems article


    # 3.0 CHALLENGES

    # 3.1 CHALLENGE 01

    idx = headers.index('Average per Year') # look up once

    # TODO Implement loop

    # print(f"\n3.1 Float converted = {publications[-7]}") # Recommender systems article


    # 3.2 CHALLENGE 02

    umsi_faculty = read_csv(faculty_path) # includes header row
    umsi_coauthored_publications = []

    # TODO Implement loop

    # Write to file
    filepath = './resnick-citations-umsi_coauthored.csv'
    # filepath = Path(__file__).resolve().parent.joinpath('resnick-citations-umsi_coauthors.csv')
    # filepath = os.path.join(abs_path, 'resnick-citations-umsi_coauthors.csv')

    # TODO Uncomment
    # write_csv(filepath, umsi_coauthored_publications, headers)


    # 3.3 CHALLENGE 03

    # Slice out the years
    idx = headers.index('1995') # first column with annual citation counts
    years = None # TODO Implement slice

    annual_counts = []

    # TODO Implement loop

    # Write to file
    filepath = './resnick-citations-annual_counts.csv'
    # filepath = Path(__file__).resolve().parent.joinpath('resnick-citations-annual_counts.csv')
    # filepath = os.path.join(abs_path, 'resnick-citations-annual_counts.csv')

    # TODO Uncomment
    # write_csv(filepath, annual_counts, ['year', 'citations'])


    # 3.4 CHALLENGE 04 (BONUS)

    max_citations = None # TODO Assign value
    max_count = None # TODO Assign value

    # TODO Implement loop

    # Write to file
    filepath = './resnick-citations-max_citations.csv'
    # filepath = Path(__file__).resolve().parent.joinpath('resnick-citations-max_citations.csv')

    # TODO Uncomment
    # write_csv(filepath, max_citations, headers)


    # 3.5 CHALLENGE 05 (BONUS)

    min_citations = None # TODO Assign value
    min_count = None # TODO Assign value

    # TODO Implement loop

    # Write to file
    filepath = './resnick-citations-min_citations.csv'
    # filepath = os.path.join(abs_path, 'resnick-citations-min_citations.csv')

    # TODO Uncomment
    # write_csv(filepath, min_citations, headers)


if __name__ == '__main__':
    main()
