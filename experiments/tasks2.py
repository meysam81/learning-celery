import threading

counterBuffer = 0
counterLock = threading.Lock()

COUNTER_MAX = 1000000


def consumer1_counter():
    global counterBuffer
    for i in range(COUNTER_MAX):
        counterLock.acquire()
        # print('{}: {}'.format(threading.current_thread().name, counterBuffer))
        counterBuffer += 1
        counterLock.release()


def consumer2_counter():
    global counterBuffer
    for i in range(COUNTER_MAX):
        counterLock.acquire()
        # print('{}: {}'.format(threading.current_thread().name, counterBuffer))
        counterBuffer += 1
        counterLock.release()


t1 = threading.Thread(name="consumer1", target=consumer1_counter)
t2 = threading.Thread(name="consumer2", target=consumer2_counter)

t1.start()
t2.start()

t1.join()
t2.join()

print(counterBuffer)
