import concurrent.futures
import time

# Define a function for the concurrency testing 
# This sets up n number of computations, to be later computer at the same time
def compute_something(n):
    print(f"Computing something {n}")
    time.sleep(1)
    return n ** 2


if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(compute_something, i) for i in range(10)]

        for future in concurrent.futures.as_completed(futures):
            print(future.result())
