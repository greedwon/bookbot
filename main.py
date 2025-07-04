from stats import get_word_count

def get_book_text(file):
    with open(file) as f:
        book_text = f.read()
        return book_text


def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = get_word_count(book_text)
    print(f"{num_words} words found in the document")
    return

main()
