import threading
import time
import random
from queue import Queue


queue = Queue(10)


class ProducerThread(threading.Thread):
    def run(self):
        global queue
        numbers = range(5)
        while True:
            number = random.choice(numbers)
            queue.put(number)
            print('Produced {}'.format(number))
            time.sleep(random.random())


class ConsumerThread(threading.Thread):
    def run(self):
        global queue
        while True:
            number = queue.get()
            queue.task_done()
            print('Consumed {}'.format(number))
            time.sleep(random.random())


producer = ProducerThread()
consumer = ConsumerThread()

producer.name = "producer"
consumer.name = "consumer"

producer.daemon = True
consumer.daemon = True

producer.start()
consumer.start()

while True:
    time.sleep(1)
