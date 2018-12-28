import time
import threading


def countdown(count):
    while count > 0:
        print("{}: {}".format(threading.current_thread().name, count))
        count -= 1
        time.sleep(1)


def countup(count):
    while count <= 10:
        print("{}: {}".format(threading.current_thread().name, count))
        count += 1
        time.sleep(1)


threading.Thread(name='countdown', args=(5,), target=countdown).start()
threading.Thread(name='countup', args=(5,), target=countup).start()
print('done counting')
