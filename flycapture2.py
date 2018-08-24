import ctypes
import numpy as np
import matplotlib.pyplot as plt 
 
_lib = ctypes.cdll.LoadLibrary('/usr/lib/libflycapture-c.so')

# Initialize Definitions
fc2Context = ctypes.c_int
context = fc2Context()

class fc2PGRGuid(ctypes.Structure):
    _fields_ = [
        ('value', ctypes.c_uint * 4),
    ]
guid = fc2PGRGuid()

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
        ]
rawImage = fc2Image()
convertedImage = fc2Image()

# Create Context
func0 = _lib.fc2CreateContext
func0.argtypes = [ctypes.POINTER(fc2Context)] 
func0(ctypes.pointer(context))

# Get Number of Cameras
func1 = _lib.fc2GetNumOfCameras
func1.argtypes = [ctypes.c_int]
(context,0);

# Get Camera From Index
func2 = _lib.fc2GetCameraFromIndex
func2.argtypes = [ctypes.c_int,ctypes.c_int,ctypes.POINTER(ctypes.c_uint*4)]
func2(context,0,ctypes.pointer(guid.value))

# Connect to Camera 
func3 = _lib.fc2Connect
func3.argtypes = [ctypes.c_int,ctypes.POINTER(ctypes.c_uint*4)]
func3(context,ctypes.pointer(guid.value))

# Start Capture
func4 = _lib.fc2StartCapture
func4.argtypes = [ctypes.c_int]
func4(context)

# Create Images
func5 = _lib.fc2CreateImage
func5.argtypes = [ctypes.POINTER(fc2Image)]
func5(ctypes.pointer(rawImage))
func5(ctypes.pointer(convertedImage)) 

# Retrieve Image Buffers
func6 = _lib.fc2RetrieveBuffer
func6.argtypes = [ctypes.c_int,ctypes.POINTER(fc2Image)]
func6(context,ctypes.pointer(rawImage))
func6(context,ctypes.pointer(convertedImage))

# Convert Image to Grayscale
func7 = _lib.fc2ConvertImageTo
func7.argtypes = [ctypes.c_int,ctypes.POINTER(fc2Image),ctypes.POINTER(fc2Image)]
func7(2147483648,ctypes.pointer(rawImage),ctypes.pointer(convertedImage))

# Convert Pixel Data to Numpy Array 
p = convertedImage.pData 
pix = np.array(p[0:1920000]);
pixels = pix.reshape((1200,1600))

# Display Image
plt.imshow(pixels, cmap='gray', interpolation='nearest')
plt.show()

# Destroy Image Buffers
func8 = _lib.fc2DestroyImage
func8.argtypes = [ctypes.POINTER(fc2Image)]
func8(rawImage)
func8(convertedImage)

# Stop Capture
func9 = _lib.fc2StopCapture
func9.argtypes = [ctypes.c_int]
func9(context) 

# Destroy Image Context
func10 = _lib.fc2DestroyContext
func10.argtypes = [ctypes.c_int]
func10(context)

