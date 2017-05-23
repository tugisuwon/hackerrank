def fermat(n):
    o = n - 1
    t = 0
    while o % 2 == 0:
        o = o / 2
        t = t + 1 
    for time in xrange(3):
        while True:
            r = random.randint(2, n)-1
            if r != 0 and r != 1:
                break
        
        rp = pow(r, o, n)
        if (rp != 1) and (rp != n - 1):
            i = 1
            while (i <= t - 1) and (rp != n - 1):
                rp = pow(rp, 2, n)
                i += 1

            if (rp != (n - 1)):
                return False
    return True 