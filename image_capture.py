import cv2

def take_snapshot():
    #initiallizing cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        #read the frames while the camera is on
        ret,frame = videoCaptureObject.read()
        #cv2.imwrite() method is used to save an image to any storage device
        cv2.imwrite("Tanvi.jpg",frame)
        result = False

    # releases the camera
    videoCaptureObject.release()
    #loses all the window that might be opened while the process
    cv2.destroyAllWindows()

take_snapshot()    