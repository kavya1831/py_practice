def replacesubstring(main_string,sub_string):
    return string.replace(main_string,sub_string)

if __name__ == '__main__':

    string = raw_input("enter the string")
    main_string = raw_input("enter the main string")
    sub_string = raw_input("enter sub string")
    print replacesubstring(main_string,sub_string)