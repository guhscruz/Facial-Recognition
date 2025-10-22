import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, video = cap.read()
    video = cv2.flip(video, 1)

    gray = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)

    face = face_cascade.detectMultiScale(gray, 1.3, 5)

    for(x, y, z, h) in face:
        cv2.rectangle(video, (x, y), (x + z, y + h), (0, 255, 0), 2)
        roi_gray = gray[y: y + h, x: x + z]
        roi_color = video[y: y + h, x: x + z]

        print(int((x + z) / 2), int((y + h) / 2))

    cv2.imshow("Facial Recognition", video)
    key = cv2.waitKey(1) & 0xFF

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()