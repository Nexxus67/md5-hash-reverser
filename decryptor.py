import hashlib
import itertools
import string
import sys
import time

def print_welcome_message():
    print("""
    *********************************************
    *                                           *
    *              MD5 Reverser                 *
    *                                           *
    *********************************************
    """)

def crack_md5_hash(target_hash, max_length=6):
    chars = string.ascii_lowercase + string.digits
    total_attempts = sum(len(chars) ** length for length in range(1, max_length + 1))
    attempt_counter = 0

    for length in range(1, max_length + 1):
        for attempt in itertools.product(chars, repeat=length):
            attempt_str = ''.join(attempt)
            if hashlib.md5(attempt_str.encode()).hexdigest() == target_hash:
                return attempt_str
            attempt_counter += 1
            print_progress(attempt_counter, total_attempts)
    return None

def print_progress(current, total):
    bar_length = 50
    progress = current / total
    block = int(bar_length * progress)
    text = f"\r[{'#' * block + '-' * (bar_length - block)}] {current}/{total} attempts"
    sys.stdout.write(text)
    sys.stdout.flush()

if __name__ == "__main__":
    print_welcome_message()
    target_hash = input("Please enter the MD5 hash to crack: ")
    start_time = time.time()
    password = crack_md5_hash(target_hash)
    end_time = time.time()
    if password:
        print(f"\nPassword found: {password}")
    else:
        print("\nPassword not found within the given constraints.")
    print(f"Time taken: {end_time - start_time:.2f} seconds")

