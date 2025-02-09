from collections import Counter


def main():
    filepath = "books/frankenstein.txt"

    with open(filepath) as f:
        file_contents = f.read()
        # print(file_contents)
        # print(word_count(file_contents))
        # print(dict(character_counter(file_contents)))
        print(f'--- Begin report of {filepath} ---')
        print(f'{word_count(file_contents)} words found in the document\n')
        
        for key, value in character_counter(file_contents).items():
            if key.isalpha():
                print(f"The '{key}' character was found {value} times")

def word_count(str):
    words = str.split()
    return len(words)

# From a string, return a dictionary of character count frequencies. Characters are case-insensitive (lowercased).
def character_counter(str):
    counter = Counter(str.lower()) 

    # sort the dictionary by key
    sorted_counter = dict(sorted(counter.items()))

    return sorted_counter

main()