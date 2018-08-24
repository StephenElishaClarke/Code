import ctypes
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
 
lib = ctypes.cdll.LoadLibrary('/home/bil/Code/capture_library.so')

##################################################################

fc2Context = ctypes.c_uint
context = fc2Context()

#class fc2TimeStamp(ctypes.Structure):
#    _fields_ = [
#        ('seconds', ctypes.c_long),
#        ('microSeconds', ctypes.c_uint),
#        ('cycleSeconds', ctypes.c_uint),
#        ('cycleCount', ctypes.c_uint),
#        ('cycleOffset', ctypes.c_uint),
#        ('reserved', ctypes.c_uint * 8),
#        ]
#TS = fc2TimeStamp() 


class fc2Image(ctypes.Structure):
    _fields_ = [
        ('rows', ctypes.c_uint),
        ('cols', ctypes.c_uint),
        ('stride', ctypes.c_uint),
        ('pData', ctypes.POINTER(ctypes.c_ubyte)),
        ('dataSize', ctypes.c_uint),
        ('receivedDataSize', ctypes.c_uint),
        ('format', ctypes.c_uint),
        ('bayerFormat', ctypes.c_uint),
        ('imageImpl', ctypes.c_void_p),
        #('ptrData',ctypes.POINTER(ctypes.c_char))
        ]
image = fc2Image()

#################################################################
 
func = lib.GrabImages
func.restype = None
func.argtypes = [ctypes.POINTER(fc2Context), ctypes.POINTER(fc2Image)]
func(ctypes.pointer(context),ctypes.pointer(image))

p = image.pData
pix = np.array(p[0:1920000]);
pixels = pix.reshape((1200,1600))

plt.imshow(pixels, cmap='gray', interpolation='nearest')
plt.show()
