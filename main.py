def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_counts = count_letters(text)
    sorted_letter_counts = sort_letter_counts(letter_counts)
    print(f"--- Begin report of {book_path} ---")
    print_report(num_words, sorted_letter_counts)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_letters(text):
    # Convert the text to lowercase to count all letters
    lowered_text = text.lower()
    letter_counts = {}
    for char in lowered_text:
        if char.isalpha():  # Check if the character is a letter, if needed
            letter_counts[char] = letter_counts.get(char, 0) + 1
    return letter_counts

def sort_letter_counts(letter_counts):
    # Convert dictionary to a list of tuples and sort by the count
    sorted_counts = sorted(letter_counts.items(), key=lambda item: item[1], reverse=True)
    return sorted_counts

def print_report(num_words, sorted_letter_counts):
    print(f"{num_words} words found in the document\n")
    for letter, count in sorted_letter_counts:
        print(f"The '{letter}' character was found {count} times")
    print(f"--- End report ---")

main()
