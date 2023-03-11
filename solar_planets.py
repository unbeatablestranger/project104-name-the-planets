import cv2

img = cv2.imread("solar-system.jpg")
cv2.imshow("output", img)

cv2.putText(    img,
                "Sun",
                (90, 80),
                cv2.FONT_HERSHEY_COMPLEX,
                2.5,
                (204, 0, 0)
            )

cv2.putText(    img,
                "Mercury",
                (110, 250),
                cv2.FONT_HERSHEY_COMPLEX,
                0.5,
                (255,255,255)
            )

cv2.putText(    img,
                "Venus",
                (190, 170),
                cv2.FONT_HERSHEY_COMPLEX,
                0.5,
                (255,255,255)
            )

cv2.putText(    img,
                "Earth",
                (290, 270),
                cv2.FONT_HERSHEY_COMPLEX,
                0.5,
                (255,255,255)
            )

cv2.putText(    img,
                "Mars",
                (375, 180),
                cv2.FONT_HERSHEY_COMPLEX,
                0.5,
                (255,255,255)
            )

cv2.putText(    img,
                "Jupiter",
                (490, 390),
                cv2.FONT_HERSHEY_COMPLEX,
                1.5,
                (255,255,255)
            )

cv2.putText(    img,
                "Saturn",
                (780, 120),
                cv2.FONT_HERSHEY_COMPLEX,
                0.75,
                (255,255,255)
            )

cv2.putText(    img,
                "Uranus",
                (970, 290),
                cv2.FONT_HERSHEY_COMPLEX,
                0.5,
                (255,255,255)
            )

cv2.putText(    img,
                "Neptune",
                (1100, 150),
                cv2.FONT_HERSHEY_COMPLEX,
                0.5,
                (255,255,255)
            )
           
print(img)

cv2.imwrite('Solar_systemwithname.jpg',img)

cv2.waitKey(0)