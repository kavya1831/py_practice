import string

def case(alphabet):

    '''

    :param alphabet: has the string to be case equalised
    :return: lower case converted string
    '''
    check = str.lower()
    return check

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
    case_string = case(str)
    ispalindome(case_string)