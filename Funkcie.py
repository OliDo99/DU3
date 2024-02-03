import glob
import os
def count_file(search_word_count,total_search_word_count): 
    for filename in glob.glob('*.txt'):
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
            file =open(filename, "r")
            word_count = file.read().lower().count(search_word_count)
            total_search_word_count = total_search_word_count + word_count
            file.close()
            print(f"Pocet vyskytu hladaneho slova v subore {filename} : {word_count}")
    return total_search_word_count


def print_file(total_search_word_count):
    print(f"Pocet vyskytu hladaneho slova vo vsetkych suboroch : {total_search_word_count}")

def Main():
    print_file(total_search_word_count = count_file(input('Enter the word: '),0))