import cv2, time

face_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

vid = cv2.VideoCapture('film.mp4')

while 1:
    check, frame = vid.read()

    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_img, 1.2, 5)

    for x, y, p, q in faces:
        frame = cv2.rectangle(frame, (x,y), (x+p,y+q), (0,255,0), 3)

    cv2.imshow("Camera",frame)
    key = cv2.waitKey(1)

    #time.sleep(1)
    if key == ord('m'):
        break

cv2.destroyAllWindows()
