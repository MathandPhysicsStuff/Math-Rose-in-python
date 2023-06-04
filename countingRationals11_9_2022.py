

N = 5

def countRationals1(N):

    n = 1 #numerator
    c = 1 #counter
    d = c #denominator
    switch = 1
    
    # range to loop over
    r0 = 1 
    r1 = c

    while (c <= 2*N-1):

        if c <= N:
            r0 = 1
            r1 = c
            n = 1
            d = c

        else:

            if r0 < N:
                r0 += 1
            else:
                r0 = N

            r2 = N
            n = r0
            d = r2

        for i in range(r0, r1+1):

            if switch % 2 == 0:
                print(d, n)
            else:
                print(n, d)

            if n <= r1:
                n += 1
            if d > 1:
                d -= 1

        c += 1
        switch += 1
        print("")

def smoothCount(N, step):

    n = 1 #numerator
    c = 1 #counter
    d = c #denominator
    switch = 1
    
    # range to loop over
    r0 = 1 
    r1 = c
    k_list = []

    while (c <= 2*N-1):

        if c <= N:
            r0 = 1
            r1 = int((c-r0)/step)+2
            n = 1
            d = c
            
        else:

            if r0 < N:
                r0 += 1
            else:
                r0 = N
            
            r1 = int((N-r0)/step)+r0+1
            n = r0
            d = N


        for i in range(r0, r1):

            if switch % 2 == 0:
                k_list.append((d, n))
                #print(d, n)

            else:
                k_list.append((n, d))
                #print(n, d)

            if n < r1:
                n += step

            if d >= 1:
                d -= step

        c += 1
        switch += 1
        #print("")
    return k_list


def countRationals(N, step):

    n = 1 #numerator
    c = 1 #counter
    d = c #denominator
    switch = 1
    
    # range to loop over
    r0 = 1 
    r1 = c
    k_list = []
    k_list2 = []
    n_list = []
    n_list2 = []

    while (c <= 2*N-1):

        if c <= N:
            r0 = 1
            r1 = int((c-r0)/step)+2
            n = 1
            d = c
            
        else:

            if r0 < N:
                r0 += 1
            else:
                r0 = N
            
            r1 = int((N-r0)/step)+r0+1
            n = r0
            d = N


        for i in range(r0, r1):

            if switch % 2 == 0:
                k_list.append((d, n))
                k_list2.append(d/n)

            else:
                k_list.append((n,d))
                k_list2.append(n/d)

            if n < r1:
                n += step

            if d >= 1:
                d -= step

        c += 1
        switch += 1
    
    for i,j in zip(k_list, k_list2):
        
        if j not in n_list2:
            n_list2.append(j)
            n_list.append(i)

    return n_list


#print((countRationals(6, 1)))








