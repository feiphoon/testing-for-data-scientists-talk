CATALOGUE_1 = {
    "Hyperbole and a Half": {
        "author": "Allie Brosh",
        "pages": 369
    },
    "Rainbow in the Cloud": {
        "author": "Maya Angelou",
        "pages": 105
    },
    "Bloody Brilliant Women": {
        "author": "Cathy Newman",
        "pages": 358
    },
}


def get_book_author(catalogue, book_name):
    """Returns the author of a given book name from a given catalogue.
    """
    return catalogue[book_name]["author"]


def get_book_pages(catalogue, book_name):
    """Returns the number of pages of a given book name from a given catalogue.
    """
    return catalogue[book_name]["pages"]
