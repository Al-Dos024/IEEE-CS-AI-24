library_catalogue = {
    # title                               author                      publication_year   
    "A Song of Ice and Fire": {"author": "George R. R. Martin", "publication_year": 1996},
    "The Lord of the Rings": {"author": "J. R. R. Tolkien", "publication_year": 1937},
    "Harry Potter": {"author": "J. K. Rowling", "publication_year": 1997},
}

book_title = "Harry Potter"
print(f"Title: {book_title}")
print(f"Author: {library_catalogue[book_title]['author']}")
print(f"Publication Year: {library_catalogue[book_title]['publication_year']}")
