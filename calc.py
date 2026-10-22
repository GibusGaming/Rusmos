from math import *
def calc_slv(s):
    s=s.replace('^','**')
    s=s.replace('\/','**(1/')
    s=s.replace('!','factorial(')
    return eval(s)
