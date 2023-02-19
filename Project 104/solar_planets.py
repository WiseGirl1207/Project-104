import cv2

img=cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sun",
            (100,400),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,69,255)
            )

cv2.putText(img,
            "Mercury",
            (115,180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (150,150,150)
            )

cv2.putText(img,
            "Venus",
            (190,265),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (46,148,215)
            )

cv2.putText(img,
            "Earth",
            (285,145),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (240,140,100)
            )

cv2.putText(img,
            "Mars",
            (380,265),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (30,80,150)
            )

cv2.putText(img,
            "Jupiter",
            (575,40),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (123,149,169)
            )

cv2.putText(img,
            "Saturn",
            (770,315),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (219,231,239)
            )

cv2.putText(img,
            "Uranus",
            (960,130),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (242,237,209)
            )

cv2.putText(img,
            "Jupiter",
            (1115,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (230,90,80)
            )

cv2.imshow("output", img)
cv2.waitKey(0)
cv2.imwrite("Solar_systemwithname.jpg",img)