import threading

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def check_primes(start, end, result):
    primes = [n for n in range(start, end) if is_prime(n)]
    result.extend(primes)

def threaded_prime_checker(start, end, num_threads=4):
    step = (end - start) // num_threads
    threads = []
    results = []

    for i in range(num_threads):
        thread_start = start + i * step
        thread_end = start + (i + 1) * step if i < num_threads - 1 else end
        result = []
        thread = threading.Thread(target=check_primes, args=(thread_start, thread_end, result))
        threads.append((thread, result))
        thread.start()

    all_primes = []
    for thread, result in threads:
        thread.join()
        all_primes.extend(result)

    all_primes.sort()
    return all_primes

import threading
from collections import Counter
import os

def process_lines(lines, result):
    word_count = Counter()
    for line in lines:
        words = line.strip().lower().split()
        word_count.update(words)
    result.append(word_count)

def threaded_word_count(filename, num_threads=4):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    total_lines = len(lines)
    chunk_size = total_lines // num_threads
    threads = []
    results = []

    for i in range(num_threads):
        start = i * chunk_size
        end = None if i == num_threads - 1 else (i + 1) * chunk_size
        chunk = lines[start:end]
        result = []
        thread = threading.Thread(target=process_lines, args=(chunk, result))
        threads.append((thread, result))
        thread.start()

    final_count = Counter()
    for thread, result in threads:
        thread.join()
        final_count.update(result[0])

    return final_count
