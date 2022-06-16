

import time
from random import randint
from threading import Thread

def get_thread(thread_name):
	time.sleep(1)
	print(thread_name)

print('Последовательное выполнение:')

threads = [Thread(target = get_thread, args = ('thread'+str(randint(1,8)), )) for i in range(5)]

time1 = time.time() 

for t in threads:
	t.start()
	t.join()

print(f'Время последовательного выполнения: {round(time.time() - time1, 4)} сек.')

print()

print('Параллельное выполнение:')

threads = [Thread(target = get_thread, args = ('thread'+str(randint(1,8)), )) for i in range(5)]
time1 = time.time()

for t in threads:
	t.start()
for t in threads:
	t.join()

print(f'Время параллельного выполнения: {round(time.time() - time1, 4)} сек.')