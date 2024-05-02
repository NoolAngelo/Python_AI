from threading import Thread

num_threads = 5
choosing = [False] * num_threads
number = [0] * num_threads

def lock(thread_id):
    choosing[thread_id] = True
    number[thread_id] = max(number) + 1
    choosing[thread_id] = False

    for i in range(num_threads):
        if i != thread_id:
            while choosing[i]:
                pass

            while number[i] != 0 and (number[i] < number[thread_id] or (number[i] == number[thread_id] and i < thread_id)):
                pass

def unlock(thread_id):
    number[thread_id] = 0

def critical_section(thread_id):
    print(f"Thread {thread_id} is in the critical section")

def thread_function(thread_id):
    lock(thread_id)
    critical_section(thread_id)
    unlock(thread_id)

threads = []
for i in range(num_threads):
    thread = Thread(target=thread_function, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()