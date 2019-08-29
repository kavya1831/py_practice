def calculate(arr):

    if str(type(arr))=="<type 'list'>":
      return "array as list","xyz"

    sum = 0
    for item in arr:
        sum+=item
    avg=sum/n
    return sum,avg

if __name__ == '__main__':


    n = int(input("enter the no. of elements to be entered in array"))
    print "enter",+n ,"elements"
    arr = []
    for i in range(n):
        arr.append(int(input()))

    print arr

    sum ,avg =calculate(arr)
    print "sum of array elements is", sum
    print "avg of array elements is", avg