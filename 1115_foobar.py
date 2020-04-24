"""交替打印FooBar
两个不同线程会共用一个FooBar实例，其中一个线程将会调用 foo() 方法，
另外一个现成将会调用 bar() 方法。
确保 "foobar" 被输出 n 次
"""
from threading import Thread, Semaphore
import time

class FooBar:
    def __init__(self, n):
        self.n = n
        self.sem1 = Semaphore(1)
        self.sem2 = Semaphore(0)
    
    def foo(self):
        for i in range(self.n):
            self.sem1.acquire()  # if >0, proceed, then -1; if ==0, wait
            print('foo', end='')
            self.sem2.release()  # sem2 +1
    
    def bar(self):
        for i in range(self.n):
            self.sem2.acquire()
            print('bar', end='')
            self.sem1.release()


# def test(a):
#     # print thread name
#     print(t.name)
#     print(a)
#     time.sleep(2)
#     # release semaphore
#     sem.release()

# # set the semaphore tobe 5
# sem = Semaphore(5)
# for i in range(10):
#     # get a semaphore
#     sem.acquire()
#     t = Thread(target=test, args=(i,))
#     t.start()

if __name__ == '__main__':
    foobar = FooBar(3)
    t1 = Thread(target=foobar.foo)
    t2 = Thread(target=foobar.bar)
    t1.start()
    t2.start()
