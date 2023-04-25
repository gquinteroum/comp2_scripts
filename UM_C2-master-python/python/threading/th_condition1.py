import random
import logging
import threading
import time


def consumer(cond):
    """wait for the condition and use the resource"""
    logging.debug('Starting consumer thread')
    with cond:
        cond.wait()
        logging.debug('Resource is available to consumer: %s' % threading.current_thread().name)


def producer(cond):
    """set up the resource to be used by the consumer"""
    logging.debug('Starting producer thread')
    time.sleep(random.randrange(2, 5))
    with cond:
        logging.debug('Making resource available: %s' % threading.current_thread().name)
        cond.notify()


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s (%(threadName)-2s) %(message)s',
)

condition = threading.Condition()
c1 = threading.Thread(name='c1', target=consumer, args=(condition,))
c2 = threading.Thread(name='c2', target=consumer, args=(condition,))
p1 = threading.Thread(name='p1', target=producer, args=(condition,))
p2 = threading.Thread(name='p2', target=producer, args=(condition,))

c1.start()
time.sleep(1)
c2.start()
p1.start()
p2.start()
