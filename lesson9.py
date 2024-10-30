#functions
from datetime import date
import math


def calc_area_triangle(b,h):
    area= 0.5 * b * h
    print(area)

def calc_area_circle(radius):
    area = math.pi * radius * radius
    area = round(area,2)
    print("Area of circle is",area,"cm^2")

def print_todays_date():
    today= date .today()
    print(today)

calc_area_triangle(b=8, h=13)
calc_area_triangle(b=8, h=43)

triangles=[[8,9],[6,13],[21,27],[16,41]]
for t in triangles:
    calc_area_triangle(t[0],t[1])

calc_area_circle(8.73653)

print_todays_date()