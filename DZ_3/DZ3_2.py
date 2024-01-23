from multiprocessing import Pool, cpu_count
from time import time

def factorize_single(number):
    return [i for i in range(1, number + 1) if number % i == 0]

def synchronous_factorize(numbers):
    return [factorize_single(num) for num in numbers]

def parallel_factorize(numbers):
    with Pool(processes=cpu_count()) as pool:
        return pool.map(factorize_single, numbers)

if __name__ == "__main__":
    
    test_numbers = [18, 19, 20, 21, 22, 23, 24, 25, 100, 101, 102, 103, 104, 105]

    # Синхронне виконання
    start_time = time()
    sync_results = synchronous_factorize(test_numbers)
    sync_duration = time() - start_time

    # Паралельне виконання
    start_time = time()
    parallel_results = parallel_factorize(test_numbers)
    parallel_duration = time() - start_time

    print("Synchronous Execution: Time =", sync_duration, ", Results =", sync_results)
    print("Parallel Execution: Time =", parallel_duration, ", Results =", parallel_results)