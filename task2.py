input_data1 = []
input_data2 = []

file_name_input_data1 = input('Введите имя файла с входными данными1: ')
with open(file_name_input_data1) as inp:
    for line in inp:
        line = line.strip()
        input_data1.append(line)

file_name_input_data2 = input('Введите имя файла с входными данными2: ')
with open(file_name_input_data2) as inp:
    for line in inp:
        line = line.strip()
        input_data2.append(line)

circle_center_coordinates = input_data1[0].split()
circle_radius = input_data1[1]

dx = float(circle_center_coordinates[0])
dy = float(circle_center_coordinates[1])
radius = float(input_data1[1])

for i in range(len(input_data2)):
    x = float(input_data2[i].split()[0])
    y = float(input_data2[i].split()[1])
    if (x - dx)**2 + (y - dy)**2 < radius**2:
        print(1)
    elif (x - dx)**2 + (y - dy)**2 == radius**2:
        print(0)
    else:
        print(2)
