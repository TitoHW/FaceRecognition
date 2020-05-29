import cv2, os

cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)

#deteksi wajah
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#id wajah per orang
face_id = input ('\n Masukkan ID wajah, kemudian tekan enter : ')
print ("\n [INFO] Mulai menangkap wajah. Arahkan pada kamera dan tunggu... ")

#inisialisasi wajah per orang
count = 0
while(True) :
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    for(x,y,w,h) in faces :
        cv2.rectangle (img, (x,y), (x+w, y+h), (255,0,0), 2)
        count += 1

        #menyimpan foto pada folder trainer
        cv2.imwrite("dataset/" + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h, x:x+w])
        cv2.imshow('image', img)
        k = cv2.waitKey(10) & 0xff
        if k == 27 :
            break
        elif count >= 30 :
            break

#membersihkan memori
print("\n [INFO] Keluar program ")
cam.release()
cv2.destroyAllWindows()