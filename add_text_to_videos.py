import cv2

cap = cv2.VideoCapture(0)

#Set WIDTH
cap.set(3, 1280)
#SET HEIGHT
cap.set(2, 720)
while(cap.isOpened()):
    ret, frame = cap.read()
    if(ret == True):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
