#Importing the libraries
import numpy  as np #for mathematical calculations
import cv2 #for image processing
import pytesseract

cap=cv2.VideoCapture(0) #for capturing the video
#if send the path of the video file instead of 0 then it will play the video file
#0 is for the default camera 
while cap.isOpened():
    _,frame=cap.read() #for reading the frame
    #cv2.imwrite("image.jpg",frame) #for saving the frame
    #cv2.imwrite("blackandwhite.jpg",blackandwhite) #for saving the black and white frame
    # show the frame raw and black and white
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray)
    print(text)
    cv2.imshow("frame",frame) 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print("La captura de video ha finalizado")
