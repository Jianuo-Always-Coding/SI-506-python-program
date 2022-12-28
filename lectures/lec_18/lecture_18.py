# SI 506 Lecture 18

import json
import pprint
import re

from datetime import datetime as dt


def has_subject(keyword, name, value):
    """Determines if the passed in < keyword > dictionary contains passed in the
    < name > and < value > values. If a match is obtained the boolean True is
    returned; otherwise False is returned.

    keyword = {'name': < name >, 'value': < value >, ...}

    Parameters:
        keyword (dict): "name", "value", and other key-value pairs
        name (str): keyword['name'] value
        value (str): keyword['value'] value

    Returns:
        bool: True if a match is obtained; otherwise False
    """

    if keyword['name'] == name and keyword['value'] == value:
        return True
    else:
        return False


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
    """Program entry point.  Orchestrates program's flow of execution.

    Parameters:
        None

    Returns:
        None
    """

    # Configure pretty printer
    pp = pprint.PrettyPrinter(indent=2, sort_dicts=False, width=100)

    # 2.3 CHALLENGE 01
    articles = None # Call function

    # print(f"\n2.3.1 All articles (n={len(articles)})")

    # Get 2022 articles only
    articles_2022 = []

    # TODO Implement loop

    # print(f"\n2.3.2 2022 articles (n={len(articles_2022)})")

    # Write to file

    # TODO Call function


    # 3.0 NESTED LOOPS

    nums = [
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40, 50],
        [100, 200, 300, 400, 500],
        [1000, 2000, 3000, 4000, 5000]
    ]

    # print(f"\n3.0 Nested loop example")

    # TODO Implement loop

    # Get all articles touching on Dementia
    dementia = []

    # TODO Uncomment
    # for article in articles:
    #     for keyword in article['keywords']:
    #         if keyword['name'] == 'subject' and keyword['value'] in ("Alzheimer's Disease", 'Dementia'):
    #             dementia.append(article)
    #             break # avoid appending duplicates due to either/or membership check

    # print(f"\n3.0 Dementia articles (n={len(dementia)})")

    # Write to file
    # write_json('stu-nyt-dementia-articles.json', dementia)


    # 3.1 CHALLENGE 02

    # Get all subjects, group by first character in string
    subjects = {}

    # TODO Implement function

    # Write to file
    # write_json('stu-nyt-subjects.json', subjects)

    # BONUS Sort dict items

    # TODO Uncomment
    # subjects = {k: v for k, v in sorted(subjects.items())}
    # write_json('stu-nyt-subjects_sorted.json', subjects)

    # 3.2 CHALLENGE 03

    subject_articles = {}

    # TODO Implement function

    # Write to file
    # write_json('stu-nyt-subject_articles.json', subject_articles)

    # BONUS Sort dict items

    # TODO Uncomment
    # subject_articles = {k: v for k, v in sorted(subject_articles.items())}
    write_json('stu-nyt-subject_articles_sorted.json', subject_articles)


if __name__ == '__main__':
    main()
