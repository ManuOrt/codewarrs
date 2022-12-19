import statistics

def better_than_average(class_points, your_points):

    for enum in class_points:
        redondeo = statistics.mean(class_points)
        if redondeo < your_points:
            return True
        else:
            return False
print(better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75))