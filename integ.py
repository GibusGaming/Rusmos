from dif_int import *
from math import *
def integ(exp,start,end):
    x = start
    idk = prints(exp,1)
    st = eval(str(idk))
    x = end
    idk = prints(exp,1)
    ed = eval(str(idk))
    print(idk)
    return ed-st
print(integ('2*x',1,3))
