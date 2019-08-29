class calculations:

    def __init__(self,num1,num2):
        self.a = num1
        self.b = num2

    def sum(self,a,b):
        add = a+b
        print(add)

    def sub(self,a,b):
        if a<b:
            print "val of a smaller than b"
        else:
            sub= a-b
            print(sub)

    def mul(self,a,b):
        mul = a*b
        print(mul)

if __name__ == '__main__':

    a = input("enter the value of A")
    b = input("enter the value of B")
    num = calculations(a,b)
    num.sum()
    num.sub(a,b)
    num.mul(a,b)