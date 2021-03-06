import cv2
import numpy as np

recorder = cv2.VideoCapture(0)

while (True) :
    ret, frame = recorder.read()
    
    hsv = cv2.cvtColor (frame, cv2.COLOR_BGR2HSV)
    
    lower_blue = np.array ([105, 0, 0])
    upper_blue = np.array ([255, 255, 255])
    
    mask = cv2.inRange (hsv,lower_blue, upper_blue)
    
    res = cv2.bitwise_and (frame, frame, mask = mask)
    
    #cv2.imshow ('frame', frame)
    cv2.imshow ('mask', mask)
    #cv2.imshow ('res', res)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
recorder.release()
cvs2.destroyAllWindows()
