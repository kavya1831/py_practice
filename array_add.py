#list1=input("enter list 1")
#list2=input("enter list 2")
list1 = [1,2,3,4]
list2 = [2,3,4,5]
print("list1:" +str(list1))
print("list2:" +str(list2))
res = [list1[i] + list2[i] for i in range(len(list1))]
print("result:"+str(res))
