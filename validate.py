def validation(valid_array,data_for_validation):
    '''

    :param valid_array: json object's key
    :param data_for_validation: json object
    :return: true(if key is present in both data_for_validation & validate_array), missing(if key is missing in valid_array)
    '''


    for key in data_for_validation:
      if key not in valid_array:
          return "missing"
    return True


if __name__ == '__main__':
    valid_array = ["email_id","password","name"]
    data_for_validation = ({
        "name": "kavya",
     "email_id" : "kkm18311@gmail.com",
     "password": "rko"
    }
    )
    print data_for_validation
    print(validation(valid_array,data_for_validation))