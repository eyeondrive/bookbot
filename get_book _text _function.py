def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


def main():
    # Fetch Book Text
    #import pandas
    filepath = "./books/frankenstein.txt"
    book_text = get_book_text(filepath)
    #book_dataframe = pandas.DataFrame({'text': [book_text]})
    #print(book_dataframe.head(3))
    print (book_text)

main()    