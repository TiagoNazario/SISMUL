#include <stdio.h>

float rectangle_surface(float width, float length)
{
    return width * length;
}

float rectangle_perimeter(float width, float length)
{
    return 2 * (length + width);
}

float rectangle_equalSides(float width, float length)
{
    if (width == length)
        printf("equal");
    else
        printf("not equal");
}