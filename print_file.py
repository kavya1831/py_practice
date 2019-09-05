import string

file = open("names.txt","r")
str= file.read()
lines = str.split("\n")
unique = set(lines)
unique_list = list(unique)
print unique_list


