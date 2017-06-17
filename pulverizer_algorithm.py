def pulverizer(a, b):
        """
        uses the extended euclidean algorithm(pulverizer),
        to calculate the gcd of a and b, the number of steps
        and calculates the coefficents e,f such that
        gcd(a, b) = e*a + f*d
        """
        if abs(a) > abs(b):
                x, y = abs(a), abs(b)
                #x = c*a + d*b, y = e*a + f*d
                c, d, e, f = 1 if a > 0 else -1, 0, 0, 1 if b > 0 else -1
                case = 0
        else:
                x, y = abs(b), abs(a)
                #x = c*a + d*b, y = e*a + f*d
                c, d, e, f = 1 if b > 0 else -1, 0, 0, 1 if a > 0 else -1
                case = 1
        counter = 0	#counter of steps
        while y != 0:
                q = x // y * (a*b)//abs((a*b)) # quotient
                c, d, e, f = e, f, c - q*e, d - q*f
                r = x % y
                x = y
                y = r
                counter = counter + 1
        if case  == 0:
                return x, counter, c, d
        else:
                return x, counter, d, c
        
