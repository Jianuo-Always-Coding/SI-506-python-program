# LAB EXERCISE 08
import json
print('Lab Exercise 08 \n')


# PROBLEM 1.1

def read_json(filepath, encoding='utf-8'):
    """Reads a JSON document, decodes the file content, and returns a list or
    dictionary if provided with a valid filepath.

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file

    Returns:
        dict/list: dict or list representations of the decoded JSON document
    """
    # TODO
    # Uncomment the below lines and correct the mistakes

    with open(filepath, 'r', encoding=encoding) as file_obj:
        return json.load(file_obj)

# Problem 2.1

def illustration_books(data):
    """Returns a dictionary of category name as key and list of books having
    illustration contributors as value. For a dictionary representing one single
    book, the value of the key 'contributor_note' corresponds to the name of the
    illustrations contributor. This value being an empty string signifies that
    the book has no illustrations contributor. Dictionary to be returned
    contains only those categories which have one or more books with illustrations.

    Parameters:
        data(list): a list of dictionaries each of which contains a list of books.

    Returns:
        dict: a dictionary which has category name as the key and list of book
        titles which have illustration contributions by people other than the
        author as the value.
    """
    books_list = {}
    for dict_ in data:
        category = dict_['list_name']
        books = dict_['books']
        titles = []
        for book_dict in books:
            if book_dict['contributor_note']:
                titles.append(book_dict['title'])
            if len(titles):
                books_list[category] = titles
    return books_list


# Problem 3.1

def get_publishers(data):
    """Returns a dictionary containing name of the publisher as the key and the
    count of books published by the respective publisher as the value.

   Parameters:
        data(list): a list of dictionaries each of which contains a list of books.

    Returns:
        dict: dictionary with key as the name of the publisher and value as the
        number of books published by that publisher.
    """
    publishers = {}
    for book in data:
        best_books = book['books']
        for best in best_books:
            publishers[best['publisher']] = publishers.get(best['publisher'], 0) + 1
    return publishers

        


# Problem 4.1

def bestselling_books(data, publishers_list):
    """Returns a list of book titles that have appeared on the NYT's
    'Bestselling Books For The Week' more than 200 times and are present in the publishers_list.


    Parameters:
        data(list): a list of dictionaries each of which contains a list of books.
        publishers_list(list): list of publisher names.

    Returns:
        list: list of book titles
    """
    titles = []
    for book in data:
        best_books = book['books']
        for best in best_books:
            if best['weeks_on_list'] > 200 and best['publisher'] in publishers_list:
                titles.append(best['title'])
    return titles

# Problem 5.1
def write_json(filepath, data, encoding='utf-8', ensure_ascii=False, indent=2):
    """Serializes object as JSON. Writes content to the provided filepath.

    Parameters:
        filepath (str): the path to the file
        data (dict)/(list): the data to be encoded as JSON and written to the file
        encoding (str): name of encoding used to encode the file
        ensure_ascii (str): if False non-ASCII characters are printed as is;
                            otherwise non-ASCII characters are escaped.
        indent (int): number of "pretty printed" indention spaces applied to encoded JSON

    Returns:
        None
    """
    # TODO
    # Uncomment the below lines and correct the mistakes

    with open(filepath, 'w', encoding=encoding) as file_obj:
        json.dump(data, file_obj, ensure_ascii=ensure_ascii, indent=indent)


# Call functions below
def main():
    """
    This function serves as the point of entry and controls the flow of this
    Python script

    Parameters:
        None

    Returns:
        None
    """

    print("Problem 01:\n")

    # Problem 1.2
    books_data = read_json('./nyt-books.json')


    # Uncomment to check
    # print(books_data[0])
    # print(f'Length of books_data list from json file is: {len(books_data)}\n')

    # Problem 1.3
    list_names = []
    for dict_ in books_data:
        list_names.append(dict_['list_name'])


    # Uncomment to check
    # print(f'Categories present in the data are:\n {list_names}\n')

    print("Problem 02:\n")

    # Problem 2.2
    books_with_illustrations = illustration_books(books_data)

    # Uncomment to check
    # print(f'Books with Illustrations:\n {books_with_illustrations}\n')

    print("Problem 03:\n")

    # Problem 3.2
    publishers_data = get_publishers(books_data)

    # Uncomment to check
    # print(f'publishers_data:\n {publishers_data}\n')

    # Problem 3.3
    frequent_publishers = []

    # Implement loop
    for key, value in publishers_data.items():
        if value > 3:
            frequent_publishers.append(key)

    # Uncomment to check
    # print(f'\nFrequent Publishers:\n {frequent_publishers}\n')

    print("Problem 04:\n")

    # Problem 4.2 (1 points)
    max_times_best_selling = bestselling_books(books_data, frequent_publishers)

    # Uncomment to check
    # print(f'\nBest Selling books for more than 200 times on a list:\n {max_times_best_selling}\n')

    print("Problem 05:\n")


    # Problem 5.2
    books_dictionary = {}
    books_dictionary['books_with_illustrations'] = books_with_illustrations
    books_dictionary['frequent_publishers'] = frequent_publishers
    books_dictionary['max_times_best_selling'] = max_times_best_selling
    write_json('stu_books_data.json', books_dictionary)


if __name__ == "__main__":
    main()
