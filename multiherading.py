# Multithreading
import threading

import time


def func1():
    for i in range(5):
        print(f'Number => {i}')
        time.sleep(4)


#
def func2():
    for i in 'ABCDE':
        print(f'Character => {i}')
        time.sleep(1)


thread1 = threading.Thread(target=func1)
thread2 = threading.Thread(target=func2)

start_time = time.time()
thread1.start()

thread2.start()

thread1.join()
thread2.join()
end_time = time.time()
print(f'Total time => {end_time - start_time}')
# print('Process finished')

import time
import threading


def say_hi(name):
    print(f'Hello {name}')
    time.sleep(1)


def func(n):
    for i in range(1, n):
        print(i ** 2)
        time.sleep(1)


t1 = threading.Thread(target=say_hi, args=('Hello',))
t2 = threading.Thread(target=func, args=(5,))

t1.start()
t2.start()

t1.join()
t2.join()
