


def main():
    from stats import get_num_words, get_num_letters
    import sys
    #filepath = "./books/frankenstein.txt"
    #print(sys.argv[0])
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        for i in range(1,len(sys.argv)):
            filepath = sys.argv[i]
            print(f"this is book file {filepath}")
            output_words = get_num_words(filepath)
            output_letters = get_num_letters(filepath)
            print("============ BOOKBOT ============")
            print(f"Analyzing book found at {filepath}...")
            print("----------- Word Count ----------")
            print(f"Found {output_words} total words")
            print("--------- Character Count -------")
            output_letters = sorted(output_letters.items(), reverse=True, key=lambda item: item[1])
            for i in output_letters:
               print(f"{i[0]}: {i[1]}")
            print("============= END ===============")

main()    