# SI 506 Lecture 23

import json
import pprint

from datetime import datetime
from pathlib import Path


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

    # Configure pretty printer
    pp = pprint.PrettyPrinter(indent=2, sort_dicts=False, width=100)

    # 1.0 GET DATA
    nyt_articles = read_json('./nyt-articles-climate.json')

    print(f"\n1.0 articles count = {len(nyt_articles)}")


    # 1.2 SIMPLE EXAMPLE

    article_word_counts = {}
    for article in nyt_articles:
        article_word_counts[article['web_url']] = article['word_count']

    # TODO Uncomment
    # write_json('./stu-nyt-article_word_counts-v1p0.json', article_word_counts)

    # dict comprehension
    article_word_counts = None # TODO comp

    # TODO Uncomment
    # write_json('./stu-nyt-article_word_counts-v1p1.json', article_word_counts)


    # 2.0 TRANSFORMING VALUES

    # For pathlib attributes see https://docs.python.org/3/library/pathlib.html

    article_pub_dates = {}
    for article in nyt_articles:
        path = article['web_url'].split('/')[-1][:-5] # drops extension/suffix
        # path = Path(article['web_url']).stem # better
        pub_date = article['pub_date'].split('T')[0]
        article_pub_dates[path] = pub_date

    # TODO Uncomment
    # write_json('./stu-nyt-article_pub_dates-v1p0.json', article_pub_dates)

    article_pub_dates = None # TODO comp

    # TODO Uncomment
    # write_json('./stu-nyt-article_pub_dates-v1p1.json', article_pub_dates)


    # 3.0 CONDITIONAL STATEMENTS
    multimedia = {}
    for article in nyt_articles:
        if article['document_type'].lower() == 'multimedia':
            multimedia[article['web_url']] = article

    # print(f"\n3.0.1 Multimedia for loop (n={len(multimedia)})")

    # TODO Uncomment
    # write_json('./stu-nyt-articles-multimedia-v1p0.json', multimedia)

    # Dictionary comprehension
    multimedia = None # TODO comp

    # print(f"\n3.0.2 Multimedia dict comp (n={len(multimedia)})")

    # TODO Uncomment
    # write_json('./stu-nyt-articles-multimedia-v1p1.json', multimedia)


    # 3.1 CHALLENGE 01

    # Article (slim version)
    articles_short = []
    for article in nyt_articles:
        articles_short.append(
            {
                'web_url': article['web_url'],
                'pub_date': article['pub_date'],
                'document_type':  article['document_type'],
                'type_of_material': article['type_of_material'],
                'word_count': article['word_count']
                }
            )

    # TODO Uncomment
    # write_json('./stu-nyt-articles_short-v1p0.json', articles_short)

    # Alternative (for loop / dict comprehension)
    keep_keys = ('web_url', 'pub_date', 'document_type', 'type_of_material', 'word_count')
    articles_short = []

    # TODO Implement

    # TODO Uncomment
    # write_json('./stu-nyt-articles_short-v1p1.json', articles_short)

    # Alternative (list and dict composition combined)
    articles_short = None # TODO comp

    # TODO Uncomment
    # write_json('./stu-nyt-articles_short-v1p2.json', articles_short)


    # 3.2 IF-ELSE

    # Read time estimated at 238 words/min.
    # https://thereadtime.com/#:~:text=How%20Long%20Does%20It%20Take,seconds%20to%20read%201000%20words.

    # TODO Uncomment
    # articles_read_time = {}
    # for article in articles_short:
    #     if article['document_type'].lower() == 'article':
    #         path = article['web_url'].split('/')[-1][:-5]
    #         if (article['word_count']) >= 750:
    #             articles_read_time[path] = {'word_count': article['word_count'], 'read time': 'LONG'}
    #         else:
    #             articles_read_time[path] = {'word_count': article['word_count'], 'read time': 'SHORT'}

    # print(f"\n3.2.1 articles_read_time (n={len(articles_read_time)})")

    # TODO Uncomment
    # write_json('./stu-nyt-articles_read_time-v1p0.json', articles_read_time)

    # TODO Uncomment
    # articles_read_time = {
    #     article['web_url'].split('/')[-1][:-5]: (
    #         {'word_count': article['word_count'], 'read time': 'LONG'}
    #         if (article['word_count']) >= 750
    #         else {'word_count': article['word_count'], 'read time': 'SHORT'}
    #         )
    #     for article in articles_short if article['document_type'].lower() == 'article'
    #     }

    # print(f"\n3.2.1 articles_read_time (comp) (n={len(articles_read_time)})")

    # TODO Uncomment
    # write_json('./stu-nyt-articles_read_time-v1p1.json', articles_read_time)

    # 3.3 IF-ELIF-ELSE

    # TODO Uncomment
    # articles_read_time = {
    #     article['web_url'].split('/')[-1][:-5]: (
    #         {'word_count': article['word_count'], 'read time': 'LONG'}
    #         if article['word_count'] >= 1000
    #         else {'word_count': article['word_count'], 'read time': 'MEDIUM'}
    #         if 500 <= (article['word_count']) < 1000
    #         else {'word_count': article['word_count'], 'read time': 'SHORT'}
    #         )
    #     for article in articles_short if article['document_type'].lower() == 'article'
    #     }

    # TODO Uncomment
    # write_json('./stu-nyt-articles_read_time-v1p2.json', articles_read_time)


    # 4.0 NESTED LOOPS

    # Get authors
    authors = {}
    for article in nyt_articles:
        val = []
        for person in article['byline']['person']:
            val.append(
                {
                    'firstname': person['firstname'],
                    'middlename': person['middlename'],
                    'lastname': person['lastname']
                    }
                )
        authors[article['web_url']] = val

    # TODO Uncomment
    # write_json('./stu-nyt-article_authors-v1p0.json', authors)

     # dictionary comprehension (with nested list comprehension)
    authors = None # TODO comp

    # TODO Uncomment
    # write_json('./stu-nyt-article_authors-v1p1.json', authors)


    # 5.0 ANOTHER EXAMPLE
    months = {i: [] for i in reversed(range(1, 12))}

    # print(f"\n5.0.1 months dict = {months}")

    # TODO Uncomment
    # for article in articles_short:
    #     month = datetime.strptime(article['pub_date'], '%Y-%m-%dT%H:%M:%S%z').month
    #     if month in months.keys():
    #         months[month].append(article)
    #     else:
    #         months[month] = [article]

    # TODO Uncomment
    # write_json('./stu-nyt-article_monthly.json', months)

    # Filter out non-articles (e.g., multimedia)
    monthly_word_count_totals = {i: 0 for i in reversed(range(1, 12))}
    for month, articles in months.items():
        for article in articles:
            if article['document_type'].lower() == 'article':
                monthly_word_count_totals[month] += (article['word_count'])

    # TODO Uncomment
    # print('\n5.0.1 monthly articles word count (totals)')
    # pp.pprint(monthly_word_count_totals)

    # Return lists of word counts
    monthly_word_counts = {i: [] for i in reversed(range(1, 12))}
    for month, articles in months.items():
        for article in articles:
            if article['document_type'].lower() == 'article':
                monthly_word_counts[month].append(article['word_count'])

    # TODO Uncomment
    # print('\n5.0.2 monthly article word counts lists')
    # pp.pprint(monthly_word_counts)

    # Total word counts per month
    monthy_word_counts_sum = {month: sum(counts) for month, counts in monthly_word_counts.items()}

    # TODO Uncomment
    # print('\n5.0.3 monthly articles word count (totals)')
    # pp.pprint(monthy_word_counts_sum)

    # Average word counts per month (floor division)
    # TODO Uncomment
    # monthy_word_counts_avg = {
    #     month: (sum(counts) // len(counts))
    #     for month, counts in monthly_word_counts.items()
    #     }

    # TODO Uncomment
    # print('\n5.0.4 monthly articles word count (average)')
    # pp.pprint(monthy_word_counts_avg)


if __name__ == '__main__':
    main()
