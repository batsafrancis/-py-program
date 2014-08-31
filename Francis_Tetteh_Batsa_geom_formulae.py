__author__ = 'francis'
from numbers import Number
from numpy import*
import math


#################  AREA  AND PERIMETER OF A TRIANGLE  ##################

def triangle_area(side_a=None, side_b=None, side_c=None, height=None, angle_alpha=None) -> Number:
    """
    calculates the area of a triangle with al sides given, two sides and an angle (alpha) and in the
    case of base and height.

>>> triangle_area(3,4)
    @param height:The height of triangle
    @param side_a:the length of the triangle
    @param side_b: The side b of the triangle
    @param side_c: The side c of the triangle
    @param angle_alpha: The the angle between the sides of the triangle
    @return: Area of a triangle (square units)
    6
    """
    if (side_a is not None) & (height is not None):
        area = side_a * height / 2    # side_a is the base in this case
        return area
    ################ TWO SIDES AND THE ANGLE BETWEEN THEM  #######
    elif (side_a is not None) & (side_b is not None) & (angle_alpha is not None):
            area = 0.5*side_a*side_b*sin(angle_alpha)  # side_a and side_b can be  any of the two sides
            return area
    elif (side_a is not None) & (side_b is not None) & (side_c is not None):
   ######## HORN' FORMULA ( Given three sides ) ########
        if (side_a is not None) & (side_b is not None) & (side_c is not None):
            if ((side_a + side_b) > side_c) & ((side_a + side_c) > side_b) & ((side_b + side_c) > side_a):  # CONDITION
                s = (side_a + side_b + side_c) / 2  # s is the perimeter of the triangle
            area = math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))    # area of the triangle
            return area
        else:
            return "The sum of any two sides of the triangle must be greater that the third side"


def rectangle_perimeter(length: Number, width: Number)->Number:
    """
calculates the perimeter of a rectangle with

  >>> rectangle_perimeter(1,4)
    @param length: The length of the rectangle
    @param width: The width of the rectangle
    @return: The perimeter of rectangle (unit)
    10
    """
    return 2*length + 2*width


##################  VOLUME AND SURFACE AREA OF A CYLINDER #############################
def cylinder_volume(radius: Number, height: Number)->Number:
    """
calculates the volume of the cylinder with

 >>> cylinder_volume(2, 4)
    @param radius:The radius of the cylinder
    @param height: The height of the cylinder
    @return:  Volume of cylinder (cubic units)
    50.26548245743669
    """
    return pi*(radius**2)*height


def cylinder_surface_area(radius: Number, height: Number)-> Number:
    """
     calculates the surface area of a cylinder

     >>> cylinder_surface_area(3,4)
     @param radius: The radius of the cylinder
     @param height: The height of the cylinder
     @return: surface area of a cylinder(square units)
     131.94689145077132
     """
    return 2*pi*radius*height + 2*pi*radius**2


################  VOLUME OF A CONE  ################################################
def cone_volume(radius, height):
    """
 Calculates the volume of a cone with

>>> cone_volume(3,4)
    @param radius: The radius of the cone
    @param height: The height of the cone
    @return: Volume of cone(cubic units)
    9.42477796076938
    """
    return 1/3*pi*radius**height


##############  VOLUME OF A SPHERE #################################################
def sphere_volume(radius: Number) -> Number:
    """
Calculates the volume of a cone

>>> sphere_volume(3)
    @param radius:Base radius of the cone
    @return: Volume of sphere (cubic units)
    12.566370614359172
    """
    return 4*(pi/3*radius)


#############  VOLUME OF A FRUSTUM CONE ###########################################
def frustum_cone_volume(top_radius, base_radius, height):
    """
   Calculates the volume of frustum cone the arguments

    >>> frustum_cone_volume(2,3,4)
    @param top_radius: The radius of the top or the cut of the cone
    @param base_radius: The base radius of the cone
    @param height:The height of of the frustum cone
    @return: Volume of the frustum of a cone(cubic unit)
    79.58701389094142
    """
    return 1/3*pi*height*(top_radius**2 + top_radius*base_radius + base_radius**2)


############  AREA AND PERIMETER OF PARALLELOGRAM  ################################
def parallelogram_area(base, height):
    """
    calculate parallelogram area

    >>> parallelogram_area(3,4)
    @param base:The base of the parallelogram
    @param height:The height of the parallelogram
    @return: Area of the parallelogram
    12
    """
    return base * height


def parallelogram_perimeter(base: Number, width: Number)->Number:
    """
   calculates the Area of parallelogram with

>>> parallelogram_perimeter(3,7)
    @param base:   The base length
    @param width: The height of the parallelogram
    @return:Perimeter parallelogram (unit )
    21
    """
    return 2*base+2*width


###########  AREA OF A RHOMBUS  #################################################
def rhombus_area(long_diagonal, short_diagonal):
    """
 calculate the Area of a rhombus with

>>>  rhombus_area(1,2)
    @param long_diagonal: the longest diagonal
    @param short_diagonal: the shortest diagonal
    @return: area of rhombus (area unit)
    8
    """
    return 0.5*long_diagonal*short_diagonal


######### VOLUME OF TETRAHEDRON  ##############################################
def tetrahedron_volume(base: Number)-> Number:
    """
    calculate tetrahedron volume.

    @param base: this is the base length
    @return: volume of a tetrahedron (cubic units)

    >>> tetrahedron_volume(6)
    4.242640687119286
    """
    return (base**2)/12*math.sqrt(2)


################ VOLUME OF A REGULAR PYRAMID  #################################
def regular_pyramid_volume(base: Number, height: Number) -> Number:
    """
    calculates the volume of a regular pyramid.

    >>>  regular_pyramid_volume(3,5)
    @param base: Base length of the pyramid
    @param height: Height of the pyramid
    @return:volume of regular pyramid(cube unit)
    5
    """
    return 1/3*base*height
print("regular pyramid", regular_pyramid_volume(3, 5))


############ TRIANGULAR PRISM  ##############################################
def triangular_prim_volume(base, length, height):
    """
    Calculates the volume of the triangular prism given :

>>> triangular_prim_volume(3,3,4 )
    @param base: The base of the triangular prism
    @param length: The length of the triangular prism
    @param height: The height of th triangular prism
    @return: Volume of a triangular prism (cubic unit)
    18
    """
    area = 1/2*(base*length*height)
    return area


if __name__ == "__main__":

    print("Area of triangle ", triangle_area(side_a=5, angle_alpha=7))
    print("perimeter of rectangle", rectangle_perimeter(1, 4))
    print("Volume_of_cylinder ", cylinder_volume(2, 4))
    print("surface area of a cylinder ", cylinder_surface_area(3, 4))
    print("volume of a cone", cone_volume(3, 2))
    print(" Volume of sphere", sphere_volume(3))
    print("Volume of a frustum cone", frustum_cone_volume(2, 3, 4))
    print("Area of the parallelogram ", parallelogram_area(3, 4))
    print("Perimeter parallelogram  ", parallelogram_area(3, 7))
    print("Area of rhombus  ", rectangle_perimeter(1, 3))
    print("volume of a tetrahedron", tetrahedron_volume(6))
    print("regular pyramid", regular_pyramid_volume(3, 5))
    print("Volume of a triangular prism", triangular_prim_volume(3, 3, 4))
