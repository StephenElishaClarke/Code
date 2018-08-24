import ctypes
import numpy as np
 
lib = ctypes.cdll.LoadLibrary('/home/bil/Code/capture_library.so')

fc2Context = ctypes.c_uint
context = fc2Context()

class fc2PGRGuid(ctypes.Structure):
    _fields_ = [ 
        ('value', ctypes.c_uint * 4), 
    ]   
guid = fc2PGRGuid()

 
class fc2TimeStamp(ctypes.Structure):
       _fields_ = [ 
                  ('seconds', ctypes.c_int),
                  ('ptr', ctypes.POINTER(ctypes.c_int)),
                  ]

class fc2Image(ctypes.Structure):
      _fields_ = [
          ('rows', ctypes.c_uint),
          ('cols', ctypes.c_uint),
          ('pData', ctypes.POINTER(ctypes.c_ubyte)),
          ('dataSize', ctypes.c_uint),
         #('rawImage',  ),
      ]
image = fc2Image()

 
TS = fc2TimeStamp()
#TS.seconds = 4 
#print(TS.seconds)


### Populate Stucture ###
func = lib.GrabImages
func.restype = None
func.argtypes = [ctypes.POINTER(fc2Context),ctypes.POINTER(fc2TimeStamp)]
func(ctypes.pointer(context),ctypes.pointer(TS))

#func.argtypes = [ctypes.POINTER(fc2Context),ctypes.POINTER(fc2TimeStamp),ctypes.POINTER(fc2Image)]
#func(ctypes.pointer(context),ctypes.pointer(TS),ctypes.pointer(image))

print(TS.seconds)
#print(image.rawImage)
print(image.pData)
