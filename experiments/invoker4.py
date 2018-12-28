from tasks4 import add
import time
from celery.result import AsyncResult
from tasks4 import data_extractor

# result = add.delay(1, 2)
#
# while True:
#     result2 = AsyncResult(result.task_id)
#     status = result2.status
#     print(status)
#     if 'SUCCESS' in status:
#         print('result after 5 sec wait {}'.format(result2.get()))
#         break
#     time.sleep(5)

data_extractor.delay()