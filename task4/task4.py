file_name_input_data = input('Введите имя файла с входными данными: ')

input_data = []
with open(file_name_input_data) as inp:
    for line in inp:
        line = line.strip()
        input_data.append(int(line))

count = 0
while max(input_data) != min(input_data):
    input_data.sort()
    average = sum(input_data) / len(input_data)
    if average - min(input_data) >= max(input_data) - average:
        count += 1
        input_data[0] = input_data[0] + 1
    else:
        count += 1
        input_data[-1] = input_data[-1] - 1
print(count)
