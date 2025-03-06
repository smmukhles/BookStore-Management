from save_all_books import view_all_books
from view_all_books import view_all_books


def update_books(all_books):
    view_all_books(all_books)
    book_index = int(input("Enter the number of the book to update ")) - 1
    if 0 <=book_index <len(all_books):
        book = all_books[book_index]
        print(f"\nUpdating {book['title']} by {book['author']}")


        book['title'] = input(f"Enter New Title (current: {book['title']}): ")
        book['author'] = input(f"Enter New Author (current: {book['author']}): ")
        book['isbn'] = input(f"Enter New ISBN (current: {book['isbn']}): ")
        book['year'] = input(f"Enter New Year (current: {book['year']}): ")
        book['price'] = input(f"Enter New Price (current: {book['price']}): ")
        book['title'] = input(f"Enter New Title (current: {book['title']}): ")
        book['quantity'] = input(f"Enter New Quantity (current: {book['quantity']}): ")
        try:
            book['isbn'] = int(book['isbn'])
            book['price'] = int(book['price'])
            book['quantity'] = int(book['quantity'])
        except ValueError:
            print("Invalid input for ISBN, price, ir quanitty. Please enter valid integer.")
            return
            save_all_books(all_books)
            print("Book Updated Successfully!")

    else:
        print("Invalid Selection. Please try again!")
    return all_books
        

        



                