import sys
from stats import *

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    path = sys.argv[1]

def get_book_text():
    with open(path) as file:
        book_text = file.read()
    return book_text

book = get_book_text()
amount_of_letters = letter_count(book)
sorted_list = dict_to_list(amount_of_letters)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {path}...")
print("----------- Word Count ----------)")
print(f"Found {get_num_words(book)} total words")
print("--------- Character Count -------")
for i in sorted_list:
    print(f"{i['char']}: {i['num']}")
print("============= END ===============")