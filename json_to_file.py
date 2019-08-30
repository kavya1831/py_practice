import json


def json_file(sample_json):
    '''

    writes the data in the json to the file sample.json
    '''


    with open('sample.json', 'w') as outfile:
      json.dump(sample_json, outfile)

if __name__ == '__main__':

    sample_json= {}
    sample_json['details'] = []

    sample_json['details'].append({'name': 'kavya',
                                  'usn': '4gm16is052',
                                  'college': 'GMIT'})

    sample_json['details'].append({'name': 'teju',
                                  'usn': '4bd16is101',
                                  'college': 'BIET'})

    sample_json['details'].append({'name': 'spoorthi',
                                  'usn': '4ms16is044',
                                  'college': 'MSRIT'})

    json_file(sample_json)