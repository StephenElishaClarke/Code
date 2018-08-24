#include "C/FlyCapture2_C.h" 
#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>
//#include <string.h>

/*
struct fc2TimeStamp
{   int seconds;
    int *ptr;
};

*/

/*
struct fc2Image
{   int rows;
    int cols;
    //const unsigned char *pData;
    unsigned int dataSize;
    int pixels[1200][1600];   //unsigned char *ptrData;
    char *ptrData;
};

*/

/*
void SetTimeStamping(fc2Context context, BOOL enableTimeStamp)
{
    fc2Error error;
    fc2EmbeddedImageInfo embeddedInfo;

    error = fc2GetEmbeddedImageInfo(context, &embeddedInfo);
    if (error != FC2_ERROR_OK)
    {   
                printf("Error in fc2GetEmbeddedImageInfo: %s\n", fc2ErrorToDescription(error));
    }   

    if (embeddedInfo.timestamp.available != 0)
    {   
        embeddedInfo.timestamp.onOff = enableTimeStamp;
    }   

    error = fc2SetEmbeddedImageInfo(context, &embeddedInfo);
    if (error != FC2_ERROR_OK)
    {   
                printf("Error in fc2SetEmbeddedImageInfo: %s\n", fc2ErrorToDescription(error));
    }   
}

*/

void GrabImages(fc2Context context) // ,struct fc2TimeStamp *ptr, struct fc2Image *ptrData, struct fc2Image pixels)
{

    fc2PGRGuid guid;
    const unsigned char pData;
    unsigned char *ppData;
    unsigned int dataSize = 1920000; //15360000;    
    //fc2TimeStamp prevTimestamp = {0}; 

    char *tester = "hello";
   
    unsigned int numCameras = 0;
    //int pixels[1200][1600];
    //ptrData = &pixels;

    fc2CreateContext(&context);
    fc2GetNumOfCameras(context, &numCameras);
    fc2GetCameraFromIndex(context, 0, &guid);

    fc2Connect(context, &guid);
    //SetTimeStamping(context, TRUE);
    fc2StartCapture(context);    

    fc2Image rawImage;
    fc2Image convertedImage;

    fc2CreateImage(&rawImage);
    fc2CreateImage(&convertedImage);
    
    /*
    fc2SetImageDimensions(&convertedImage,
                unsigned int rows,
                unsigned int cols,
                unsigned int stride,
                fc2PixelFormat pixelFormat,
                fc2BayerTileFormat bayerFormat);
    
    */
 
    //fc2SetImageData(&convertedImage,&pData,dataSize);

    // Retrieve the image
    fc2RetrieveBuffer(context, &rawImage);
    fc2RetrieveBuffer(context, &convertedImage);
    
    //fc2SetImageData(&rawImage,&pData,dataSize);
   
    /*
    // Get and print out the time stamp
    fc2TimeStamp ts = fc2GetImageTimeStamp(&rawImage);
    int diff = (ts.cycleSeconds - prevTimestamp.cycleSeconds) * 8000 +
               (ts.cycleCount - prevTimestamp.cycleCount);
    prevTimestamp = ts;
    printf("timestamp [%d %d] - %d\n",
                   ts.cycleSeconds,
                   ts.cycleCount,
                   diff);
    */ 
     
    //ptr->seconds = 5; //ts.cycleSeconds; 

    fc2ConvertImageTo(FC2_PIXEL_FORMAT_MONO8,&rawImage,&convertedImage);
 
    //fc2GetImageDimensions   useful?
 
    //fc2GetImageData(&rawImage,&ppData);

    //int var = 20;
    //int *ptr;
    //ptr = &var;
    //printf("%d\n",*ptr);

    //FILE *fp; 
    //fp=fopen("file.txt","w+");
    //for(i = 0; i<1200;i++)
    //fprintf(fp,"%" PRIu16 "\n",*(ppData+500));
    //fprintf(fp,"%c\n",*(ppData+2));    // %o\n, *ppData
    //fprintf(fp,"%02X\n",*ppData);           
    // x\n for pData address     02X for bytes 
    //fclose(fp);
   
     
    int c = getchar();
 
    //printf("%c\n", *pData);     
 
    //void *memcpy(char *pData, char *ppData, size_t dataSize);
    //fc2SaveImage(&convertedImage,"image.png",FC2_PNG);

    fc2DestroyImage(&rawImage);
    fc2DestroyImage(&convertedImage);
    fc2StopCapture(context); // check for errors
    fc2DestroyContext(context);

};

int main()
{
	fc2Context context;
        GrabImages(context);

        return 0;

};
