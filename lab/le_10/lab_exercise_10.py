import json
import pprint

def create_thinned_articles(articles, keyword_name):
    """Returns a list of "thinned" dictionary representations of an NYT article.
    Delegates to the function < get_keywords_by_name() >, the task of retrieving a
    list of subject keyword values when assigning the 'keywords' key-value pair.

    Each "thinned" article dictionary comprises the following keys:

    {
        'abstract': < value >,
        'snippet': < value >,
        'lead_paragraph': < value >,
        'headline_main: < value >,
        'keywords': < value >,
        'word_count': < value >,
        'pub_date': < value >
    }

    Extracts the associated values from each article dictionary element in the
    < nyt_articles > list and maps them to the appropriate keys in a dictionary
    literal.

    Two key-value pairs require special handling:

    'headline_main': assign the article "headline" string mapped to the "main" key.

    'keywords': assign a list of values obtained by calling the function
                < get_keywords_by_name() > and passing to it as arguments the
                current article dictionary and the passed in < keyword_name >.
                Call the function from inside the dictionary comprehension.

    Parameters:
        articles (list): a list of article dictionaries.
        keyword_name (str): the keyword name (e.g., "subject") employed as a filter.

    Returns:
        list: a list of thinned article dictionaries.
    """

    return [{
        'abstract': art['abstract'],
        'snippet': art['snippet'],
        'lead_paragraph': art['lead_paragraph'],
        'headline_main': art['headline']['main'],
        'keywords': get_keywords_by_name(art, keyword_name),
        'word_count': art['word_count'],
        'pub_date': art['pub_date']
    } for art in articles]

def create_thinned_article_tuples(articles):
    """Returns a list of tuples that represent a further "thinning" of NYT article attributes.
    Each tuple contains the following items:

    (
        < headline_main >,
        < pub_date YYYY-MM-DD only > ,
        < word_count >
    )

    WARN: The < pub_date > value is limited to Year-Month-Day (YYYY-MM-DD) portion of the original
    date and time string.

    Parameter:
        articles (list): a list of article dictionaries.

    Returns:
        list: a list of tuples.
    """

    # list_of_tuples = []
    # for art in articles:
    #     list_of_tuples.append((art['headline_main'], art['pub_date'].split('T')[0], art['word_count']))
    return [(art['headline_main'], art['pub_date'].split('T')[0], art['word_count']) for art in articles]

def filter_articles(articles, keyword, min_word_count=None):
    """Returns a list of article dictionaries filtered on the passed in < keyword >
    and < min_word_count > (if provided) arguments.

    If a < min_word_count > integer value is provided by the caller, include a compound
    conditional statement that returns articles that include the < keyword > in their
    list of keyword values AND possess a word count that is greater than or equal to
    < min_word_count >. Otherwise, return all articles that include the < keyword > in
    their list of keyword values irrespective of word count.

    Parameters:
        articles (list): a list of article dictionaries.
        keyword (str): subject keyword associated with certain articles.
        min_word_count (int): minimum number of words found in an article.

    Returns:
        list: a list of articles filtered on < keyword > and, optionally,
              < min_word_count >.
    """

    if min_word_count:
        # filter_articles = []
        # for art in articles:
        #     if keyword in art['keywords'] and art['word_count'] >= min_word_count:
        #         filter_articles.append(art)
        return [art for art in articles if keyword in art['keywords'] and art['word_count'] >= min_word_count]
    else:
        return [art for art in articles if keyword in art['keywords']]



def get_keywords_by_name(article, keyword_name):
    """Returns a list of < article > keyword values if, and only if, the associated
    keyword dictionary 'name' value matches the passed in < keyword_name >.

    Each article < keywords > dictionary element is structured as follows:

    {
        'name': < keyword name, e.g., "subject" >,
        'value': < keyword value, e.g., "Space" >,
        ...
    }

    Parameters:
        article (dict): a dictionary representation of a single article.
        keyword_name (str): the keyword name (e.g., "subject") employed as a filter.

    Returns:
        list: a list of keyword values.
    """
    # values = []
    # for keyword in article['keywords']:
    #     if keyword['name'] == keyword_name:
    #         values.append(keyword['value'])
    return [keyword['value'] for keyword in article['keywords'] if keyword['name'] == keyword_name] 


def get_word_count(article_tuple):
    """Returns the < article_tuple > word count item.

    Parameter:
        article_tuple (tuple): a tuple representation of an article.

    Returns:
        int: the article word count.
    """

    return article_tuple[2]


def read_json(filepath, encoding='utf-8'):
    """Reads a JSON document, decodes the file content, and returns a list or
    dictionary if provided with a valid filepath.

    Parameters:
        filepath (str): path to file.
        encoding (str): name of encoding used to decode the file.

    Returns:
        dict/list: dict or list representations of the decoded JSON document.
    """
    with open(filepath, 'r', encoding=encoding) as file_obj:
        return json.load(file_obj)


def sum_word_counts(article_tuples):
    """Returns the total word count for all articles in < article_tuples >.

    Parameter:
        article_tuples (list): a list of article tuples.

    Returns:
        int: total word count after adding up all article word counts.
    """

    # sum = 0
    # for art in article_tuples:
    #     sum += art[2]
    return sum([art[2] for art in article_tuples])


def write_json(filepath, data, encoding='utf-8', ensure_ascii=False, indent=2):
    """Serializes object as JSON. Writes content to the provided filepath.

    Parameters:
        filepath (str): the path to the file.
        data (dict)/(list): the data to be encoded as JSON and written to the file
        encoding (str): name of encoding used to encode the file.
        ensure_ascii (str): if False non-ASCII characters are printed as is;
        otherwise non-ASCII characters are escaped.
        indent (int): number of "pretty printed" indention spaces applied to
        encoded JSON.

    Returns:
        None
    """
    with open(filepath, 'w', encoding=encoding) as file_obj:
        json.dump(data, file_obj, ensure_ascii=ensure_ascii, indent=indent)


def main():
    """Serves as the point of entry and controls the flow of this
    Python script.

    Parameters:
        None
    Returns:
        None
    """

    # configure pretty printer
    pp = pprint.PrettyPrinter()

    FILEPATH = "./nyt_articles_space.json"

    TEST_KEYWORDS = {
        'keywords': [
            {
                "name": "subject",
                "value": "Space",
                "rank": 1,
                "major": "N"
            },
            {
                "name": "subject",
                "value": "telescope",
                "rank": 2,
                "major": "N"
            },
            {
                "name": "test",
                "value": "test_value",
                "rank": 3,
                "major": "N"
            }
        ]
    }

    # Problem 1
    print("\nProblem 1")

    # read in the specified file
    nyt_api_articles = read_json(FILEPATH)

    test_keywords = get_keywords_by_name(TEST_KEYWORDS, 'subject')
    # pp.pprint(test_keywords)

    # Problem 2
    print("\nProblem 2")

    articles = create_thinned_articles(nyt_api_articles, 'subject')
    # pp.pprint(articles)

    # Problem 3
    print("\nProblem 3")

    articles_min1000 = filter_articles(articles, 'Space', 1000)
    # pp.pprint(articles_min1000)

    articles_asteroids = filter_articles(articles, 'Asteroids')
    # pp.pprint(articles_asteroids)

    articles_space_station = filter_articles(articles, 'International Space Station', 1000)
    # pp.pprint(articles_space_station)

    # Problem 4
    print("\nProblem 4")

    article_tuples = create_thinned_article_tuples(articles_min1000)
    # pp.pprint(article_tuples)

    # Problem 5
    print("\nProblem 5")

    total_words_asteroids = sum_word_counts(create_thinned_article_tuples(articles_asteroids))
    # print("Asteroid word count: ", total_words_asteroids)

    total_words_space_station = sum_word_counts(create_thinned_article_tuples(articles_space_station))
    # print("Space station word count: ", total_words_space_station)

    # Problem 6
    print("\nProblem 6")

    test_word_count = get_word_count(article_tuples[0])
    # print(f"Word count is {test_word_count}")

    sorted_articles = sorted(article_tuples, key=get_word_count, reverse=True)
    # pp.pprint(sorted_articles)

    write_json('stu_sorted_articles.json', sorted_articles)


if __name__ == "__main__":
    main()
