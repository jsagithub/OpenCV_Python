import cv2
import datetime
cap = cv2.VideoCapture(0)

# Set WIDTH
#cap.set(3, 1280)
# SET HEIGHT
#cap.set(2, 720)

while(cap.isOpened()):
    ret, frame = cap.read()
    if(ret == True):
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Whidth' + str(cap.get(3))
    datet=str(datetime.datetime.now())
        cv2.putText(frame, datet, (10, 50), font, 1,
                    (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
