import unittest
from booklovers import BookLover

class BookLoverTestSuite(unittest.TestCase):



    def test_1_add_book(self):
        bl = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        bl.add_book("Book1", 5)

        self.assertEqual(1, bl.num_books)
        self.assertFalse(bl.book_list.empty)
        self.assertEqual("Book1", bl.book_list.iloc[0][0])
        self.assertEqual(5, bl.book_list.iloc[0][1])

    def test_2_add_book(self):
        bl = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        bl.add_book("Book1", 5)
        bl.add_book("Book1", 5)

        self.assertEqual(1, bl.num_books)
        self.assertFalse(bl.book_list.empty)
        self.assertEqual("Book1", bl.book_list.iloc[0][0])
        self.assertEqual(5, bl.book_list.iloc[0][1])

    def test_3_has_read(self):
        bl = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        bl.add_book("Book1", 5)
        self.assertTrue(bl.has_read("Book1"))

    def test_4_has_read(self):
        bl = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        self.assertFalse(bl.has_read("Book1"))

    def test_5_num_books_read(self):
        bl = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        bl.add_book("A", 5)
        bl.add_book("B", 5)
        bl.add_book("C", 5)
        bl.add_book("D", 5)
        bl.add_book("E", 2)
        self.assertEqual(bl.num_books, bl.num_books_read())
        self.assertEqual(5, bl.num_books_read())

    def test_6_fav_books(self):
        bl = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        bl.add_book("A", 5)
        bl.add_book("B", 5)
        bl.add_book("C", 5)
        bl.add_book("D", 5)
        bl.add_book("E", 2)
        favs = bl.fav_books()
        self.assertEqual(4, len(favs))

if __name__ == "__main__":
    unittest.main(verbosity=3)