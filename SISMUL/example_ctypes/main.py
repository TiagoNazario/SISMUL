import ctypes
lib = ctypes.cdll.LoadLibrary('./clibrary.so')
print(lib.fn(1, 2, 3))