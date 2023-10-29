import pandas as pd

class BookLover:
    name: str
    email: str
    fav_genre: str
    num_books: int
    book_list: pd.DataFrame

    def __init__(self, name, email, fav_genre, num_books = 0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})) -> None:
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list

    def add_book(self, book_name: str, rating: int):
        if not self.has_read(book_name):
            new_book = pd.DataFrame({
                'book_name': [book_name], 
                'book_rating': [rating]
                })

            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1 
        else:
            print("This book already exists in your book list")

    def has_read(self, book_name: str):
        if self.book_list.loc[self.book_list['book_name'] == book_name].empty:
            return False
        else:
            return True

    def num_books_read(self):
        return self.num_books

    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]
    
if __name__ == "__main__":
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("A", 5)
    test_object.add_book("A", 5)
    test_object.add_book("B", 5)
    test_object.add_book("C", 5)
    test_object.add_book("D", 5)
    test_object.add_book("E", 2)
    print(test_object.num_books_read())
    print(test_object.fav_books())
    print(test_object.book_list.loc[0][1])

    # And so forth