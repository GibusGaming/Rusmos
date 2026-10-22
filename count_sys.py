alph = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def coconut(n,fb,tb):
    global alph
    if type(n) != int:
        n = int(n,fb)
    if n == 0:
        return 0
    else:
        res = ''
        while n > 0:
            res = alph[(n%tb)] + res
            n//=tb
        return res

