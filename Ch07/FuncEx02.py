def circle_area():
    area = radius**2 * 3.14
    return area
def rect_area(side, height):
    area = side * height
    return area

def tri_area(side, height):
    area = side * height / 2
    return area

radius = int(input("반지름:"))
area0 = circle_area()
print("원의 면적:", area0)
