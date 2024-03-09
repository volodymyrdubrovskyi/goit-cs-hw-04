from pathlib import Path
from multiprocessing import Semaphore, Process, Queue
from time import time

from support_func import read_file, create_files_list

result_dic = {}

def find_word_in_file(condition, path: Path, word, q: Queue):
    with condition:
        text = read_file(path)
        if word in text:
            q.put(str(path)) 

def main():
    initial_folder = Path("./Files")
    word = "Hello"
    result_dic[word] = []
    file_list = create_files_list(initial_folder)
    
    time_of_start = time()

    pool = Semaphore(3)
    q = Queue()
    processes = []
    for file in file_list:
        proc = Process(name=str(file), target=find_word_in_file, args=(pool, file, word, q))
        proc.start()
        processes.append(proc)
    [el.join() for el in processes]

    while not q.empty():
        result_dic[word].append(q.get())

    print(f"Using Multiprocessing.....\nList of files with word '{word}' in folder '{initial_folder}':")
    for file in result_dic[word]:
        print(f"{file}")
    print(f"Time elapsed: {round(time()-time_of_start, 5)}")

if __name__ == "__main__":
    main()