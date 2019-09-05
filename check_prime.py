def prime(num):

    '''

    :param num: number to check if prime
    :return:nothing
    '''

    flag = 0
    if ((num % 6 == 1)|(num % 6 == 5)):
         for i in range(2, num):
            if (num%i == 0):
                flag = 1
                print "NOT PRIME NUMBER"
                break
         if (flag == 0):
            print "PRIME NUMBER"
    else:
       print " NOT PRIME NUMBER"

if __name__ == '__main__':

    n = int(input("enter a number"))
    prime(n)