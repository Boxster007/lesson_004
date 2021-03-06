import simple_draw as sd


point_initial_triangle = sd.get_point(100, 300)
point_initial_square = sd.get_point(300, 150)
point_initial_pentagon = sd.get_point(500, 300)
point_initial_hexagon = sd.get_point(150, 400)
length_initial = 100
angle_initial = 60
user_color = sd.COLOR_YELLOW


def triangle(point=point_initial_triangle, angle=angle_initial, length=length_initial, color=user_color):
    number_of_angles = 3
    angle_delta = 180 - (number_of_angles - 2) * 180 / number_of_angles
    end_point = point
    for i in range(number_of_angles):
        v = sd.get_vector(start_point=end_point, angle=angle + angle_delta * i, length=length, width=3)
        end_point = v.end_point
        v.draw(color=color)


def square(point=point_initial_square, angle=angle_initial, length=length_initial, color=user_color):
    number_of_angles = 4
    angle_delta = 180 - (number_of_angles - 2) * 180 / number_of_angles
    end_point = point
    for i in range(number_of_angles):
        v = sd.get_vector(start_point=end_point, angle=angle + angle_delta * i, length=length, width=3)
        end_point = v.end_point
        v.draw(color=color)


def pentagon(point=point_initial_pentagon, angle=angle_initial, length=length_initial, color=user_color):
    number_of_angles = 5
    angle_delta = 180 - (number_of_angles - 2) * 180 / number_of_angles
    end_point = point
    for i in range(number_of_angles):
        v = sd.get_vector(start_point=end_point, angle=angle + angle_delta * i, length=length, width=3)
        end_point = v.end_point
        v.draw(color=color)


def hexagon(point=point_initial_hexagon, angle=angle_initial, length=length_initial, color=user_color):
    number_of_angles = 6
    angle_delta = 180 - (number_of_angles - 2) * 180 / number_of_angles
    end_point = point
    for i in range(number_of_angles):
        v = sd.get_vector(start_point=end_point, angle=angle + angle_delta * i, length=length, width=3)
        end_point = v.end_point
        v.draw(color=color)


color_names = {
    '0': {'name': 'red', 'color': sd.COLOR_RED},
    '1': {'name': 'orange', 'color': sd.COLOR_ORANGE},
    '2': {'name': 'yellow', 'color': sd.COLOR_YELLOW},
    '3': {'name': 'green', 'color': sd.COLOR_GREEN},
    '4': {'name': 'cyan', 'color': sd.COLOR_CYAN},
    '5': {'name': 'blue', 'color': sd.COLOR_BLUE},
    '6': {'name': 'purple', 'color': sd.COLOR_DARK_PURPLE},
}


print('?????????????????? ??????????: ')
for color_name in color_names:
    print("{}: {}".format(color_name, color_names[color_name]['name']))

user_color = input("??????????????, ????????????????????, ???????????????? ????????: ")

while user_color in color_names:
    triangle(color=color_names[user_color]['color'])
    square(color=color_names[user_color]['color'])
    pentagon(color=color_names[user_color]['color'])
    hexagon(color=color_names[user_color]['color'])
    user_color = input("??????????????, ????????????????????, ???????????????? ????????: ")
else:
    print("???? ?????????? ???????????????????????? ??????????!")
