# #!/usr/bin/python3
# """ Log Parsing """
# """Scripts reads stdin line by line, compute metrics.
# * Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
# * Each 10 lines and after a keyboard interruption (CTRL + C), prints those statistics since the beginning:
#     - Total file size: File size: <total size>
#     - where is the sum of all previous (see input format above)
#     - Number of lines by status code:
#         - possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
#         - if a status code doesn’t appear, don’t print anything for this status code
#         - format: <status code>: <number>
#         - status codes should be printed in ascending order
# """
# import sys
# import time
# import requests

# IP = sys.argv[1]
# DATE = sys.argv[2]
# VERB = sys.argv[3]
# STATUS = sys.argv[4]
# FILE_SIZE = sys.argv[5]

# try:
#     pass
# except KeyboardInterrupt as KI:
#     print(f"{'\n'*10}")
#     print(f"File size : {FILE_SIZE}\n ")

import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    ))
    sys.stdout.flush()