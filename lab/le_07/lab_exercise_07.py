import csv
from fileinput import filename
import pprint
# WARN: Ensure that "import csv" is at the top of the file.

# LAB EXERCISE 07
print('\nLab Exercise 07')

# Problem 01
# TODO uncomment and repair the read_csv_to_dicts() function

def read_csv_to_dicts(filepath, encoding='utf-8', newline='', delimiter=','):
    """Accepts a file path, creates a file object, and returns a list of
    dictionaries that represent the row values using the cvs.DictReader().

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences
        delimiter (str): delimiter that separates the row values

    Returns:
        list: nested dictionaries representing the file contents
     """

    with open(filepath, 'r', newline=newline, encoding=encoding) as file_obj:
        data = []
        reader = csv.DictReader(file_obj, delimiter=delimiter)
        for line in reader:
            data.append(line)

        return data

def write_dicts_to_csv(filepath, data, fieldnames, encoding='utf-8', newline=''):
    """
    Writes dictionary data to a target CSV file as row data using the csv.DictWriter().
    The passed in fieldnames list is used by the DictWriter() to determine the order
    in which each dictionary's key-value pairs are written to the row.

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list): dictionary content to be written to the target file
        fieldnames (seq): sequence specifing order in which key-value pairs are written to each row
        encoding (str): name of encoding used to encode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences

    Returns:
        None
    """

    with open(filepath, 'w', encoding=encoding, newline=newline) as file_obj:
        writer = csv.DictWriter(file_obj, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)

def remove_DVD(movies):
    """
    Loops over a list of nested dictionaries, containing movie data
    Accesses the 'DVD' column and utilizes a built-in function in order to delete it

    Parameters:
        movies (list): nested dictionaries containing movie data

    Returns:
        list: nested dictionaries containing movie data
    """
    for movie in movies:
        del(movie['DVD'])
    return movies

# Problem 02
def clean_runtime(movie):
    """
    Accesses the data point Runtime (str) and casts the number value to an integer after separating
    the number value and the unit

    Parameters:
        movie (dict): dictionary containing key-value pairs representing data for one movie

    Returns:
        dict: dictionary containing "key: value" pairs representing data for one movie
    """
    movie['Runtime'] = int(movie['Runtime'].split()[0])
    return movie

def clean_boxoffice(movie):
    """
    Accesses the data point BoxOffice (str) and casts the value to an integer after separating
    the dollar sign ($) from the number value and removing commas
    Utilizes a try-except statement to handle 'N/A' values

    Parameters:
        movie (dict): dictionary containing key-value pairs representing data for one movie

    Returns:
        dict: dictionary containing "key: value" pairs representing data for one movie
    """
    try:
        movie['BoxOffice'] = int(movie['BoxOffice'].lstrip('$').replace(',', ''))
    except:
        movie['BoxOffice'] = 0
    return movie


def clean_imdb_data(movie):
    """
    Accesses the data point imdbVotes (str) and casts the value to an integer after removing commas
    Accesses the data point imdbRating (str) and casts the value to a float

    Parameters:
        movie (dict): dictionary containing key-value pairs representing data for one movie

    Returns:
        dict: dictionary containing "key: value" pairs representing data for one movie
    """
    movie['imdbVotes'] = int(movie['imdbVotes'].replace(',', ''))
    movie['imdbRating'] = float(movie['imdbRating'])
    return movie

# Problem 03
def get_most_popular_movies(movies):
    """
    Loops over a list of dictionaries, representing movies, checks whether the movie's 'BoxOffice'
    value is greater than 100000000 and whether the movie's 'imdbRating' is greater than 7

    If True, it appends a dictionary literal with the movie's 'Title' as the key and
    a tuple with the movie's 'BoxOffice' value and 'imdbRating' value.
        < Title >: (< BoxOffice >, < imdbRating >)

    Parameters:
        movies (list): nested dictionaries containing movie data

    Returns:
        list: nested dictionaries containing data on popular movies
    """
    popular_movies = []
    for movie in movies:
        if movie['BoxOffice'] > 100000000 and movie['imdbRating'] > 7:
            popular_movies.append({movie['Title']:(movie['BoxOffice'],movie['imdbRating'])})
    return popular_movies
# Problem 04
def count_sub_genres(movies):
    """
    Creates an empty dictionary `sub_genres` and assigns 4 new key-value pairs
    with their value set to 0 and the below sub-genres in this exact order:
        {'Sci-Fi': 0, 'Fantasy': 0, 'Thriller': 0, 'Mystery': 0}
    Loops over the list of movies and implements an if-elif statement to check if
    each genre is contained in the movie's 'Genre' value. If True, it increments the
    count by 1.

    Parameters:
        movies (list): nested dictionaries containing movie data

    Returns:
        dict: dictionary of key-value pairs with the key as a genre and value as a count
    """
    sub_geners = {}
    sub_geners['Sci-Fi'] = 0
    sub_geners['Fantasy'] = 0
    sub_geners['Thriller'] = 0
    sub_geners['Mystery'] = 0
    for movie in movies:
        if 'Sci-Fi' in movie['Genre']:
            sub_geners['Sci-Fi'] += 1
        elif 'Fantasy' in movie['Genre']:
            sub_geners['Fantasy'] += 1
        elif 'Thriller' in movie['Genre']:
            sub_geners['Thriller'] += 1
        elif 'Mystery' in movie['Genre']:
            sub_geners['Mystery'] += 1
    return sub_geners


# Problem 05
def create_new_movies_dicts(movies):
    """
    Loops over the list of movies and implements an if-else statement to check if
    the movie's 'Runtime' is greater than 2 hours (120 mins). If True, it appends
    a dictionary literal, which includes a selection of key-value pairs accessed from the
    original data, a new key-value pair 'Length': 'Long', and a nested dictionary assigned
    to a new key 'imdbInfo', to an empty list:
        'Length': 'Long'
        'imdbInfo': {'imdbRating': < imdbRating >, 'imdbVotes': < imdbVotes >, 'imdbID': < imdbID >}
    Otherwise, it appends a dictionary literal, which includes a selection of key-value pairs accessed
    from the original data, a new key-value pair 'Length': 'Short', and a nested dictionary assigned to
    a new key 'imdbInfo', to an empty list:
        'Length': 'Short'
        'imdbInfo': {'imdbRating': < imdbRating >, 'imdbVotes': < imdbVotes >, 'imdbID': < imdbID >}

    Parameters:
        movies (list): nested dictionaries containing movie data

    Returns:
        list: new set of nested dictionaries containing movie data
    """
    movies_new = []
    
    for movie in movies:
        if movie['Runtime'] > 120:
            movie['Length'] = 'Long'
            # movie['Length']:'Long'
            movie['imdbInfo'] = {}
            movie['imdbInfo']['imdbRating'] = movie['imdbRating']
            movie['imdbInfo']['imdbVotes'] = movie['imdbVotes']
            movie['imdbInfo']['imdbID'] = movie['imdbID']
        else:
            
            # movie['Length'] = 'Short'
            movie['imdbInfo'] = {}
            movie['imdbInfo']['imdbRating'] = movie['imdbRating']
            movie['imdbInfo']['imdbVotes'] = movie['imdbVotes']
            movie['imdbInfo']['imdbID'] = movie['imdbID']
        movies_new.append(movie)
    return movies_new


# Call functions below
def main():
    """
    This function serves as the point of entry and controls the flow of this Python script

    Parameters:
        None

    Returns:
        None
    """
    # Configure pretty printer, if helpful
    pp = None

    # Problem 01
    print("\nProblem 01:")

    horror_movies = read_csv_to_dicts('horror_movies.csv')
    # print(horror_movies)
    horror_movies = remove_DVD(horror_movies)
    # print(horror_movies)
    # Problem 02
    print("\nProblem 02:")

    #Set Up
    ##WARN: Be careful not to modify the 'test_movie' dictionary
    test_movie = {'Title': 'Train to Busan',
                'Year': '2016',
                'Rated': 'Not Rated',
                'Released': '20-Jul-16',
                'Runtime': '118 min',
                'Genre': 'Action, Horror, Thriller',
                'Director': 'Sang-ho Yeon',
                'Writer': 'Joo-Suk Park, Sang-ho Yeon',
                'Actors': 'Gong Yoo, Jung Yu-mi, Ma Dong-seok',
                'Plot': 'While a zombie virus breaks out in South Korea, passengers struggle to survive on the '
                        'train from Seoul to Busan.',
                'Language': 'Korean, Hawaiian, English',
                'Country': 'South Korea',
                'Awards': '35 wins & 39 nominations',
                'imdbRating': '7.6',
                'imdbVotes': '217,609',
                'imdbID': 'tt5700672',
                'Type': 'movie',
                'BoxOffice': '$2,129,768 '
            }
    #End Set Up

    #2.1.1
    runtime_test = clean_runtime(test_movie)
    # print(runtime_test)

    #2.1.2
    boxoffice_test = clean_boxoffice(test_movie)
    # print(boxoffice_test)

    #2.1.3
    imdb_test = clean_imdb_data(test_movie)
    # print(imdb_test)

    #2.2.0
    for movie in horror_movies:
        clean_runtime(movie)
        clean_boxoffice(movie)
        clean_imdb_data(movie)
    # print(horror_movies[1])
    # Problem 03
    print("\nProblem 03:")

    popular_horror_movies = get_most_popular_movies(horror_movies)
    # print(popular_horror_movies)

    # Problem 04
    print("\nProblem 04:")
    subgenre_counts = count_sub_genres(horror_movies)
    print(subgenre_counts)

    # Problem 05
    print("\nProblem 05:")
    horror_movies_new = create_new_movies_dicts(horror_movies)
    print(horror_movies_new[1])

    write_dicts_to_csv('./stu_horror_movies_new.csv', horror_movies_new, horror_movies[0].keys())

if __name__ == "__main__":
    main()
