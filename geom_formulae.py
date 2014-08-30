__author__ = 'francis'
from numbers import Number
from numpy import*
import math


def triangular_area(height: Number, length: Number)->Number:
    """
calculate the area of a triangle
    @param height:The height of triangle
    @param length:the length of the triangle
    @return:Area
    >>> triangular_area(3,4)
    6
    """
    return 0.5*height*length

print(triangular_area(3, 4))


def rectangle_perimeter(length: Number, width: Number)->Number:
    """
calculates the perimeter of a rectangle with

  >>> rectangle_perimeter(3,4)
    @param length: The length of the rectangle
    @param width: The width of the rectangle
    @return: The perimeter of rectangle (unit)
    56
    """
    return 2*length + 2*width

print(rectangle_perimeter(3, 4))


def cylinder_volume(radius: Number, height: Number)->Number:
    """
calculates the volume of the cylinder with

 >>> cylinder_volume(3, 4)
    @param radius:The radius of the cylinder
    @param height: The height of the cylinder
    @return:  Volume of cylinder (cubic units)
    """
    return pi*radius**2*height
print(cylinder_volume(3, 4))


def cylinder_surface_area(radius: Number, height: Number)-> Number:
    """
 calculates the surface area of a cylinder

>>> cylinder_surface_area(3,4)
     @param radius: The radius of the cylinder
     @param height: The height of the cylinder
     @return: surface area of a cylinder(square unit)
     """
    return 2*pi*radius*height + 2*pi*radius**2
print(cylinder_surface_area(3, 4))


def cone_volume(radius, height):
    """
 Calculates the volume of a cone with

>>> cone_volume(3,4)
    @param radius: The radius of the cone
    @param height: The height of the cone
    @return: Volume of cone
    """
    return 1/3*pi*radius**height
print(cone_volume(3, 4))


def sphere_volume(radius: Number) -> Number:
    """
Calculates the volume of a cone

>>> sphere_volume(3)
    @param radius:Base radius of the cone
    @return: Volume of cone (cubic unit)
    """
    return 4*(pi/3*radius)
print(sphere_volume(3))


def frustum_cone_volume(top_radius, base_radius, height) ->Number:
    """
Calculates the volume of frustum cone with

>>> frustum_cone_volume(2,3,4)
    @param top_radius: The radius of the top or the cut
    @param base_radius: The base radius
    @param height:The height of of the frustum cone
    @return: Volume of the frustum of a cone(cubic unit)
    """
    return 1/3*pi*height*(top_radius**2 + top_radius*base_radius + base_radius**2)
print(frustum_cone_volume(2, 3, 4))


def parallelogram_area(base, height):
    """
    calculate parallelogram area

    >>> parallelogram_area(3,4)
    @param base:The base of the parallelogram
    @param height:The height of the parallelogram
    @return: Area of th of the parallelogram
    """
    return base * height
print(parallelogram_area(3, 4))


def parallelogram_perimeter(base: Number, width: Number)->Number:
    """
   calculates the Area of parallelogram with

>>> parallelogram_perimeter(3,4)
    @param base:   The base length
    @param width: The height of the parallelogram
    @return:Perimeter parallelogram (unit )
    """
    return 2*base+2*width
print(parallelogram_area(3, 5))


def rhombus_area(long_diagonal, short_diagonal):
    """
 calculate the Area of a rhombus with

>>>  rhombus_area(1,2)
    @param long_diagonal: the longest diagonal
    @param short_diagonal: the shortest diagonal
    @return: area of rhombus (area unit)
    2
    """
    return 0.5*long_diagonal*short_diagonal
print(rectangle_perimeter(1, 1))


def tetrahedron_volume(base)-> Number:
    """
    calculate tetrahedron volume.

    @param base: this is the base length
    @return: volume of a tetrahedron (cubic unit)

    >>> tetrahedron_volume(3)

    10
    """
    return (base**2)/12*math.sqrt(2)

print(tetrahedron_volume(2))


def regular_pyramid_volume(base: Number, height: Number) -> Number:
    """
    calculate the volume of a regular pyramid.
    >>>  regular_pyramid_volume(3,4)
    @param base: Base length of the pyramid
    @param height: Height of the pyramid
    @return:volume of regular pyramid(cube unit)
    """
    return 1/3*base*height
print(regular_pyramid_volume(3, 4))


if __name__ == "__main__":
    sampleSide = 4
    print("area:",
          square_area(sampleSide),
          "perimeter:",
          square_perimeter(sampleSide))