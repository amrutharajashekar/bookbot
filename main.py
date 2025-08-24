
from stats import get_word_count, get_book_text, get_char_count , generate_new_dict
import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book = sys.argv[1]
print("Analyzing book found at {book}...")
print("----------- Word Count ----------")
print(f"Found {get_word_count(book)} total words")
print("--------- Character Count -------")
content = get_book_text(book)
char_dict = get_char_count(content)
fine_char_dict = generate_new_dict(char_dict)
for item in fine_char_dict:
    if item["char"].isalpha():
        print(f"{item["char"]}: {item["num"]}")
print("============= END ===============")