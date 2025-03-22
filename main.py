import sys
from stats import get_num_words, get_char_counts, transform_dict

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


def print_report(file_path, word_count, char_counts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_info in char_counts:
        key = char_info["char"]
        value = char_info["count"]
        if key.isalpha():
            print(f"{key}: {value}")
    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    char_counts = get_char_counts(book_text.lower())
    print_report(sys.argv[1], get_num_words(book_text), transform_dict(char_counts))


main()
