import threading
import time
def square_calculator(number):
    result = number ** 2
    print(f"Square of {number} is {result}")

def thread_operation(numbers):
    threads = []

    print("Performing operation with threads...")
    for number in numbers:
        thread = threading.Thread(target=square_calculator, args=(number,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def sample(n, lock, thread_number):
    with lock:
        if n == 0:
            return

        print(f'Thread Number: {thread_number} - Count: {n}')
        time.sleep(1)

        sample(n - 1, lock, thread_number)

def locks_and_liveness():
    num_threads = int(input("Enter the number of threads: "))
    depth = int(input("Enter the depth of the recursive countdown: "))

    lock = threading.RLock()
    threads = []

    for i in range(num_threads):
        t = threading.Thread(target=sample, args=(depth, lock, i + 1))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

def main():
    while True:
        print("List of parallel computing operation")
        print("####################################")
        print("1. Thread")
        print("2. Locks and Liveness")
        print("3. Not Available")
        print("4. Not Available")
        print("5. Not Available")
        print("6. Not Available")
        print("7. Not Available")
        print("8. Not Available")
        print("9. Exit")
        print("####################################")
        print(" Name: Amen\n")

        choice = input("Choose a number: ")

        if choice == '1':
            print("\nThreads selected.")

            numbers = input("Enter numbers separated by space: ")
            numbers = [int(x) for x in numbers.split()]
            thread_operation(numbers)
        elif choice == '2':
            print("\nLocks and Liveness selected.")
            locks_and_liveness()
        elif choice == '3':
            print("\nNot Available.")
        elif choice == '4':
            print("\nNot Available.")
        elif choice == '5':
            print("\nNot Available.")
        elif choice == '6':
            print("\nNot Available.")
        elif choice == '7':
            print("\nNot Available.")
        elif choice == '8':
            print("\nNot Available.")
        elif choice == '9':
            print("Exiting the program. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please enter a number from 1 to 9.")

if __name__ == "__main__":
    main()
main()