import cv2
import sys

cap = None

if '-h' in sys.argv or '--help' in sys.argv or len(sys.argv) > 2:
    print 'Usage: python test.py <optional video path>'

elif len(sys.argv) == 1:
    print 'Trollifying webcam...'
    cap = cv2.VideoCapture(0)

elif len(sys.argv) == 2:
    print 'Trollifying %s...' % sys.argv[1]
    cap = cv2.VideoCapture(sys.argv[1])

troll_face = cv2.imread('troll.jpg', 1)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

if face_cascade.empty():
    raise Exception('Classifier not loaded.')

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret:
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            frame[y:y+h, x:x+w] = cv2.resize(troll_face, (w, h))

        # Display the resulting frame
        cv2.imshow('frame', frame)

    if cv2.waitKey(int(1000/60)) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
