# helpers for IO and conversion between
# python values and functional values
def ch2num(n):
    return n(lambda a: a+1)(0)
def ch2tup(p):
    return (p(lambda a:lambda b:a), p(lambda a:lambda b:b))
def ch2bool(q):
    return q(True)(False)
def ch2ipair(i):
    return(ch2num(fst(i)), ch2num(snd(i)))
def ch2int(i):
    return ch2num(fst(i))-ch2num(snd(i))
def to_list(*values):
    if len(values)>1:
        return pair(tr)(pair(values[0])(to_list(values[:1])))
    elif len(values) == 1:
        return cons(values[0])(to_list())
    else:
        return nil

# church booleans
def tr(a):
    return lambda b: a
def fs(a):
    return lambda b: b

# church bool functions in german for extra confusion
def und(p):
    return lambda q: p(q)(p)
def oder(p):
    return lambda q: p(p)(q)
def nicht(p):
    return p(fs)(tr)
def xor(p):
    return lambda q: p(nicht(q))(q)

# the main church numeral functions
def succ(n):
    return lambda f: lambda a: f(n(f)(a))
def is0(n):return n(lambda a: fs)(tr)
def add(n):
    return lambda m: n(succ)(m)
def mul(n):
    return lambda m: lambda f: n(m(f))
def exp(n):
    return lambda m: m(n)
def nats(n = int):
    result, i = (lambda f: lambda a: a), 1
    while (i <= n):
        i += 1
        result = succ(result)
    return result
def ints(n):
    if(n>0):
        return pair(nats(n))(zero)
    elif(n<0):
        return pair(zero)(nats(-n))
    else:
        return szero
def pred(n):
    phi=lambda p:pair(snd(p))(succ(snd(p)))
    return n(phi)(pair(zero)(zero))(lambda a:lambda b:a)
def sub(n):
    return lambda m: m(pred)(n)
def lte(n):
    return lambda m: is0(sub(n)(m))
def eq(n):
    return lambda m: und(lte(n)(m))(lte(m)(n))


# the numerals themselves
def zero(f):
    return lambda a: a
one = lambda f: lambda a: f(a)
two = succ(one)
three = add(two)(one)
four = exp(two)(two)
five = add(two)(three)
six = mul(two)(three)
seven = nats(7)
eight = exp(two)(three)
nine = exp(three)(two)
ten = add(five)(five)
one_hundred = nats(100)

# the church pair encoding functions
def pair(a):
    return lambda b: lambda f: f(a)(b)
def fst(p):
    return p(lambda a: lambda b: a)
def snd(p):
    return p(lambda a: lambda b: b)

# the church list encoding functions
def nil(f):
    return(pair(tr)(tr)(f))
def isNil(l):
    return fst(l)
def cons(h):
    return lambda t: pair(fs)(pair(h)(t))
def head(l):
    return fst(snd(l))
def tail(l):
    return snd(snd(l))

# integers as pairs
szero = pair(zero)(zero)
def ssucc(i):
    return one_zero(pair(succ(fst(i)))(snd(i)))
def one_zero(i):
    return pair(sub(fst(i))(snd(i)))(sub(snd(i))(fst(i)))
def neg(i):
    return pair(snd(i))(fst(i))
def sadd(i):
    return lambda j: pair(add(fst(i))(fst(j)))(add(snd(i))(snd(j)))
def ssub(i):
    return lambda j: sadd(i)(neg(j))
def smul(i):
    return lambda j: pair(add(mul(fst(i))(fst(j)))(mul(snd(i))(snd(j))))(add(mul(fst(i))(snd(j)))(mul(snd(i))(fst(j))))


# a future me problem is to impliment a printing function
#def out(val, a = "none", b = True, c="none", d=False):
#    if not d:
#        d = c
#    if(a == "num" or a == "Num"):
#        result = val(lambda a: a+1)(0)
#    elif(a == "pair" or a == "Pair"):
#        result = ''
#        print((out(fst(val), a, False, c), out(snd(val), a, False, d)))
#    elif(a == "bool" or a == "Bool"):
#        result = val(True)(False)
#    elif(a == "list" or a == "List"):
#        result = []
#    elif(a == "none", a == "None"):
#        result = a
#    else:
#        result = None
#    if b:
#        print(result)
#    return (result, val)
