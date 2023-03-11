#1 task
message_1 = "Hello World"
print(message_1)
message_1 = "Bye World"
print(message_1)

#2 task
name = "Sharah"
print("Hello," + name + ",would you like to learn some Python today?")

#3 task
message = '"A person who never made a mistake never tried anything new."'
print('Albert Einstein once said,' + message)

#4 task
name_1 = "  \tYura\n  "
surname_1 = "\tMontana\n"
age_1 = "\t20"
print(name_1 + surname_1 + str(age_1))

#5 task
print("Osovskiy Yuriy" + "\nУкраїна" + "\n58000" + "\nЧернівці" + "\nвул.Русська38")

#6 task

meters = 1000

inches = meters * 39.37
feet = meters * 3.28
miles = meters * 0.00062
yards = meters * 1.09

print("Дистанція у метрах: {:.2f}".format(meters))
print("Дистанція у дюймах: {:.2f}".format(inches))
print("Дистанція у футах: {:.2f}".format(feet))
print("Дистанція у милях: {:.2f}".format(miles))
print("Дистанція у ярдах: {:.2f}".format(yards))

#10 завдвння

import math

lat1, lon1 = 39.9075000, 116.3972300

lat2, lon2 = 50.4546600, 30.5238000

lat1 = math.radians(lat1)
lon1 = math.radians(lon1)
lat2 = math.radians(lat2)
lon2 = math.radians(lon2)

distance = 6371.032 * math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2))
print("{:>10.3f}".format(distance))






