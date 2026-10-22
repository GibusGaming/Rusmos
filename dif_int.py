from sympy import *
from math import *
def prints(ex,typ):
  x = Symbol('x')
  idk = sympify(ex.replace('^','**'))
  if typ == 'Производная':
    return diff(idk,x)  
  else: 
    return integrate(idk,x)


