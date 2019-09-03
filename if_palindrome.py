def ispalindome(str):

    '''

    :param str: string to check if palindrome
    :return: nothing
    '''
    rev_str= str[::-1]
    print rev_str

    if str== rev_str:
        print "pallindome"
    else:
        print "not palindome"


if __name__ == '__main__':

    str=raw_input("enter string")
    ispalindome(str)