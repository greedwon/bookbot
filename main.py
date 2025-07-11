import sys
from stats import get_word_count, get_character_count

def get_book_text(file):
    with open(file) as f:
        book_text = f.read()
        return book_text

def sort_on(items):
    return items["num"]

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    book_text = get_book_text(book)
    num_words = get_word_count(book_text)
    char_count = get_character_count(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_count.sort(reverse=True, key=sort_on)
    for letter in char_count:
        print(f"{letter['char']}: {letter['num']}")
    return

main()
