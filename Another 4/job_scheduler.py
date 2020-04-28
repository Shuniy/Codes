"""
Implement a job scheduler which takes in a function f
and an integer n, and calls f after n milliseconds.
"""

from time import sleep\

def sample_function():
    print("Hello")

def schedule_function(f, delay_in_ms):
    delay_in_ms = delay_in_ms / 1000
    sleep(delay_in_ms)
    f()

schedule_function(sample_function, 100000)