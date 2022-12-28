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
    articles = read_json('./nyt-articles-20221031.json')

    print(f"\n2.3.1 All articles (n={len(articles)})")

    # Get 2022 articles only
    articles_2022 = []
    for article in articles:
        if article['pub_date'].startswith('2022'):
            articles_2022.append(article)

    print(f"\n2.3.2 2022 articles (n={len(articles_2022)})")

    # Alternative
    # WARN: '2022-02-06T10:00:12+0000' triggers runtime exception invalid isoformat str
    # HACK: slice string article['pub_date'][:-5] removes '+0000'
    # articles_2022 = []
    # for article in articles:
    #     pub_date = dt.fromisoformat(article['pub_date'][:-5])
    #     if pub_date.year == 2022:
    #         articles_2022.append(article)

    # Alternative: regex
    # WARN: '2022-02-06T10:00:12+0000' triggers runtime exception invalid isoformat str
    # HACK: employ regular expression that excludes '+0000'
    # articles_2022 = []
    # for article in articles:
    #     pub_date = re.search(r"[0-9,\-,T,\:]+(?=\+0000)", article['pub_date']).group()
    #     pub_date = dt.fromisoformat(pub_date)
    #     if pub_date.year == 2022:
    #         articles_2022.append(article)

    # Write to file
    write_json('stu-nyt-articles-2022.json', articles_2022)


    # 3.0 NESTED LOOPS

    nums = [
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40, 50],
        [100, 200, 300, 400, 500],
        [1000, 2000, 3000, 4000, 5000]
    ]

    print(f"\n3.0 Nested loop example")
    for i in nums:
        for j in i:
            print(sum(i) * j) # sum the list element then multiply by each element


    # Get all articles touching on Dementia
    dementia = []
    for article in articles:
        for keyword in article['keywords']:
            if keyword['name'] == 'subject' and keyword['value'] in ("Alzheimer's Disease", 'Dementia'):
                dementia.append(article)
                break # avoid appending duplicates due to either/or membership check

    print(f"\n3.0 Dementia articles (n={len(dementia)})")

    # Write to file
    write_json('stu-nyt-dementia-articles.json', dementia)


    # 3.1 CHALLENGE 02

    # Get all subjects, group by first character in string
    subjects = {}
    for article in articles:
        for keyword in article['keywords']:
            if keyword['name'] == 'subject' and keyword['value'] not in subjects:
                key = keyword['value'][0].upper() # new key, e.g. 'A'
                val = keyword['value']
                if key not in subjects.keys():
                    subjects[key] = [val] # new key, new list
                elif val not in subjects[key]:
                    subjects[key].append(val) # duplicates not added

    # Write to file
    write_json('stu-nyt-subjects.json', subjects)

    # BONUS Sort dict items
    subjects = {k: v for k, v in sorted(subjects.items())}

    write_json('stu-nyt-subjects_sorted.json', subjects)

    # 3.2 CHALLENGE 03

    subject_articles = {}
    for key, val in subjects.items():
        for subject in val:
            for article in articles:
                story = {
                            'headline_main': article['headline']['main'],
                            'web_url': article['web_url'],
                            'pub_date': article['pub_date']
                        }
                for keyword in article['keywords']:
                    if has_subject(keyword, 'subject', subject):
                        if subject not in subject_articles.keys():
                            subject_articles[subject] = [story] # new list
                        else:
                            subject_articles[subject].append(story)

    # Write to file
    write_json('stu-nyt-subject_articles.json', subject_articles)

    # BONUS Sort dict items
    subject_articles = {k: v for k, v in sorted(subject_articles.items())}

    # Write to file
    write_json('stu-nyt-subject_articles_sorted.json', subject_articles)


if __name__ == '__main__':
    main()
