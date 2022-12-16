#Importing the libraries
import numpy  as np #for mathematical calculations
import cv2 #for image processing


cap=cv2.VideoCapture("video.mp4") #for capturing the video
#if send the path of the video file instead of 0 then it will play the video file
#0 is for the default camera 
filter=0 #for selecting the filter
while cap.isOpened():
    _,frame=cap.read() #for reading the frame
    #cv2.imwrite("image.jpg",frame) #for saving the frame
    #cv2.imwrite("blackandwhite.jpg",blackandwhite) #for saving the black and white frame
    # show the frame raw and black and white
     
    # if the 'q' key is pressed, stop the loop
    if cv2.waitKey(1) & 0xFF == ord('n'):
        filter=1 #for converting the frame to black and white
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break 
    elif cv2.waitKey(1) & 0xFF == ord('s'):
        filter = 2 #for converting the frame to sepia
        
    if filter==1:
        blackandwhite=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame",blackandwhite)
    elif filter==2:
        sepia = np.array([[0.272, 0.534, 0.131],
                          [0.349, 0.686, 0.168],
                          [0.393, 0.769, 0.189]])
        sepia = cv2.transform(frame, sepia)
        cv2.imshow("frame",sepia)
    else:
        cv2.imshow("frame",frame)
print("La captura de video ha finalizado")
