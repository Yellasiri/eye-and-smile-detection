import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
eye_data = cv2.CascadeClassifier('haarcascade_eye.xml')


def detect(gray, frame):
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print(faces)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)
        print(smiles)
        eye_coordinates = eye_data.detectMultiScale(roi_gray, 1.1, 10)
        print(eye_coordinates)

        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)
        for (x__, y__, w__, h__) in eye_coordinates:
                cv2.rectangle(roi_color, (x__, y__), (x__ + w__, y__ + h__), (0, 255, 0), 2)
    return frame

img = cv2.imread('image3.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

canvas = detect(gray, img)

cv2.imshow('Video', canvas)

cv2.waitKey()

print('code complete')