#include "C/FlyCapture2_C.h" 
#include <stdio.h>
#include <stdlib.h>


void GrabImages(fc2Context context, fc2Image *image)
{

    fc2PGRGuid guid;

    fc2CreateContext(&context);
    fc2GetNumOfCameras(context,0);
    fc2GetCameraFromIndex(context, 0, &guid);

    fc2Connect(context, &guid);
    fc2StartCapture(context);    

    fc2Image rawImage;
    fc2Image convertedImage;

    fc2CreateImage(&rawImage);
    fc2CreateImage(&convertedImage);
    
    fc2RetrieveBuffer(context, &rawImage);
    fc2RetrieveBuffer(context, &convertedImage);
    
    *image = convertedImage;
    // image = &convertedImage;

    fc2ConvertImageTo(FC2_PIXEL_FORMAT_MONO8,&rawImage,&convertedImage);

    //fc2DestroyImage(&rawImage);
    //fc2DestroyImage(&convertedImage);
    fc2StopCapture(context); // check for errors
    fc2DestroyContext(context);

};
