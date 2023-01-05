import threading
import time


def thread_function(name):
    print(f"Thread {name}: starting")
    time.sleep(2)
    print(f"Thread {name}: finishing")


if __name__ == "__main__":
    threads = []
    for i in range(3):
        t = threading.Thread(target=thread_function, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


'''
This program defines a function thread_function that takes a single argument (name) and prints a message indicating that the thread is starting and 
then sleeping for 2 seconds.

In the main function, the program creates three threads and starts them using the start method. The join method is then used to wait for the 
threads to complete before the program exits.

When the program is run, the threads will run concurrently, and the messages from each thread will be interleaved:

Thread 0: starting
Thread 1: starting
Thread 2: starting
Thread 0: finishing
Thread 1: finishing
Thread 2: finishing

'''