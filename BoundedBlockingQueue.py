"""
Implement a thread safe bounded blocking queue that has the following methods:

BoundedBlockingQueue(int capacity) The constructor initializes the queue with a maximum capacity.

void enqueue(int element) Adds an element to the front of the queue. If the queue is full, 
the calling thread is blocked until the queue is no longer full.

int dequeue() Returns the element at the rear of the queue and removes it. 
If the queue is empty, the calling thread is blocked until the queue is no longer empty.

int size() Returns the number of elements currently in the queue.

Your implementation will be tested using multiple threads at the same time. Each thread will either be a producer 
thread that only makes calls to the enqueue method or a consumer thread that only makes calls to the dequeue method. 
The size method will be called after every test case.
"""
from threading import Semaphore
from collections import deque

class BoundedBlockingQueue(object):
    def __init__(self, capacity):
        self.queue = deque()
        self.s1 = Semaphore(capacity)
        self.s2 = Semaphore(0)

    def enqueue(self, val):
        self.s1.acquire()
        self.queue.append(val)
        print(self.queue)
        self.s2.release()

    def dequeue(self):
        self.s2.acquire()
        val = self.queue.popleft()
        self.s1.release()

        return val

    def size(self):
        return len(self.queue)


queue = BoundedBlockingQueue(3)

queue.enqueue(1);   # The producer thread enqueues 1 to the queue.
queue.enqueue(0)
queue.enqueue(2)
print(queue.dequeue());    # The consumer thread calls dequeue and returns 1 from the queue.
print(queue.dequeue());    # Since the queue is empty, the consumer thread is blocked.
print(queue.dequeue())
queue.enqueue(3);   # The producer thread enqueues 3 to the queue.
queue.enqueue(4);   # The producer thread is blocked because the queue's capacity (2) is reached.
print(queue.dequeue());    # The consumer thread returns 2 from the queue. The producer thread is unblocked and enqueues 4 to the queue.
print(queue.size());       # 2 elements remaining in the queue. size() is always called at the end of each test case.
