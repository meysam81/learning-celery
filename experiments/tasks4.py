from celery import Celery
import time
from celery.exceptions import SoftTimeLimitExceeded
from datetime import timedelta
from celery.decorators import periodic_task
from celery.schedules import crontab
import redis

app = Celery('tasks', backend='redis://', broker='redis://localhost:6379/0')


@app.task(name='tasks.add')
def add(x, y):
    time.sleep(10)
    print('{} + {} = {}'.format(x, y, x + y))
    return x + y


def backoff(attempts):
    """
    1, 2, 4, 8, 16, 32, ...
    :param attempts:
    :return:
    """
    return 2 ** attempts


@app.task(bind=True, max_retries=4, soft_time_limit=5)
def data_extractor(self):
    try:
        for i in range(1, 11):
            print('Crawling HTML DOM!')
            time.sleep(2)
            if i == 1:
                raise ValueError("Crawling index error")
    except SoftTimeLimitExceeded:
        print('exceeded soft limit')
    except Exception as exc:
        print('There was an exception lets retry after 5 secs.')
        raise self.retry(exc=exc, countdown=backoff(self.request.retries))


key = 'dsa6f451sad35f1sd35fs3ad5f1s3daf13dsa5f11'


@periodic_task(bind=True, run_every=crontab(minute='*/1'), name='tasks.send_mail_from_queue')
def send_mail_from_queue(self):
    r = redis.Redis()
    timeout = 60 * 5
    have_lock = False
    my_lock = r.lock(key, timeout=timeout)

    try:
        have_lock = my_lock.acquire(blocking=False)
        # critical section
        if have_lock:
            messages_sent = "example.email"
            print("{}: email message sent successfully, [{}]".
                  format(self.request.hostname, messages_sent))
            time.sleep(10)
        # end section

    finally:
        print("release resources")
        if have_lock:
            my_lock.release()


