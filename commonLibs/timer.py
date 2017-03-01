''' Simple timer measuring example.'''

import time


class Timer(object):
    '''The timer class is for computing the time elapsed.'''
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *kwargs):
        self.end = time.time()
        self.timeElapsed = self.end - self.start
        return "Time elapsed is %d", self.timeElapsed


if __name__ == "__main__":
    with Timer() as T:
        time.sleep(3)
        print "I waited for 3 seconds"
    print "Time Elapsed: %d" % T.timeElapsed
