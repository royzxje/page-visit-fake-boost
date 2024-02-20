import requests
import time
from threading import Thread

THREAD_COUNT = 4

def boost(url, num):
    for i in range(1, num):
        response = requests.get(url, headers=header)
        # print(response.status_code)


# example user agent as proxy to send request to web page
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}

print('Welcome! Enter the camo url for your visitor count picture: ')
url = input()

print('Number of boost on visitor counts: ')
num = int(input())

print('Working on it...')
start = time.time()

threads = []
for i in range(THREAD_COUNT):
    t = Thread(target=boost, args=(url, int(num/THREAD_COUNT),))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print('Success!')
print('Time Taken: ' + str(round(time.time() - start, 3)) + " sec")