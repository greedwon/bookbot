from stats import get_word_count, get_character_count

def get_book_text(file):
    with open(file) as f:
        book_text = f.read()
        return book_text


def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = get_word_count(book_text)
    letter_tally = get_character_count(book_text)
    print(f"{num_words} words found in the document")
    print(letter_tally)
    return

main()
