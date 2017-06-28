__author__ = 'fernando.ormonde'

import numpy
import math
import time
import random
import pp
import sys

def generate_jump(r):
    theta = random.uniform(0,2)*math.pi
    x = r*math.cos(theta)
    y = r*math.sin(theta)
    return x,y

def generate_n_jump(n, r):
    x, y = 0,0
    for i in range(n):
        jump = generate_jump(r)
        incx, incy =  jump
        x += incx
        y += incy
    return x,y


def simulate_jumps(N,n,r):
    x = numpy.zeros(N)
    y = numpy.zeros(N)
    for i in range(N):
        xy = generate_n_jump(n, r)
        x[i] = xy[0]
        y[i] = xy[1]
    return x,y

t0 = time.time()
print simulate_jumps(2, 10, 1)
t1 = time.time()


#ppservers = ()

#if len(sys.argv) > 1:
#    ncpus = int(sys.argv[1])
#    job_server = pp.Server(ncpus, ppservers=ppservers)

#else:
#    job_server = pp.Server(ppservers=ppservers)

#print "Starting pp with", job_server.get_ncpus(), "workers"

#job1 = job_server.submit(simulate_jumps, (1000, 1000, 1),(generate_n_jump, generate_jump), ("numpy", "math", "random"))


#result = job1()

#print "Distance from origin is", result

#start_time = time.time()


#inputs = (10000, 15000, 1200)
#jobs = [(input, job_server.submit(simulate_jumps, (input, 100, 1), (generate_n_jump, generate_jump), ("numpy", "math", "random"))) for input in inputs]

#for input, job in jobs:
#    print "Results for", input, "jumps are", job()



#print "Time elapsed: ", time.time() - start_time, "s"
#job_server.print_stats()


