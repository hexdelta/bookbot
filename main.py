def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    chars_dict = character_count(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    sorted_list = sort_chars(chars_dict)
    for item in sorted_list:
        print (f"The '{item['char']}' character was found {item['num']} times") 
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(bulk_text):
    words = bulk_text.split()
    return len(words)

def character_count(text):
    chars = {}
    for c in text:
        character = c.lower()
        if character in chars:
            chars[character] += 1
        else:
            chars[character] = 1
    return chars

def sort_on(d):
    return d["num"]

def sort_chars(dict):
    sorted_list = []
    for char in dict:
        if char.isalpha():
            sorted_list.append({"char": char, "num": dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list   
main()