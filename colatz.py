from threading import Thread
from queue import Queue


def colatz(a):
    x = 0
    while a > 1:
        x += 1
        if a % 2 == 0:
            a = int(a / 2)
        else:
            a = (a * 3) + 1
        if x > 1000:
            print(f"Failed at number: {a}")
            return False
    return True


def count(snum, enum, result_queue):
    for i in range(snum, enum + 1):
        if not colatz(i):
            result_queue.put(False)
            return
    result_queue.put(True)


if __name__ == '__main__':
    result_queue = Queue()
    threads = [
        Thread(target=count, args=(2, 250000, result_queue)),
        Thread(target=count, args=(250001, 500000, result_queue)),
        Thread(target=count, args=(500001, 750000, result_queue)),
        Thread(target=count, args=(750001, 1000000, result_queue)),
    ]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    results = [result_queue.get() for _ in threads]
    print("Results:", results)
    print("Final Result:", all(results))