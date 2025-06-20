from stats import get_num_words, get_character_count, sort_character_count
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
book_file_path = sys.argv[1]

def get_book_text(book_file_path):
    with open(book_file_path) as book_file:
        book_text = book_file.read()
    return book_text

def main():
    num_words = get_num_words(get_book_text(book_file_path))
    character_counts = sort_character_count(get_character_count(get_book_text(book_file_path)))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for character in character_counts:
        print(f"{character['char']}: {character['num']}")
    print("============= END ===============")
    
main()