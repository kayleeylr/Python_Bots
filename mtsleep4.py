#! usr/bin/env python

import threading
from time import sleep, ctime

loops = [4,2]

class ThreaFunc(object):
    
	def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        apply(self.func, self.args)

    def loop(nloop, nesc):
       print 'start loop', nloop,'at:' ctime()
       sleep(nsec)
       print 'loop', nloop, 'done at:',ctime()

	def main():
       print 'starting at:' ,ctime()
       thread=[]
       nloops = range(len(loops))

       for i in nloops :#creat all threads
       t= threading.Thread(target = ThreadFunc(loop, (i,loops[i]), loop.__name__))
       threads.append(t)

       for i in nloops :#start all thread
           threads[i].join()

       print 'all DONE at:',ctime()


if __name__ == '__main__':
    main()
	   

