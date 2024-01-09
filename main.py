def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    word_count = count_words(text)
    char_count = count_chars(text)
    sorted_chars = sort_chars(char_count)
    print_report(book_path, word_count, sorted_chars)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    char_count = {}

    for char in text:
        lowered = char.lower()
        if not lowered in char_count:
            char_count[lowered] = 1
        else:
            char_count[lowered] += 1

    return char_count

def sort_on(dict):
    return dict["count"]

def sort_chars(char_dict):
    sorted_chars = []
    for char in char_dict:
        sorted_chars.append({"char": char, "count": char_dict[char]})
    sorted_chars.sort(key=sort_on, reverse=True)
    return sorted_chars

def print_report(path, word_count, sorted_chars):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print()
    for char_count in sorted_chars:
        if char_count["char"].isalpha():
            print(f"The '{char_count["char"]}' character was found {char_count["count"]} times")
    print("--- End report ---")
    

main()

