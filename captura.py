import cv2

camera = cv2 = cv2.VideoCapture(0) #código para captura da imagem pela webcam, parâmetro 0 <= única câmera do pc

while (True): #looping infinito
    conectado, imagem = camera.read()

    cv2.imshow("Face", imagem)
    cv2.waitKey(1)

camera.release()
cv2.destroyAllWindows()
