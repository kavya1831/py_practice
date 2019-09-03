def divisor(num):

    '''

    :param num: the number of which divisors has to be obtained
    :return: nothing
    '''

    for i in range(1,n+1):
                if (n%i==0):
                    print(i)

if __name__ == '__main__':

    n = int(input("enter a number"))
    print "The divisors of ",n ,"are: "
    divisor(n)