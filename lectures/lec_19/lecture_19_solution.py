# SI 506 Lecture 19

import csv
import json


def get_author_name(author):
    """Accesses the author's last name, first name, and middle name values and
    returns a three-item tuple to the caller.

    Tuple item order is listed below:

    ( < lastname >, < firstname >, < middlename >)

    Parameters:
        author (dict): representation of a byline author

    Returns:
        tuple: three-item tuple comprising the authors last name, first name, and
               middle name
    """

    return author.get('lastname'), author.get('firstname'), author.get('middlename')


def get_subject_keywords(article):
    """Returns a list of "subject" string values retrieved from the passed in
    < article >'s "keywords" list. Each < article > includes a "keywords" key-value
    pair comprising a list of dictionaries. This function filters on keywords with
    a "name" value equal to "subject" and also ensures that no duplicate keyword
    values are appended to the list to be returned to the caller.

    'keywords': [
           {
               'name': 'subject',
               'value': '< word | phrase >',
               ...,
           },
           ...
        ]

    Parameters:
        article (dict): representation of an article

    Returns:
        list: "subject" values associated with the < article >
    """

    subjects = []
    for keyword in article['keywords']:
        if keyword['name'] == 'subject' and keyword['value'] not in subjects:
            subjects.append(keyword['value'])
    return subjects


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


def write_dicts_to_csv(filepath, data, fieldnames, encoding='utf-8', newline=''):
    """
    Writes dictionary data to a target CSV file as row data using the csv.DictWriter().
    The passed in fieldnames list is used by the DictWriter() to determine the order
    in which each dictionary's key-value pairs are written to the row.

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list): dictionary content to be written to the target file
        fieldnames (seq): sequence specifing order in which key-value pairs are written to
                          each row
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

    # 1.1 CHALLENGE 01

    # Get articles
    articles = read_json('./nyt-articles-research-20221102.json')

    print(f"\nCh 01 Articles (n={len(articles)})")

    keyword_counts = {}
    for article in articles:
        keywords = get_subject_keywords(article)
        for keyword in keywords:
            if keyword not in keyword_counts.keys():
                keyword_counts[keyword] = 1 # seed
            else:
                keyword_counts[keyword] += 1 # increment

    # Sort by value (reversed = -x[1]), then by key (x[0])
    keyword_counts = {k: v for k, v in sorted(keyword_counts.items(), key=lambda x: (-x[1], x[0]))}

    # Write to file
    write_json('stu-nyt-keyword_counts.json', keyword_counts)


    # 1.2 CHALLENGE 02

    # NOTE: Given break move dict literal inside if block (more efficient)
    subject_keywords = ('Dinosaurs', 'Fossils', 'Paleontology', 'Pterosaurs')
    paleontology = []
    for article in articles:
        keywords = get_subject_keywords(article)
        for keyword in keywords:
            if keyword in subject_keywords:
                paleontology.append({
                    'headline_main': article['headline']['main'],
                    'byline': article['byline']['original'],
                    'web_url': article['web_url'],
                    'pub_date': article['pub_date'],
                    })
                break # prevents dups

    print(f"\n1.2 paleontology articles count = {len(paleontology)}")

    # Write to file
    write_dicts_to_csv('stu-nyt-paleontology.csv', paleontology, paleontology[0].keys())


    # 1.3 CHALLENGE 03

    authors = []
    for article in articles:
        for person in article['byline']['person']:
            name = get_author_name(person)
            if name not in authors:
                authors.append(name)

    print(f"\nauthors (n={len(authors)})")

    # Sort Authors
    # TypeError: '<' not supported between instances of 'NoneType' and 'str' if x[2]
    # WARN: convert None to empty string to avoid runtime exception (middlename value)
    # INFO: str(x or '') returns '' if x is falsy (e.g., None)
    authors = [author for author in sorted(authors, key=lambda x: (x[0], x[1], str(x[2] or '')))]

    print(f"\nAuthors = {authors[1]}")

    write_csv('stu-nyt-authors.csv', authors, ('last_name', 'first_name', 'middle_name'))


    # 1.4 CHALLENGE 04

    citations = {}
    for article in articles:
        for person in article['byline']['person']:
            name = get_author_name(person)
            if name[2]:
                key = f"{name[0]}, {name[1]} {name[2]}"
            else:
                key = f"{name[0]}, {name[1]}"

            story = {
                'pub_date': article['pub_date'],
                'headline_main': article['headline']['main'],
                'web_url': article['web_url']
                }

            if key not in citations.keys():
                citations[key] = [story] # new list literal
            else:
                citations[key].append(story)

    # Sort Authors
    citations = {k: v for k, v in sorted(citations.items(), key=lambda x: x[0])}

    # Write to file
    write_json('stu-nyt-citations.json', citations)


    # 1.5 CHALLENGE 05

    print(f"\n1.5.1 citations count = {len(citations)}")

    # Duplicate: Rabin, Roni = Rabin, Roni Caryn
    # Insert 2022-08-030 Paxlovid story (2nd element)
    citations['Rabin, Roni Caryn'].insert(1, citations['Rabin, Roni'][0])
    del(citations['Rabin, Roni']) # remove

    print(f"\n1.5.2 citations count = {len(citations)}")
    print(f"\n1.5.3 Roni Caryn Rabin Paxlovid article = {citations['Rabin, Roni Caryn'][1]}")

    # Write to file
    write_json('stu-nyt-citations-corrected.json', citations)


if __name__ == '__main__':
    main()
