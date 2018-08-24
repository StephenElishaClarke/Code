import ctypes
import numpy as np
import itertools


_lib = ctypes.cdll.LoadLibrary('/home/bil/Code/capture_lib.so')

##########################################
# Definitions of variables and functions #
##########################################

fc2Context = ctypes.c_void_p
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
image = fc2Image()

class fc2TimeStamp(ctypes.Structure):
    _fields_ = [
        ('ptr', ctypes.POINTER(ctypes.c_int)),
        ('seconds', ctypes.c_long),
        ('microSeconds', ctypes.c_uint),
        ('cycleSeconds', ctypes.c_uint),
        ('cycleCount', ctypes.c_uint),
        ('cycleOffset', ctypes.c_uint),
        ('reserved', ctypes.c_uint * 8),
    ]

TS = fc2TimeStamp()
#TS.seconds = 4




class Enum(dict):
    def __init__(self, name, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)
        self.reverse = dict([(self[n], n) for n in self])
        self.name = name

    def name_to_value(self, name):
        return dict.__getitem__(self, name)

    def value_to_name(self, value):
        return self.reverse[value]

    def __getitem__(self, k):
        if isinstance(k, (str, unicode)):
            return self.name_to_value(k)
        elif isinstance(k, int):
            return self.value_to_name(k)
        else:
            raise ValueError(
                "Invalid enum key {}, must be str, unicode or int: {}".format(
                    k, type(k)))



def arg_type_convert(v, atype=None, byref=None):
    """
    This needs to know the un-pointered type when arg by value
    """
    if byref:
        if type(v) == atype:
            return v
        # this should be a simple ctype that will be pointed to
        if type(v).__module__ == 'ctypes':  # this is a valid ctypes object
            return ctypes.byref(v)
        if type(type(v)).__module__ == '_ctypes':  # defined struct, etc
            return ctypes.byref(v)
        # this is a non-ctypes object, so making it into a ctypes object
        # would 'shadow' the arg, causing any change to the generated
        # ctype object to be lost. so throw an exception
        raise Exception(
            "Arguments passed by reference must "
            "be ctypes object: {}, {}".format(v, type(v)))
    if type(v) != atype:
        return atype(v)
    return v

class Function(object):
    def __init__(self, name, restype, *args):
        self.name = name
        self.restype = restype
        self.args = args
        self.func = None
        self.lib = None
        self.converter = None

    def generate_spec(self, lib):
        # TODO do I need the namespace here... probably for typedefs
        self.converter = []
        # TODO generate converter for __call__, maybe even a *gasp* doc string
        for n, vt in self.args:
            argtype = type(vt).__name__  # this is a type of a type
            if argtype == 'PyCSimpleType':  # pass by value
                self.converter.append(
                    lambda v, a=vt, b=False:
                    arg_type_convert(v, a, b)
                )
            elif argtype == 'PyCPointerType':  # pass by ref
                self.converter.append(
                    lambda v, a=vt, b=True:
                    arg_type_convert(v, a, b)
                )
            elif argtype == 'PyCStructType':
                self.converter.append(
                    lambda v, a=vt, b=False:
                    arg_type_convert(v, a, b)
                )
            else:
                raise Exception(
                    "Unknown arg type {} for {} {}".format(argtype, n, vt))
        self.assign_lib(lib)
        self.__doc__ = 'args: {}'.format(self.args)


    def assign_lib(self, lib):
        self.lib = lib
        self.func = getattr(self.lib, self.name)
        self.func.restype = self.restype
        self.func.argtypes = [v for _, v in self.args]

    def __call__(self, *args):
        if self.func is None:
            raise Exception(
                "Function has not been bound to a library: see assign_lib")
        if self.converter is None:
            raise Exception(
                "Function spec has not been generated: see generate_spec")
        if len(self.converter) != len(args):
            raise Exception(
                "Invalid number of args {} != {}".format(
                    len(args), len(self.converter)))
        return self.func(*[
            c(a) for (c, a) in itertools.izip(self.converter, args)])

    def __dump__(self):
        """
        # set restype and argtypes of lib function
        def function_name(arg1, arg2, arg3, ...):
            # do arg conversion
            lib.function_name(arg1, arg2, arg3)
        """
        raise Exception
        pass


fc2PixelFormat = Enum('fc2PixelFormat', [ ('FC2_PIXEL_FORMAT_MONO8', 2147483648),
])


fc2BayerTileFormat = Enum('fc2BayerTileFormat', [('FC2_BT_NONE', 0),
])

###########################################################
# Create Context, Connect to Camera and Print Information #
########################################################### 


fc2CreateContext = Function(
    'fc2CreateContext', ctypes.c_uint,
    ('pContext', ctypes.POINTER(fc2Context)),
)
fc2CreateContext.generate_spec(_lib)
_lib.fc2CreateContext(context);   #fc2CreateContext(&context);


fc2GetCameraFromIndex = Function(
    'fc2GetCameraFromIndex', ctypes.c_uint,
    ('context', ctypes.c_void_p),
    ('index', ctypes.c_uint),
    ('pGuid', ctypes.POINTER(fc2PGRGuid)),
)
fc2GetCameraFromIndex.generate_spec(_lib)
_lib.fc2GetCameraFromIndex(context, 0, guid); # (context, 0, &guid);


fc2Connect = Function(
    'fc2Connect', ctypes.c_uint,
    ('context', ctypes.c_void_p),
    ('guid', ctypes.POINTER(fc2PGRGuid)),
)
fc2Connect.generate_spec(_lib)
_lib.fc2Connect(context,guid);  #fc2Connect(context, &guid);

_lib.SetTimeStamping(context,1);  # 1 as a logical value here

_lib.fc2StartCapture(context);

grab = _lib.GrabImages
grab.restype = None
#grab.argtypes = [ctypes.POINTER(fc2TimeStamp),ctypes.c_int]
#grab(context,ctypes.pointer(fc2TimeStamp))
grab.argtypes = [ctypes.POINTER(fc2Context),ctypes.POINTER(fc2TimeStamp)]
grab(context,ctypes.pointer(TS))
print(TS.seconds)

#grab_func = _lib.GrabImages(context,1)    # fix up!?   k_numImages = 1

#func.restype = None
#func.argtypes = [ctypes.POINTER(fc2Context),ctypes.POINTER(fc2TimeStamp)]
#func(ctypes.pointer(context),ctypes.pointer(TS))

