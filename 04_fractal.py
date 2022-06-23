import simple_draw as sd
sd.resolution = (1200, 600)
start_point = sd.get_point(300, 30)
start_angle = 90
start_length = 100.
const_delta = 30


def draw_branches(point=start_point, angle=start_angle, length=start_length, delta=const_delta):
    if length < 10:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw()
    next_point = v1.end_point
    next_angle1 = angle - delta
    next_angle2 = angle + delta
    next_length = length * .75
    draw_branches(point=next_point, angle=next_angle1, length=next_length)
    draw_branches(point=next_point, angle=next_angle2, length=next_length)


draw_branches()
sd.pause()