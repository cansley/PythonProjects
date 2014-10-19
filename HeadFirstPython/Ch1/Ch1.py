__author__ = 'cxa70'

movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]

#exercise 1
# this is really beyond what the book called for.
# the book was just looking for movies.insert(1, 1975), etc.
def upsert_year(movie_title, year, movie_collection):
    return_coll = movie_collection[:]
    if movie_title in return_coll:
        title_idx = return_coll.index(movie_title)
    else:
        return_coll.append(movie_title)
        title_idx = return_coll.index(movie_title)

    if title_idx+1 < len(return_coll):
        test_val = return_coll[title_idx+1]
    else:
        test_val = None

    if isinstance(test_val, int):
        if title_idx+1 >= len(return_coll):
            return_coll.append(year)
        else:
            return_coll[title_idx+1] = year
    else:
        return_coll.insert(title_idx+1, year)
    return return_coll


#exercise 2
def create_list():
    return ["The Holy Grail", 1975, "The Life of Brian", 1979, "The Meaning of Life", 1983]


def create_complex_list():
    return ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman", ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]


def print_list(indent_string, val_list):
    currentList = list(val_list)
    for val in currentList:
        if isinstance(val, list):
            print_list(indent_string*2, val)
        else:
            print(indent_string, val)


def main():
    newMovies = upsert_year("The Holy Grail", 1975, movies)
    newMovies = upsert_year("The Life of Brian", 1979, newMovies)
    newMovies = upsert_year("The Meaning of Life", 1983, newMovies)
    print(newMovies)

    newMovies = create_list()
    count = 0
    while count < len(newMovies):
        print(newMovies[count])
        count += 2

    newMovies = create_complex_list()
    for movie in newMovies:
        if isinstance(movie, str):
            print(movie)
        elif isinstance(movie, list):
            print_list("-->", movie)