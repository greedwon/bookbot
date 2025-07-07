from stats import get_word_count, get_character_count

def get_book_text(file):
    with open(file) as f:
        book_text = f.read()
        return book_text

def sort_on(items):
    return items["num"]

def main():
    book = "books/frankenstein.txt"
    book_text = get_book_text(book)
    num_words = get_word_count(book_text)
    char_count = get_character_count(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print(f"{char_count}")
    for char in char_count:
        char = char_count["char"]
        num = char_count["num"]
        print(f"{char}: {num}")
    return

main()
