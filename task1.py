def find_path_to_first_element(array, step_interval_array):
    string_test = 'start'
    output_data = ''
    list_test = []
    count = 0
    while string_test[0] != array[0]:
        if string_test == 'start':
            string_test = ''
        for j in range(step_interval_array):
            if count < len(array) and len(string_test) < step_interval_array:
                string_test += array[count]
                count += 1
            elif len(string_test) == step_interval_array and count < len(array):
                count = count
            else:
                count = 0
        list_test.append(string_test)
        if string_test[-1] == array[-1]:
            string_test = string_test[-1]
            count = 0
        else:
            string_test = string_test[-1]
    for element in list_test:
        output_data += element[0]
    return output_data


def create_array(array_length):
    array = ''
    for i in range(1, array_length + 1):
        array += str(i)
    return array


file_name_input_data = input('Введите имя файла с входными данными: ')

with open(file_name_input_data) as inp:
    input_data = inp.readline().strip()

input_data_array_length = int(input_data.split()[0])
input_data_step_interval_array = int(input_data.split()[1])

print(find_path_to_first_element(create_array(input_data_array_length), input_data_step_interval_array))
