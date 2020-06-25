def SieveOfEratosthenes(n):

    # Create a boolean array "prime[0..n]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    # Print all prime numbers
    mylist = []
    for p in range(n + 1):
        if prime[p]:
            mylist.append(p)
    f = open("D:\Python_Github\Squarefree_Binomial_Coefficients\Prime_numbers.txt","w")
    f.write(str(mylist))
    f.close()
#    return(list)

SieveOfEratosthenes(11243247)
