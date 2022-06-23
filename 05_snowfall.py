# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# TODO здесь ваш код


# sd.snowflake(center=point_0, length=200, factor_a=0.5)
y = 500
x = 100

y2 = 450
x2 = 150

y3 = 400
x3 = 200

while True:
    sd.clear_screen()
    point = sd.get_point(x, y)
    sd.snowflake(center=point, length=50)
    y = y - 10
    if y < -50:
        break
    x = x * 1.1


    point2 = sd.get_point(x2, y2)
    sd.snowflake(center=point2, length=30)
    y2 = y2 - 10
    if y2 < -50:
        break
    x2 = x2 * 1.1

    point3 = sd.get_point(x3, y3)
    sd.snowflake(center=point3, length=30)
    point = sd.get_point(x3, y3)
    y3 = y3 - 10
    if y3 < -50:
        break
    x3 = x3 * 1.1

    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


