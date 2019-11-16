def fib(n, out='fibs.txt'):
    if n <= 1: return 1
    c, p, s = [1, 1], 0, 2
    with open(out, 'w') as f:
        while s != n:
            c, s = [c[1], sum(c)], s+1
            f.write(str(c[0]) + '\n')
            s+=1
