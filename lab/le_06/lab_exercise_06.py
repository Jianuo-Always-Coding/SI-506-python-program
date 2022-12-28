
import csv
import os
from pathlib import Path

# - START LAB EXERCISE 06
print('Lab Exercise 06 \n')


# PROBLEM 01
def read_file(filepath, encoding='utf-8'):
    """
    Opens file from the path stored in filepath argument.
    Reads the file line by line and stores each line of the file
    as a string in a list. Returns a list of strings.

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file

    Returns
        list: list of strings
    """

    # TODO - Uncomment the lines below and modify the incorrect implementation of the function.

    data = []
    with open(filepath, 'r', encoding=encoding) as file_obj:
        # return file_obj.readline()
        for line in file_obj.readlines():
            data.append(line.strip())
    return data

    


# PROBLEM 02
def has_phrase(poem, phrase):
    """Loops over the poem and checks to see if a phrase is present in the poem.

    Parameters:
        poem (list): a list of strings where each string element is a line from the poem - "The Hill We Climb".
        phrase (str): phrase to look for in the poem.

    Returns:
        bool: True or False depending on presence or absence of the phrase in the poem.
    """

    #TODO Implement function
    for line in poem:
        if phrase.lower() in line.lower():
            return True
    return False

# PROBLEM 03
def file_lines_with_phrase(poem, phrase):
    """Loops over the list poem and find the lines that contain the phrase.

    Parameters:
        poem (list): a list of strings where each string element is line from the poem - "The Hill We Climb".
        phrase (str): a string to look for in the poem.

    Returns:
        list: a list of lines of the poem that contain the phrase.
    """
    lines = []
    for line in poem:
        if phrase.lower() in line.lower():
            lines.append(line)
    return lines
     
    #TODO Implement function


# PROBLEM 04
def find_phrases(poem, phrases):
    """Loops over the list of phrases. Employs the find_phrase() and file_lines_with_phrase()
    function to find phrases that exist in the poem and the corresponding lines in which
    the phrase is a substring.

    Parameters:
        poem (list): list of strings where each string element is a line from the poem - "The Hill We Climb".
        phrases (list): list of phrases where each list element is a string.

    Returns:
        list: a list of tuples with each tuple element containing 2 elements - the phrase,
        and the list of lines that have the phrase as substring.
    """

    data = []
    for phrase in phrases:
        if has_phrase(poem, phrase):
            lines = file_lines_with_phrase(poem, phrase)
            data.append((phrase, lines))
    return data
    #TODO Implement function


# PROBLEM 05
def write_file(filepath, data, encoding='utf-8'):
    """Writes content to a target file encoded as UTF-8. Each element in the passed in sequence is written to a new line.

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list): list of tuples comprising the content to be written to the target file
        encoding (str): name of encoding used to decode the file

    Returns:
        None
    """

    #TODO Implement function
    with open(filepath, 'w', encoding=encoding) as file_obj:
        for line in data:
            file_obj.write(f"{line}\n")   

def main():
    """
    Program entry point. Controls flow of execution. All function calls must be made from main().

    Parameters:
        None

    Returns:
        None
    """

    filepath = Path('hill_we_climb.txt').absolute()

    poem = read_file(filepath)

    phrases = [
        "we will rise",
        "the American Dream",
        "diversity",
        "even as we",
        "peace",
        "terror",
        "brave enough",
        "democracy",
        "america"
                ]
    phrases_in_poem = find_phrases(poem, phrases)


    # PROBLEM 6
    frequent_phrases = []
    for phrase_detail in phrases_in_poem:
        phrase, lines = phrase_detail
        if len(lines) >= 3:
            frequent_phrases.append(lines)

    filepath = './stu_frequent_phrases_results.txt'
    # print(frequent_phrases)
    write_file(filepath, frequent_phrases)

if __name__ == '__main__':
    main()


# END LAB EXERCISE