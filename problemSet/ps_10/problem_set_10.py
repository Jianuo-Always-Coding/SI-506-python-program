# PROBLEM SET 10
import json
from datetime import datetime


def read_json(filepath, encoding='utf-8'):
    """Reads a JSON document, decodes the file content, and returns a list or
    dictionary if provided with a valid filepath.

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file

    Returns:
        dict/list: dict or list representations of the decoded JSON document
    """

    with open(filepath, 'r', encoding=encoding) as file_obj:
        return json.load(file_obj)


def get_subject_keyword(article):
    """Returns the subject keyword for a given article.

    Parameters:
        article (dictionary): A dictionary containing information
        about a Star Wars themed New York Times article.

    Returns:
        str: A string representation of the subject keyword
    """

    return article['keywords']['value']


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


def filter_articles(data, keys_to_exclude):
    """Filters each dictionary down to necessary information within the given < data >
    list based on the < keys_to_exclude > list.

    WARN: the comprehension expression is comprised of a dictionary comprehension
    nested within a list comprehension.

    Parameters:
        data (list): A list of dictionaries, each containing information
                     about a Star Wars themed New York Times article.
        keys_to_exclude (list): A list of key names to exclude from each article
                                dictionary.

    Returns:
        list: A list of dictionaries, each containing filtered information
              about a Star Wars themed New York Times article.
    """

    # for article in data:
    #     for k, v in article.items():
    #         if k not in keys_to_exclude:
    #             append({article[k]:v})
    return [{k: v for k, v in article.items() if k not in keys_to_exclude} for article in data]

def convert_article_value(data):
    """Converts a value in each article key-value pair. Special handling required for the
    following < data > key-value pairs:

    If the key is 'keywords', assume the value is a list. Map (i.e., assign the first element
    in the list to current article key.

    If the key is 'pub_date', assume its value is a string. Convert value to a datetime object
    using the datetime.strptime() with the datetime string formatted as

    '< Year >-< Month >-< Day >T< Hour >:< Minute >:< Second >< %z UTC offset >".

    WARN: This function employs a nested loop to interact with an article's key-value pairs.

    Parameters:
        data (list): A list of dictionaries, each containing information
                     about a Star Wars themed New York Times article.

    Returns:
        list: A list of dictionaries, with the value for all desired keys
              converted properly.
    """

    for article in data:
        for k, v in article.items():
            if k == 'keywords':
                article[k] = v[0]
            elif k == 'pub_date':
                article[k] = datetime.strptime(article['pub_date'], '%Y-%m-%dT%H:%M:%S%z')
    return data


def count_words_by_year(data):
    """Retrieves the total word count for each subject keyword by year. Each key-value
    pair in the dictionary returned to the caller possesses the following structure:

    {
        <'subject_keyword'> : {
            <pub_date year>: <word count>,
            <pub_date year>: <word count>
            }
        }

    Creates an empty dictionary named < word_count_year>. Loops over < data >.
    In the loop block performs the following tasks:

    1. Delegates to the function < get_subject_keyword > the task of retrieving the
    current article's subject keyword. Assigns return value to a local variable.

    2. Retrieves the year from the article's publication date. Assigns value
    to a local variable.

    3. Checks if the subject keyword is a member of < word_count_year > keys. If True,
    performs task described in step 4 inside a nested if-else statement. Otherwise
    maps (i.e., assigns) a new dictionary comprising a single key-value pair to the
    < word_count_year > "subject_keyword" "pub_year" key. Formats the new dictionary
    value as follows:

    {< pub_year >: < article word count >}

    4. If the previous step's conditional statement evaluates to True, implements
    a nested if-else conditional statement that checks if the current article's
    publication year is a member of the < word_count_year > "subject_keyword"
    dictionary's keys. If True ADDS the current article's word count to the
    matching < word_count_year > "subject_keyword" "pub_year" word count. If False
    maps (i.e. assigns) the current article's word count to a new < word_count_year >
    "subject_keyword" "pub_year" dictionary.

    Parameters:
        data (dictionary): A list of dictionaries, each containing information
        about a Star Wars themed New York Times article.

    Returns:
        A dictionary containing key-value pairs with the structure noted above.
    """

    word_count_year = {}
    for article in data:
        subject_keyword = get_subject_keyword(article)
        year = article['pub_date'].year
        # print(article['pub_date'].year)
        if subject_keyword in word_count_year.keys():
            if year in word_count_year[subject_keyword].keys():
                word_count_year[subject_keyword][year] += article['word_count']
            else:
                word_count_year[subject_keyword][year] = article['word_count']
        else:
            word_count_year[subject_keyword] = {}
            word_count_year[subject_keyword][year] = article['word_count']
    return word_count_year

def get_avg_word_count(star_wars_word_count):
    """Returns a new dictionary based on the passed in < star_wars_word_count >
    dictionary's key-value pairs.

    Implements a dictionary comprehension that lops over < star_wars_word_count >
    dictionary's items. The existing subject keyword keys are retained as the
    new dicitonary's key's while the value mapped (i.e., assigned) to each key
    constitutes the sum of the average of the each yearly value held in the
    the associated dictionary value (utilize dict.values() to access the values).

    The dictionary returned to the caller is structured as follows:

    {
        < subject keyword 01 >: < average of yearly values for each subject keyword >
        ...
    }

    WARN: The function block is limited to a single line of code.

    Parameters:
        star_wars_word_count (dict): A dictionary containing information about
                                     each subject and its total word count per year.

    Returns:
        dict: new dictionary structured as described above.
    """
    return {k: sum(v.values()) / len(v) for k, v in star_wars_word_count.items()}

    

def check_for_character_in_headline(article, character):
    """Checks if a character's name or part of it is present in an article's
    headline. Splits the character string into a list and loops through it.
    Utilizes case-insensitive comparison and returns True if any part of a
    character's name is present in the 'main' key of the 'headline' key within
    the article dictionary. Returns False in any other case.

    Parameters:
        article (dictionary): A dictionary containing information about a Star Wars themed New
        York Times article.
        character (str): A string representing a character's name

    Returns:
        A boolean indicating whether the character's name is present in the article's headline.
    """
    for element in character.split(' '):
        if element.lower() in article['headline']['main'].lower():
            return True
    return False

    # return character.split().lower() in article['main'].lower()

    


def star_wars_character_count(data, characters, character_count):
    """Finds the number of times a Star Wars character's name is found within an article
    headline. Utilizes a dictionary comprehension to do so. Loops over < data > and within
    the loop, looping over < characters >.

    Delegates to the the function < check_for_character_in_headline > the task of
    identifying a character's name or part of it in an article's headline. If confirmed,
    updates the < character_count > by adding one to the value of the character that was found.

    Parameters:
        data (list): A list of dictionaries, each containing information
                     about a Star Wars themed New York Times article.
        characters (list): A list of characters' names
        character_count (dict): A dictionary containing each character's name
                                and the number of times they were mentioned in an article.

    Returns:
        dict: A dictionary containing each character's name and the number of times
              they were mentioned in an article.
    """

    # for article in data:
    #     for character in characters:
    #         if check_for_character_in_headline(article, character): 
    #             character_count.update({character: character_count[character] + 1})
    # return character_count

    return {character: character_count[character] + 1 for article in data for character in characters if check_for_character_in_headline(article, character)}


def get_author_name(article):
    """Gets author name from a given article. Using a try-except block, concatenates the
    value present in the 'firstname' key within the first element of the 'person' list of
    the 'byline' key of the article with the 'lastname' key present in the same list. Make
    sure to include a space in your string concatenation between first and last name. Returns
    None if the try block triggers an error.

    Parameters:
        article (dict): A dictionary containing information
                        about a Star Wars themed New York Times article.

    Returns:
        str: A string containing the author's name.
    """

    try:
        # print(article['byline']['person'][0]['firstname'])
        return article['byline']['person'][0]['firstname'] + ' ' + article['byline']['person'][0]['lastname']
    except:
        return None

def section_authors(data):
    """Finds the author name and section of each article. Uses a list comprehension in
    order to do so. Returns a series of key-value pairs structured as follows:

    {<section name>: [<author name>]}

    Parameters:
        data (dict): A dictionary containing information about each subject
                    and its total word count per year.

    Returns:
        list: A list of dictionaries in the format noted above.
    """
    return [{article['section_name']: [get_author_name(article)]} for article in data if get_author_name(article)]

# Entry
def main():
    """Entry point for the program.

    Parameters:
        None

    Returns:
        None
    """
   
    nyt_star_wars = read_json('nyt-articles-star-wars.json')
    # print(nyt_star_wars[0])

    print('Problem 1:\n')
    
    keys_to_exclude = ['abstract', 'web_url', 'snippet', 'lead_paragraph', 'source', 'document_type', 'news_desk', 'type_of_material']
    nyt_star_wars_filtered = filter_articles(nyt_star_wars, keys_to_exclude)
    # print(nyt_star_wars_filtered[0])

    nyt_star_wars = convert_article_value(nyt_star_wars_filtered)
    # print(nyt_star_wars[0])

    print('Problem 2:\n')
    star_wars_word_count = count_words_by_year(nyt_star_wars)
    # print(star_wars_word_count)

    print('Problem 3:\n')
    avg_word_count = get_avg_word_count(star_wars_word_count)
    # print(avg_word_count)
    highest_avg = {k: v for k, v in avg_word_count.items() if v == max(avg_word_count.values())}
    # print(max(avg_word_count.values()))
    # for k, v in avg_word_count.items():
    #     # print(k)
    #     if v == max(avg_word_count.values()):
    #         highest_avg[k] = v


        
    # print(highest_avg)

    print('Problem 4:\n')
    star_wars_characters = ['Luke Skywalker', 'Darth Vader', 'Yoda', 'Leia Organa', 'Owen Lars', 'Han Solo', 'Obi Wan Kenobi']
    character_count = {'Luke Skywalker': 0, 'Darth Vader': 0, 'Yoda': 0, 'Leia Organa': 0, 'Owen Lars': 0, 'Han Solo': 0, 'Obi Wan Kenobi': 0}
    
    characters = star_wars_character_count(nyt_star_wars, star_wars_characters, character_count)
    # print(characters)

    print('Problem 5:\n')
    authors = section_authors(nyt_star_wars)
    # print(authors)
    
    authors_merged = {}

    for author in authors:
        for k, v in author.items():
            if k in authors_merged.keys(): 
                authors_merged[k].extend(v)
            else:
                authors_merged[k] = v
    print(authors_merged)

    write_json('stu_authors.json', authors_merged)


if __name__ == "__main__":
    main()
