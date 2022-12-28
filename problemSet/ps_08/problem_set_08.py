# PROBLEM SET 08

# Do not modify or remove this import statement
import json

# PROBLEM 1

def read_json(filepath, encoding='utf-8'):
    """Reads a JSON file and converts it to a Python dictionary.

    Parameters:
        filepath (str): a path to the JSON file
        encoding (str): name of encoding used to decode the file

    Returns:
        dict/list: dict or list representations of the decoded JSON document
    """
    with open(filepath, 'r', encoding=encoding) as file_obj:
        return json.load(file_obj)

# PROBLEM 2

def convert_to_float(value):
    """Implements error handling to check if the passed-in value is a NON-INTEGER
    that can be converted to a float.
    If possible, the non-integer value is converted and assigned back to its
    variable.

    Parameters:
        value (any): a value that may be able to be converted to a float. In this
                        case, these are the values from a single book dictionary.
    Returns:
        value (float|any): value will be float, if possible. Otherwise it will returned unchanged.
    """
    if type(value) == int:
        return value
    try:
        return float(value)
    except:
        return value

def clean_book(book, desired_keys=None):
    """Accepts a dictionary representation of a book. Creates an empty dictionary.
    Loops through the keys and values of < book >.

    If < desired_keys > is not None, check if each key is in < desired_keys >.
    If it is, add that key and its value to the new dictionary. At the same time,
    call < convert_to_float > to make that value a float, if possible.

    If < desired_keys > is None, add each key and its value to the new dictionary
    while calling < convert_to_float > to make that value a float, if possible.

    Parameters:
        book (dict): dictionary representation of a book on the NYT bestsellers list
        desired_keys (list): represents which keys should still be in the cleaned book dictionary

    Returns:
        dict: a new, cleaned dictionary representation of the book with only the desired
                keys and "price" now a float
    """
    result = {}
    # print('book = ', book)

    
    for key, value in book.items():
        if desired_keys:
            for desired_key in desired_keys:
                if desired_key == key:
                    result[key] = convert_to_float(value)
        else:
            result[key] = convert_to_float(value)
    return result

# PROBLEM 3

def write_json(filepath, data, encoding='utf-8', indent=2):
    """Serializes object as JSON. Writes content to the provided filepath.

    Parameters:
        filepath (str): the path to the file

        data (dict)/(list): the data to be encoded as JSON and written to
        the file

        encoding (str): name of encoding used to encode the file

        indent (int): number of "pretty printed" indention spaces applied to
        encoded JSON

    Returns:
        None
    """

    with open(filepath, 'w', encoding=encoding) as file_obj:
        json.dump(data, file_obj, indent=indent)


# PROBLEM 4

def get_average_price_by_rank(bestseller_lists, rank):
    """Given a list of bestseller lists and a rank, finds the average price of
    the books of that rank over the 8 weeks of lists. Includes duplicates of
    the same book if that book ranked in the same position multiple times over
    the eight weeks.

    Parameters:
        bestseller_lists (list): list of dictionaries, each dictionary represents
                                a weekly bestseller list and contains the key "books"
                                with a value that is a list of book dictionaries.
        rank (int): an integer 1-10 representing the rank of the books of interest
                    such as No. 1 bestsellers (1) or No. 5 bestsellers (5).

    Returns:
        float: the average price (rounded to nearest cent) for all books (including
                repeats) of the given rank over the eight weeks of lists
    """

    total_price = 0
    for week in bestseller_lists:
        for book in week['books']:
            if book['rank'] == rank:
                total_price += book.get('price')
    return round(total_price / 8, 2)


# PROBLEM 5

def get_books_by_publisher(bestseller_lists, publisher):
    """Given a publisher and eight weeks of bestseller lists, finds all of the
    books published by the publisher on those eight lists and returns the books
    as a list of dictionaries. Includes repeats if a book remained on the list for
    multiple weeks.

    Parameters:
        bestseller_lists (list): list of dictionaries, each dictionary represents
                                a weekly bestseller list and contains the key "books"
                                with a value that is a list of book dictionaries.
        publisher (str): the name of a book publisher that has a book on at least one
                        of the eight weekly bestseller lists.

    Returns:
        list : list of dictionaries, each representing a book published by the given
                publisher, includes repeats if a book remained on the list for
                multiple weeks
    """
    result = []
    for element in bestseller_lists:
        for book in element['books']:
            if book['publisher'].lower() == publisher.lower():
                result.append(book)
    return result


# PROBLEM 6

def score_book(book):
    """Checks the rank of a book. If the book is rank 1-5, assigns a score
    of 15. If the book rank is 6-10, assigns a score of 10. Rank 11-15, score of 5.

    Parameter:
        book (dict): dictionary representation of a book on the NYT bestsellers list

    Returns:
        int: a score of 15, 10, or 5, depending on the rank of the book.
    """

    if book['rank'] > 0 and book['rank'] <= 5:
        return 15
    elif book['rank'] >= 6 and book['rank'] <= 10:
        return 10
    else:
        return 5


# PROBLEM 7

def score_publisher(bestseller_lists, publisher):
    """Scores a publisher based on the rank of its books on the 8 weekly
    bestseller lists. Calls < get_books_by_publisher > to find the publisher's
    books, uses < score_book > to find the score for each book and adds that
    to the publisher score. This includes repeat books so that a publisher
    gets credit for a book remaining on the bestseller list for multiple
    weeks.

    Parameters:
        bestseller_lists (list): list of dictionaries, each dictionary represents
                                a weekly bestseller list and contains the key "books"
                                with a value that is a list of book dictionaries.
        publisher (str): the name of a book publisher that has a book on at least one
                        of the eight weekly bestseller lists.

    Returns:
        int: the total scores of all the publisher's books (including repeats) over
        the 8 weeks of bestseller lists
    """
    score = 0
    book_list = get_books_by_publisher(bestseller_lists, publisher)
    for book in book_list:
        score += score_book(book)
    return score

# PROBLEM 8

def find_publishers(bestseller_lists):
    """Creates a list of the unique publisher names (no repeats) that appear
    throughout the weekly bestseller lists.

    Parameters:
        bestseller_lists (list): list of dictionaries, each dictionary represents
                                a weekly bestseller list and contains the key "books"
                                with a value that is a list of book dictionaries.

    Returns:
        list: list of strings; the names of all the publishers that have at least
            one book on a bestseller list for these 8 weeks.
    """

    result = []
    for dictionary in bestseller_lists:
        for book in dictionary['books']:
            if book['publisher'] not in result:
                result.append(book['publisher'])
    return result

# PROBLEM 9

def create_scoreboard(bestseller_lists):
    """Creates a new, empty dictionary. Given eight weeks of bestseller lists,
    this function calls < find_publishers > to find all unique publisher names
    from the lists. Then, using < score_publisher > assigns a "publisher name",
    "score" key-value pair to the new dictionary for each publisher. Returns the
    dictionary with publisher names and scores.

    Parameters:
        bestseller_lists (list): list of dictionaries, each dictionary represents
                                a weekly bestseller list and contains the key "books"
                                with a value that is a list of book dictionaries.

    Returns:
        dict: a "scoreboard" of each publisher that appears on the bestseller
                lists and their total scores based on the rankings of their
                books. The keys are strings of publisher's names and the
                values are integer scores.
    """

    scoreboard = {}
    all_publishers = find_publishers(bestseller_lists)
    for publisher in all_publishers:
        scoreboard[publisher] = score_publisher(bestseller_lists, publisher)
    return scoreboard



def main():
    """Program entry point.

    Parameters:
        None

    Returns:
        None
    """

    # PROBLEM 1

    young_adult_bestsellers = read_json('young_adult_bestsellers.json') 

    young_adult_bestsellers_week_1 = young_adult_bestsellers[0] 

    # print(f'\nPROBLEM 1.3 Young Adult Bestsellers Week 1: {young_adult_bestsellers_week_1}')

    # PROBLEM 2

    integer_to_test = 5
    string_to_test = "NYT Books of the Year"
    float_to_test = "24.57"

    integer_return = convert_to_float(integer_to_test) 
    string_return = convert_to_float(string_to_test) 
    float_return = convert_to_float(float_to_test) 

    # print(f'\nPROBLEM 2.3 Integer must remain an integer: {integer_return}')
    # print(f'\nPROBLEM 2.3 String must remain a string: {string_return}')
    # print(f'\nPROBLEM 2.3 Float-like string must be returned as a float: {float_return}')

    keep_keys = [
        'rank',
        'rank_last_week',
        'isbns',
        'publisher',
        'description',
        'price',
        'title',
        'author'
        ]
    for element in young_adult_bestsellers:
        for i in range(len(element['books'])):
            # print('book = ', book)
            element['books'][i] = clean_book(element['books'][i], desired_keys=keep_keys)

    # TODO Use nested loops to clean all books in < young_adult_bestsellers >

    # print(f'\nPROBLEM 2.6 Cleaned Young Adult Bestsellers Week 1: {young_adult_bestsellers_week_1}')

    # PROBLEM 3

    filepath = 'clean_young_adult_bestsellers.json'

    # TODO Call < write_json >
    write_json(filepath, young_adult_bestsellers)
    # PROBLEM 4

    rank_1_avg = get_average_price_by_rank(young_adult_bestsellers, 1) # TODO Call function
    rank_10_avg = get_average_price_by_rank(rank=10, bestseller_lists=young_adult_bestsellers) # TODO Call function with reverse keyword arguments

    # print(f'\nPROBLEM 4.3 Average Price of No. 1 Young Adult Books: ${rank_1_avg}')
    # print(f'\nPROBLEM 4.4 Average Price of No. 10 Young Adult Books: ${rank_10_avg}')

    # PROBLEM 5

    fiction_bestsellers = read_json('fiction_bestsellers.json')

    fiction_bestsellers_week_8 = fiction_bestsellers[-1] # TODO Slice

    # print(f'\nPROBLEM 5.4 Fiction Bestsellers Week 8: {fiction_bestsellers_week_8}')

    # print("\nPROBLEM 5.5-6 Doubleday Books' Rankings")

    doubleday_books = get_books_by_publisher(fiction_bestsellers, "Doubleday") # TODO Call function
    # print(doubleday_books)
   

    for book in doubleday_books:
        # print(book)
        print(f'\nTitle: {book["title"]}')
        print(f'Rank: {book.get("rank")}')

    # PROBLEM 6
    # print(doubleday_books)
    first_book_score = score_book(doubleday_books[0]) # TODO Call function
    penultimate_book_score = score_book(doubleday_books[-2]) # TODO Call function
    # REMINDER: "penultimate" means second to last

    # TODO Uncomment and replace "?first book title?" and "?penultiamte book title?"
    #       with the correct expressions

    print(f'\nPROBLEM 6.3 First Doubleday Book: {doubleday_books[0]["title"]}; Score: {first_book_score}')
    print(f'\nPROBLEM 6.4 Penultimate Doubleday Book: {doubleday_books[-2]["title"]}; Score: {penultimate_book_score}')

    # PROBLEM 7
    
    doubleday_score = score_publisher(publisher="Doubleday", bestseller_lists=fiction_bestsellers) # TODO Call function with reverse keyword arguments

    # print(f'\nPROBLEM 7.3 Doubleday Publisher Score: {doubleday_score}')

    # PROBLEM 8

    fiction_publishers = find_publishers(fiction_bestsellers) # TODO Call function

    # print(f'\nPROBLEM 8.3 Fiction Publishers: {fiction_publishers}')

    # PROBLEM 9

    fiction_publishers_scoreboard = create_scoreboard(fiction_bestsellers) # TODO Call function

    # print(f'\nPROBLEM 9.3 Scoreboard of Fiction Publishers: {fiction_publishers_scoreboard}')

    filepath = 'fiction_publishers_scoreboard.json'
    write_json(filepath, fiction_publishers_scoreboard)
    # TODO Call < write_json >

# Do not modify or remove this if statement
if __name__ == "__main__":
    main()
