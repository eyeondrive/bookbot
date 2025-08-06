def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


def get_num_words(filepath):
    book_text = get_book_text(filepath)
    lowercase_text = book_text.lower()
    split_text = lowercase_text.split()
    num_words = len(split_text)
    return num_words
    #print(f"{num_words} words found in the document")

def get_num_letters(filepath):
    book_text = get_book_text(filepath)
    lowercase_text = book_text.lower()
    count_of_each_letter = {char: lowercase_text.count(char) for char in lowercase_text if char.isalpha()}
    #split_text = lowercase_text.split()
    
    return count_of_each_letter