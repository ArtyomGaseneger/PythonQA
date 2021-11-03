from csv import DictReader
from json import dump, load

books_list = []
with open("Homework_03/data/books.csv", "r") as books_file:
    books = DictReader(books_file)
    for book in books:
        book_data = {key.lower(): book[key] for key in ("Title", "Author", "Pages", "Genre")}
        books_list.append(book_data)

with open("Homework_03/data/users.json", "r") as users_file:
    users = load(users_file)

num_books = len(books_list)
num_users = len(users)
books_per_user = num_books // num_users
books_rest = num_books % num_users
users_list = []
stop = 0
for user in users:
    start = stop
    stop += books_per_user
    if user["index"] < books_rest:
        stop += 1
    user_data = {key: user[key] for key in ("name", "gender", "address", "age")}
    user_data["books"] = books_list[start:stop]
    users_list.append(user_data)

with open("Homework_03/data/results.json", "w") as results_file:
    dump(users_list, results_file, indent=4)
