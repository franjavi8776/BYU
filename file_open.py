with open ('books.txt') as file_books:
    for book in file_books:
        book = book.strip()
        print(book)
