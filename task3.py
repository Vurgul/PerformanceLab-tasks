import json


def parsing_json(data_dict: dict, revisions_list):
    if type(data_dict) == dict:
        for key1 in data_dict.keys():
            if key1 == 'id':
                for key2 in data_dict.keys():
                    if key2 == 'value':
                        for element in revisions_list:
                            if element[key1] == data_dict[key1]:
                                data_dict[key2] = element[key2]
            else:
                parsing_json(data_dict[key1], revisions_list)
    elif type(data_dict) == list:
        for element in data_dict:
            parsing_json(element, revisions_list)
    return data_dict


def parsing_json_rev(revisions_dict, check_list=[]):
    check_dick = {}
    if type(revisions_dict) == dict:
        for key1, value1 in revisions_dict.items():
            if key1 == 'id':
                for key2, value2 in revisions_dict.items():
                    if key2 == 'value':
                        check_dick[key1] = value1
                        check_dick[key2] = value2
                        check_list.append(check_dick)
            else:
                parsing_json_rev(revisions_dict[key1])
    elif type(revisions_dict) == list:
        for element in revisions_dict:
            parsing_json_rev(element)
    return check_list


with open('tests.json', 'r') as tests_data:
    first_data_dict = json.load(tests_data)

with open('values.json', 'r') as values_data:
    second_data_dict = json.load(values_data)

check_list1 = parsing_json_rev(second_data_dict)
report = parsing_json(first_data_dict, check_list1)

with open('report.json', 'w') as report_data:
    json.dump(report, report_data, indent=1)
