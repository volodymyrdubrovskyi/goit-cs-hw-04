from pathlib import Path
from threading import Thread, Semaphore
from time import time

from support_func import read_file, create_files_list

result_dic = {}

def find_word_in_file(condition, path: Path, word):
    with condition:
        text = read_file(path)
        if word in text:
            result_dic[word].append(str(path))

def main():
    initial_folder = Path("./Files")
    word = "Hello"
    result_dic[word] = []
    file_list = create_files_list(initial_folder)
    
    time_of_start = time()
    threads = []
    pool = Semaphore(3)
    for file in file_list:
        thread = Thread(name=str(file), target=find_word_in_file, args=(pool, file, word))
        thread.start()
        threads.append(thread)
    [el.join() for el in threads]

    print(f"Using Threads.....\nList of files with word '{word}' in folder '{initial_folder}':")
    for file in result_dic[word]:
        print(f"{file}")
    print(f"Time elapsed: {round(time()-time_of_start, 5)}")

if __name__ == "__main__":
    main()