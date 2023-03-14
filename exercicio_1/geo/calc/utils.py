import ctypes
import os

shared_lib_path = os.path.join(os.path.dirname(__file__), "_aux.so")


def print_rectangle_surface(width, length):

    lib = ctypes.cdll.LoadLibrary('./_aux.so')
    width = ctypes.c_float(width)
    length = ctypes.c_float(length)
    lib.rectangle_surface.restype = ctypes.c_float


def print_rectangle_perimenter(width, length):

    lib = ctypes.cdll.LoadLibrary('./_aux.so')
    width = ctypes.c_float(width)
    length = ctypes.c_float(length)
    lib.rectangle_perimeter.restype = ctypes.c_float


def print_rectangle_equalSides(width, length):
    lib = ctypes.cdll.LoadLibrary('./_aux.so')
    width = ctypes.c_float(width)
    length = ctypes.c_float(length)
    lib.rectangle_equalSides.restype = ctypes.c_float


print_rectangle_surface(10, 10)
