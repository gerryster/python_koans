#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    check_sides([a, b, c])
    if a == b and b == c:
        return 'equilateral'
    elif a == b or b == c or a == c:
        return 'isosceles'
    else:
        return 'scalene'

# This should be a frozen data structure and a constant but I'm not sure how to
# do that yet.
indicies_to_check = [
    [0, 1, 2],
    [0, 2, 1],
    [1, 2, 0],
]

def check_sides(sides):
  if any(i <= 0 for i in sides):
    raise TriangleError('all sides must be greater than zero')

  for check_spec in indicies_to_check:
    if sides[check_spec[0]] + sides[check_spec[1]] < sides[check_spec[2]]:
        raise TriangleError('the sum of any two sides should be greater than the third side')



# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
